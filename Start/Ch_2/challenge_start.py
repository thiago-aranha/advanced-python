# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
from collections import Counter

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

#counterEvents = Counter(data["features"]["properties"]["type"])
counterEvents = dict()

for event in data['features']:
    counterEvents[event['properties']['type']] = counterEvents.get(
        event['properties']['type'], 0) + 1

for event, count in counterEvents.items():
    print(f"Event: {event}: {count}")