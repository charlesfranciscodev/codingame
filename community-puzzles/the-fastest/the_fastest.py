from datetime import datetime

format_str = "%H:%M:%S"
min_time = datetime.strptime("23:59:59", format_str)
n = int(input())
for i in range(n):
    time_str = input()
    time = datetime.strptime(time_str, format_str)
    if (time < min_time):
        min_time = time

print(min_time.strftime(format_str))
