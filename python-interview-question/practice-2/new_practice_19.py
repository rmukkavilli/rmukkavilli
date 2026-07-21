#Time: O(r + s)
# Space: O(s + m) for responded and missing IDs
# 
def requests_without_responses(
    requests: list[dict],
    responses: list[dict]
) -> list[str]:
    result = []
    resp_dict = {}
    seen = set()
    for resp in responses:
        req_id = resp["request_id"]
        resp_dict[req_id] = req_id
    print(resp_dict)

    for req in requests: 
        req_id =  req["request_id"]
        if req_id not in resp_dict and req_id not in seen: 
            seen.add(req_id)
            result.append(req_id)
    return result



requests = [
    {"request_id": "r1", "endpoint": "/auth"},
    {"request_id": "r2", "endpoint": "/profile"},
    {"request_id": "r3", "endpoint": "/payments"},
    {"request_id": "r2", "endpoint": "/profile"},
    {"request_id": "r4", "endpoint": "/health"}
]

responses = [
    {"request_id": "r2", "status_code": 200},
    {"request_id": "r4", "status_code": 500}
]
print(requests_without_responses(requests, responses))


# o/p  ["r1", "r3"]