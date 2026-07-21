def find_flaky_tests(results: list[dict]) -> list[str]:
    status_map: dict[str, set[str]] = {}
    for result in results:
        key = f"{result['suite']}.{result['test']}"
        # adding key to set
        status_map.setdefault(key, set()).add(result['status'])

    return [key for key, statuses in status_map.items() 
            if "PASS" in statuses and "FAIL" in statuses]

results = [
    {"suite": "login", "test": "valid_login", "status": "PASS"},
    {"suite": "login", "test": "locked_account", "status": "FAIL"},
    {"suite": "payments", "test": "add_card", "status": "FAIL"},
    {"suite": "login", "test": "valid_login", "status": "FAIL"},
    {"suite": "login", "test": "locked_account", "status": "FAIL"},
    {"suite": "payments", "test": "add_card", "status": "PASS"}
]
print(find_flaky_tests(results))

# O/ P ["login.valid_login", "payments.add_card"]