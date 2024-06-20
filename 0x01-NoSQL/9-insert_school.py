#!/usr/bin/env python3
"""Function that creates a dcocument with key-value pairs"""


def insert_school(mongo_collection, **kwargs):
    """Create a document with kwargs and add to collection"""

    my_id = mongo_collection.insert_one(kwargs)
    return (my_id.inserted_id)
