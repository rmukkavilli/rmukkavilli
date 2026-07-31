from typing import List
import pytest

def two_sum(nums: List[int], target: int) -> List[int]:
    nums_dict = {}
    res = []
    for i, num in enumerate(nums):
        needed = target - num
        if needed in nums_dict:
            return [nums_dict.get(needed), i]
        nums_dict[num] = i
    raise ValueError(f"two_sum not found for target : {target}")

nums = [3,3]
target = 6
print(two_sum(nums, target))


def test_with_valid_only_matching_target_elements():
    assert two_sum([3,3 ], 6) == [0, 1]

def test_with_valid_more_than_target_elements():
    assert two_sum([5,5,5,4,2], 6) == [3,4]

def test_with_more_than_one_matching_target():
    assert two_sum([3,3,4,2], 6) == [0,1]

def test_with_more_than_one_not_matching_target():
    with pytest.raises(ValueError): two_sum([0,1], 0)

def test_no_target_matching_elements():
    with pytest.raises(ValueError):
        two_sum([5,5, 3,3, 7, 8, 7,8], 2)

    