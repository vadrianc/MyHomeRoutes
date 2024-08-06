import csv
import re
import matplotlib.pyplot as plt
import numpy as np

class Plotter:
    def __init__(self, results_csv):
        self.results_csv = results_csv

    def draw_single(self, start, end):
        data = {}

        with open(self.results_csv, "r", encoding='utf-8') as csvfile:
            tracks_reader = csv.reader(csvfile)

            for track in tracks_reader:
                if track[0] == start and track[1] == end:
                    hour = int(track[2]);
                    driving_time_minutes = self.get_total_minutes(track[4])
                    data[hour] = driving_time_minutes

        xpoints = np.array(list(data.keys()))
        ypoints = np.array(list(data.values()))
        plt.plot(xpoints, ypoints)

        plt.xticks(xpoints)
        plt.yticks(ypoints)

        plt.title("Driving from {} to {}".format(start, end))
        plt.xlabel("Hour")
        plt.ylabel("Duration (Minutes)")

        plt.grid()
        plt.show()

    def get_total_minutes(self, time_str):
        times = re.findall(r'\d+', time_str)
        if (len(times) == 1):
            return int(times[0])
        else:
            return int(times[0]) * 60 + int(times[1])