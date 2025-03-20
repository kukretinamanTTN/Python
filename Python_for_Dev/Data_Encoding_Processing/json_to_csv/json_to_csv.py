import csv
import json

with open("data.json", "r") as jsonfile, open("file.csv", "w") as csvfile:
    data = json.load(jsonfile)
    writer = csv.DictWriter(csvfile, [key for key,value in data[0].items()])
    writer.writeheader()
    for row in data:
        writer.writerow(row)