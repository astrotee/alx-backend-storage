#!/usr/bin/env python3
"pymongo"

def list_all(mongo_collection):
    "list all documents in the passed collection"
    return mongo_collection.find()
