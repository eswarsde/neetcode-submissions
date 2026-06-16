class Solution:

    def encode(self, strs: List[str]) -> str:
        # length based encoding
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded 


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            word_len = ""
            while s[i] != "#":
                word_len += s[i]
                i+=1
                
            word_len_num = int(word_len)
            # Skip the '#'
            start_index = i+1
            end_index = start_index + word_len_num
            result.append(s[i+1: end_index])  
            i = end_index     

        return result




