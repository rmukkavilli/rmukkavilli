# Time: O(len(nums1) + len(nums2))
# Space: O(len(nums2))
def next_greater_element(
    nums1: list[int],
    nums2: list[int]
) -> list[int]:
    stack = []
    next_greater={}
    res = []

    for num in nums2:
        while stack and num > stack[-1]:
            key = stack.pop()
            next_greater[key] = num
        stack.append(num)
  
    for num in nums1:
        res.append(next_greater.get(num, -1))
    return res


    print(stack)
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(next_greater_element(nums1, nums2))
