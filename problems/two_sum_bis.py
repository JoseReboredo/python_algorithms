# Two Sum (Hashmap Classic) - Grok

# Problem
# -> Given a list of integers nums and an integer target, return indices of the two numbers that add up to target.
# -> Assume exactly one valid pair, no reusing the same element.

# Examples:
# nums = [2,7,11,15], target = 9 → [0,1]
# nums = [3,2,4], target = 6 → [1,2]
# nums = [3,3], target = 6 → [0,1]

# → Do brute-force O(n²) first (nested loops), then hashmap O(n) version — discuss time/space trade-offs.

nums = [2,7,11,15]
target = 9

# Store indices of numbers seen, check complement to find the pair in O(n)
# | Approach    | Time  | Space | Notes                                       |
# | ----------- | ----- | ----- | ------------------------------------------- |
# | Brute-force | O(n²) | O(1)  | Nested loops, simple                        |
# | Hashmap     | O(n)  | O(n)  | One pass, very efficient, uses extra memory |

lookup = {}
for k, n in enumerate(nums):
    complement = target - n
    if complement in lookup:
        print([lookup[complement], k])
        break
    lookup[n] = k


# Edges cases all handled

# Negative numbers: [ -1, -2, -3, -4, -5], target=-8 → [-3,-5]
# Duplicates: [3,3], target=6 → [0,1]
# Single pair assumption (as per problem)
