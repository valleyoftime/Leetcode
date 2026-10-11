# TC - O(N)
# SC - O(N)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dictionary = {}
        for idx, num in enumerate(nums):
            target_el = target - num
            if target_el in dictionary:
                return [idx, dictionary[target_el]]
            dictionary[num] = idx
        return []
