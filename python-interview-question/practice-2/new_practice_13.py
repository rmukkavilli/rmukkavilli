def max_failure_streaks(results: list[dict]) -> dict[str, int]:
    # Write your solution here
    current_streaks: dict[str, int] = {}
    max_streaks: dict[str, int] = {}
    status_map:dict[str, str] = {}
    for result in results:
        key = f"{result['suite']}.{result['test']}"
        if key not in current_streaks:
            current_streaks[key] = 0
            max_streaks[key] = 0
        if result['status'] == 'FAIL':
            current_streaks[key] +=1
            max_streaks[key] = max(max_streaks[key],  current_streaks[key])
        else:
            current_streaks[key] = 0
    return max_streaks

results = [
    {"suite": "login", "test": "valid_login", "status": "FAIL"},
    {"suite": "payments", "test": "add_card", "status": "FAIL"},
    {"suite": "login", "test": "valid_login", "status": "FAIL"},
    {"suite": "login", "test": "valid_login", "status": "PASS"},
    {"suite": "payments", "test": "add_card", "status": "FAIL"},
    {"suite": "login", "test": "valid_login", "status": "FAIL"},
    {"suite": "payments", "test": "add_card", "status": "PASS"}
]
print(max_failure_streaks(results))

# o/p : {
#     "login.valid_login": 2,
#     "payments.add_card": 2
# }