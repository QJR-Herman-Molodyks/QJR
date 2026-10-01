# # migrate_users.py
# import json
# from crypto_items import encrypt_users_db, hash_password
#
# # Завантажувати поточний (незашифрований) файл
# with open("db/users.qjr", "r") as f:
#     old_users = json.load(f)
#
# # Перетворити на нову структуру
# new_users = {}
# for username, data in old_users.items():
#     new_users[username] = {
#         "password": data["password"],  # Вже захешовані паролі
#         "permission": {
#             "admin": 2,
#             "user": 1,
#             "guest": 0
#         }.get(username, 0)  # Встановлюємо permission за username
#     }
#
# # Шифруємо
# encrypted_users = encrypt_users_db(new_users)
#
# # Зберігаємо в новий файл
# with open("db/users.qjr", "w") as f:
#     json.dump(encrypted_users, f, indent=4)
#
# print("✅ Users DB encrypted successfully!")
# print(json.dumps(encrypted_users, indent=4))
#
# import json
# from crypto_items import encrypt_users_db
#
# # Завантаження старої БД
# with open("db/users.qjr", "r") as f:
#     old_users = json.load(f)
#
# # Нова структура
# new_users = {}
#
# role_map = {
#     "admin": 2,
#     "user": 1,
#     "guest": 0
# }
#
# permission = role_map.get(username, 0)
#
# for username, data in old_users.items():
#     new_users[username] = {
#         "password": data["password"],
#         "role": data.get("role", "guest"),
#         "permission": role_map.get(data.get("role", "guest"), 0)
#     }
#     new_users[username] = {
#         # якщо вже було захешовано — не чіпаємо
#         "password": data["password"],
#
#         # нормальна мапа ролей (краще ніж username-based)
#         # "permission": {
#         #     "admin": 2,
#         #     "user": 1,
#         #     "guest": 0
#         # }.get(data.get("role", "user"), 1)
#
#     }
#
# # Шифрування
# encrypted_users = encrypt_users_db(new_users)
#
# # Збереження
# with open("db/users.qjr", "w") as f:
#     json.dump(encrypted_users, f, indent=4)
#
# print("Users DB encrypted successfully")
import json
import hashlib
import hmac

from crypto_items import encrypt_users_db, decrypt_users_db

# -----------------------------
# CONFIG
# -----------------------------

ROLE_MAP = {
    "admin": 2,
    "user": 1,
    "guest": 0
}

SECRET_KEY = b"QJR_SECRET_KEY_CHANGE_ME"  # для HMAC (за бажанням)

# -----------------------------
# HELPERS
# -----------------------------

def sha512(data: str) -> str:
    return hashlib.sha512(data.encode("utf-8")).hexdigest()


def make_hmac(data: str) -> str:
    return hmac.new(SECRET_KEY, data.encode("utf-8"), hashlib.sha512).hexdigest()

# -----------------------------
# LOAD OLD DB
# -----------------------------

with open("db/users.qjr", "r") as f:
    raw = json.load(f)

# якщо БД зашифрована — розшифруй
try:
    old_users = decrypt_users_db(raw)
except Exception:
    old_users = raw  # fallback якщо вже plain

# -----------------------------
# MIGRATION
# -----------------------------

new_users = {}

for username, data in old_users.items():

    # -------------------------
    # PASSWORD FIX (IMPORTANT)
    # -------------------------
    password = data.get("password", "")

    # якщо раптом пароль НЕ hex SHA512 — можна нормалізувати
    # (але НЕ подвійно хешувати)
    if len(password) != 128:
        password = sha512(password)

    # -------------------------
    # ROLE / PERMISSION FIX
    # -------------------------

    role = data.get("role", username)  # fallback старого стилю
    permission = ROLE_MAP.get(role, ROLE_MAP.get(username, 0))

    # -------------------------
    # BUILD NEW USER OBJECT
    # -------------------------

    new_users[username] = {
        "password": password,
        "permission": permission,
        "role": role
    }

# -----------------------------
# OPTIONAL: HMAC INTEGRITY LAYER
# -----------------------------

db_string = json.dumps(new_users, sort_keys=True)
db_hmac = make_hmac(db_string)

final_db = {
    "data": new_users,
    "hmac": db_hmac
}

# -----------------------------
# ENCRYPT + SAVE
# -----------------------------

# encrypted = encrypt_users_db(final_db)
encrypted = encrypt_users_db(final_db["data"])

with open("db/users.qjr", "w") as f:
    json.dump(encrypted, f, indent=4)

print("✅ Migration completed successfully!")
print(json.dumps(final_db, indent=4))