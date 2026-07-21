def retryable_endpoints(responses: list[dict]) -> list[str]:
    # Write your solution here
    result = []
    seen = set()
    for response in responses:
        key = response["endpoint"]
        status_code = response["status_code"]
        if status_code == 429 or 500 <= status_code <= 599 :
            if key not in seen:
                seen.add(key)
                result.append(key)
            else:
                continue
    return result


responses = [
    {"endpoint": "/auth", "status_code": 500},
    {"endpoint": "/profile", "status_code": 401},
    {"endpoint": "/auth", "status_code": 503},
    {"endpoint": "/token", "status_code": 429},
    {"endpoint": "/health", "status_code": 200},
    {"endpoint": "/orders", "status_code": 404},
    {"endpoint": "/token", "status_code": 500}
]

print(retryable_endpoints(responses))