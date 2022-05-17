# Storing values in a dictionary allows us to go through the number array visiting each value only one time. 
# Space Complexity will be worse, however Time Complexity will be improved to O(n).
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        visited_nums = {}
        
        # enumerate provides both the index and the value.
        # i is the index, and the array value will be in the dictionary value slot.
        
        for i, value in enumerate(nums):
            if target - value in visited_nums:
                return([visited_nums[target - value], i])
            elif value not in visited_nums:
                visited_nums[value] = i

# ______________________________________________________________________________________________

# Naive Two Sum Solution with the time complexity O(n^2).
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)-1):
            for y in range(x+1, len(nums)):       
                if nums[x] + nums[y] == target:
                    return([x, y])
