class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        first_string = strs[0]

        for i in range(len(first_string)):
            current_char = first_string[i]
            for word in strs:
                # len(word) <= i -> this word is too short to have a character at position i
                # this word does have a character at position i, but it's the wrong one. It disagrees with the reference string. The prefix cannot grow. Stop
                if len(word) <= i or word[i] != current_char:
                    return first_string[:i] 
        return first_string

















































        #####################
        #  The Horizontal Scanning 
        # take first word, check full match on second, start trimming down from right until it exists in all words 
        #  O(N×L) -> N -> number of words and L is avg length of the strings