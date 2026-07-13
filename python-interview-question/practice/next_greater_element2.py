# Time and Space complexity is O(N)
# The tricker part and differecen between nextGenElements to this one is
# is to re loop to get circular effect to get the correct results.
def nextGreaterElements2(nums: list[int]) -> list[int]:
    stack = []
    result = [-1] * len(nums)

    for i in range(2*len(nums)):
        # index back to start once complete
        curr = nums[i % len(nums)] 
        while stack and curr > nums[stack[-1]]:
            index = stack.pop()
            result[index] = curr
        if i< len(nums):
            stack.append(i)
    return result


#Input:
nums = [1,2,1]
print(nextGreaterElements2(nums))

# Output:
# [2,-1,2]