def aggregate_failures(logs: list[dict]) -> dict[str, dict[str, int]]:
    status_dict= {}
    for log in logs:
        service = log['service']
        status = log['status']
        error  = log['error']
        if status == 'FAIL':
            if service not in status_dict:
                status_dict[service] = {}
            if error not in status_dict[service]:
                status_dict[service][error] = 0
            status_dict[service][error] +=1
    return status_dict

logs = [
    {"service": "auth", "status": "FAIL", "error": "timeout"},
    {"service": "auth", "status": "FAIL", "error": "401"},
    {"service": "payments", "status": "FAIL", "error": "timeout"},
    {"service": "auth", "status": "FAIL", "error": "timeout"},
    {"service": "payments", "status": "PASS", "error": None},
    {"service": "search", "status": "PASS", "error": None}
]

print(aggregate_failures(logs))

# o/p: 
# {
#     "auth": {
#         "timeout": 2,
#         "401": 1
#     },
#     "payments": {
#         "timeout": 1
#     }
# }