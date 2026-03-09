# Longest Substring Without Repeating Characters (Sliding Window / Two Pointers – Classic Medium-Hard) - Grok

# Problem
# -> Given a string s, find the length of the longest substring without repeating characters.

# Examples:
# "abcabcbb" → 3 ("abc")
# "bbbbb" → 1 ("b")
# "pwwkew" → 3 ("wke")
# "" → 0
# "dvdf" → 3 ("vdf")

def get_longest_substring(s: str) -> int:

    max_length = 0
    window = ""
    for char in s:
        len_window = len(window)
        if len_window > 0 and char in window:
            if len_window > max_length:
                max_length = len_window
            window = "".join(window[window.find(char)+1:])

        window = window + char

    if len(window) > max_length:
        return len(window)
    return max_length

tests = [
    "abcabcbb", # → 3 ("abc")
    "bbbbb", # → 1 ("b")
    "pwwkew", # → 3 ("wke")
    "", # → 0
    "dvdf", # → 3 ("vdf")
]

for test in tests:
    print(get_longest_substring(test))

# Best solution, use:
# set()
# 2 pointers

# def longest_substring(s: str) -> int:
#     seen = set()
#     left = 0
#     max_length = 0
#
#     for right in range(len(s)):
#
#         while s[right] in seen:
#             seen.remove(s[left])
#             left += 1
#
#         seen.add(s[right])
#         max_length = max(max_length, right - left + 1)
#
#     return max_length