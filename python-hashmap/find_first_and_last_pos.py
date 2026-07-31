# time is O(log n) and space is O(1).
def search_range(nums: list[int], target: int) -> list[int]:

    def find_first() -> int:
        left, right = 0, len(nums) -1
        
        ans = -1
        while left <= right :
            mid = left + (right -left) // 2
        
            if target == nums[mid]:
                ans = mid
                right = mid -1
            elif nums[mid] < target:
                left = mid +1
            else:
                right = mid - 1
        return ans

    def find_last() -> int:
        left, right = 0, len(nums) -1
    
        ans = -1
        while left <= right :
            mid = left + (right -left) // 2
        
            if target == nums[mid]:
                ans = mid
                # search in right hand side
                left = mid +1
            elif nums[mid] < target:
                left = mid +1
            else:
                right  = mid - 1
        return ans

    return[find_first(), find_last()]
    


nums = [5, 7, 7, 8, 8, 10]

print(search_range(nums, 7))
# [1, 2]

print(search_range(nums, 8))
# [3, 4]

print(search_range(nums, 6))
# [-1, -1]

# Output:
# [-1,-1]