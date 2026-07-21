# Time complexity : O(N) 
# Space complexity : O(f+s) worst case O(N)
def count_failures_by_suite(results: list[dict]) -> dict[str, int]:
    # Write your solution here
    res_dic = {}
    for result in results:
        suite_name = result['suite']
        status_val = result['status']
        test_val = result['test']
        if status_val =='FAIL':
            # print(suite_name)
            # res_dic[suite_name] = res_dic.get(suite_name, 0) + 1
            if status_val not in res_dic:
                res_dic[suite_name] = []
            res_dic[suite_name].append(test_val)
    return res_dic



results = [
    {"suite": "login", "test": "valid_login", "status": "PASS"},
    {"suite": "login", "test": "locked_account", "status": "FAIL"},
    {"suite": "payments", "test": "add_card", "status": "FAIL"},
    {"suite": "login", "test": "expired_token", "status": "FAIL"},
    {"suite": "payments", "test": "remove_card", "status": "PASS"}
]

print(count_failures_by_suite(results))
# Expected: {"login": 2, "payments": 1}