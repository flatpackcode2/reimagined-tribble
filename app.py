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
def get_text():
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

@app.route('/search')
def search():
    operator=request.args.get('operator')
    terms=request.args.get('terms')
    print(f'the operators are {operator}')
    print(f'''{operator=='and'}''')
    if operator == 'or':
        response = Content.select().where(Content.body.contains(terms))
    if operator == 'and':
        response = Content.select().where(Content.body.contains(terms))

    if (operator !='or' and operator!='and'):
        response={
        'message':'Operator is invalid. Please use either \'and\' or \'or\'',
        'operator':operator,
        'terms':terms
        }
    
    return make_response(jsonify(response),200)

    #get paragraphs
    hits = Content.raw('SELECT body FROM content where ')
    print(f'the terms are {terms}')

    string
    
    response={
        'message':'OK',
        'operator':operator,
        'terms':terms
    }
    return make_response(jsonify(response),200)
