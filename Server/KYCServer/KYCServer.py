import flask
import json
import postgresql
import uuid

app = flask.Flask(__name__)

def create_db():
    db.execute("CREATE TABLE (id SERIAL PRIMARY KEY, public_key not null varchar(40) Unique, hash varchar(40) not null Unique)")

def db_conn():
    return postgresql.open('pq://eax@localhost/eax')

def to_json(data):
    return json.dumps(data) + "\n"

def resp(code, data):
    return flask.Response(
        status=code,
        mimetype="applicataion/json",
        response=to_json(data)
        )

def did_validate():
    errors = []
    json = flask.request.get_json()
    if json is None:
        errors.append(
            "No JSON sent. Did you forget to set Content-Type header" +
            " to application/json?")
        return (None, errors)

    return (json, errors)

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

@app.route('/api/1.0/newDid', methods=['GET'])
def get_did():
    
    return resp(200, {"did": str(uuid.uuid4())})

@app.route('/api/1.0/', methods=['POST'])
def post_theme():
    (json, errors) = theme_validate()
    if errors:  # list is not empty
        return resp(400, {"errors": errors})

    with db_conn() as db:
        insert = db.prepare(
            "INSERT INTO themes (title, url) VALUES ($1, $2) " +
            "RETURNING id")
        [(theme_id,)] = insert(json['title'], json['url'])
        return resp(200, {"theme_id": theme_id})


if __name__ == '__main__':
    app.debug = True  # enables auto reload during development
    create_db()
    app.run()