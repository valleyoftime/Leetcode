# TC - O(n)
# SC - O(1)
class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        ans = mapping[s[-1]]
        length = len(s)
        for i in range(length - 2, -1, -1):
            if mapping[s[i]] >= mapping[s[i + 1]]:
                ans += mapping[s[i]]
            else:
                ans = abs(ans - mapping[s[i]])
        return ans
