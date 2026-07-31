def top_k_errors(errors: list[int], k: int) -> list[int]:
    # Your implementation
    freq_dict = {}
    result = []
    for error in errors:
        freq_dict[error] = freq_dict.get(error, 0)+1
    print(freq_dict)
    res = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    for key, value in res[:k]:
        result.append(key)
    return result


tests = [
    ([500, 404, 500, 401, 404, 500, 403], 2, [500, 404]),
    ([], 2, []),
    ([500, 500], 0, []),
]

for errors, k, expected in tests:
    print(top_k_errors(errors, k), expected)