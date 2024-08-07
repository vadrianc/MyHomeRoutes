import csv
import re
import matplotlib.pyplot as plt
import numpy as np

class Plotter:
    def __init__(self, results_csv):
        self.results_csv = results_csv

    def draw(self, routes):
        plt.title("Driving time")
        plt.xlabel("Hour")
        plt.ylabel("Duration (Minutes)")

        hours = self.get_hours(routes[0], routes[1])
        all_durations = []

        for start, end in self.pairwise(routes):
            durations = self.get_driving_times(start, end)

            plt.plot(hours, durations, label = "{} to {}".format(start, end))
            all_durations = np.unique(np.concatenate((all_durations, durations)))

        plt.xticks(hours)
        plt.yticks(all_durations)
        plt.grid(visible=True, which='both', axis='both')
        plt.legend()
        plt.show()

    def pairwise(self, iterable):
        "s -> (s0, s1), (s2, s3), (s4, s5), ..."
        a = iter(iterable)
        return zip(a, a)

    def get_hours(self, start, end):
        hours = []

        with open(self.results_csv, "r", encoding='utf-8') as csvfile:
            tracks_reader = csv.reader(csvfile)

            for track in tracks_reader:
                if track[0] == start and track[1] == end:
                    hours.append(int(track[2]))

        return hours
    
    def get_driving_times(self, start, end):
        durations = []

        with open(self.results_csv, "r", encoding='utf-8') as csvfile:
            tracks_reader = csv.reader(csvfile)

            for track in tracks_reader:
                if track[0] == start and track[1] == end:
                    driving_time_minutes = self.get_total_minutes(track[4])
                    durations.append(driving_time_minutes)

        return durations

    def get_total_minutes(self, time_str):
        times = re.findall(r'\d+', time_str)
        if (len(times) == 1):
            return int(times[0])
        else:
            return int(times[0]) * 60 + int(times[1])