def positions_until_higher_latency(latencies: list[int]) -> list[int]:
    stack = []
    res = [0] * len(latencies)
    for i, num in enumerate(latencies):
        while(stack and num  > latencies[stack[-1]]):
            index = stack.pop()
            res[index] = i - index
        stack.append(i)
        print(stack)
    return res


#            [0 , 1, 2, 3, 4, 5]
latencies = [120, 100, 150, 90, 200]
# Expected: [2, 1, 2, 1, 0]
print(positions_until_higher_latency(latencies))