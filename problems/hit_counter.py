# Problem
# -> Design a hit counter

# Implement a system that counts how many events happened in the last 60 seconds.
# Rules:
# timestamp is in seconds
# Only count hits in the last 60 seconds

# You must implement
# hit(timestamp: int)
# get_hits(timestamp: int) -> int

# Example
# hit(1)
# hit(2)
# hit(3)
#
# get_hits(4) → 3
#
# hit(65)
#
# get_hits(65) → 2

# Explanation
# timestamps: 1,2,3,65
# window at 65 = [6..65]
#
# only hits: 3,65

# This solution is:
# O(n) every get_hits

class Hit:
    def __init__(self):
        self.window = []

    def hit(self, ts: int) -> None:
        self.window.append(ts)

    def get_hits(self, ts: int) -> int:
        # remove old hits -> this makes it slow
        #self.window[:] = [ w for w in self.window if w + 60 > ts]
        # without list comprehension
        while self.window and self.window[0] + 60 < ts:
            self.window.pop(0) # pop(0) is expensive 0(n) or O(n2) is many elements removed

        return len(self.window)

# Faster using queues
from collections import deque

class QHit:
    def __init__(self):
        self.q_window = deque()

    def hit(self, ts: int) -> None:
        self.q_window.append(ts)

    def get_hits(self, ts: int) -> int:
        # remove old hits -> this makes it slow
        while self.q_window and ts - self.q_window[0] >= 60:
            self.q_window.popleft()

        return len(self.q_window)

counter = Hit()
counter.hit(1)
counter.hit(2)
counter.hit(3)

# 3
print(counter.get_hits(4))

counter.hit(65)

# 2?? 1 right??
print(counter.get_hits(65))
