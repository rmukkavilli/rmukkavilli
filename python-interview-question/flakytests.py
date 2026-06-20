tests = {
    "CameraTest": ["PASS", "FAIL", "PASS"],
    "SensorTest": ["PASS", "PASS", "PASS"],
    "NavigationTest": ["FAIL", "PASS", "FAIL"],
    "APITest": ["PASS", "PASS", "PASS"]
}
list=[]
val_to_find =["FAIL", "PASS"]
for key,value in tests.items():
    if "FAIL" in value and "PASS" in value:
        print(value)
        list.append(key)
print(list)