# Time Complexity : O(N) since we are processing each logs message 
# Space complexity : O(N) Storing in dict
def group_logs(logs: list[str]) -> dict[str, list[str]]:
    log_group = {}
    for log in logs:
        log_split = log.split(maxsplit=2)
        timestamp = log_split[0]
        severity = log_split[1]
        message = " ".join(log_split[2:])
        if severity not in log_group:
            log_group[severity] = []
        log_group[severity].append(message)
    return log_group

logs = [
    "2025-01-01 INFO Service started",
    "2025-01-01 ERROR Database connection failed",
    "2025-01-01 INFO User logged in",
    "2025-01-01 WARN Low disk space",
    "2025-01-01 ERROR Timeout"
]
print(group_logs(logs))

# Expected output :
# {
#     "INFO": [
#         "Service started",
#         "User logged in"
#     ],
#     "ERROR": [
#         "Database connection failed",
#         "Timeout"
#     ],
#     "WARN": [
#         "Low disk space"
#     ]
# }