def move_zeros(list):
    left = 0
    right = 1
    while left < len(list) and right < len(list):
        if list[left] == 0 and list[right] != 0:
            temp = list[left]
            list[left] = list[right]
            list[right] = temp
            left +=1
        right +=1
        print(right)
    return list

l = [1,2,0,0]
print(move_zeros(l))
