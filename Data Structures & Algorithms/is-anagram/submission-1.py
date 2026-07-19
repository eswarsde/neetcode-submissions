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
     

        

        