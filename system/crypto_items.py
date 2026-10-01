#
# import hashlib
# import base64
# import hmac
# import time
# import globals
#
# def hash_password_256(password: str) -> str:
#     return hashlib.sha256(password.encode()).hexdigest()
#
# def hash_password(password: str) -> str:
#     # hash1 = hashlib.sha512(password.encode()).hexdigest()
#     # return hashlib.sha512(hash1.encode()).hexdigest()
#     return hashlib.sha512(password.encode()).hexdigest()
#
# # def hash_auth(auth_time: str) -> str:
# #     hash_1 = hashlib.sha512(auth_time.encode()).hexdigest()
# #     hash_2 = hashlib.sha512(hash_1.encode()).hexdigest()
# #     hash_3 = hashlib.sha512(hash_2.encode()).hexdigest()
# #     hash_4 = hashlib.sha512(hash_3.encode()).hexdigest()
# #     hash_5 = hashlib.sha512(hash_4.encode()).hexdigest()
# #     hash_6 = hashlib.sha512(hash_5.encode()).hexdigest()
# #     hash_7 = hashlib.sha512(hash_6.encode()).hexdigest()
# #     hash_8 = hashlib.sha512(hash_7.encode()).hexdigest()
# #     hash_9 = hashlib.sha512(hash_8.encode()).hexdigest()
# #     hash_10 = hashlib.sha512(hash_9.encode()).hexdigest()
# #     hash_11 = hashlib.sha512(hash_10.encode()).hexdigest()
# #     hash_12 = hashlib.sha512(hash_11.encode()).hexdigest()
# #     hash_13 = hashlib.sha512(hash_12.encode()).hexdigest()
# #     hash_14 = hashlib.sha512(hash_13.encode()).hexdigest()
# #     hash_15 = hashlib.sha512(hash_14.encode()).hexdigest()
# #     return hashlib.sha512(hash_15.encode()).hexdigest()
#
# SECRET_KEY = "qjr-signature-s&St3m"
#
# def encrypt_ban_time(ban_until: int) -> str:
#     """Шифрує час із HMAC підписом"""
#     ban_str = str(ban_until)
#     signature = hmac.new(
#         SECRET_KEY.encode(),
#         ban_str.encode(),
#         hashlib.sha512
#     ).hexdigest()
#     # return f"{ban_str}:{signature}"
#     return f"{ban_str}>{signature}"
#
# def decrypt_ban_time(encrypted: str) -> int:
#     """Перевіряє HMAC і повертає час"""
#     try:
#         # ban_str, signature = encrypted.split(':')
#         # ban_str, signature = encrypted.split('>')
#         ban_str, signature = encrypted.rsplit('>', 1)
#         # ban_str, signature = encrypted.rsplit(':', 1)
#
#         # Перевіряємо підпис
#         expected_signature = hmac.new(
#             SECRET_KEY.encode(),
#             ban_str.encode(),
#             hashlib.sha512
#         ).hexdigest()
#
#         # Перевірка цілісності
#         if not hmac.compare_digest(signature, expected_signature):
#             print("❌ File has changed! Signature is not matched!")
#             raise ValueError("Invalid signature")
#
#         return int(ban_str)
#     except ValueError as e:
#         print(f"Error: {e}")
#         return -1  # -1 = помилка дешифрування (не плутати з 0!)
#
#
# def is_user_banned(encrypted_ban_time: str) -> bool:
#     """Перевіряє, чи користувач забанено"""
#     ban_until = decrypt_ban_time(encrypted_ban_time)
#
#     if ban_until == -1:
#         print("⚠️ Помилка розшифрування! Користувач не має доступу.")
#         return True  # Забороняємо доступ при помилці (безпека)
#
#     if ban_until == 0:
#         return False  # Не забанено
#
#     current_time = int(time.time())
#     return current_time < ban_until
#
#
# import json
#
#
# # Функції для署名 користувачів
# def generate_user_key(username: str) -> str:
#     """Генерує унікальний ключ для користувача"""
#     # return hashlib.sha256(f"{SECRET_KEY}:{username}".encode()).hexdigest()
#     return hashlib.sha256(f"{SECRET_KEY}>{username}".encode()).hexdigest()
#
#
# def sign_user_field(username: str, field_value: str) -> str:
#     """Підписує окреме поле користувача HMAC"""
#     user_key = generate_user_key(username)
#     signature = hmac.new(
#         user_key.encode(),
#         field_value.encode(),
#         hashlib.sha512
#     ).hexdigest()
#     # return f"{field_value}:{signature}"
#     return f"{field_value}>{signature}"
#
#
# def verify_user_field(username: str, signed_field: str) -> tuple[bool, str]:
#     """Перевіряє HMAC поля і повертає (valid, value)"""
#     try:
#         # field_value, signature = signed_field.split(':')
#         # field_value, signature = signed_field.split('>')
#         field_value, signature = signed_field.rsplit('>', 1)
#         user_key = generate_user_key(username)
#
#         expected_signature = hmac.new(
#             user_key.encode(),
#             field_value.encode(),
#             hashlib.sha512
#         ).hexdigest()
#
#         if not hmac.compare_digest(signature, expected_signature):
#             print(f"❌ User field compromised! Signature mismatch for {username}")
#             globals.set_banned(username)
#             return False, ""
#
#         return True, field_value
#     except ValueError as e:
#         print(f"❌ Error verifying field: {e}")
#         globals.set_banned(username)
#         return False, ""
#
#
# def encrypt_users_db(users_dict: dict) -> dict:
#     """Шифрує весь users dict з HMAC підписами"""
#     encrypted = {}
#
#     for username, data in users_dict.items():
#         encrypted[username] = {
#             # "password": sign_user_field(username, data["password"]),
#             "password": hash_password(data["password"]),
#             # "password": hashlib.sha512(data["password"].encode()).hexdigest(),
#             "permission": sign_user_field(username, str(data["permission"])),
#         }
#
#     return encrypted
#
#
# def decrypt_users_db(encrypted_dict: dict) -> dict:
#     """Дешифрує users dict і перевіряє підписи"""
#     decrypted = {}
#
#     for username, data in encrypted_dict.items():
#         # pwd_valid, password = verify_user_field(username, data["password"])
#         # pwd_valid, password = len(data["password"])==512
#         perm_valid, permission = verify_user_field(username, data["permission"])
#
#         # if not (pwd_valid and perm_valid):
#         if not perm_valid:
#             print(f"⚠️ User {username} data is corrupted!")
#             globals.set_banned(username)
#             continue
#
#         decrypted[username] = {
#             # "password": password,
#             "password": encrypted_dict[username]["password"],
#             "permission": int(permission),
#         }
#
#     return decrypted
#
#
# def get_permission_name(perm_level: int) -> str:
#     """Піксає ім'я рівня доступу"""
#     levels = {0: "Guest", 1: "User", 2: "Admin"}
#     return levels.get(perm_level, "Unknown")
#
# # def unwrap_signed_field(username: str, signed_field: str) -> str | None:
# #
# #     current = signed_field
# #
# #     while ">" in current:
# #         try:
# #             value, signature = current.rsplit(">", 1)
# #
# #             user_key = generate_user_key(username)
# #
# #             expected_signature = hmac.new(
# #                 user_key.encode(),
# #                 value.encode(),
# #                 hashlib.sha512
# #             ).hexdigest()
# #
# #             if not hmac.compare_digest(signature, expected_signature):
# #                 print("❌ Invalid signature")
# #                 return None
# #
# #             current = value
# #
# #         except Exception as e:
# #             print(f"❌ Error: {e}")
# #             return None
# #
# #     return current
#
#
# # for i in range(1, 16):
# #     print(f"hash_{i} = hashlib.sha512(hash_{i-1}.encode()).hexdigest()")
#
# # print(hash_password("admin"))
# # print(hash_password("1234"))
# # print(hash_password("bogdan1234"))
#
# # print(hash_auth("0"))
# # print(encode_auth('0'))
#
# # import hashlib
# # import os
# #
# # password = "my_password".encode()
# # salt = os.urandom(16)
# # print(f"Salt > {salt}")
# #
# # hashed = hashlib.pbkdf2_hmac(
# #     "sha256",
# #     password,
# #     salt,
# #     100000
# # )
# # print(hashed)
import hashlib
import hmac
import time
import globals

