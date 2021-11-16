# How Many Numbers Are Smaller Than the Current Number?
# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
# That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

# Return the answer in an array.


# If we sort this list, and know the length of this list, then we can easily tell
# how many numbers are lower than the one we are currently looking at.
# However, the output will no longer be in the order we need, therefore we will create a dictionary
# called smaller_count.
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Bottlenecked by sort. Sorts upperbounded at O(n log n))
        sorted_nums = sorted(nums, reverse = True)
        smaller_count = {}       
        
        for i in range(len(sorted_nums)-1):
            curr_num = sorted_nums[i]
            next_num = sorted_nums[i+1]
        # I will need to create a dictionary to put the order back to 
        # where the proper output should be.
            if next_num < curr_num:
                remaining_values = len(sorted_nums)-(i+1)
                smaller_count[curr_num] = remaining_values
            
        smaller_count[sorted_nums[-1]] = 0
        
        output = []
        for num in nums:
            output.append(smaller_count[num])
            
        return output


# Below is another solution that works with inefficient time complexity.


# Complexity of N^2. Very inefficient.
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Creates empty array 'output' to keep track of output.
        output = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if j != i and nums[j] < nums[i]:
                    count += 1
            output.append(count)
        return output
