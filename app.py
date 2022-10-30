from cgitb import text
import time
import requests

import redis
from flask import Flask, request, jsonify, make_response
from constants import *
from models.content import Content
from models.base_model import db

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.before_request
def before_request():
    db.connect()

@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        print(db)
        print(db.close())
    return exc

@app.route('/')
def hello():
    x = requests.get(f'http://metaphorpsum.com/paragraphs/{DEFAULT_PARAGRAPHS}/{DEFAULT_SENTENCES}')

    try:
        content = Content(body=x.text)
        print(content)
        content.save()
        response={
            'message':x.text,
            'data':{
                'body':'text'
            }
        }
        return make_response(jsonify(response),200)
    except:
        response ={
            'message': 'Unable to retrieve text'
        }
        return make_response(jsonify(response),200)
