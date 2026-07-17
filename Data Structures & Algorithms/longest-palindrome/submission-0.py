from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int: 



        # odd plaidrom - aba -> has one odd times char and reset of them event times count
        # even palindrom -> abba -> both characters appear even number of time 
        # for this question, they are asking given a string of characters what is the longest palindrome u can produce
          # this means u can also skip some characters
          # the idea bceomes 
          # for any char that is appearing event number of times (2,4,6) => keep add 2 as that is how much the characters contribute to length of output palidronme
          # for any char that is odd -> techincally in a odd length palindrome, there can only be  char that is can be add. which is why we have a break;
        counter = defaultdict(int)
        result = 0

        for char in s:
            counter[char] +=1
            if counter[char] % 2 == 0:
                result +=2

        
        for count in counter.values():
            if count % 2 == 1:
                result +=1
                break

        return result

    # def longestPalindrome(self, s: str) -> int:
    #     seen = set()
    #     result = 0

    #     for char in s:
    #         if char in seen:
    #             seen.remove(char)
    #             result +=2
    #         else:
    #             seen.add(char)

    #     if seen:
    #         result+=1

    #     return result
        