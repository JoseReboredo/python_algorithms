# Problem
# -> detect overlapping meetings

# Input
# meetings = [
# [9,10],
# [10,11],
# [10.5,12]
# ]

# Output
# True

meetings = [
    [9,10],
    [10,11],
    [10.5,12]
]

# we sort meeting by starting time
meetings.sort(key=lambda x : x[0])

overlapping = False
for k, meeting in enumerate(meetings):
    if k == 0:
        continue

    if meetings[k-1][1] > meeting[0]:
        overlapping = True
        break

print(overlapping)

# Nicer tracking previous end
meetings = [
    [9,10],
    [10,11],
    [10.5,12]
]

meetings.sort(key=lambda x: x[0])

overlapping = False
prev_end = meetings[0][1]

for meeting in meetings[1:]:
    if meeting[0] < prev_end:
        overlapping = True
        break

    prev_end = meeting[1]

print(overlapping)
