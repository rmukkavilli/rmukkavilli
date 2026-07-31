# Problem 1 — REVIEW: Hash Map + One-Pass Processing
# Given test execution records in chronological order: do it O(N) time
# O/p : ["profile.update", "payments.card"]
# Complexity:

# Time: O(n)
# Space: O(u), where u is the number of unique tests
def latest_failed_tests(results: list[dict]) -> list[str]:
    res = {}
    for result in results:
        res[ result['test']] = result['status']
    return [status for status, error in res.items() if error == "FAIL"]

results = [
    {"test": "login.valid", "status": "FAIL"},
    {"test": "payments.card", "status": "PASS"},
    {"test": "login.valid", "status": "PASS"},
    {"test": "profile.update", "status": "FAIL"},
    {"test": "payments.card", "status": "FAIL"}
]
print(latest_failed_tests(results))