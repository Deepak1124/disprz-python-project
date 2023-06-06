import time
import psutil

class StatsRecorder:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.memory_usage = None

    def start(self):
        self.start_time = time.time()
        self.memory_usage = psutil.Process().memory_info().rss

    def stop(self):
        self.end_time = time.time()

    def get_elapsed_time(self):
        if self.start_time is None or self.end_time is None:
            raise ValueError("Timer not started or stopped")
        return self.end_time - self.start_time

    def get_memory_usage(self):
        if self.memory_usage is None:
            raise ValueError("Memory usage not recorded")
        return self.memory_usage
