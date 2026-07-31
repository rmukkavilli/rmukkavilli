# Time: O(n)
# Space: O(s + e) for the stored services and their unique errors
# use  group_dict[service] insted of  group_dict.get.. since its only going to add one level up the results are not accurate.

def count_errors_by_service(failures: list[dict]) -> dict:
    group_dict = {}
    for failure in failures:
        service = failure["service"]
        error = failure["error"]
        if service not in group_dict:
            group_dict[service] = {}
        group_dict[service][error] = group_dict[service].get(error, 0)+1
    return group_dict

failures = [
    {"service": "auth", "error": "401"},
    {"service": "payments", "error": "timeout"},
    {"service": "auth", "error": "401"},
    {"service": "payments", "error": "500"},
    {"service": "auth", "error": "token_expired"},
    {"service": "payments", "error": "timeout"}
]
print(count_errors_by_service(failures))


# expected o/p:
# {
#     "auth": {
#         "401": 2,
#         "token_expired": 1
#     },
#     "payments": {
#         "timeout": 2,
#         "500": 1
#     }
# }