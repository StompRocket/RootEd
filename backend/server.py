from bottle import route, run, get
import json
import db
import os

@route("/")
def return_all():
    return db.dump()

@route("/words/<words>")
def return_json(words):
    words = words.split("-")
    rwords = {}
    rroots = {}
    for word in words:
        print(word)
        rwords[word] = {
                "roots": [ w for w in db.get_word_roots(word) ],
                "definition": db.get_word_definition(word)
            }
        print(rwords[word])

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    run(host='127.0.0.1', port=port, debug=True)
