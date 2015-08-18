#!/usr/bin/env python
import csv
import requests

# Write results to this file
resultfile = open('results.csv', 'w')

# Field names are hardcoded here.
field_names = ['name', 'frame_number', 'start', 'villaines-221', 'fougeres-310', 'tinteniac-364', 'loudeac-449', 'carhaix-525', 'brest-618', 'carhaix-703', 'loudeac-782', 'tinteniac-867', 'fougeres-921', 'villaines-1009', 'mortagne-1090', 'dreux-1165', 'finish-1230']
resultwriter = csv.DictWriter(resultfile, fieldnames=field_names, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
resultwriter.writeheader()

# Let's start reading from input file and write data to results file
with open('riders.csv', 'r') as csvfile:
    riderdata = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for row in riderdata:
        rider_name_given = row['name'].split(', ')
        rider_name="{0} {1}".format(rider_name_given[1].title(), rider_name_given[0].title())
        print("Getting data for {0}".format(rider_name))
        frame_number = row['frame_number']
        rider_url = 'http://suivi.paris-brest-paris.org/data/{0}.txt'.format(frame_number)
        req = requests.get(rider_url)
        if req.ok:
            ride_data = req.text.split(';')
            resultwriter.writerow({'name': rider_name, 'frame_number': frame_number, 'start': ride_data[0], 'villaines-221': ride_data[1], 'fougeres-310': ride_data[2], 'tinteniac-364': ride_data[3], 'loudeac-449': ride_data[4], 'carhaix-525': ride_data[5], 'brest-618': ride_data[6], 'carhaix-703': ride_data[7], 'loudeac-782': ride_data[8], 'tinteniac-867': ride_data[9], 'fougeres-921': ride_data[10], 'villaines-1009': ride_data[11], 'mortagne-1090': ride_data[12], 'dreux-1165': ride_data[13], 'finish-1230': ride_data[14]})
            print("Written data for {0}".format(rider_name))
resultfile.close()
