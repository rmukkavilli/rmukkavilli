def failures_in_both_environments(results: list[dict]) -> list[str]:
    failed_env: dict[str, set[str]] = {}
    result = []

    for log in results:
        if log["status"] == "FAIL":
            key = f"{log['suite']}.{log['test']}"
            failed_env.setdefault(key, set()).add(log["environment"])

    for test_key, env_set in failed_env.items():
        if "staging" in env_set and "production" in env_set:
            result.append(test_key)

    return result
  


    print(failed_env)

results = [
    {"environment": "staging", "suite": "login", "test": "valid_login", "status": "FAIL"},
    {"environment": "production", "suite": "login", "test": "valid_login", "status": "FAIL"},
    {"environment": "staging", "suite": "payments", "test": "add_card", "status": "FAIL"},
    {"environment": "production", "suite": "payments", "test": "add_card", "status": "PASS"},
    {"environment": "production", "suite": "payments", "test": "add_card", "status": "FAIL"},
    {"environment": "staging", "suite": "login", "test": "locked_account", "status": "FAIL"}
]
print(failures_in_both_environments(results))

# O/p: ["login.valid_login", "payments.add_card"]