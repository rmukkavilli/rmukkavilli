def filter_records(records: list[dict], filters: dict) -> list[dict]:
    result = []
    for record in records:
        if all(key in record and record[key] == value for key, value in filters.items()):
                result.append(record)
    return result

records = [
    {"name": "Alice", "age": 30, "city": "SF"},
    {"name": "Bob",   "age": 25, "city": "NY"},
    {"name": "Carla", "age": 30, "city": "NY"},
]

filters = {"age": 30, "city": "NY"}
print(filter_records(records, filters))