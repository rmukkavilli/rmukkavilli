def find_logs(logs):
    log_dict = {}
    for log in logs:
        status = log[0]
        reason = log[1]
        dict_2 = {}
        if not reason in log_dict:
            log_dict[reason] = {'PASS': 0, 'FAIL': 0}
        log_dict[reason][status] +=1
    return log_dict
 

logs = [
    ("PASS", "login"),
    ("FAIL", "payment"),
    ("FAIL", "payment"),
    ("PASS", "search"),
    ("FAIL", "login"),
    ("PASS", "payment"),
]
print(find_logs(logs))