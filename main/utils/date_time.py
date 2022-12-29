import time
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Start time = {current_time}")

current_time_millis = time.time
start_time = 0
end_time = 0
time_passed = end_time - start_time
