def is_valid_brackets(expression: str) -> bool:
    # Your implementation
    match_dict= {
        ']':'[',
        '}':'{',
        ')':'(',
    }
    stack = []
    if len(expression) == 0:
        return True
    for ch in expression:
        if ch in '({[':
            stack.append(ch)
        else:  
            if stack and stack[-1] == match_dict[ch]:
                stack.pop()
            else:
                # explicit case when stack empty but trying for any elements like ]
                return False
    return len(stack) == 0
        
    
tests = [
    ("{[()]}", True),
    ("{[(])}", False),
    ("(((", False),
    ("", True),
    ("]", False),
    ("()[]{}", True),
    ("A#$$$", False),
]

for expression, expected in tests:
    print(expression, is_valid_brackets(expression), expected)