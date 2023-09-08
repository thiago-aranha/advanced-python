# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import csv
import pprint
import datetime

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD

#Step 1: Ordering
def getSignificant(d):
    if (d["properties"]["sig"] is None):
        return 0
    return d["properties"]["sig"]

finalList = sorted(data["features"], key=getSignificant, reverse=True)

#Step 2: Get 40 Most Significants
finalList = finalList[:40]

#Step 3: Order by most recent
finalList.sort(key=lambda x: x["properties"]["time"], reverse=True)

#Step 4: Generate header and rows variables
header = ["Magnitude", "Place", "Felt Reports", "Date", "Google Map link"]
rows = []

def createGMapsLink(latitude, longitude):
    return f"https://maps.google.com/maps/search/?api=1&query={latitude}%2C{longitude}"

for quake in finalList:
    rows.append([
        quake["properties"]["mag"],
        quake["properties"]["place"],
        quake["properties"]["felt"],
        str(datetime.date.fromtimestamp(int(quake["properties"]["time"])/1000)),
        createGMapsLink(quake["geometry"]["coordinates"][1],
                        quake["geometry"]["coordinates"][0])
    ])

#Step 5: Generate CSV file
with open("report.csv","w") as csvFile:
    writer = csv.writer(csvFile, delimiter=",")
    writer.writerow(header)
    writer.writerows(rows)