def insert_possition(nums:list[int], target:int):
    if nums is None or target is None:
        return -1
    left = 0
    right = len(nums) -1
    
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        
        if nums[mid] < target:
            left = mid +1
        else:
            right = mid - 1
    return left



nums = [1,3,5,6]
print(insert_possition(nums, 7))
print(insert_possition([5], None))
def test_insert_possition_empty():
    assert insert_possition([], 0) == 0

def test_insert_possition_None():
    assert insert_possition(None, 1) == -1

def test_insert_possition_for_existing():
    assert insert_possition([1], 1) == 0

def test_insert_possition_for_zero():
    assert insert_possition([1], 0) == 0

def test_insert_possition_sorted_nums():
    assert insert_possition([1,2,3,4,5,6,7,8,9], 10 ) == 9

def test_insert_possition_unsorted_nums():
    assert insert_possition([6,124,6,81, 5,89,44], 80) == -1

def test_insert_position_before_all():
    assert insert_position([1, 3, 5, 6], -2) == 0