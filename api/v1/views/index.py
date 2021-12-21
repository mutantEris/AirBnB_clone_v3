#!/usr/bin/python3
"""
index module
"""
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import jsonify

names = ["amenities", "cities", "places", "reviews", "states", "users"]
classes = [Amenity, City, Place, Review, State, User]

@app_views.route("/status", methods=["GET"], strict_slashes=False)
def status():
    """
    status of api
    """
    return jsonify({"status": "OK"})


@app_views.route("/stats", methods=["GET"], strict_slashes=False)
def stats():
    """
    Retrieves the number of each object by type
    """
    stats = {}
    for iter in range(len(classes)):
        stats[names[iter]] = storage.count(classes[iter])
    return jsonify(stats)
