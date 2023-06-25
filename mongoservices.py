import pymongo
from pymongo import MongoClient
from flask import Flask,jsonify, request
import requests
import json
import urllib

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

    def select_sample(self, data):
        try:
            #return jsonify(data)
            db = mongoservices.condb(self)
            samples_coll = db.AllRideRequests
            out = samples_coll.find_one(data, {"_id": 0 })
            outs = json.dumps(out)
            outt = urllib.parse.unquote(outs)
            return jsonify(outt)  
            #return jsonify({"code":"1","status" : "ok"})
            #return jsonify({"code":"1","status" : "ok", "data": outs})
        except Exception as ex:
            return jsonify({"code":"0","status":ex})

    def select_driver(self, data):
        try:
            #return jsonify(data)
            db = mongoservices.condb(self)
            samples_coll = db.AllRideRequests
            out = samples_coll.find(data, {"_id": 0 }).sort( { "driverId": 1 } )
            outs = json.dumps(out)
            outt = urllib.parse.unquote(outs)
            return jsonify(outt)  
            #return jsonify({"code":"1","status" : "ok"})
            #return jsonify({"code":"1","status" : "ok", "data": outs})
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
