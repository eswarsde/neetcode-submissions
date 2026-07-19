class Solution:
    def firstUniqChar(self, s: str) -> int:

        seen = {}

        for char in s:
            seen[char]= seen.get(char, 0) + 1

        for idx, char in enumerate(s):
            if seen[char] == 1:
                return idx

        return -1

