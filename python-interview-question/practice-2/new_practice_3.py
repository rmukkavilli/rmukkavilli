# Time complexity O(N) since we go every list 
# Space complexity O(N) and storing list
def find_flaky_runs(runs) -> dict:
    flaky_run ={}
    result = []
    for run in runs:
       if run['test_name'] not in flaky_run:
          flaky_run[run['test_name']] = []
       flaky_run[run['test_name']].append(run['status'])
    for key,value in flaky_run.items():
        if 'pass' in value and 'fail' in value:
            result.append(key)
    return result



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