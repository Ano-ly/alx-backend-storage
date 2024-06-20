#!/usr/bin/env python3
"""Function that creates a dcocument with key-value pairs"""


def insert_school(mongo_collection, **kwargs):
    """Create a document with kwargs and add to collection"""

    document1 = dict()
    for item, value in kwargs.items():
        document1.update({item: value})
    my_id = mongo_collection.insert_one(document1)
    return (my_id.inserted_id)
