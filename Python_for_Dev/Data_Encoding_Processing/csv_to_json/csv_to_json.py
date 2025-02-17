import json
import csv

#username.csv to file.json
with open('username.csv', 'r') as csv_file, open('file.json', 'w') as json_file:
    reader = csv.DictReader(csv_file)
    json.dump([row for row in reader], json_file, indent=4)
