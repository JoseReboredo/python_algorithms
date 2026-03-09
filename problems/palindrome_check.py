# Palindrome Check (String + Basic Logic) - Grok proposed

# Problem
# -> Write a function is_palindrome(s: str)
# -> bool that returns True if the string s is a palindrome (reads the same forwards and backwards),
# -> ignoring case, spaces, and non-alphanumeric characters.

# Examples:
# "A man, a plan, a canal: Panama" → True
# "race a car" → False
# "" (empty) → True
# "a" → True

# Tips
# → Great for string cleaning (.isalnum(), .lower()) and two-pointer technique.

# Time: O(n)
# Space: O(n)

# another way of doing it:
# import re
# cleaned = re.sub(r'[^a-z0-9]', '', s.lower())
def clean(s: str) -> str:
    s = s.lower()
    letters = [l for l in s if l.isalnum()]

    return "".join(letters)


def is_palindrome(s: str) -> bool:

    s_cleaned = clean(s)
    # if not s_cleaned: Not needed the problem says an empty string is a polidrome
    #     return False

    left_pointer = 0
    right_pointer = len(s_cleaned)-1
    while left_pointer < right_pointer: # != if the len if not odd it will fail, use <
        if s_cleaned[left_pointer] != s_cleaned[right_pointer]:
            return False
        left_pointer += 1
        right_pointer -= 1

    return True

inputs = [
    "A man, a plan, a canal: Panama", # -> True
    "race a car", # -> False
    "", # -> True
    "a" # -> True
]

for input in inputs:
    print(is_palindrome(input))
