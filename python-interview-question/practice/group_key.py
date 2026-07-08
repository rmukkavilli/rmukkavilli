from collections import defaultdict
def group_by_key(items: list[dict], key: str) -> dict:
    #key_group = {}
    key_group = defaultdict(list)
    for item in items:
        item_key = item[key]
        # key_val = item["name"]
        # val = item["age"]
        if item_key not in key_group:
            key_group[item_key] = []
        key_group[item_key].append(item)
    return dict(key_group)



            

users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob",   "age": 25},
    {"name": "Carla", "age": 30},
    {"name": "Dave",  "age": 25},
]
print(group_by_key(users, "age"))