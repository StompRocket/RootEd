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
study_sets = db.study_sets

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

for study_set in load_local("sets.json"):
    study_sets.insert_one(study_set)

def get_word_definition(word):
    return words.find_one({"word": word})["definition"]

def get_word_roots(word):
    for root in words.find_one({"word": word})["roots"]:
        yield root
def get_root_definition(root):
    return roots.find_one({"root": root})["definition"]

def get_study_set(set_id):
    return study_sets.find_one({"id": set_id})["words"]

def get_sets():
    prot = {}
    for study_set in study_sets.find({}):
        prot[study_set["id"]] = study_set["words"]

    return prot
