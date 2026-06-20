def group_code(logs):
    

    dict={}

    # for log in logs:
    #     if log.startswith("INFO"):
    #         info = log.replace("INFO","").strip()
    #         dict["INFO"] = dict.get("INFO", 0)+1
    #     elif log.startswith("ERROR"):
    #         print(log)
    #         error = log.replace("ERROR","").strip()
    #         print( dict.get("ERROR", 0))
    #         dict["ERROR"] = dict.get("ERROR", 0)+1
    #     elif log.startswith("WARN"):
    #         warn = log.replace("WARN","").strip()
    #         dict["WARN"] = dict.get("WARN", 0)+1
    for log in logs:
        severity, code = log.split()
        print(code)
       # severity = log.replace("ERROR","").strip()
        #dict[severity] = dict.get(severity, 0) + 1
        dict[code] = dict.get(code, 0) + 1
    return dict

# logs = [

#     "INFO Service Started",

#     "ERROR Camera Timeout",

#     "WARN Retry",

#     "ERROR Network Failure",

#     "INFO Success"

#     ]

logs = [
    "ERROR 500",
    "ERROR 404",
    "ERROR 500",
    "ERROR 403",
    "ERROR 404"
]

print(group_code(logs))