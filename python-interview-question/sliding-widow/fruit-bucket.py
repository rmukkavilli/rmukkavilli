def fruit_bucket(fruits, k):
    window_len = 2
    max_window = {}
    max_window_len = 0
    left = 0
    for right in range(len(fruits)):
        max_window[fruits[right]] = max_window.get(fruits[right],0)+1

        while len(max_window) > k:
            max_window[fruits[left]] -=1
            if max_window[fruits[left]] == 0:
                del max_window[fruits[left]]
            left +=1
        max_window_len = max(max_window_len, right - left +1)
    print(max_window)
    return max_window_len 


fruits = [1, 2, 3,3,3,2,2]
k = 2
print(fruit_bucket(fruits, k))