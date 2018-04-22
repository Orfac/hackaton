import ipfsapi
import  json

def from_ipfs_to_hash(hash34):
    return hash34[1:len(hash34)]


def from_hash_to_ipfs(hash32):
    
    return chr(81) + chr(109)  + hash32


def connection_to_ipfs_net():
    return ipfsapi.connect('https://ipfs.infura.io', 5001)


def send_to_ipfs(json_f):
    api = connection_to_ipfs_net()
    

    res = api.add('test.txt')
    print(len(res['Hash']))
    return from_ipfs_to_hash(res['Hash'])


def get_from_ipfs(hash):
    transport_hash = from_hash_to_ipfs(hash)
    api = connection_to_ipfs_net()
    return api.get(transport_hash)



