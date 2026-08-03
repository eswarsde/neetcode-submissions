class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # combinations - order doesn't matter - [2, 3, 4] and [4, 3, 2] are the same

        # 1. Avoiding Duplicate Combinations (The start_index)
            # In permutations, [2, 3] and [3, 2] are different. In combinations, they are the same! To prevent your code from generating both, we have to enforce an order. We do this by passing a start_index to our DFS function. When we loop through choices, we only look at the current index and anything to the right of it.
        
        # 2. Unlimited Reuse of Elements
         # The problem states you can use the same number an unlimited number of times. This means when we make a choice and recurse down the tree, we pass down our current index i, not i + 1

        path = []
        result = []
        def dfs_backtracking(remaining, start_index):
            # base case 
            if remaining == 0:
                result.append(path[:])
                return
            # overshoot
            if remaining < 0:
                return

            # choices => choose => explore => un-choose
            # Start loop at 'start_index' to prevent backwards lookup (which creates duplicates)
            for i in range(start_index, len(nums)):
                choice = nums[i]
                path.append(choice)
                # problem states you can use the same number an unlimited number of times. This means when we make a choice and recurse down the tree, we pass down our current index i, not i + 1
                dfs_backtracking(remaining - choice, i)
                path.pop()




        dfs_backtracking(target, 0)
        return result