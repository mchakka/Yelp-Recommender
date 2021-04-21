from flask import Blueprint, request
import logging
import json


LOG = logging.getLogger(__name__)

main = Blueprint('main', __name__)


@main.route('/')
def inital_load():
    return 'Hi, the server is up and running'

# I don't think we need the following route, we should just let the model use the path to the filtered csv dataset
# directly

# # returns the path to csv
# @main.route('/api/getRawFilteredData')
# def get_filtered_data():
#     return 'Hello'


# trains model
@main.route('/api/trainModel')
def train():
    return 'Hello'


# returns recommendations
@main.route('/api/getReccomendations')
def getrecs():
    #payload is inital parameters

    return 'Hello'


# returns details of a restaurant
@main.route('/api/getRestaurantDetails', methods=['GET', 'POST'])
def get_details():
    # payload is resturant business id
    json_data = open('api/yelp_academic_dataset_business.json')
    counter = 0
    business_id = request.args.get('business_id')

    # temp_business_id = 'BYI0T3QhmYC1Y3fvxnXukg'
    found = False

    for item in json_data:
        jdata = json.loads(item)
        #print(jdata['business_id'])
        if jdata['business_id'] == business_id:
            found = True
            break
        counter += 1

    if not found:
        return 'Cannot find details for that business_id'

    print(item)

    return item