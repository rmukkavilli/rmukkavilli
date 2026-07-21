def find_flaky_tests(results: list[dict]) -> list[str]:
    # Write your solution here
    pass


results = [
    {"suite": "login", "test": "valid_login", "status": "PASS"},
    {"suite": "login", "test": "locked_account", "status": "FAIL"},
    {"suite": "payments", "test": "add_card", "status": "FAIL"},
    {"suite": "login", "test": "valid_login", "status": "FAIL"},
    {"suite": "login", "test": "locked_account", "status": "FAIL"},
    {"suite": "payments", "test": "add_card", "status": "PASS"}
]

["login.valid_login", "payments.add_card"]