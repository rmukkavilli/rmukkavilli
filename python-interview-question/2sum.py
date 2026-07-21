nums = [1,3,4,5,6,7,10,25,356]
target = 8
seen = {}
index=0
for n in nums:
    needed = target-n
    if needed in seen:
      print(seen[needed], index)
    else:
        seen[n] = index
    index +=1
