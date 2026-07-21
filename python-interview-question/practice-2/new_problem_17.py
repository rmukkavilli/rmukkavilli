def slow_endpoints(
    responses: list[dict],
    threshold_ms: int
) -> dict[str, float]:
    latency_sums: dict[str, int] = {}
    request_counts: dict[str, int] = {}
    result ={}
    for resp in responses:
        end_point = resp['endpoint']
        latency = resp['latency_ms']
        if end_point not in latency_sums:
            latency_sums[end_point] = 0
            request_counts[end_point] = 0
        latency_sums[end_point] = latency_sums[end_point] + latency
        request_counts[end_point] = request_counts[end_point] + 1
    for end_point in latency_sums:
        avg = latency_sums[end_point]/request_counts[end_point]
        if avg >= threshold_ms:
            result[end_point] = avg
    return result
    



responses = [
{"endpoint": "/auth", "latency_ms": 100},
{"endpoint": "/profile", "latency_ms": 80},
{"endpoint": "/auth", "latency_ms": 300},
{"endpoint": "/payments", "latency_ms": 500},
{"endpoint": "/profile", "latency_ms": 120},
{"endpoint": "/auth", "latency_ms": 200}
]

print(slow_endpoints(responses, 100))
print(slow_endpoints(responses, 200))
print(slow_endpoints(responses, 500))