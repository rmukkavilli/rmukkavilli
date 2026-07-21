def count_failures_by_environment(
    results: list[dict]
) -> dict[str, dict[str, int]]:
    # Write your solution here
    res_dict = {}
    for result in results: 
        key = result["environment"]
        status = result["status"]
        suite = result["suite"]
        if status == "FAIL":
            if key not in res_dict:
                res_dict[key] = {}
            if suite not in res_dict[key]:
                res_dict[key][suite]  = 0
            res_dict[key][suite] +=1
    return res_dict


results = [
    {"environment": "staging", "suite": "login", "status": "FAIL"},
    {"environment": "staging", "suite": "login", "status": "PASS"},
    {"environment": "staging", "suite": "payments", "status": "FAIL"},
    {"environment": "production", "suite": "login", "status": "FAIL"},
    {"environment": "production", "suite": "payments", "status": "PASS"},
    {"environment": "production", "suite": "login", "status": "FAIL"}
]
print(count_failures_by_environment(results))


# o/p:

# {
#     "staging": {
#         "login": 1,
#         "payments": 1
#     },
#     "production": {
#         "login": 2
#     }
# }