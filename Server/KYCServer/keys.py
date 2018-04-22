from pymongo import MongoClient


def get_keys():
    client = MongoClient()
    db = client['KeyStorage']
    keys_q = db['keys']
    return keys_q


def add_key_pair(private_key, public_key):
    keys_q = get_keys()
    keys_q.insert_one(
        {'private_key': private_key, 'public_key': public_key}
    )


def get_private_key(public_key):
    keys_q = get_keys()
    key = keys_q.find_one({'public_key': public_key})
    if key is None:
        return None
    else:
        return key['private_key']



