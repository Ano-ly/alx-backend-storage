#!/usr/bin/env python3
"""Use pymongo to work with MongoDB database"""


def list_all(mongo_collection):
    """List all documents in a collection"""
    ret_list = []
    for doc in mongo_collection.find():
        ret_list.append(eval(doc))
    return (doc)
