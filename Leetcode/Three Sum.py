# Three Sum solution with a time complexity of O(n^2) and space complexity O(|ans|)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) < 3:
            return []

        ans = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    ans.append((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    while nums[r] == nums[r + 1] and l < r:
                        r -= 1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1
        return ans




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
        
