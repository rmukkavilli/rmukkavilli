def is_valid(s: str) -> bool:
    stack = []
    pairs = {
        "(":")",
        "{":"}",
        "[":"]",
    }
    for ch in s:
        if ch in '[{(':
            stack.append(ch)
        else:
            print("read form pairs ",pairs[ch])
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack

s = "{[]}"
t = "((("
v = "((())"
print(is_valid(s))
print(is_valid(t))
print(is_valid(v))