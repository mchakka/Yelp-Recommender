from flask import Blueprint
import logging

LOG = logging.getLogger(__name__)

main = Blueprint('main', __name__)


@main.route('/')
def inital_load():
    return 'Hi, the server is up and running'

@main.route('/api/get_data')
def welcome():
    return 'Hello'