from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key idea is all anagram words have same frequenecy count of chars
        # so create a 26 array signatire for each word as add it as key in dictory 
        # when we process the next workd, just see if it matches the key, add the value in as list
        

        ans = {}

        for word in strs:
             # 1. Create the fingerprint (count array)
            count = [0]*26

            for char in word:
                count[ord(char) - ord("a")] +=1

            key = tuple(count)
            if key not in ans:
                ans[key] = []

            ans[key].append(word)
        return list(ans.values())

            






        