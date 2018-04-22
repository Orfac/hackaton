import ipfsapi

def from_ipfs_to_hash(hash34):
    byte32array = bytearray(hash34, 'utf-8')
    byte32array.pop(0)
    byte32array.pop(0)
    return list(byte32array)

def from_hash_to_ipfs(hash32):
    byte34array = bytearray(hash32, 'utf-8')
    byte34array.insert(0, 81)
    byte34array.insert(0, 109)
    return list(byte34array)

def connection_to_ipfs_net():
    return ipfsapi.connect('https://ipfs.infura.io', 5001)

def send_to_ipfs(json_f):
    api = connection_to_ipfs_net()
    res = api.add(json_f)
    return from_ipfs_to_hash(res['hash'])

def get_from_ipfs(hash):
   return api.get(hash)


