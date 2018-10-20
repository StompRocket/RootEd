import json
from pymongo import MongoClient

# JSON Structure

structure = {
    "words": {
        "biology": {
            "roots": [
                "bio",
                "logy"
            ],
            "definition": "The science of life and of living organisms, including their structure, function, growth, origin, evolution, and distribution. It includes botany and zoology and all their subdivisions."
        },
        "biochemistry": {
            "roots": [
                "bio",
                "chem"
            ],
            "definition": "The study of the chemical substances and vital processes occurring in living organisms; biological chemistry; physiological chemistry."
        }
    },
    "roots": {
        "bio": "Life",
        "logy": "The study of",
        "chem": "Small Atom Things"
    }
}

print(json.dumps(structure))

client = MongoClient()
db = client.rootedvocab
words = db.words
roots = db.roots

# call this for different JSON files, like for the roots and words
def load_local(json_file):
    with open(json_file, "r") as data:
        f = data.read()
        data.close()

    print(f)
    for i in json.loads(f):
        yield i

# load the roots to the DB
for root in load_local("roots.json"):
    roots.insert_one(root)

for word in load_local("words.json"):
    words.insert_one(word)

def get_word_definition(word):
    return words.find_one({"word": word})["definition"]

def get_word_roots(word):
    for root in words.find_one({"word": word})["roots"]:
        yield root
