import pymongo
from pymongo import MongoClient
import requests
import json
from bson.json_util import dumps
import json
from flask import Flask, jsonify, request, _request_ctx_stack, render_template
import os
import mongoservices
import mapservices
from flask_cors import cross_origin
from functools import wraps
from six.moves.urllib.request import urlopen
from jose import jwt
import sys
import random


class mongoservices:

    def condb(self):
        uri = 'mongodb+srv://superkious:Ray100182@cluster0.rrbkqgx.mongodb.net/?retryWrites=true&w=majority'
        # create client
        client = MongoClient(uri)
        db = client.Towing
        return db
        
    def save_sample(self, data):
        try:
            db = mongoservices.condb(self)
            samples_coll = db.AllRideRequests
            samples_coll.insert_one(data)
            return jsonify({"code":"1","status":"success"})
        except Exception as ex:
            return jsonify({"code":"0","status":ex})

    def save_sample(self, data):
        try:
            db = mongoservices.condb(self)
            samples_coll = db.AllRideRequests
            samples_coll.insert_one(data)
            return jsonify({"code":"1","status":"success"})
        except Exception as ex:
            return jsonify({"code":"0","status":ex})

    def update_sample(self, data, upd):
        try:
            db = mongoservices.condb(self)
            samples_coll = db.AllRideRequests
            collection.update_one(data, upd)
            samples_coll.insert_one(data)
            return jsonify({"code":"1","status":"success"})
        except Exception as ex:
            return jsonify({"code":"0","status":ex})

    def select_sample(self, data):
        try:
            #return jsonify(data)
            db = mongoservices.condb(self)
            samples_coll = db.AllRideRequests
            cursor = samples_coll.find(data, {"_id": 0 }).sort("_id", -1).limit(1)
            #cursor = samples_coll.find_one(data, {"_id": 0 })
            #json_data = json.dumps(cursor)
            #return jsonify(json_data)  
            #return jsonify({"code":"1","status" : "ok"})
            list_cur = list(cursor)
            json_data = dumps(list_cur)
            return jsonify({"code":"1","status" : "ok", "data": json_data})
        except Exception as ex:
            return jsonify({"code":"0","status":ex})

    def select_driver(self, data):
        try:
            #return jsonify(data)
            db = mongoservices.condb(self)
            samples_coll = db.AllRideRequests
            cursor = samples_coll.find(data, {"_id": 0 }).sort("_id", -1)
            list_cur = list(cursor)
            json_data = dumps(list_cur)
            #return jsonify(json_data)  
            #return jsonify({"code":"1","status" : "ok"})
            return jsonify({"code":"1","status" : "ok", "data": json_data})
        except Exception as ex:
            return jsonify({"code":"0","status":ex})
            
    def save_smpl(self, data):
        try:
            url = "https://ap-southeast-1.aws.data.mongodb-api.com/app/data-lbmdo/endpoint/data/v1/action/insertOne"
            payload = json.dumps({
                "collection": "AllRideRequests",
                "database": "Towing",
                "dataSource": "Cluster0",
                "document" :   data 
                })
            headers = {
                'Content-Type': 'application/json',
                'Access-Control-Request-Headers': '*',
                'api-key': 'ey8rbwtawEydjeAMhEBOQyY9liOjWfz6qmYQF2zdaFoCy5QadhV8GwroSPybZELL'
                }
            response = requests.request("POST", url, headers=headers, data=payload)
            return jsonify({"code":"1","status":response.text})
        except Exception as ex:
            return jsonify({"code":"0","status":ex})
