def failure_counts(events):
    failure_count = {}
    for event in events:
        if event[1] !='PASS':
            failure_count[event[0]] = failure_count.get(event[0],0)+1
    return failure_count
events = [
    ("test_login", "PASS"),
    ("test_payment", "FAIL"),
    ("test_login", "FAIL"),
    ("test_search", "PASS"),
    ("test_payment", "FAIL"),
]
print(failure_counts(events))