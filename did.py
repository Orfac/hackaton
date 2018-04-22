from urllib import request

class did:
    def __init__(self):
        self.d = __get_did()

    def __get_did(self):
        return request.urlopen("http://127.0.0.1:5000/api/1.0/newDid")

        req = urllib2.Request('http://127.0.0.1:5000/api/1.0/')
        req.add_header('Content-Type', 'application/json')

        response = urllib2.urlopen(req, json.dumps(data))

    def get_file(public_key):
        req = urllib2.Request('http://127.0.0.1:5000/api/1.0/')
        req.add_header('Content-Type', 'application/json')
        response = urllib2.urlopen(req, json.dumps({"public_key": public_key}))