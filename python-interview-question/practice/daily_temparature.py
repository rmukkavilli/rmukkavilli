def daily_temperatures(temperatures: list[int]) -> list[int]:
    temp_stack = []
    res = [0] * len(temperatures)
    print(res)
    for i, temp in enumerate (temperatures):
        while temp_stack and temp > temperatures[temp_stack[-1]]:
             index = temp_stack.pop()
             res[index] = i - index
        temp_stack.append(i)
    return res


#temperatures = [73,74,75,71,69,72,76,73]
temperatures = [120,100,150, 90,200]
print(daily_temperatures(temperatures))