import json 
import csv 

def csv_to_json(csv_file, json_file):
    # Read CSV file
    with open(csv_file, 'r') as csv_input:
        csv_reader = csv.DictReader(csv_input)
        # Convert CSV to list of dictionaries
        data = list(csv_reader)
    
    # Write JSON file
    with open(json_file, 'w') as json_output:
        json.dump(data, json_output, indent=2)
csv_to_json('suggestions.csv', 'seasons.json')