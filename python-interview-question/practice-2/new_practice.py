def failing_test_counts(events: list[tuple[str, str]]) -> list[tuple[str, int]]:
    fail_count = {}
    for event in events:
        event_code = event[0]
        status = event[1]
        if status == 'FAIL':
            fail_count[event_code] = fail_count.get(event_code, 0)+1
    return tuple(fail_count.items())


events = [
    ("login_test", "PASS"),
    ("checkout_test", "FAIL"),
    ("login_test", "FAIL"),
    ("search_test", "PASS"),
    ("checkout_test", "FAIL"),
]
tests = []
print(failing_test_counts(tests))

# o/P
# [
#     ("checkout_test", 2),
#     ("login_test", 1),
# ]