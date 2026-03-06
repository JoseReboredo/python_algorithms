# Log Rate Aggregator (Very Backend-Oriented)

# Input
# (event_type, timestamp)
# logs = [
# ("login", 10),
# ("purchase", 12),
# ("login", 15),
# ("logout", 18),
# ("login", 20)
# ]

# Expected output
# {
# "login": 3,
# "purchase": 1,
# "logout": 1
# }

# Time: O(n)
# Space: O(k)  (k = number of event types)

logs = [
    ("login", 10),
    ("purchase", 12),
    ("login", 15),
    ("logout", 18),
    ("login", 20)
]

output = {}
for log in logs:
    if log[0] not in output:
        output[log[0]] = 1
    else:
        output[log[0]] += 1

print(output)