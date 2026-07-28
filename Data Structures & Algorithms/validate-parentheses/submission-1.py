class Solution:
    def isValid(self, s: str) -> bool:

        
        # Input: s = "([{}])"

        # open bracket - we push it to the stack 
        # close bracket - we check ithe top of the stack to see if it matches ( we need a lookup dict of close to open )
        # if stack is empty , return true
        
        # Edge cases
        # input is odd length 
        
        paranthesis_string_len = len(s)
        if paranthesis_string_len % 2 == 1: # % 2 will return reminder, so for odd length, it returns 1
            return False
        close_to_open_bracket_lookup = {
            "]": "[",
            ")": "(",
            "}": "{",
        }
        stack = []

        for bracket in s:
            if bracket in close_to_open_bracket_lookup: # close bracket
                if stack and stack[-1] == close_to_open_bracket_lookup[bracket]:
                    stack.pop()
                else: # there should have been a open bracket in the stack, since there isn't
                    return False
            else: # open bracket
                stack.append(bracket)

        if stack:
            return False
        return True
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       














       
       
       
  
       
        #close_to_open_map = { ")" : "(", "]" : "[", "}" : "{" }
        # stack = []

        # for char in s:
        #     if char in close_to_open_map:
        #         if stack and stack[-1] == close_to_open_map[char]:
        #             stack.pop()
        #         else:
        #             return False
        #     else:
        #         stack.append(char)        
        
        # if stack:
        #     return False
        # else:
        #     return True