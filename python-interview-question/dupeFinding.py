nums = [1,2,3,4]
seen= set()
for num in nums:
    if num in seen:
        return 'True'
    else:
        seen.add(num)
return False