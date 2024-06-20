#!/usr/bin/env python3
"""Use pymongo to work with MongoDB database"""


def top_students(mongo_collection):
    """Return students sorted by average score"""

    for doc in mongo_collection.find():
        scores = [item["score"] for item in doc["topics"]]
        avg_score = sum(scores)/len(scores)
        mongo_collection.update_one(
            {"_id": doc["_id"]},
            {"$set": {"averageScore": avg_score}}
        )
    ret = mongo_collection.aggregate([{"$sort": {"averageScore": -1}}])
    return (list(ret))
