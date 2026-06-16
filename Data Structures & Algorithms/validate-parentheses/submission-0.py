class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open_map = { ")" : "(", "]" : "[", "}" : "{" }
        stack = []

        for char in s:
            if char in close_to_open_map:
                if stack and stack[-1] == close_to_open_map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)        
        
        if stack:
            return False
        else:
            return True