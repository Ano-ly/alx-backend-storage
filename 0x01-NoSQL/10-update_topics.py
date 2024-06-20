#!/usr/bin/env python3
"""Function that creates a dcocument with key-value pairs"""


def update_topics(mongo_collection, name, topics):
    """Add/ update topics in document"""

    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
