def multiply(nums):
    res = [1,1,1,1]
    # Brute force.
    # for i in range(len(nums)):
    #     print(i)
    #     temp = nums[i] 
    #     nums[i] = 1
    #     # get multiplication here.

    #     product =1

    #     for n in nums:
    #         product = n*product
    #     nums[i] =temp
    #     result.append(product)
    # return result

    # Using LP * RP
    # Left product calculation
    for i in range(1, len(nums)):
        res[i] = nums[i-1] * res[i-1]
    #print(res)
    
    # Right product calculation:
    # i = 3 (last element):
# res[3] = res[3] * right_product = 6 * 1 = 6
# right_product = right_product * nums[3] = 1 * 4 = 4

# # i = 2:
# res[2] = res[2] * right_product = 2 * 4 = 8
# right_product = right_product * nums[2] = 4 * 3 = 12

# # i = 1:
# res[1] = res[1] * right_product = 1 * 12 = 12
# right_product = right_product * nums[1] = 12 * 2 = 24

# # i = 0:
# res[0] = res[0] * right_product = 1 * 24 = 24
# right_product = right_product * nums[0] = 24 * 1 = 24
    # right_product
    right_product = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] = res[i]* right_product
        right_product = right_product * nums[i]
    return res
nums = [1,2,3,4]
print(multiply(nums))
