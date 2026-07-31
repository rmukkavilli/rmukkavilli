def find_first_duplicate(events: list[str]) -> str | None:
    if events is None:
        return None
    seen = set()
    for event in events:
        if event.lower() in seen:
            return event
        seen.add(event.lower())
    return None


s= ["A", "b", "c", "D", "E"]
s1= [" ", "b", " ", "D", "E"]
s2= []
s3 = None
s4 = ["invalid", "valid", "inValid" , "VALID", "invalid"]
print(find_first_duplicate(s))
print(find_first_duplicate(s1))

print(find_first_duplicate(s2))
print(find_first_duplicate(s3))
print(find_first_duplicate(s4))

def test_empty_list():
    assert find_first_duplicate([]) is None

def test_None_list():
    assert find_first_duplicate(None) is None

def test_no_duplicate_list():
    assert find_first_duplicate(["A", "b", "c", "D", "E"]) is None

def test_duplicates_with_empty_string():
    assert find_first_duplicate(["", "b", "", "D", "E"]) == ""

def test_valid_InValid():
    assert find_first_duplicate(["invalid", "valid", "inValid" , "VALID", "invalid"]) == "inValid"