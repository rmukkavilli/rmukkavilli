def latest_failed_tests(results: list[dict]) -> list[str]:
    # Write your solution here
    status_map : dict[str, str] = {}
    for result in results:
        key = f"{result['suite']}.{result['test']}"
        status_map[key] = result["status"]
    print(status_map)
    return [key for key, statuses in status_map.items() 
            if "FAIL" in statuses ]

    


results = [
    {"suite": "login", "test": "valid_login", "status": "FAIL"},
    {"suite": "login", "test": "locked_account", "status": "PASS"},
    {"suite": "payments", "test": "add_card", "status": "FAIL"},
    {"suite": "login", "test": "valid_login", "status": "PASS"},
    {"suite": "login", "test": "locked_account", "status": "FAIL"},
    {"suite": "payments", "test": "add_card", "status": "FAIL"},
    {"suite": "payments", "test": "remove_card", "status": "PASS"}
]
print(latest_failed_tests(results))

# output: ["login.locked_account", "payments.add_card"]

