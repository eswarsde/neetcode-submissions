class Solution:
    def decodeString(self, s: str) -> str:
        # Stacks to remember the outer context while we process inner brackets
        previous_text_stack: list[str] = []
        multiplier_stack: list[int] = []
        
        # Variables to track the state of the current bracket level
        current_text = ""
        current_multiplier = 0
        
        for char in s:
            if char.isdigit():
                # Shift the current number left by a base of 10 to handle multi-digit numbers
                current_multiplier = (current_multiplier * 10) + int(char)
                
            elif char.isalpha():
                # Standard letter: add it to the current block of text
                current_text += char
                
            elif char == '[':
                # Entering a nested block: save the outer context to the stacks
                previous_text_stack.append(current_text)
                multiplier_stack.append(current_multiplier)
                
                # Reset the current state to process the new inner block
                current_text = ""
                current_multiplier = 0
                
            elif char == ']':
                # Exiting a nested block: retrieve the outer context
                previous_text = previous_text_stack.pop()
                multiplier = multiplier_stack.pop()
                
                # Multiply the inner text and attach it to the outer text context
                current_text = previous_text + (current_text * multiplier)
                
        return current_text

        #Example: "3[a2[c]]"