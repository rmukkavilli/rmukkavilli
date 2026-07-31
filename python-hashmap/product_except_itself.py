def product_except_self(nums: list[int]) -> list[int]:
    res = [1] * len(nums) 
    left_product = 1
    for n in range(len(nums)):
        res[n] = left_product
        left_product *= nums[n]
        print(left_product)
    print(res)

    right_product = 1
    for n in range(len(nums) -1, -1, -1):
        res[n] *=right_product
        right_product *=nums[n]
    print(res)


    

nums= [1,2,3,4]
print(product_except_self(nums))