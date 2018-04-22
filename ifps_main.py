import ipfsapi
import json


def from_ipfs_to_hash(hash34):
    byte32array = bytearray(hash34, 'utf-8')
    byte32array.pop(0)
    byte32array.pop(0)
    return list(byte32array)


def from_hash_to_ipfs(hash32):
    hash32.insert(0, 109)
    hash32.insert(0, 81)
    return hash32.encode('utf-8')


def connection_to_ipfs_net():
    return ipfsapi.connect('https://ipfs.infura.io', 5001)


def send_to_ipfs(path):
    api = connection_to_ipfs_net()
    res = api.add(path)
    return from_ipfs_to_hash(res['hash'])


def get_from_ipfs(hash):
    transport_hash = from_hash_to_ipfs(hash)
    return api.get(transport_hash)



