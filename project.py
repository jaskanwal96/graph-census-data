from flask import Flask
from flask import render_template
from flask import request, redirect, jsonify, url_for, flash
from flask import session as login_session
from flask import Blueprint
from flask.json import jsonify
import random
import string
from models import adults
from mongoengine import connect, Q
import json
from flask import make_response
from functools import wraps

app = Flask(__name__, static_url_path='/static')
connect('census')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template('search.html')

@app.route('/getCensusData/<int:page>', methods=['GET', 'POST'])
def getCensusData(page):
    page_nb = page
    items_per_page = 10 
    offset = (page_nb - 1) * items_per_page
    all_data = [{"age": adult.age,"workclass": adult.workclass,"sex" : adult.sex, "education" : adult.education, "occupation" : adult.occupation, "relationship" : adult.relationship, "race" : adult.race, "native_country" : adult.native_country} for adult in adults.objects.skip( offset ).limit( items_per_page )]
    return jsonify({"data" : all_data})


@app.route('/getCensusData/', methods=['GET', 'POST'])
def getCensusFilteredData():
    json_data = request.get_json()
    print(json_data)
    sex = []
    relationship = []
    race = []
    if(json_data['sex'] and len(json_data['sex'])!= 0):
        sex = json_data['sex']
    else:
        pipeline = [
        {
            "$group":{
                "_id" : "$sex",
                 
            }
        }
        ]   
        sex = [result['_id'] for result in adults.objects.aggregate(*pipeline)]
    if(json_data['relationship'] and len(json_data['relationship'])):
        relationship = json_data['relationship']
    else:
        pipeline = [
        {
            "$group":{
                "_id" : "$relationship",
                 
            }
        }
        ]   
        relationship = [result['_id'] for result in adults.objects.aggregate(*pipeline)]
    if(json_data['race'] and len(json_data['race'])!=0):
        race = json_data['race']
    else:
        pipeline = [
        {
            "$group":{
                "_id" : "$race",
                 
            }
        }
        ]   
        race = [result['_id'] for result in adults.objects.aggregate(*pipeline)]
    print(sex, relationship , race)
    final_res = adults.objects.filter(sex__in=sex).filter(relationship__in=relationship).filter(race__in=race)
    all_data = [{"age": adult.age,"workclass": adult.workclass,"sex" : adult.sex,"education" : adult.education, "occupation" : adult.occupation, "relationship" : adult.relationship, "race" : adult.race, "native_country" : adult.native_country} for adult in final_res[:10]]
    return jsonify({"data" : all_data})


@app.route('/getSexData')
def showSexdataChart():
    
    """Get Males and Females in the Census Data"""
    total_count = adults.objects().count()
    male_count = adults.objects(sex=" Male").count()
    sex_data = {"Male" :  male_count, "Female" : total_count - male_count}
    return jsonify(sex_data)

@app.route('/getRelationshipData')
def showRelationshipChart():
    
    """Get People in relationship in the Census Data"""
    pipeline = [
        {
            "$group":{
                "_id" : "$relationship",
                 "count": {
                     "$sum":1
                    }
            }
        }
    ]
    results = adults.objects.aggregate(*pipeline)
    relationship_data = [{"label" : result['_id'], "value": result['count']} for result in results]
    
    return jsonify({"data" : relationship_data})

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
