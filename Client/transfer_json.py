import json
from crypt import encrypt_message, decrypt_message
from ifps_main import send_to_ipfs, get_from_ipfs
import RestApi


def send_json(message,public_key):
    encoding_message = encrypt_message(message, public_key)

    return send_to_ipfs(
        json.dumps({"message": str(encoding_message)})
        )



def get_json(hash, private_key):
    encoded_message = get_from_ipfs(hash)
    return decrypt_message(encoded_message, private_key)["message"]


def send_to_another_customer(public_key, public_key_ico, hash):
    add_block(public_key, public_key_ico, hash)
