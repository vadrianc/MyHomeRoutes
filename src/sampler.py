from collections.abc import Callable
from datetime import datetime, timedelta
from threading import Timer

class Sampler:
    def gather(self, function: Callable, interval):
        print("\nStarted at {}\n".format(datetime.now()))
        function()

        timer = Timer(interval, self.gather, [function, interval])
        timer.start()
