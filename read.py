# Chibogu Chisom
# 2020-02-11
# Path: read.py


import csv
import json
import hashlib
import pandas as pd
import os

#filename == name of file being split 

def get_csv_file():
    with open('test (2).csv', 'r') as f:
        reader = csv.reader(f)
        return list(reader)

def create_csv_file(csv_data):
    #use pandas to write sha key to last column, and skip first row
    df = pd.read_csv('test (2).csv', header=0)
    #remove any undefined columns
    df = df.dropna(axis=1, how='all')
    #add sha key to last column
    df['HASH'] = df.apply(lambda x: get_sha_key(x), axis=1)
    df.to_csv('test (2).csv', index=False)




def get_sha_key(data):
    return hashlib.sha256(str(data).encode('utf-8')).hexdigest()

def create_json_file(data):
    #make directory for storing files
    

 #generate CHIP-0007 compatible json
    json_data = { 
        "format": "CHIP-0007",
        "Serial Number": data[0],
        "File Name": data[1],
        "UUID": data[2],
        "Gender": data[4],
        "Description": data[3],
        "sha256": data[4]
    }
    with open('nft_jsons/{}.json'.format(data[1]), 'w') as f:
        #
        json.dump(json_data, f, indent=2)




def main():
 
    csv_data = get_csv_file()
    create_csv_file(csv_data)
    for line in csv_data:
        create_json_file(line)

if __name__ == '__main__':
    main()
    