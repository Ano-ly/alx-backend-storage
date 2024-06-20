#!/usr/bin/env python3
"""Function that finds a document in a collection"""


def update_topics(mongo_collection, name, topics):
    """Find a document in a collection"""

    res = mongo_collection.find()
    fil_res = []
    for doc in res:
        if topics in doc.topics:
            fil_res.append(doc)
    return (fil_res)
