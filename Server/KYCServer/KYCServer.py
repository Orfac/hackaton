import flask
from flask import Flask, request, jsonify, Response
import json
from ledger import *

app = Flask(__name__)

def to_json(data):
    return json.dumps(data) + "\n"

def resp(code, data):
    return Response(
        status=code,
        mimetype="applicataion/json",
        response=to_json(data)
        )

def affected_num_to_code(cnt):
    code = 200
    if cnt == 0:
        code = 404
    return code

# e.g. failed to parse json
@app.errorhandler(400)
def page_not_found(e):
    return resp(400, {})

@app.errorhandler(404)
def page_not_found(e):
    return resp(400, {})

@app.errorhandler(405)
def page_not_found(e):
    return resp(405, {})


@app.route('/api/1.0/new', methods=['POST'])
def get_file():
    content = request.json
    add_transaction(content['public_key'],
                   content['public_key_ico'],
                   content['hash'])

    return resp(200, "OK")


if __name__ == '__main__':
    app.debug = True  # enables auto reload during development
    app.run()