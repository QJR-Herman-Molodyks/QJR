
# TODO: Add via HMAC in
# TODO: {globals.home()}/../sphere/qjrsphere_verification.qjr
# TODO: Verify the HMAC-Signature of the DB of Hashes
# TODO: And put the JSON with QJRsphere DBs SHA-512 Hashes.

"""
It needs to look like this:
{
    "sphere_admin.qjr": "<SHA-512 HASH>",
    "sphere_user_1.qjr": "<SHA-512 HASH>",
    "sphere_user_2.qjr": "<SHA-512 HASH>",
}><HMAC Signature>
"""

import hmac
import os
import hashlib
import json
import secrets

import globals


VERIFICATION_FILE = "qjrsphere_verification.qjr"
KEY_FILE = "qjrsphere_hmac.key"


def get_sphere_path():
    return os.path.join(globals.home, "..", "sphere")


def get_key_path():
    return os.path.join(
        globals.home,
        "keys",
        KEY_FILE
    )


def load_or_create_key():
    key_path = get_key_path()

    os.makedirs(os.path.dirname(key_path), exist_ok=True)

    if not os.path.exists(key_path):
        key = secrets.token_bytes(32)

        with open(key_path, "wb") as file:
            file.write(key)

        return key

    with open(key_path, "rb") as file:
        return file.read()


def hash_file(path):
    sha512 = hashlib.sha512()

    with open(path, "rb") as file:
        while chunk := file.read(1024 * 1024):
            sha512.update(chunk)

    return sha512.hexdigest()


def get_sphere_files(sphere_path):
    files = []

    if not os.path.isdir(sphere_path):
        return files

    for filename in os.listdir(sphere_path):
        path = os.path.join(sphere_path, filename)

        if not os.path.isfile(path):
            continue

        if not filename.endswith(".qjr"):
            continue

        if filename == VERIFICATION_FILE:
            continue

        files.append(filename)

    return sorted(files)


def build_manifest(sphere_path):
    hashes = {}

    for filename in get_sphere_files(sphere_path):
        path = os.path.join(sphere_path, filename)

        hashes[filename] = hash_file(path)

    return {
        "hashes": hashes
    }


def serialize_manifest(manifest):
    return json.dumps(
        manifest,
        sort_keys=True,
        separators=(",", ":")
    ).encode("utf-8")


def create_hmac(manifest, key):
    payload = serialize_manifest(manifest)

    return hmac.new(
        key,
        payload,
        hashlib.sha256
    ).hexdigest()


def save_verification(sphere_path):
    key = load_or_create_key()
    manifest = build_manifest(sphere_path)
    manifest["hmac"] = create_hmac(manifest, key)

    verification_path = os.path.join(
        sphere_path,
        VERIFICATION_FILE
    )

    with open(verification_path, "w", encoding="utf-8") as file:
        json.dump(
            manifest,
            file,
            indent=4,
            ensure_ascii=False
        )


def verify_sphere(sphere_path):
    verification_path = os.path.join(sphere_path, VERIFICATION_FILE)

    if not os.path.exists(verification_path):
        return False, ["Verification database doesn't exist."]

    try:
        key = load_or_create_key()

        with open(verification_path, "r", encoding="utf-8") as file:
            stored_manifest = json.load(file)

    except Exception as error:
        return False, [f"Cannot read verification database -> {error}"]

    stored_hashes = stored_manifest.get("hashes")
    stored_hmac = stored_manifest.get("hmac")

    if not isinstance(stored_hashes, dict):
        return False, ["Invalid verification database."]

    if not isinstance(stored_hmac, str):
        return False, ["Verification HMAC is missing."]

    manifest = {
        "hashes": stored_hashes
    }

    expected_hmac = create_hmac(manifest, key)

    if not hmac.compare_digest(expected_hmac, stored_hmac):
        return False, ["Verification database HMAC is invalid."]

    errors = []

    current_files = set(get_sphere_files(sphere_path))
    verified_files = set(stored_hashes.keys())

    missing_files = verified_files - current_files
    added_files = current_files - verified_files

    for filename in sorted(missing_files):
        errors.append(f"Missing Sphere database    -> {filename}")

    for filename in sorted(added_files):
        errors.append(f"Unexpected Sphere database -> {filename}")

    for filename in sorted(current_files & verified_files):
        path = os.path.join(sphere_path, filename)

        current_hash = hash_file(path)
        stored_hash = stored_hashes[filename]

        if not hmac.compare_digest(current_hash, stored_hash):
            errors.append(f"\033[31mHash mismatch -> {filename}\033[0m")

    if errors:
        return False, errors

    return True, []

