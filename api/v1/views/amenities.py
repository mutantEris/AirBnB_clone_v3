#!/usr/bin/python3
"""Creates a new view for Amenity objects"""
from api.v1.views import app_views
from models.amenity import Amenity
from models import storage
from flask import jsonify, abort, request

@app_views.route('/amenities', methods=['GET', 'POST'])
def amenities():
    if request.method == 'GET':
        allmenities = storage.all('Amenity')
        allmenities = [obj.to_json() for obj in allmenities.values()]
        return jsonify(allmenities)
    if request.method == 'POST':
        req = request.get_json()
        if req is None:
            abort(400, 'Not a JSON')
        if req.get('name') is None:
            abort(400, 'Missing name')
        noo = Amenity(**req)
        noo.save()
        return jsonify(x.to_json()), 201
