# Problem proposed by Claude:

# You have a list of tasks, each represented by a character (e.g. 'A', 'B', 'C'). A CPU can execute one task per time unit.
# After executing a task, the same task type cannot run again for n cooldown units — the CPU must idle or run a different task during that time.

# Problem
# -> Given a list of tasks and a cooldown n, return the minimum number of time units needed to finish all tasks.

# Example:
# tasks = ['A', 'A', 'A', 'B', 'B', 'B']
# n = 2
#
# Output: 8
# One valid schedule: A -> B -> idle -> A -> B -> idle -> A -> B

# Why this is a good problem for you:
#
#   - It's a frequent senior-level interview question (LeetCode medium, but requires real reasoning)
#   - It builds on your existing hit_counter / sliding_window thinking
#   - Tests greedy algorithms and heap/priority queue knowledge — both common in Python interviews
#   - collections.Counter and heapq are the idiomatic Python tools here, good to practice

tasks = ['A', 'A', 'A', 'B', 'B', 'B']
n = 2

# the minimum time would be when there is no cooldown

# class TaskScheduler:
#     def __init__(self, cooldown: int):
#         self.cooldown = cooldown
#
#     def get_min_processing_time_for_tasks_list(tasks: [str]) -> int:
#         # get number of tasks per type
#         counters = []
#         for task in tasks:
#             if task not in counters:
#                 counters[task] = 1
#             else:
#                 counters[task] += 1
#
#         # each task is 1 unit, I understand
#         # I will do the floor devisionh
#         time_units = 0

# Solution using the greedy frame formula we discussed:
#
# Frames are anchored by the most frequent task.
# Frame size = n + 1 (the task + n cooldown slots)
# Number of full frames = max_freq - 1
# Tail = how many tasks share the max frequency
#
# Two cases:
#   1. Not enough tasks to fill frames -> idle slots needed
#      answer = (max_freq - 1) * (n + 1) + tasks_with_max_freq
#   2. Enough tasks to fill everything -> no idle time needed
#      answer = len(tasks)
#
# Final answer = max of both cases

from collections import Counter

def least_interval(tasks: list[str], n: int) -> int:
    freq = Counter(tasks)

    max_freq = max(freq.values())
    tasks_with_max_freq = sum(1 for count in freq.values() if count == max_freq)

    # Case 1: frame formula
    frame_based = (max_freq - 1) * (n + 1) + tasks_with_max_freq

    # Case 2: no idle needed, just run all tasks
    return max(len(tasks), frame_based)


# Output: 8
print(least_interval(tasks, n))

# Extra test: enough task types to fill all slots, no idle needed
# A->B->C->A->B->C->A->B->C = 9 units, len(tasks) = 9
print(least_interval(['A','A','A','B','B','B','C','C','C'], 2))  # 9








