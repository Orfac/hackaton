import crypto.PublicKey.RSA
import random

def generate_keys():
    # module_length кратен 256 и больше 1024
    module_length = 256 * 16
    private_key = RSA.generate(module_length, Random.new().read)
    public_key = privatekey.publickey()
    return {'private': private_key, 'public': public_key}


def encrypt_message(a_message, publickey):
    encrypted_msg = publickey.encrypt(a_message, 32)[0]
    encoded_encrypted_msg = base64.b64encode(encrypted_msg)
    return encoded_encrypted_msg


def decrypt_message(encoded_encrypted_msg, privatekey):
    decoded_encrypted_msg = base64.b64decode(encoded_encrypted_msg)
    decoded_decrypted_msg = privatekey.decrypt(decoded_encrypted_msg)
    return decoded_decrypted_msg
