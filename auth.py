from passlib.hash import sha256_crypt

def encrypt(password):
    return sha256_crypt.encrypt(password)

def verify(password, hashed_password):
    return sha256_crypt.verify(password, hashed_password)

