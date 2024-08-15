import googlemaps
import os
#import pprint
import csv
from datetime import datetime

class Track:
    def __init__(self, key_file, from_txt, to_txt, two_way = False):
        self.key_file = key_file
        self.from_txt = from_txt
        self.to_txt = to_txt
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
        with open(self.from_txt, "r", encoding='utf-8') as from_file, open(self.to_txt, "r", encoding='utf-8') as to_file, open(results_csv, 'a', newline ='', encoding='utf-8') as results_csv:
            if not results_file:
                writer = csv.writer(results_csv)
                writer.writerows([["Start Address", "End Address", "Hour", "Distance", "Duration"]])

            from_list = from_file.read()
            from_list = from_list.splitlines()
            
            to_list = to_file.read()
            to_list = to_list.splitlines()

            writer = csv.writer(results_csv)

            for start in from_list:
                for end in to_list:
                    self.save_directions_data(writer, start, end, now)
                    if self.two_way:
                        self.save_directions_data(writer, end, start, now)


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