def group_failed_tests(results: list[dict]) -> dict[str, list[str]]:
    # Write your solution here
    res_dic = {}
    for result in results:
        suite_key = result['suite']
        test_val = result['test']
        status_val = result['status']
        if status_val == 'FAIL':
            if suite_key not in res_dic:
                res_dic[suite_key] = []
            res_dic[suite_key].append(test_val)
    return res_dic



results = [
    {"suite": "login", "test": "valid_login", "status": "PASS"},
    {"suite": "login", "test": "locked_account", "status": "FAIL"},
    {"suite": "payments", "test": "add_card", "status": "FAIL"},
    {"suite": "login", "test": "expired_token", "status": "FAIL"},
    {"suite": "payments", "test": "remove_card", "status": "PASS"}
]
print(group_failed_tests(results))
# Expected:
# {
#     "login": ["locked_account", "expired_token"],
#     "payments": ["add_card"]
# }


