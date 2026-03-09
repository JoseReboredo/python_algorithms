# Contains Duplicate (Set or Dict) - Grok

# Problem
# -> Given a list of integers nums, return True if any value appears at least twice, else False.

# Examples:
# [1,2,3,1] → True
# [1,2,3,4] → False
# [1] → False
# [] → False

# → Solve 3 ways: sort + check adjacent, set length compare, dict/counter for counts — talk about which is best and why.

def is_containing_duplicates(nums: [int]) -> bool:
    counters = {}
    for n in nums:
        if n not in counters:
            counters[n] = 1
        else:
            return True
    return False

tests = [
    [1,2,3,1], # → True
    [1,2,3,4], # → False
    [1], # → False
    [], # → False
]

for test in tests:
    print(is_containing_duplicates(test))

# Others solutions:

# sort + check adjacent

# nums.sort()
# for i in range(1, len(nums)):
#     if nums[i] == nums[i-1]:
#         return True
# return False

# Time: O(n log n) → sorting dominates
# Space: O(1) (if in-place sort)
# Advantage: constant extra space
# Drawback: Slower than hash-map for large arrays.

# Set length comparison (Pythonic)

# def contains_duplicate(nums):
#     return len(nums) != len(set(nums))

# Time: O(n)
# Space: O(n) (set stores all unique elements)
# Very concise
# Elegant for Python, often preferred in interviews for brevity

