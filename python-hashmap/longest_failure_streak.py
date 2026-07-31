def longest_failure_streaks(results: list[dict]) -> dict[str, int]:
    # Your implementation
    count_dict = {}
    max_streaks ={}
    for result in results:
        if not result["test"] in count_dict:
             count_dict[result["test"]] = 0
             max_streaks[result["test"]] = 0
        if result["status"] == "FAIL":
            count_dict[result["test"]] = count_dict.get(result["test"], 0)+ 1
            max_streaks[result["test"]] = max(max_streaks[result["test"]] ,count_dict[result["test"]])
        else:
            count_dict[result["test"]] = 0
    return max_streaks
        
results = [
    {"test": "login", "status": "FAIL"},
    {"test": "login", "status": "FAIL"},
    {"test": "payment", "status": "FAIL"},
    {"test": "login", "status": "PASS"},
    {"test": "payment", "status": "FAIL"},
    {"test": "login", "status": "FAIL"},
]

print(longest_failure_streaks(results))
# Expected: {"login": 2, "payment": 2}