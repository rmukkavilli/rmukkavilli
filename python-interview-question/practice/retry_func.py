import time

def retry(func, max_attempts: int, delay: float):
    # while max_attempts > 0:
    #     try:
    #         res = func()
    #         if res == "Success":
    #             return res
    #     except RuntimeError:
    #         time.sleep(delay)
    #         max_attempts -=1
    res = None
    for attempts in range(max_attempts):
        try:
            return func()
        except Exception as e :
            res = e
            max_attempts -=1
        if attempts < max_attempts -1:
            time.sleep(delay)
    raise res



def unstable():
    unstable.count += 1
    if unstable.count < 3:
        raise RuntimeError("Still failing")
    return "Success"

unstable.count = 0
result = retry(unstable, max_attempts=5, delay=0.5)
print(result)  # "Success"