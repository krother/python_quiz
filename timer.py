
import time

class Timer:

    def __init__(self, limit):
        self.time_limit = limit
        self.start_time = time.time()

    @property
    def time_left(self):
        time_passed = time.time() - self.start_time
        return self.time_limit - time_passed

    @property
    def expired(self):
        return self.time_left < 0
