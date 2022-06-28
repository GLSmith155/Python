# Naive Three Sum solution with a time complexity of O(n^3)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums_zero = []
        # x is range of nums except for last number
        for x in range(len(nums)-2):
            for y in range(x + 1, len(nums)):
                for z in range(x + 2, len(nums)):
                    if nums[x] + nums[y] + nums[z] == 0:
                    #    for d in range(1):
                    #        array
                        nums_zero = [nums[x],nums[y],nums[z]]
                       # nums_zero.extend(nums[x],nums[y],nums[z])
                        return([nums_zero])
                        print([nums_zero])
                        del nums_zero
                        print(nums[x],nums[y],nums[z])
        
