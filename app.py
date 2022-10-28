import time
from unittest.mock import DEFAULT
import requests

import redis
from flask import Flask, request
from constants import *

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello():
    x = requests.get(f'http://metaphorpsum.com/paragraphs/{DEFAULT_PARAGRAPHS}/{DEFAULT_SENTENCES}')

    try:
        app.logger.info(x.text)
    except:
        app.logger('Something went wrong')
    app.logger.info(DEFAULT_SENTENCES)
    app.logger.info(DEFAULT_PARAGRAPHS)
    app.logger.info(x.status_code)
    app.logger.info('request logged')
    app.logger.info(request.args)
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)
