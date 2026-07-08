def findSum(nums, target):
    seen = {}
    for n in range(len(nums)):
        sum = target - nums[n]
        print(sum, "00>", n)
        if sum not in seen:
           seen[nums[n]] = n
        else:
            return [seen[n], n]

def two_sum(nums: list[int], target: int) -> list[int] | None:
    seen = {}
    for i,num in enumerate(nums):
        sum = target -  num
        if sum in seen:
            return [seen[sum], i]
        seen[num] = i
    return None


nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums,target))

# Expected output: [0, 1]  because 2 + 7 == 9