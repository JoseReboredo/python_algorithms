# Valid Parentheses (Stack + String) - Grok

# Problem
# -> Given a string s containing only '(', ')', '{', '}', '[', ']',
# -> determine if it's valid (open brackets closed in correct order).

# Examples:
# "()[]{}" → True
# "(]" → False
# "([)]" → False
# "" → True

def is_using_valid_parentheses(s: str) -> bool:
    brackets = ["(", ")"]
    curly = ["{", "}"]
    squares = ["[","]"]

    stack = []
    for l in s:
        if l == brackets[0] or l == curly[0] or l == squares[0]:
            stack.append(l)
            continue

        # case where the string starts with a closing parentheses
        if not stack:
            return False

        last = stack.pop()
        if  last == brackets[0] and l == brackets[1]:
            continue
        if  last == curly[0] and l == curly[1]:
            continue
        if  last == squares[0] and l == squares[1]:
            continue

        return False

    if len(stack) != 0:
        return False
    return True

tests = [
    "()[]{}", # True
    "(]", # False
    "([)]", # False
    "" # True
]

for t in tests:
    print(is_using_valid_parentheses(t))



