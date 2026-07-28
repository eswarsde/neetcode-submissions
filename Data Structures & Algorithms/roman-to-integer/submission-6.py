class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_to_val = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,           
        }

        # Roman numerals are usually written largest to smallest from left to right

        result = 0
        for i in range(len(s)):
            if i + 1 < len(s) and symbol_to_val[s[i]] < symbol_to_val[s[i+1]]:
                result-=symbol_to_val[s[i]] 
            else:
                result+=symbol_to_val[s[i]]
        return result

# Time: O(n)
# Space: O(1)