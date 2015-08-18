#!/usr/bin/env python
import csv
with open('riders.csv', 'r') as csvfile:
    riderdata = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for row in riderdata:
        rider_name = row['name'].split(', ')
        print("Rider: %s %s"%(rider_name[1].title(), rider_name[0].title()))
        print("Frame Number: %s\n"%(row['frame_number']))
