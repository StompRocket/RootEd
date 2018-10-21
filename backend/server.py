from flask import Flask
from flask_cors import CORS
import json
import db
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
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
@app.route("/words/<words>")
def return_json(words):
    words = words.split("-")
    return data_from_words(words)

@app.route("/sets")
def get_set():
    return json.dumps(db.get_sets())
@app.route("/set/<set_id>")

def set_data(set_id):
    return json.dumps(data_from_words(db.get_study_set(set_id)))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(host='127.0.0.1', port=port, debug=True)
