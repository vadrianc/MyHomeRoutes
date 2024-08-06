import googlemaps
import os
#import pprint
import csv
from datetime import datetime

class Track:
    def __init__(self, key_file, tracks_csv, two_way = False):
        self.key_file = key_file
        self.tracks_csv = tracks_csv
        self.two_way = two_way
        self.init_gmaps()

    def init_gmaps(self):
        with open(self.key_file, 'r') as file:
            key_str = file.read().rstrip()
            self.gmaps = googlemaps.Client(key=key_str)

    def gather_directions_data(self):
        now = datetime.now()
        results_csv = 'results_{}.csv'.format(now.strftime("%m_%d_%Y"))
        results_file = os.path.isfile(results_csv)

        #read start - end locations
        with open(self.tracks_csv, "r", encoding='utf-8') as csvfile, open(results_csv, 'a', newline ='', encoding='utf-8') as results_csv:
            if not results_file:
                writer = csv.writer(results_csv)
                writer.writerows([["Start Address", "End Address", "Date", "Hour", "Distance", "Duration"]])

            tracks_reader = csv.reader(csvfile)
            writer = csv.writer(results_csv)

            for track in tracks_reader:
                self.save_directions_data(writer, track[0], track[1], now)
                if self.two_way:
                    self.save_directions_data(writer, track[1], track[0], now)


    def save_directions_data(self, writer, start, end, now):
        #get the directions result for the current date/time
        directions_result = self.gmaps.directions(start,
                                            end,
                                            mode="driving",
                                            units="metric",
                                            departure_time=now)

        
        #prepare and write direction result
        for direction in directions_result:
            #pprint.pp(direction)
            hour = now.strftime("%H")
            distance = direction["legs"][0]["distance"]["text"]
            duration_in_traffic = direction["legs"][0]["duration_in_traffic"]["text"]
            writer.writerows([[start, end, hour, distance, duration_in_traffic]])
            print("{} in {} from \"{}\" to \"{}\"".format(distance, duration_in_traffic, start, end))