# Example file for Advanced Python: Working With Data by Joe Marini
# read data from a CSV file into an object structure

import csv
import pprint

# read the contents of a CSV file into an object structure
result = []

# TODO: open the CSV file for reading

def isHeader(r):
    if (r[0] == "Place"):
        return True
    return False

with open("largequakes.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:

        if (not isHeader(row)):
            result.append(
                {"place": row[0],
                 "magnitude": row[1],
                 "date": row[3],
                 "link": row[2]
                 }
        )

pprint.pp(result)
