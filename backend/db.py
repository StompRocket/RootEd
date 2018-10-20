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
db = client.rooted-vocab
words = db.words


# call this for different JSON files, like for the roots and words
def load_local(json_file):
    for i in json.loads(json_file):
        yield i
