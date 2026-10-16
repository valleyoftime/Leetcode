class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        start = 0
        longest = 0
        for idx, char in enumerate(s):
            while char in seen:
                seen.remove(s[start])
                start += 1
            seen.add(char)
            longest = max(longest, idx-start+1)
        return longest
