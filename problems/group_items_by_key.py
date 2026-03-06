# Pattern: grouping with hashmap
#
# Problem
#
# You receive events from users. Group them by user_id.

# example
# events = [
#   {"user_id": 1, "event": "login"},
#   {"user_id": 2, "event": "purchase"},
#   {"user_id": 1, "event": "logout"}
# ]

# Expected Output
# {
#   1: [
#       {"user_id": 1, "event": "login"},
#       {"user_id": 1, "event": "logout"}
#      ],
#   2: [
#       {"user_id": 2, "event": "purchase"}
#      ]
# }

# Time complexity: O(n)
# Space complexity: O(n)

events = [
  {"user_id": 1, "event": "login"},
  {"user_id": 2, "event": "purchase"},
  {"user_id": 1, "event": "logout"}
]

output = {}
for event in events:
    user_id = event["user_id"]
    if user_id not in output:
        output[user_id] = []

    output[user_id].append(event)

print(output)

