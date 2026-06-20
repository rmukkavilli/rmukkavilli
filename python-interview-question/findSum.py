def matchSum(list, target):
    left=0
    right=len(list) -1
    while left < right:
        print("left", left, "right", right)
        sum = list[left] + list[right]
        if sum == target:
            return [left, right]
        if sum < target:
            left +=1
        else:
            right -=1


nums = [8,8,-8,0,9,9]
target = 0
print(matchSum(nums, target))