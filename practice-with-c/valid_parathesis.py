
def is_valid_parenthesis(s: str| None) -> bool:
    if s is None:
        return False
    stack = []
    paranthesis_dict = {
        ']':'[',
        '}':'{',
        ')':'('
    }
    for ch in s:
        if ch in '{[(':
            stack.append(ch)
        else:
            if stack and paranthesis_dict[ch] == stack[-1]:
                stack.pop()
            else:
               return False
    return len(stack) == 0

s = "()"        # True
s1 = "()[]{}"    # True
s2 = "(]"        # False
s3 = "([)]"      # False
s4 ="{[]}"      # True
s5 = "}}}}}}"
s6 = "{{(["
s7 = None
s8 = "{}()[]"


print(is_valid_parenthesis(s))
print(is_valid_parenthesis(s1))
print(is_valid_parenthesis(s2))
print(is_valid_parenthesis(s3))
print(is_valid_parenthesis(s4))
print(is_valid_parenthesis(s5))
print(is_valid_parenthesis(s6))
print(is_valid_parenthesis(s7)) # False
print(is_valid_parenthesis("abc"))
print(is_valid_parenthesis(s8))




def test_empty_string():
    assert is_valid_parenthesis("") is True

def test_None_string():
    assert is_valid_parenthesis(None) is False

def test_paranthesis_invalid():
    assert is_valid_parenthesis("}}}}}}{}}") is False

def test_paranthesis_valid():
    assert is_valid_parenthesis("({[]})") is True

def test_with_open_paranthesis():
    assert is_valid_parenthesis("{") is False

def test_with_closing_paranthesis():
    assert is_valid_parenthesis("}") is False