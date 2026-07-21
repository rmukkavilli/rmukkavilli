# class FailureTracker:

#     def __init__(self):
#         self.failure_map = {}

#     def add_failure(self, test_name: str, error_type: str):
#         ...

#     def get_failures(self):
#         ...

# tracker = FailureTracker()

# tracker.add_failure("test_login", "AUTH_ERROR")
# tracker.add_failure("test_checkout", "TIMEOUT")
# tracker.add_failure("test_profile", "AUTH_ERROR")

#print(tracker.get_failures())

# Time Complexity O( N log N) : since sorted list.
# Space Comlexity O(N)
def group_failures(
    failures: list[tuple[str, str]]) -> dict[str, list[str]]:
    group_fail = {}
    for failure in failures:
        fail_message = failure[0]
        fail_severity = failure[1]
        if fail_severity not in group_fail:
            group_fail[fail_severity] = []
        group_fail[fail_severity].append(fail_message)

     # sort the group : 
    for error in group_fail.values():
        error.sort()
    return group_fail



failures = [
    ("test_login", "AUTH_ERROR"),
    ("test_checkout", "TIMEOUT"),
    ("test_profile", "AUTH_ERROR"),
    ("test_search", "ASSERTION_ERROR"),
    ("test_cart", "TIMEOUT"),
]
print(group_failures(failures))
# O/P: {
#     "AUTH_ERROR": ["test_login", "test_profile"],
#     "TIMEOUT": ["test_cart", "test_checkout"],
#     "ASSERTION_ERROR": ["test_search"],
# }