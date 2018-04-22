import ipfsapi


def from_ipfs_to_hash(hash34):
    return hash34.encode('utf-8')[2:]


def from_hash_to_ipfs(hash32):
    hash32.insert(0, 109)
    hash32.insert(0, 81)
    return hash32.encode('utf-8')


def connection_to_ipfs_net():
    return ipfsapi.connect('https://ipfs.infura.io', 5001)


def send_to_ipfs(json_f):
    api = connection_to_ipfs_net()
    res = api.add(json_f)
    return from_ipfs_to_hash(res['hash'])


def get_from_ipfs(hash):
   return api.get(hash)


