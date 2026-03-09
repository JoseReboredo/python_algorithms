# Character Count + Palindrome Report (From Multiverse-style test) - Grok

# Problem
# -> Write a function string_report(s: str) -> str that returns a string report like:
# "The string has X characters. It is a palindrome." or "It is not a palindrome."
# -> Count all characters (including spaces/punctuation).
# -> Then check if it's a palindrome exactly as given (case-sensitive, no ignoring anything).

# Examples:
# "radar" → "The string has 5 characters. It is a palindrome."
# "hello" → "The string has 5 characters. It is not a palindrome."
# "" → "The string has 0 characters. It is a palindrome."

# → Directly inspired by Multiverse's old apprentice take-home — tests functions, strings, conditionals.

def is_palindrome(s: str) -> bool:

    left_pointer = 0
    right_pointer = len(s)-1
    while left_pointer < right_pointer:
        if s[left_pointer] != s[right_pointer]:
            return False
        left_pointer += 1
        right_pointer -= 1

    return True

def generate_report(s: str) -> str:
    if is_palindrome(s):
        return f"The string has {len(s)} characters. It is a palindrome."
    else:
        return f"The string has {len(s)} characters. It is not a palindrome."

inputs = [
    "radar",  #→ "The string has 5 characters. It is a palindrome."
    "hello", # → "The string has 5 characters. It is not a palindrome."
    "" # → "The string has 0 characters. It is a palindrome."
]

for input in inputs:
    print(generate_report(input))