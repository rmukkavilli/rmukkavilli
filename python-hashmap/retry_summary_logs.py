def retry_summary(logs: list[dict]) -> dict:
    retry_dict = {}
    for log in logs:
        end_point = log["endpoint"]
        status = log["status"]

        if end_point not in retry_dict:
            retry_dict[end_point] ={
                "requests":0,
                "retryable_errors":0,
                "longest_retryable_streak":0,
                "latest_status": 0,
                "_long_fail_streak":0,
            }
        retry_dict[end_point]["requests"] +=1
        if status == 429 or 500 <= status <= 599:
            retry_dict[end_point]["retryable_errors"] +=1
        retry_dict[end_point]["latest_status"] = status
        if status == 429 or 500 <= status <= 599:
            retry_dict[end_point]["_long_fail_streak"] +=1
            retry_dict[end_point]["longest_retryable_streak"] = max(retry_dict[end_point]["_long_fail_streak"], retry_dict[end_point]["longest_retryable_streak"])
        else:
            retry_dict[end_point]["_long_fail_streak"] = 0
    for endpoint in retry_dict.values():
        endpoint.pop("_long_fail_streak")

        
logs = [
    {"endpoint": "/login", "status": 500},
    {"endpoint": "/login", "status": 502},
    {"endpoint": "/login", "status": 200},
    {"endpoint": "/patient", "status": 404},
    {"endpoint": "/patient", "status": 503},
    {"endpoint": "/patient", "status": 503},
    {"endpoint": "/patient", "status": 200},
]
print(retry_summary(logs))
# Expected out:
# {
#     "/login": {
#         "requests": 3,
#         "retryable_errors": 2,
#         "longest_retryable_streak": 2,
#         "latest_status": 200
#     },
#     "/patient": {
#         "requests": 4,
#         "retryable_errors": 2,
#         "longest_retryable_streak": 2,
#         "latest_status": 200
#     }
# }

# unit tests :
def test_empty():
    res = retry_summary([])
    assert res == {}

def test_unknown_status_():
    res = retry_summary([
    {"endpoint": "/login", "status": 900},
    {"endpoint": "/patient", "status": 200},
    {"endpoint": "/patient", "status": 200}])
    assert res["/login"]["latest_status"] == 900
    assert res["/patient"]["latest_status"] == 200
