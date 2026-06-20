logs = [
    "INFO Service started",
    "ERROR Camera Timeout",
    "INFO Request completed",
    "ERROR Network Failure",
    "ERROR Camera Timeout",
    "WARN Retry attempted",
    "ERROR Sensor Disconnected"
]

dict = {}
# for l in logs:
#     if("ERROR" in l):
#         error = l.replace("ERROR", "").strip()
#         if error in dict:
#             dict[error] = dict.get(error, 0) + 1
#         else:
#             dict[error] = dict.get(error, 1)




for l in logs:
    if l.startswith("ERROR"):
        error = l.replace("ERROR", "").strip()
        dict[error] = dict.get(error,0)+1
print(dict)