import ipfsapi
from RestApi import *

from did import did


def main():
    #add_transaction("asdas","asdas","asda")
    api = ipfsapi.connect('https://ipfs.infura.io', 5001)
    res = api.add('hello.txt')
    b = res
    cd = api.get('QmNwBTB8VR1uYDNU4hnz4dwsGTWW5moeWAZSUczwrCy6r5')
    d = api.id()
    print(d)

if __name__ == "__main__":
    main()
