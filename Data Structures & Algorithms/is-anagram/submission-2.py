class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
    
        s_char_counter = defaultdict(int)
        t_char_counter = defaultdict(int)

        for i in range(len(s)):
            s_char_counter[s[i]] +=1 
            t_char_counter[t[i]] +=1


        return s_char_counter == t_char_counter
     

# Time complexity: O(n + m) 

# Space Complexity: O(k), k is the number of distinct characters. O(1) since we have at most 26 different characters.

# Where k is the number of distinct characters stored in the map.
# With lowercase English letters, k <= 26, so this is effectively O(1) extra space.

        