def nextGreateElement(nums1: list[int], nums2: list[int]) -> list[int]:
    num_dict = {}
    stack =[]
    res = [-1] * len(nums1)
    for i, num in enumerate (nums2):
        while stack and num > stack[-1]:
            element = stack.pop()
            num_dict[element] = num
        stack.append(num)
    for i,num in enumerate (nums1):
        print(num_dict.get(num, -1))
        res[i] = num_dict.get(num, -1)
    return res

nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(nextGreateElement(nums1, nums2))



