# TC - O(n)
# SC - O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_mapper = [0]*26
        for chars, chart in zip(s, t):
            char_mapper[ord(chars) - ord('a')] += 1
            char_mapper[ord(chart) - ord('a')] -= 1
        
        return False if any(char_mapper) != 0 else True