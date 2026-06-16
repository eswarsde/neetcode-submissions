class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char_counter = {}
        t_char_counter = {}

        def charcounter(s, counter):
            for c in s:
                if c in counter:
                    counter[c] +=1
                else:
                    counter[c] = 1
        
        charcounter(s, s_char_counter)
        charcounter(t, t_char_counter)

        return s_char_counter == t_char_counter
     

        

        