# CSV FILE READER

# This is a simple CSV file reader that can be used to read CSV files and convert them into a series of json files, with the CHIP-OO07 format

# The CSV file must have the following format:

# 1. The first line must be the header, with the following columns:

# - "Serial Number": the id of the NTF

# - "File Name": the name of the NFT

# - "UUID" : the unique id of the NFT

# - "Gender": the gender of the NFT

# - "Description": the description of the NFT

# - "Image": the image of the NFT

# - "Attributes": the attributes of the NFT

## All in this particular order

# 2. Each line within the csv file must have its own unique values for each of these parameters , and cannot repeat

# 3. For the intent of further changes to the values in the csv file, the script should be modified as follows:

# - The index of each header row must match its corresponding generator within the script. That is to say that the first header must match index [0] in the script, and the second must match index[1] and so on

```

def create_json_file(data):
#generate CHIP-0007 compatible json
   json_data = {
       "format": "CHIP-0007",
       "Serial Number": data[0],
       "File Name": data[1],
       "UUID": data[2],
       "Gender": data[4],
       "Description": data[3],
       "sha256": data[x]
       #add your extra values here
   }

```

# 4. Upon running the script, any arbitrary commas and values within the CSV file will be removed, and an SHA key will be assigned to each row of values , for easier identification

# 5. The script will create a folder called "nft_jsons" in the same directory as the script, and will place all the generated json files in there

## The test csv file for esuring the script runs is inluded in the directory

## The script is written in python 3.9.7

## The script was written by @raeeceip

## The script was written for the Zuri-HNGi9 backend challenge
