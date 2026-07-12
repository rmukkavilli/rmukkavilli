# Time Complexity : O(N)
# Space Complexity : O(1)
#1. Best Time to Buy and Sell Stock (LeetCode 121)
def best_time_to_buy_sell(nums) -> int:
    min_price = float("inf")
    max_profit = 0
    for num in nums:
        min_price = min(num, min_price)
        profit = num - min_price
        max_profit = max(profit, max_profit)
    return max_profit



#Input:  
nums = [7, 1, 5, 3, 6, 4]
print(best_time_to_buy_sell(nums))
# Output: 5
#Input: 
nums1 =  [7, 6, 4, 3, 1]
print(best_time_to_buy_sell(nums1))
# Output: 0
