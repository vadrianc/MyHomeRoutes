import googlemaps
import os
#import pprint
import csv
from datetime import datetime

def gather_directions_data():
    #read Google API Key from 'key.key' file
    with open('in\\key.key', 'r') as file:
        key_str = file.read().rstrip()
        gmaps = googlemaps.Client(key=key_str)

        now = datetime.now()
        results_csv = 'results_{}.csv'.format(now.strftime("%m_%d_%Y"))
        results_file = os.path.isfile(results_csv)

        #read start - end locations
        with open('in\\tracks.csv', "r", encoding='utf-8') as csvfile, open(results_csv, 'a', newline ='', encoding='utf-8') as results_csv:
            if not results_file:
                writer = csv.writer(results_csv)
                writer.writerows([["Start Address", "End Address", "Date", "Hour", "Distance", "Duration"]])

            tracks_reader = csv.reader(csvfile)
            for track in tracks_reader:
                #get the directions result for the current date/time
                directions_result = gmaps.directions(track[0],
                                                    track[1],
                                                    mode="driving",
                                                    units="metric",
                                                    departure_time=now,
                                                    traffic_model="pessimistic")

                writer = csv.writer(results_csv)
                #prepare and write direction result
                for direction in directions_result:
                    #pprint.pp(direction)
                    hour = now.strftime("%H")
                    start_address = direction["legs"][0]["start_address"]
                    end_address = direction["legs"][0]["end_address"]
                    distance = direction["legs"][0]["distance"]["text"]
                    duration = direction["legs"][0]["duration"]["text"]
                    writer.writerows([[start_address, end_address, hour, distance, duration]])
                    print("{} in {} between \"{}\" and \"{}\"".format(distance, duration, start_address, end_address))

gather_directions_data()