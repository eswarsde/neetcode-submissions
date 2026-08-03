class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # how to model this problem 
        # I think we can model this as backtracking problem, because at each point we have some choices to choose from -> explore -> unchoose
        # and we want to retrun all paths we take

        if not digits:
            return []
        num_string_map ={
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"            
        }
        digits_len = len(digits)
        path = []
        result = []

        def dfs_backtrack(index):
            # base case
            if len(path) == len(digits):
                result.append("".join(path))
                return

           # choices => choose => explore => un-choose
            curr_digit = digits[index]
            # corresponding letters -> choices
            letter_choices = num_string_map[curr_digit]

            for choice in letter_choices:
                path.append(choice) # choose
                dfs_backtrack(index+1) # explore
                path.pop() # unchoose

        # call for each digit ?
        dfs_backtrack(0) 
        return result