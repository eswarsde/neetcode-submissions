class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return "" 
        if len(strs) == 1:
            return strs[0]
        
        # Idea 1
         # sort by length. 
         # take the smallest and generate prefixes of all length possible
         # starting from biggest substrings, keep going and see if it is present in all the other strings

        strs = sorted(strs)
        shortest = strs[0]

        for prefix_length in range(len(shortest), 0, -1):
            prefix = shortest[:prefix_length]

            found_in_all = True

            for word in strs[1:]:
                if not word.startswith(prefix):
                    found_in_all = False
                    break

            if found_in_all:
                return prefix
       
        return ""


        

        # first_string = strs[0]

        # for i in range(len(first_string)):
        #     current_char = first_string[i]
        #     for word in strs:
        #         # len(word) <= i -> this word is too short to have a character at position i
        #         # this word does have a character at position i, but it's the wrong one. It disagrees with the reference string. The prefix cannot grow. Stop
        #         if len(word) <= i or word[i] != current_char:
        #             return first_string[:i] 
        # return first_string





        #####################
        #  The Horizontal Scanning 
        # take first word, check full match on second, start trimming down from right until it exists in all words 
        #  O(N×L) -> N -> number of words and L is avg length of the strings