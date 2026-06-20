# Space : O(N)
# Time O(1) single look up but overall O(N) set
def contains_dupes(nums):
    seen = set()
    for num in nums:
        if num in index:
            return True
        else:
            seen.add(num)
    return False

nums = [1,2,3,4,5]
print(contains_dupes(nums))