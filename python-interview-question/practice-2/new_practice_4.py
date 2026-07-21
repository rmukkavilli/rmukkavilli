from collections import defaultdict
def find_flaky_runs(runs) -> dict:
    seen_name = defaultdict(set)
    res = []
    for run in runs:
        name = run["test_name"]
        status = run["status"]
        seen_name[name] = status
    if seen_name[name] == {"pass", "fail"}:
            res.append(name)
    return res



runs = [
    {"test_name": "test_login", "run_id": 1, "status": "pass"},
    {"test_name": "test_login", "run_id": 2, "status": "fail"},
    {"test_name": "test_login", "run_id": 3, "status": "pass"},
    {"test_name": "test_checkout", "run_id": 1, "status": "pass"},
    {"test_name": "test_checkout", "run_id": 2, "status": "pass"},
    {"test_name": "test_bookmark", "run_id": 1, "status": "fail"},
    {"test_name": "test_bookmark", "run_id": 2, "status": "fail"},
]
print(find_flaky_runs(runs))