#!/usr/bin/env python
import csv
import requests
from collections import OrderedDict

with open('riders.csv', 'r') as csvfile:
    riderdata = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for row in riderdata:
        rider_name = row['name'].split(', ')
        frame_number = row['frame_number']
        print("Rider: {0} {1}".format(rider_name[1].title(), rider_name[0].title()))
        print("Frame Number: {0}".format(frame_number))
        rider_url = 'http://suivi.paris-brest-paris.org/data/{0}.txt'.format(frame_number)
        print(rider_url)
        req = requests.get(rider_url)
        if req.ok:
            ride_data = req.text.split(';')
            control_timings = OrderedDict([('start-0', ride_data[0]), ('villaines-221', ride_data[1]), ('fougeres-310', ride_data[2]), ('tinteniac-364', ride_data[3]), ('loudeac-449', ride_data[4]), ('carhaix-525', ride_data[5]), ('brest-618', ride_data[6]), ('carhaix-703', ride_data[7]), ('loudeac-782', ride_data[8]), ('tinteniac-867', ride_data[9]), ('fougeres-921', ride_data[10]), ('villaines-1009', ride_data[11]), ('mortagne-1090', ride_data[12]), ('dreux-1165', ride_data[13]), ('finish-1230', ride_data[14])])
            for key, value in control_timings.items():
                print("{0}: {1}".format(key, value))
        print("\n")
