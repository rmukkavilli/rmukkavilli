# TIme Complexity : O(N) 
# Space Complexity : O(N)

def parse_log_lines(logs: list[str]) -> list[dict]:
    result  = []
    for log in logs:
        log_entry = log.split(maxsplit=3)
        timestamp = log_entry[0] + " " +  log_entry[1]
        level = log_entry[2]
        message = log_entry[3]
        result.append({"timestamp": timestamp, "level": level, "message": message})
    return result

logs = [
    "2025-01-01 10:00:00 ERROR moduleX: timeout",
    "2025-01-01 10:01:00 INFO moduleY: started",
    "2025-01-01 10:02:00 WARN moduleZ: high memory"
]
print(parse_log_lines(logs))


# Expected O/P

# [
#     {
#         "timestamp": "2025-01-01 10:00:00",
#         "level": "ERROR",
#         "message": "moduleX: timeout"
#     },
#     {
#         "timestamp": "2025-01-01 10:01:00",
#         "level": "INFO",
#         "message": "moduleY: started"
#     },
#     {
#         "timestamp": "2025-01-01 10:02:00",
#         "level": "WARN",
#         "message": "moduleZ: high memory"
#     }
# ]