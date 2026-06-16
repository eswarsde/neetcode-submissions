class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Naive:

        AAABABB
        A
        AA
        AAA
        AAAB - A: 3 B:1, length = 4
        AAABA
        AAABABB
         
          - T: O(n^2) just for substring generation 
               for each subnstrng we also have o(n) => O(n^3)          
        """    
        """

        """ 
        left = 0
        longest = 0
        counter = {}
        max_count = 0
        

        for right in range(len(s)):
            ch = s[right]

            if ch not in counter:
                counter[ch]=0
            counter[ch] +=1 

            max_count = max(max_count, counter[ch])

            curr_window_len = right - left + 1

            while curr_window_len - max_count > k:
                left_char = s[left]

                counter[left_char] -=1
                left+=1
                curr_window_len = right - left + 1

            longest = max(longest, curr_window_len)

        return longest
        












