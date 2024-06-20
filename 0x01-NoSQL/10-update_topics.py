#!/usr/bin/env python3
"""Function that updates a document"""


def update_topics(mongo_collection, name, topics):
    """Add/ update topics in document"""

    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}},
        upsert=True
    )
