import fire
from license_toolbox.modules.licenser import Licenser

class LicenserCLI:
    def __init__(self):
        self.name: str = "Licenser CLI"
        self.version: float = 0.1

    def generate_license_key(self, key_location: str) -> None:
        l = Licenser()
        l.generate_key(key_location)

    def generate_license_file(self, unecrypted_license_path: str, encrypted_license_path: str = "license", license_key: str=None) -> None:
        l = Licenser()
        l.generate_license_file(unecrypted_license_path, encrypted_license_path, license_key)


def main():
    licensecli = LicenserCLI()
    fire.Fire(licensecli)
