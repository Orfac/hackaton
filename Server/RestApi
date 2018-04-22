import json
import requests

def add_block(public_key, public_key_ico, hash):
    
    url = 'http://127.0.0.1:5000/api/1.0/new'

    answer = requests.post(url, json= {
        "public_key": public_key,
        "public_key_ico": public_key_ico,
        "hash": hash }
        )
    
