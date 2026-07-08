from datetime import datetime
def parse_log_lines(logs: list[str]) -> list[dict]:
    result = []
    for log in logs:
        timestamp = log[:19]
        rest = log[20:].split(maxsplit=3)
        level = rest[0]
        module = rest[1].split(':')[0]
        if (len(rest) > 2):
            message = " ".join(rest[2:])
        else:
            message = ""
        result.append({
            "timestamp": timestamp,
            "level": level,
            "module": module,
            "message": message.strip(),
        })
    return result



logs = [
    "2025-01-01 10:00:00 ERROR moduleX: something happened    ",
    "2025-01-01 10:01:05 INFO moduleY: all good",
    "2025-01-01 10:01:05 INFO moduleY: ",
]
print(parse_log_lines(logs))