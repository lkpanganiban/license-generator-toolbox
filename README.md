# License Generator
Creates a license key and file to be used in protecting your code.

## Terms
 - License Key: act as the encryption and decryption mechanism
 - License File: The encrypted file containing the restrictions like expiration dates, process limits, etc.

## Usage
- Generating a license key
    ```
    license-generator generate-license-key <output-license-key-file>
    ```
- Generating an encrypted file
    ```
    license-generator generate-license-file <json-file-to-be-encrypted> <output-encrypted-file> <license-key-file>
    ```

## Notes
- The file to be encrypted only has support for json format.
- The generated license_key can be used similar to the following code.
    ```
    def decrypt_message(self, encrypted_message):
        """
        Decrypts an encrypted message
        """
        self.license_key = b'<license-key>'
        f = Fernet(self.license_key)
        decrypted_message = f.decrypt(encrypted_message)
        return decrypted_message.decode()
    ```
- You can use the encrypted license file to contain the expiration or the count of licenses being used.