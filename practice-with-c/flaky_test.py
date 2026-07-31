from typing import List, Tuple

def find_flaky_tests(runs: List[Tuple[str, str]]) -> List[str]:
    """
    Given a list of (test_name, result) tuples from multiple test runs,
    return a sorted list of flaky test names — a test is flaky if it has
    both "pass" and "fail" somewhere in its results.

    Example:
        runs = [("test_login", "pass"), ("test_login", "fail"),
                ("test_logout", "pass"), ("test_logout", "pass")]
        find_flaky_tests(runs) -> ["test_login"]
    """
    flaky_dict = {}
    res = []
    if not runs:
        return []
    for run in runs:
        test_name, status = run
        if test_name not in flaky_dict:
            flaky_dict[test_name] = []
        flaky_dict[test_name].append(status)
    flaky_list = sorted(flaky_dict.items(), key = lambda x: x[0], reverse= False)
    for key in flaky_list:
        name, results = key
        if "pass" in results and "fail" in results:
            res.append(name)
    return res


runs = [("test_login", "pass"), ("test_login", "fail"), ("test_logout", "pass"), ("test_logout", "pass")]
print(find_flaky_tests(runs))


# Unit tests
def test_find_flaky_with_empty_list():
    assert find_flaky_tests([]) == []

def test_find_flaky_with_None():
    assert find_flaky_tests(None) == []

def test_find_flaky_with_no_flakes():
    assert find_flaky_tests([("test_login", "pass"), ("test_login", "pass"), ("test_logout", "pass"), ("test_logout", "pass")]) == []

def test_find_flaky_with_duplicate_flakes():
    runs2 =[("test_login", "pass"), ("test_login", "fail"),("test_login", "pass"), ("test_login", "fail"), ("test_logout", "pass"), ("test_logout", "pass")]
    assert find_flaky_tests(runs2) == ['test_login']

def test_find_flaky_with_sorted():
    runs2 =[("test_login", "pass"), ("test_login", "fail"), ("test_ind", "pass"), ("test_ind", "fail"),("test_logout", "pass"), ("test_logout", "pass")]
    assert find_flaky_tests(runs2) == ['test_ind', 'test_login']

