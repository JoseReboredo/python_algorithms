# Pattern: sorting + iteration
#
# Problem
# -> Merge overlapping intervals.

# Example
# intervals = [[1,3],[2,6],[8,10],[15,18]]

# Output
# [[1,6],[8,10],[15,18]]

# Complexity
# Time: O(n log n)  (sorting)
# Space: O(n)

intervals = [[1,3],[2,6],[8,10],[15,18]]

# First, I sort the intervals by their start time.
# Then I iterate through them, keeping track of the last merged interval.
# If the current interval overlaps with the last one, I extend the end.
# Otherwise, I add a new interval.
intervals.sort(key=lambda x: x[0])

output = []
for interval in intervals:
    if not output:
        output.append(interval)
        continue

    last = output[-1]
    if interval[0] <= last[1]:
        last[1] = max(last[1], interval[1])
    else:
        output.append(interval)

print(output)

