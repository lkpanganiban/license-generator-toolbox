import json
from cryptography.fernet import Fernet


class Licenser:
    def __init__(self):
        self.name = "Licenser"
        self.version = 0.1
        self.license_key = "license_key"

    def generate_key(self, output_location: str = "license_key") -> None:
        """
        Generates a key and save it into a file
        """
        key = Fernet.generate_key()
        print(f"generated key: {key}")
        with open(output_location, "wb") as key_file:
            key_file.write(key)

    def _load_key(self) -> bytes:
        """
        Load the previously generated key
        """
        return open(self.license_key, "rb").read()

    def _encrypt_content(self, content: str) -> bytes:
        """
        Encrypts a content
        """
        key = self._load_key()
        encoded_content = content.encode()
        f = Fernet(key)
        return f.encrypt(encoded_content)

    def generate_license_file(
        self,
        unecrypted_license_path: str,
        encrypted_license_path: str = "license",
        license_key: str = None,
    ) -> None:
        if license_key is not None:
            self.license_key = license_key
        print(f"generating encrypted version to: {encrypted_license_path}")
        with open(unecrypted_license_path, "r") as unencrypted_json:
            restrictions = json.load(unencrypted_json)
            content = json.dumps(restrictions)
            enc_content = self._encrypt_content(content)
        with open(encrypted_license_path, "wb") as license_file:
            license_file.write(enc_content)
