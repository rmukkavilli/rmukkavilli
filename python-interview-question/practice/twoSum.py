# Time complexity : O(N) linear one pass
# Space complexity : O(N) storing entire key and value pairs in dictonary, finding take O(1)
def has_pair_with_sum(nums: list[int], target: int) -> bool:
    needed = {}
    for i,num in enumerate(nums):
        sum = target - num
        if num in needed:
            return True
        needed[sum] = i
    return False



nums = [2, 7, 11, 15]
target = 9
print("1 ->", has_pair_with_sum(nums, target))
# True, because 2 + 7 = 9

nums_1 = [1, 3, 5, 8]
target_1 = 10
print("2 ->" , has_pair_with_sum(nums_1, target_1))
# False