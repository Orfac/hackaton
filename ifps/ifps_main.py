import ipfsapi
api = ipfsapi.connect('127.0.0.1', 5001)
res = api.add('test.txt')
print(res)
print(api.cat(res['Hash']))
print(api.id())
