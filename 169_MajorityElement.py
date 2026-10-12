# TC - O(n)
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate, votes = nums[0], 1
        for i in range(1, len(nums)):
            if votes == 0:
                candidate = nums[i]
                votes = 1
                continue
            
            if candidate == nums[i]:
                votes += 1
            else:
                votes -= 1
        
        return candidate