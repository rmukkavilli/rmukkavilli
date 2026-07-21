def parse_failed_logs(logs: list[str]) -> list[dict]:
    parse_logs = []
    for log in logs:
        log_split = log.split(maxsplit=3)
        timestamp = log_split[0]
        service = log_split[1]
        severity = log_split[2]
        message = log_split[3]
        if severity == 'FAIL':
            if timestamp not in parse_logs:
                parse_logs.append({"timestamp":timestamp, "service": service, "message": message })
        
    return parse_logs


logs = [
    "2026-07-21T10:00:00 auth PASS login succeeded",
    "2026-07-21T10:01:00 auth FAIL token expired",
    "2026-07-21T10:02:00 payments FAIL card service timeout",
    "2026-07-21T10:03:00 search PASS results returned"
]
print(parse_failed_logs(logs))
# O/P:[
#     {
#         "timestamp": "2026-07-21T10:01:00",
#         "service": "auth",
#         "message": "token expired"
#     },
#     {
#         "timestamp": "2026-07-21T10:02:00",
#         "service": "payments",
#         "message": "card service timeout"
#     }
# ]