# O(n)/ O(k)
def count_error_code(list):
    dict= {}
    for errror in list:
        severity, code = errror.split()
        dict[code] = dict.get(code, 0)+1
    return dict







# Count Error Codes from Logs
logs = [
    "ERROR 500",
    "ERROR 404",
    "ERROR 500",
    "ERROR 403",
    "ERROR 404"
]
print(count_error_code(logs))


# {
#     "500": 2,
#     "404": 2,
#     "403": 1
# }

    