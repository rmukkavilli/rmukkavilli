def top_k(nums, k):
    k_val= {}

    for n in nums:
        k_val[n]=k_val.get(n, 0)+1
    sorted_dict = (sorted(k_val.items(),key=lambda x:x[1], reverse=True))
    
    values_list = []
    for x in sorted_dict[:k]:
        values_list.append(x[0])
    return values_list

nums = [1,1,1,2,2,3]
k = 2
print(top_k(nums,k))