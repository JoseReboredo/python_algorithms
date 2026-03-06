# Pattern: backend logic
# This is very realistic for a platform/backend role.
#
# Problem
# -> Implement a simple rate limiter:
# A user can only make 3 requests per 10 seconds.

# Example
# allow_request(user_id, timestamp)

# Returns
# True -> request allowed
# False -> blocked

import time

counters = {}

def remove_old_timestamp(current_timestamp, timestamps):
    timestamps[:]= [t for t in timestamps if current_timestamp - t < 10]

    # for t in timestamps:
    #     if t + 10 < current_timestamp:
    #         timestamps.remove(t)


def allow_request(user_id: str, timestamp: int) -> bool:

    if user_id not in counters:
        counters[user_id] = [timestamp]
        return True

    remove_old_timestamp(timestamp, counters[user_id])

    if len(counters[user_id]) < 3:
        counters[user_id].append(timestamp)
        return True

    return False

print(allow_request("u1", 1))
print(allow_request("u1", 2))
print(allow_request("u1", 3))
print(allow_request("u1", 4))

print(allow_request("u1", 12))
