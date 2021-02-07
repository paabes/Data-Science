# this file contains most functions defined for server file

import pickle
import json
import math
import numpy as np


__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bed,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bed
    x[2] = bath
    if loc_index >= 0:
        x[loc_index] = 1

    return round(math.sqrt(abs(__model.predict([x])[0])), 2)


def get_location_names():
    load_saved_artifact()
    return __locations

def load_saved_artifact():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[5:]  # first 5 are column names
    global __model

    with open('./artifacts/london_home_prices_model.pickle', 'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")


if __name__ == '__main__':
    load_saved_artifact()
    print(get_location_names())

    print(get_estimated_price('101 wood lane', 1000, 2, 2))