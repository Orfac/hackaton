import rsa


def generate_keys():
    public_key, private_key = rsa.newkeys(512)
    return private_key, public_key


def encrypt_message(a_message, publickey):
    crypto = rsa.encrypt(a_message, publickey)
    return crypto


def decrypt_message(encoded_encrypted_msg, privatekey):
    message = rsa.decrypt(encoded_encrypted_msg,privatekey)
    message = message.decode('utf8')
    return message

