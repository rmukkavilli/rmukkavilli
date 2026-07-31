# Popped during traversal:
# right boundary = current index

# Still in stack after traversal:
# # right boundary = end of array
# stack hold index,num
# if curr val < stack[-1][1] --> remember need to get teh num value
# prev_index, prev_val = stack.pop()
# calculate width using i - index
# max(area, prev_val * width)
# start = prev_index

# finally for remaining in stack
# ****width calculation be mindful of using len(list) - start in for loop in stack  instead of i - previndex.*****
def get_highest_rectange(list):
    if not list:
        return -1
    max_area = 0
    stack = []
    for i, num in enumerate(list):
        start = i
        # note : stack[-1][1] nothing but list
        while stack and list[i] < stack[-1][1]:
            prev_index, prev_val = stack.pop()
            width = i - prev_index
            max_area = max(max_area, width * prev_val)
            start = prev_index
        stack.append([start, num])

    for start, val in stack:
        print(start, "", val)
        width = len(list) - start
        max_area = max(max_area, width * val)
    return max_area

list = [2, 1, 5, 6, 2, 3]
# print(get_highest_rectange([2, 1, 5, 6, 2, 3]))     # 10
# print(get_highest_rectange([2, 1, 2]))              # 3
# print(get_highest_rectange([2, 2]))                 # 4
print(get_highest_rectange([3,5,6,2]))                 # 4



# unit tests
def test_get_hieghest_rectangle_with_empty():
    assert get_highest_rectange([]) == -1

def test_get_hieghest_rectangle_with_None():
    assert get_highest_rectange(None) == -1

def test_get_hieghest_rectangle_repeated_val():
    assert get_highest_rectange([1, 1, 1, 1, 1]) == 0

def test_get_hieghest_rectangle_descending_order():
    assert get_highest_rectange([9, 8, 7, 6, 5])  == 24

def test_get_hieghest_rectangle_ascending_order():
    assert get_highest_rectange([1,2, 3, 4, 5])  == 0
