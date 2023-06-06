from stats_recorder import StatsRecorder
import time

stats = StatsRecorder()

stats.start()

time.sleep(2)

stats.stop()

time_taken = stats.get_elapsed_time()
memory_usage = stats.get_memory_usage()

print("Time taken:", time_taken, "seconds")
print("Memory Usage:", memory_usage, "bytes")
