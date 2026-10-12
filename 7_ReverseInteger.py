class Solution:
    def reverse(self, x: int) -> int:
        MIN, MAX = -2**31, 2**31-1
        sign = 1
        if x < 0:
            sign = -1
            x = abs(x)
        
        rev = 0
        while x:
            rev = rev * 10 + x%10
            x //= 10

            if rev < MIN or rev > MAX:
                return 0
        
        return rev if sign == 1 else sign * rev