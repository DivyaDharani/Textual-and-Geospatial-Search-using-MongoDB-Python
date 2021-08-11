#
# Assignment5 Interface
# Name: Divya Dharani Dhanabalan
#

from pymongo import MongoClient
import os
import sys
import json
import traceback
import math

def FindBusinessBasedOnCity(cityToSearch, saveLocation1, collection):
    try:
        #Case-sensitive search
        matched_documents_cursor = collection.find({'city': {'$regex': cityToSearch, '$options': 'i'}})
        with open(saveLocation1, 'w') as file:
            for document in matched_documents_cursor:
                name = document['name'].upper()
                full_address = document['full_address'].upper()
                city = document['city'].upper()
                state = document['state'].upper()
                line = '{0}${1}${2}${3}\n'.format(name, full_address, city, state)
                file.write(line)
    except Exception as e: 
        traceback.print_exc()

def calculateDistance(lat2, lon2, lat1, lon1):
    d = 0
    try: 
        R = 3959 #miles
        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        delta_phi = math.radians(lat2 - lat1)
        delta_lambda = math.radians(lon2 - lon1)

        a = (math.sin(delta_phi/2) * math.sin(delta_phi/2)) + (math.cos(phi1) * math.cos(phi2) * 
                                                                math.sin(delta_lambda/2) * math.sin(delta_lambda/2))

        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

        d = R * c
    except Exception as e: 
        traceback.print_exc()
    return d

def FindBusinessBasedOnLocation(categoriesToSearch, myLocation, maxDistance, saveLocation2, collection):
    try:
        matched_documents_cursor = collection.find({'categories': {'$in': categoriesToSearch}})

        lat1 = float(myLocation[0])
        long1 = float(myLocation[1])

        with open(saveLocation2, 'w') as file:
            for document in matched_documents_cursor: 
                lat2 = float(document['latitude'])
                long2 = float(document['longitude'])
                d = calculateDistance(lat2, long2, lat1, long1)
                if d <= maxDistance:
                    business_name = document['name'].upper()
                    file.write(business_name + '\n')
    except Exception as e: 
        traceback.print_exc()

