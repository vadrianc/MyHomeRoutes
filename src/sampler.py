from collections.abc import Callable
from datetime import datetime, timedelta
from threading import Timer

class Sampler:
    def setup_timers(self, function: Callable):
        today=datetime.today()
        hour = 0

        print("Started at {}".format(datetime.today()))
        while hour < 24 - today.hour:
            next_sample_time = today.replace(day=today.day, hour=today.hour, minute=0, second=0, microsecond=0) + timedelta(hours=hour)
            delta_time_delay= next_sample_time - today

            timer = Timer(delta_time_delay.total_seconds(), function)
            timer.start()
            print("Timer will start in {} seconds".format(delta_time_delay.total_seconds()))

            hour = hour + 1