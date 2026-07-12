# leet code :  Valid Mountain Array (LeetCode 941)
#Time: O(n)
# Space: O(1)
#
def valid_mountain_array(arr: list[int]) -> bool:
    i = 0
    end = len(arr)
    if end < 3 :
        return False
    while i < end-1 and arr[i] < arr[i+1]:
        i +=1
        peak = arr[i]
    if peak == arr[0] or peak == arr[end -1]:
        return False
    while i < end-1 and arr[i] > arr[i+1]:
        peak = arr[i]
        i+=1
      
    return i == end -1


print(valid_mountain_array([3]))          # False
print(valid_mountain_array([1, 2, 3]))    # False
print(valid_mountain_array([1, 2, 2, 1])) # False
print(valid_mountain_array([1, 3, 2, 4])) # False
print(valid_mountain_array([0, 3, 2, 1])) # True


# Method 
# while increasing order 
# check peaks are not both ends
# while decreasing order 
# when i == arr.length -1 
# return 