SECRET_KEY = "qjr-signature-s&St3m"


# -------------------------
# HASHING (SHA-512)
# -------------------------

def hash_txt(text: str) -> str:
    return hashlib.sha512(text.encode()).hexdigest()

def hash_password(password: str) -> str:
    # """Подвійний SHA-512 хеш пароля"""
    # first = hashlib.sha512(password.encode()).hexdigest()
    # return hashlib.sha512(first.encode()).hexdigest()
    return hashlib.sha512(password.encode()).hexdigest()


def hash_password_256(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


# -------------------------
# BAN TIME (HMAC)
# -------------------------
def encrypt_ban_time(ban_until: int) -> str:
    """Підпис часу бана"""
    ban_str = str(ban_until)

    signature = hmac.new(
        SECRET_KEY.encode(),
        ban_str.encode(),
        hashlib.sha512
    ).hexdigest()

    return f"{ban_str}>{signature}"


def decrypt_ban_time(encrypted: str) -> int:
    """Перевірка HMAC та отримання часу"""
    try:
        ban_str, signature = encrypted.rsplit(">", 1)

        expected = hmac.new(
            SECRET_KEY.encode(),
            ban_str.encode(),
            hashlib.sha512
        ).hexdigest()

        if not hmac.compare_digest(signature, expected):
            raise ValueError("Invalid signature")

        return int(ban_str)

    except Exception:
        return -1


def is_user_banned(encrypted_ban_time: str) -> bool:
    ban_until = decrypt_ban_time(encrypted_ban_time)

    if ban_until == -1:
        return True

    if ban_until == 0:
        return False

    return int(time.time()) < ban_until


# -------------------------
# USER KEY + HMAC FIELDS
# -------------------------
def generate_user_key(username: str) -> str:
    return hashlib.sha256(f"{SECRET_KEY}>{username}".encode()).hexdigest()


def sign_user_field(username: str, value: str) -> str:
    user_key = generate_user_key(username)

    signature = hmac.new(
        user_key.encode(),
        value.encode(),
        hashlib.sha512
    ).hexdigest()

    return f"{value}>{signature}"


def verify_user_field(username: str, signed_value: str) -> tuple[bool, str]:
    try:
        value, signature = signed_value.rsplit(">", 1)

        user_key = generate_user_key(username)

        expected = hmac.new(
            user_key.encode(),
            value.encode(),
            hashlib.sha512
        ).hexdigest()

        if not hmac.compare_digest(signature, expected):
            globals.set_banned(username)
            return False, ""

        return True, value

    except Exception:
        globals.set_banned(username)
        return False, ""


# -------------------------
# USERS DB ENCRYPTION
# -------------------------
def encrypt_users_db(users_dict: dict) -> dict:
    encrypted = {}

    for username, data in users_dict.items():
        encrypted[username] = {
            # "password": hash_password(data["password"]),
            # "password": data["password"],
            "password": sign_user_field(username, data["password"]),
            "permission": sign_user_field(username, str(data["permission"])),
        }

    return encrypted


def decrypt_users_db(encrypted_dict: dict) -> dict:
    decrypted = {}

    for username, data in encrypted_dict.items():

        pwd_valid, password = verify_user_field(username, data["password"])
        perm_valid, permission = verify_user_field(username, data["permission"])

        if not (pwd_valid and perm_valid):
            globals.set_banned(username)
            continue

        decrypted[username] = {
            "password": password,
            "permission": int(permission),
        }

    return decrypted


def get_permission_name(level: int) -> str:
    return {
        0: "Guest",
        1: "User",
        2: "Admin"
    }.get(level, "Unknown")

def check_user_password(user_db: dict, request_password: str) -> bool:
    return hash_password(request_password) == user_db[request_password]["password"].rsplit(">")[0]