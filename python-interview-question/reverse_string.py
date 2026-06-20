s= "verily"
test = list(s)
print(s[::-1])
index =0
right = len(test) -1
while index <= right:
    print(index, "", right)
    temp = test[index]
    test[index] = test[right]
    test[right] = temp
    index +=1
    right -=1
print("".join(test))