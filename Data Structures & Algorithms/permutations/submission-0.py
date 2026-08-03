class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        num_len = len(nums)

        path = []
        result = []
        def dfs_backtracking(index):
            # base case
            if len(path) == num_len:
                result.append(path[:]) #append carefully - Append a COPY of the current path
                return

            # choices -> choose -> explore -> unchoose

            for choice in nums:
                if choice in path:
                    continue
                path.append(choice)
                dfs_backtracking(index + 1)
                path.pop()
        dfs_backtracking(0)
        return result