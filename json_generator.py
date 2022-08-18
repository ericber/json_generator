#!/usr/bin/python

'''
json_generator.py
Script that generates an output.json
'''

import json

if __name__ == '__main__':

    test_results = [
       {
            "test_id": 42185,
             "watch": "fenix6",
             "status": True
       },
       {
            "test_id": 42186,
            "watch": "venu2",
            "status": True
       },
       {
            "test_id": 42187,
            "watch": "venu2",
            "status": False
       }
    ]
    
    print ('executing json_gerator...')
    with open('output.json', 'w') as file:
        json.dump(test_results, file, indent=4)
    print ('created output.json')