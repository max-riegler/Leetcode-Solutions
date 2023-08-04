class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        
        res = 0
        
        for n in range(len(s)):
            if n + 1 < len(s) and roman[s[n]] < roman[s[n+1]]:
                res -= roman[s[n]]
            else:    
                res += roman[s[n]]
        
        return res

sol = Solution()

print(sol.romanToInt("MM"))