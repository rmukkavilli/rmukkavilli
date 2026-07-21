def dupe_find(nums):
    # nums = [1,2,3,4]
    left = 0
    seen= set()
    for num in nums:
        while num in seen:
            seen.remove(num)
        seen.add(num)
    print(seen)
    return len(seen)

nums = [2,2,3]
print(dupe_find(nums))