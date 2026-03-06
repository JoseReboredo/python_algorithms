# Log Storage System

# Problem
# -> Implement a simple log system.

# Each log has:
# (timestamp, message)

# You must support
#
# add_log(timestamp, message)
# get_logs(start, end)
# -> get_logs should return all messages whose timestamps are within the range [start, end].

# Example
# add_log(10, "login")
# add_log(12, "purchase")
# add_log(15, "logout")
#
# get_logs(11, 15)

# Expected Output
# ["purchase", "logout"]

class LogStorage:
    def __init__(self):
        self.logs = {}

    def add_log(self, timestamp, message) -> None:
        self.logs[timestamp] = message

    def get_logs(self, start, end) -> list[str]:
        return [l for k, l in self.logs.items() if start <= k <= end]

# What if there are millions of logs????

# Failure what if start = 1 and end = 1M, could even be worse than O(n) -> O(range end - start)
# Failure we could have multiple logs per second

# class LogStorageImproved:
#     def __init__(self):
#         self.logs = {}
#
#     def add_log(self, timestamp, message) -> None:
#         self.logs[timestamp] = message
#
#     def get_logs(self, start, end) -> list[str]:
#         requested_logs = []
#         for index in range(start, end+1):
#             if index in self.logs:
#                 requested_logs.append(self.logs[index])
#
#         return requested_logs

# No binary search better!!!!!!
# Not sure, this is about this solution, it will depend on a log how we manage logs and the ordering of them

import bisect

class LogStorageBinarySearch:
    def __init__(self):
        self.logs = []

    def add_log(self, timestamp, message) -> None:
        self.logs.append((timestamp,message)) # adding a tuple

    def get_logs(self, start, end) -> list[str]:
        # binary search done with the end
        timestamps = [ts for ts, _ in self.logs] # but this is O(n).. keep a different variable with a list of timestamps?

        # @see https://www.geeksforgeeks.org/python/bisect-algorithm-functions-in-python/
        left = bisect.bisect_left(timestamps, start)
        right = bisect.bisect_right(timestamps, end)

        return [msg for _, msg in self.logs[left:right]]


system = LogStorage()
system.add_log(10, "login")
system.add_log(12, "purchase")
system.add_log(15, "logout")

print(system.get_logs(11, 15))

system = LogStorageBinarySearch()
system.add_log(10, "login")
system.add_log(12, "purchase")
system.add_log(15, "logout")

print(system.get_logs(11, 15))