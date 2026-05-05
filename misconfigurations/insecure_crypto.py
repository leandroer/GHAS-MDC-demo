# Insecure Cryptography
from Crypto.Cipher import DES
import hashlib

def insecure_encrypt(plaintext, key):
    """Using insecure DES cipher (56-bit keys)"""
    # VULNERABILITY: DES is cryptographically broken and should not be used
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(plaintext)

def weak_hash(password):
    """Using weak MD5 hash"""
    # VULNERABILITY: MD5 is cryptographically broken
    return hashlib.md5(password.encode()).hexdigest()

def another_weak_hash(password):
    """Using weak SHA1 hash"""
    # VULNERABILITY: SHA1 is deprecated for password hashing
    return hashlib.sha1(password.encode()).hexdigest()
