# Pattern: hash lookup

# Problem
# -> Given a list of numbers and a target, return two indices whose values add up to the target.

# Example:
# nums = [2, 7, 11, 15]
# target = 9

# Expected output:
# [0,1]

nums = [2, 7, 11, 15]
target = 9

lookup = {}

# The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
# The enumerate() function adds a counter as the key of the enumerate object.
for i, n in enumerate(nums):
    complement = target -n

    if complement not in lookup:
        lookup[n] = i
        continue

    print([lookup[complement], i])
    break

# my solution, I forgot about the problem asking for indexes not the values
# nums = [2, 7, 11, 15]
# target = 9
#
# lookup = {}
# output = []
# for n in nums:
#     if target > n:
#         lookup[n] = 9 - n
#     if lookup[n] not in lookup:
#         continue
#
#     output = [lookup[n], n]
#     break
#
# print(output)

