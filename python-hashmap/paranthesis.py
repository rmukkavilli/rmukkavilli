def is_valid_parentheses(s: str) -> bool:
    if not s:
        return False
    stack = []
    match_dict = {
        ']':'[',
        '}':'{',
        ')':'(',
    }

    for ch in s: 
        if ch in '{[(':
            stack.append(ch)
        else:
            if stack and match_dict[ch] == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
    print(stack)    
    return len(stack) == 0


s = "()"        # True
s1 = "()[]{}"    # True
s2 = "(]"        # False
s3 = "([)]"      # False
s4 ="{[]}"      # True
s5 = "}}}}}}"
s6 = "{{(["
print(is_valid_parentheses(s))
print(is_valid_parentheses(s1))
print(is_valid_parentheses(s2))
print(is_valid_parentheses(s3))
print(is_valid_parentheses(s4))
print(is_valid_parentheses(s5))
print(is_valid_parentheses(s6))


# Unit test cases:
def test_empty_string():
    assert is_valid_parentheses("") is False

def test_None_string():
    assert is_valid_parentheses(None) is False

def test_no_closing_paranthesis():
    assert is_valid_parentheses("}}}}}}") is False

def test_all_opening_paranthesis():
    assert is_valid_parentheses("{{([") is False

def test_valid_paranthesis():
    assert is_valid_parentheses("()") is True