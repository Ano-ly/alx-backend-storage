#!/usr/bin/env python3
"""Function that finds a document in a collection"""


def schools_by_topic(mongo_collection, topic):
    """Find a document in a collection"""

    res = mongo_collection.find()
    fil_res = []
    for doc in res:
        if topic in doc.get("topics", []):
            fil_res.append(doc)
        print(doc)
    return (fil_res)
