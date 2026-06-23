def move_zeros(list):
    left = 0
    for right in range(len(list)):
        if list[right] !=0:
            list[left], list[right] = list[right], list[left]
            left +=1
    return list

print(move_zeros([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]
print(move_zeros([1, 2]))  # Output: [1, 2]
print(move_zeros([0, 0, 1]))  # Output: [1, 0, 0]



 # left = 0
    # right = 0
    # while left < len(list) and right < len(list):
    #     if list[left] == 0 and list[right] != 0:
    #         temp = list[left]
    #         list[left] = list[right]
    #         list[right] = temp
    #         left +=1
    #     right +=1
    #     print(right)
    # return list