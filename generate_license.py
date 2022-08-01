import json
from cryptography.fernet import Fernet


def load_key():
    """
    Load the previously generated key
    """
    return open("license_key", "rb").read()

def encrypt_message(message):
    """
    Encrypts a message
    """
    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    
    return encrypted_message

def generate_license_file(encrypted_mesage):
    with open("license", "wb") as license_file:
        license_file.write(encrypted_mesage)

if __name__ == "__main__":
    with open("unencrypted.json", "r") as unencrypted_json:
        restrictions = json.load(unencrypted_json)
    message = json.dumps(restrictions)
    encmessage = encrypt_message(message)
    generate_license_file(encmessage)
