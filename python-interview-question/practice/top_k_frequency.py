# Time Complextity : O(N log K)
# Space Complextity : O(N)
# with heap : O(N) and O(N)
#
import heapq
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    freq_dict = {}
    result = []
    heap = []
    for num in nums:
        freq_dict[num] = freq_dict.get(num,0) + 1
    print(freq_dict)
    for num, freq in freq_dict.items():
        print("num ", num)
        print("freq", freq)
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    # for freq, num in heap:
    #     result.append(num)
    # return result, instead of this code below code more of pythonic
    return [num for freq, num in heap]
    
    

    # sorted_freq = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    # for key, value in sorted_freq[:k]:
    #     result.append(key)
    # return result


#Input:
nums = [1,1,1,2,3,2]
k = 2
print(top_k_frequent(nums, k))

# Output:
# [1,2]