# Given numbers and a window size:
# nums = [1,3,2,6,-1,4,1,8,2]
# k = 3

# Return the average of every window.
# [2.0, 3.67, 2.33, 3.0, 1.33, 4.33, 3.67]

# This solution complexity O(n * k)

def get_average(wind: [int]) -> float:
    return sum(wind)/len(wind)

def get_window(numbers: [int], kn: int, p: int) -> list:
    if p + kn > len(numbers):
        return []
    return numbers[p:p+kn]

nums = [1,3,2,6,-1,4,1,8,2]
k = 3

averages = []
for pos in range(len(nums)):
    window = get_window(nums, k, pos)
    if not window:
        break

    averages.append(get_average(window))

print(averages)

# BEST solution sliding window -> complexity O(n)

nums = [1,3,2,6,-1,4,1,8,2]
k = 3

# init averages
window_sum = sum(nums[:k])
averages = [window_sum / k]

# go through the whole list
for i in range(k, len(nums)):
    window_sum += nums[i]      # add new element
    window_sum -= nums[i-k]    # remove old element
    averages.append(window_sum / k)

print(averages)


