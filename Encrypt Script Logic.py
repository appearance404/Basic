# Encrypt critical parts of your script and decrypt them at runtime. Here’s a basic example of encrypting a string and decrypting it:

from Crypto.Cipher import AES
import base64

def encrypt_logic(data, key):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data.encode())
    return base64.b64encode(nonce + tag + ciphertext).decode()

def decrypt_logic(data, key):
    data = base64.b64decode(data)
    nonce, tag, ciphertext = data[:16], data[16:32], data[32:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag).decode()

key = b'secret_key_123456'  # Must be 16, 24, or 32 bytes long
encrypted_data = encrypt_logic("Sensitive operation", key)
decrypted_data = decrypt_logic(encrypted_data, key)
print(decrypted_data)
