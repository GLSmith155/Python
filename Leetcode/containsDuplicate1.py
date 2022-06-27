https://leetcode.com/problems/contains-duplicate/submissions/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        # For each value in num, assign it to x, and if already in dict, return True, else add to dict.
        for x in nums:
            key = x
            if key in dict:
                return True
            else:
                dict[key] = key
        return False
