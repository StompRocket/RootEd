from bottle import route, run, get
import json
import db
import os

def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if bottle.request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors

@route("/")
@enable_cors
def return_all():
    return db.dump()

def data_from_words(words):
    rwords = {}
    rroots = {}
    for word in words:
        print(word)
        rwords[word] = {
                "roots": [ w for w in db.get_word_roots(word) ],
                "definition": db.get_word_definition(word)
            }
        for root in db.get_word_roots(word):
            rroots[root] = db.get_root_definition(root)

    return {
        "words": rwords,
        "roots": rroots
    }
@route("/words/<words>")
@enable_cors
def return_json(words):
    words = words.split("-")
    return data_from_words(words)
@enable_cors
@route("/sets")
def get_set():
    return json.dumps(db.get_sets())
@enable_cors
@route("/set/<set_id>")
def set_data(set_id):
    return json.dumps(data_from_words(db.get_study_set(set_id)))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    run(host='127.0.0.1', port=port, debug=True)
