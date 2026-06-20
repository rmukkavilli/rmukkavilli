sensor_status = {
"camera":"OK",
"lidar":"FAIL",
"radar":"OK",
"gps":"FAIL"
}

list=[]
for key,value in sensor_status.items():
    print(key, "", value)
    if "FAIL" in value:
        list.append(key)
print(list)

