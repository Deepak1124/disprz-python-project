# Build a retry decorator with retry time and retry interval to run a function 3 time 
# with interval of 3 sec
import time


def retry(retry_time, retry_interval):
  def decorator(func):
    def wrapper(*args, **kwargs):
      for _ in range(retry_time):
        try:
          return func(*args, **kwargs)
        except Exception as e:
          print("In exception")
          time.sleep(retry_interval)
          continue

      raise Exception("Function execution failed after 3 retries.")


    return wrapper

  return decorator


@retry(3, 3)
def my_func():
  raise Exception("This function will raise an exception")

my_func()