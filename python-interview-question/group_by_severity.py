def group_by_severity(logs):
    severity_dict={}
    for log in logs:
        error, code = log.split(" ", 1)
        if error not in severity_dict:
            severity_dict[error] = []
            
        severity_dict[error].append(code)
    return severity_dict    


logs = [
    "ERROR Disk Failure",
    "WARN CPU High",
    "ERROR Memory Full",
    "INFO Service Started",
    "WARN High Temperature"
    ]
print(group_by_severity(logs))


# Expected resuts: 
# {
# 'ERROR': ['Disk Failure', 'Memory Full'],
# 'WARN': ['CPU High', 'High Temperature'],
# 'INFO': ['Service Started']
# }