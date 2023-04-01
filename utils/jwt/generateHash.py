import re
import hashlib

def generate_hash_password(password, value='indicator'):
    # value 作为混淆字符串
    sha256 = hashlib.sha256(password.encode("utf-8"))
    sha256.update(value.encode("utf-8"))
    password_sha256 = sha256.hexdigest()
    return password_sha256