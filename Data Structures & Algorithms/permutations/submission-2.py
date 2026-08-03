class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        num_len = len(nums)

        path = []
        result = []
        def dfs_backtracking():
            # base case
            if len(path) == num_len:
                # append carefully - Append a COPY of the current path
                result.append(path[:])
                return
            # choices -> choose -> explore -> unchoose

            for choice in nums:
                # can't choose the same number again as per the problem 
                if choice in path:
                    continue
                path.append(choice)
                dfs_backtracking()
                path.pop()
        dfs_backtracking()
        return result


# Time complexity: O(n!∗n)
# Space complexity: O(n!∗n) for the output list.