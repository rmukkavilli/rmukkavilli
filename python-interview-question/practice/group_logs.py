# Time complexty : O(N)
# Space complexity : O (N)

def group_logs_by_severity(logs: list[str]) -> dict[str, list[str]]:
    log_dict = {}
    for log in logs:
        main_log = log.split(maxsplit=3)
        severity = main_log[2]
        message = main_log[3]
        if severity not in log_dict:
            log_dict[severity] = []
        log_dict[severity].append(message)
    return log_dict


logs = [
    "2025-01-01 10:00:00 ERROR moduleX: timeout",
    "2025-01-01 10:01:00 INFO moduleY: started",
    "2025-01-01 10:02:00 ERROR moduleZ: database failed",
    "2025-01-01 10:03:00 WARN moduleX: high memory",
    "2025-01-01 10:04:00 INFO moduleY: finished",
]
print(group_logs_by_severity(logs))