
import hashlib
# import globals

def hash_sha512(text: str) -> str:
    return hashlib.sha512(text.encode()).hexdigest()

def check_hash(sphere_db_content: dict, verification_db: dict, username: str):
    try:
        return hash_sha512(sphere_db_content) == verification_db[f"sphere_{username}.qjr"]
    except Exception:
        return False
