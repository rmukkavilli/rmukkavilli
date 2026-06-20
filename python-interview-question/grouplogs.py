logs = [

"INFO Service Started",

"ERROR Camera Timeout",

"WARN Retry",

"ERROR Network Failure",

"INFO Success"

]

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
    severity = log.split()[0]
    dict[severity] = dict.get(severity, 0) + 1
print(dict)
