def summarize_failures(results: list[dict]) -> dict:
    struct_dict = {}
    for res in results:
        comp = res["test"]
        env = res["environment"]
        status = res["status"]
       # key = f"{comp}.{env}"
        
        if comp not in struct_dict:
            struct_dict[comp] = {}
        if env not in struct_dict[comp]:
            struct_dict[comp][env]= {
                "total": 0,
                "failures": 0,
                "longest_failure_streak": 0,
                "latest_status": None,
                "_long_fail_streak":0,
            }
        stats = struct_dict[comp][env]
        
        stats["total"] += 1
        stats["latest_status"] = status
        if status == "FAIL":
            stats["failures"] += 1
            stats["_long_fail_streak"] +=1
            stats["longest_failure_streak"] = max(stats["longest_failure_streak"], stats["_long_fail_streak"])
        else:
            stats["_long_fail_streak"] = 0
        
   # print(struct_dict)
    for comp in struct_dict:
        for env in struct_dict[comp]:
            if stats["_long_fail_streak"] > 0:
                del stats["_long_fail_streak"]
    
    return struct_dict
  
        

        # if "total" not in  struct_dict[comp][env]:
        #     struct_dict[comp][env]["total"] = 0
        # struct_dict[comp][env]["total"] +=1
        # if "failures" not in  struct_dict[comp][env]:
        #     struct_dict[comp][env]["failures"] = 0
        # if status == "FAIL":
        #     struct_dict[comp][env]["failures"] =  struct_dict[comp][env].get(status, 0)+1
        # if "latest_status" not in struct_dict[comp][env]:
        #     struct_dict[comp][env]["latest_status"] = None
        # struct_dict[comp][env]["latest_status"] = struct_dict[comp][env] = status
        # # if "longest_failure_streak" not in struct_dict[comp][env]:
        # #     struct_dict[comp][env]["longest_failure_streak"] = 0
        # # if status not in struct_dict[comp][env]:
        # #     max_failure_streak[comp][env][status] = 0
        # #     current_count[comp][env][status] = 0
        # # if max_failure_streak[comp][env] == "FAIL":
        # #     print(current_count[comp][env][status].get(comp,0))
        # #     current_count[comp][env][status] = current_count[comp][env][status].get(comp,0) +1
        # #     max_failure_streak[comp][env][status] = max(max_failure_streak[comp][env][status], current_count[comp][env][status])
        # # else:
        # #     current_count[comp] = 0
        # # struct_dict[comp][env]["longest_failure_streak"] = max_failure_streak[comp][env][status]



              
    
results = [
    {"test": "login", "environment": "staging", "status": "FAIL"},
    {"test": "payment", "environment": "prod", "status": "PASS"},
    {"test": "login", "environment": "staging", "status": "FAIL"},
    {"test": "login", "environment": "prod", "status": "PASS"},
    {"test": "payment", "environment": "prod", "status": "FAIL"},
    {"test": "login", "environment": "staging", "status": "UNKNOWN"},
]
print(summarize_failures(results))



def test_empty_results():
    result = summerize_failures([])
    assert result == {}
def test_all_passes():
     results = [
        {"test": "login", "environment": "prod", "status": "PASS"},
        {"test": "login", "environment": "prod", "status": "PASS"},
    ]
     assert summerize_failures(results)["login"]["prod"] == {
        "total": 2,
        "failures":0,
        "longest_failure_streak": 0,
        "latest_status": 'PASS',
     }