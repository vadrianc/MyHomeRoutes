from collections.abc import Callable
from datetime import datetime, timedelta
from threading import Timer

class Sampler:
    def setup_timers(self, function: Callable):
        now=datetime.now()
        hour = 0

        print("Started at {}\n".format(datetime.now()))

        while hour < 24 - now.hour:
            next_sample_time = now.replace(day=now.day, hour=now.hour, minute=0, second=0, microsecond=0) + timedelta(hours=hour)
            delta_time_delay = next_sample_time - now
            if delta_time_delay.total_seconds() < 0:
                delta_time_delay = timedelta(hours=0)

            timer = Timer(delta_time_delay.total_seconds(), function)
            timer.start()
            print("Timer will start in {} seconds".format(delta_time_delay.total_seconds()))

            hour = hour + 1