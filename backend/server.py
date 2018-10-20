from bottle import route, run, get
import json
import db

@route("/")
def return_all():
    return db.dump()

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    run(host='127.0.0.1', port=port, debug=True)
