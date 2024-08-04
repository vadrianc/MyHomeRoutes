from my_home_routes import gather_directions_data
from datetime import datetime, timedelta
from threading import Timer

def setup_timers():
    today=datetime.today()
    hour = 1

    print("Started at {}".format(datetime.today()))
    while hour < 24 - today.hour:
        next_sample_time = today.replace(day=today.day, hour=today.hour, minute=0, second=0, microsecond=0) + timedelta(hours=hour)
        delta_time_delay= next_sample_time - today

        timer = Timer(delta_time_delay.total_seconds(), gather_directions_data)
        timer.start()
        print("Timer will start in {} seconds".format(delta_time_delay.total_seconds()))

        hour = hour + 1


setup_timers()