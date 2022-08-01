# License Generator
Creates a license key and file to be used in the pipeline.

## Terms
 - License Key: act as the encryption and decryption mechanism
 - License File: The encrypted file containing the restrictions like expiration dates, process limits, etc.

## Usage
1. Run `generate_key.py` this will generate a `license_key` file.
2. Copy the contents of the `license_key` file.
3. Add the copied contents inside your script/module to be protected. Remember to set the type as a `b` or binary instead of string.
4. Create an `unecrypted.json` this will serve as the container where you put the credentials, expiry, etc.
5. Run the `generate_license.py` this will create a `license` file. 

## Developers
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