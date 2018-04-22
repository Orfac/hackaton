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


import ipfsapi
api = ipfsapi.connect('https://ipfs.infura.io', 5001)
res = api.add('test2.txt')
b = res
cd = api.get('QmNwBTB8VR1uYDNU4hnz4dwsGTWW5moeWAZSUczwrCy6r5')
c = api.cat(res['Hash'])
d = api.id()
l = from_ipfs_to_hash(b['Hash'])
print('asd')



