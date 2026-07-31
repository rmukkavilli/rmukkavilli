def all_tests_passed(results: list[str]) -> bool:
    #  this might fail for timed out.
    #  if not results:
    #      return False
    #  if "fail" in results and "pass" in results:
    #      return False
    #  if "pass" not in results:
    #     return False
    #  if "unknown" in results or "skip" in results or "error" in results:
    #     return False
    #  return True
    return all(key =="pass" for key in results)
    #return bool(results) and all(r=="pass" for r in results)
    

results = ["fail", "pass", "timedout"]
print(all_tests_passed(results))

def test_all_results_pass():
    assert all_tests_passed(["pass", "pass", "pass"]) is True

def test_all_results_fails():
    assert all_tests_passed(["fail", "fail", "fail"]) is False

def test_results_flaky():
    assert all_tests_passed(["fail", "pass", "fail"]) is False

def test_results_unknown():
    assert all_tests_passed(["fail", "pass", "unknown"]) is False

def test_results_skip():
    assert all_tests_passed(["fail", "pass", "skip"]) is False

def test_results_error():
    assert all_tests_passed(["fail", "pass", "error"]) is False
    