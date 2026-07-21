def get_highest_rectange(list) -> int:
    stack = []
    max_val = 0
    for i, num in enumerate(list):
        start  = i
        while stack and stack[-1][1] > num:
            prev_index, prev_hieght = stack.pop()
            width = i - prev_index
            max_val = max(max_val, prev_hieght*width)
            start = prev_index
        stack.append((start, num))
    # remaining left off eleemnts
    for start, hieght in stack:
        # ensure compare with len of list
        width = len(list) - start
        max_val = max(max_val, width * hieght)

    return max_val

list = [2, 1, 5, 6, 2, 3]
print(get_highest_rectange([2, 1, 5, 6, 2, 3]))     # 10
print(get_highest_rectange([2, 1, 2]))              # 3
print(get_highest_rectange([2, 2]))                 # 4