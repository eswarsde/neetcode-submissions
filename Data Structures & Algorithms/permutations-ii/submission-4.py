class Solution:
    # https://neetcode.io/problems/permutations/question?list=allNC
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Sort the array first so duplicates are adjacent to each other
        nums.sort()
        
        num_len = len(nums)
        visited = [False] * num_len

        path = []
        result = []

        def dfs_backtacking():
            # Base case: if the path length equals the input length, we found a permutation
            if len(path) == num_len:
                result.append(path[:])
                return

            # choices -> choose -> explore -> unchoose
            for idx, choice in enumerate(nums):
                # If the number is already used in the current permutation, skip it
                if visited[idx] == True:
                    continue

                # Duplicate skipping logic:
                # If the current number is the same as the previous one AND 
                # the previous one is NOT visited, it means we are about to create 
                # a duplicate permutation at this depth level, so we skip.


                # **The Core Rule:** This logic forces identical numbers to be used in a strict left-to-right order. It prevents your code from generating the exact same recursive branches multiple times.

                # Here is the direct breakdown of how that specific line works:

                # ### The Code Breakdown

                # * **`i > 0`**: Ensures we don't check out of bounds on the first element.
                # * **`nums[i] == nums[i - 1]`**: Detects that the current number is a duplicate of the one right before it (this only works because we used `nums.sort()` earlier to group duplicates together).
                # * **`not visited[i - 1]`**: This is the anchor. It means the previous identical number was just placed in this exact position, its entire permutation tree was fully explored, and it was subsequently *un-chosen* (backtracked) so its `visited` state was reset to `False`.

                # ### The Visual Example

                # Imagine your sorted input is `[1A, 1B, 2]`.

                # You want to generate `[1A, 1B, 2]`. You **do not** want to generate `[1B, 1A, 2]` because, in the final output, they both just look like `[1, 1, 2]`.

                # 1. **The `1A` Branch:** Your loop puts `1A` in the very first slot. It explores all possibilities `[1A, 1B, 2]` and `[1A, 2, 1B]`. Once done, it backtracks, removes `1A` from the first slot, and sets `visited[0] = False`.
                # 2. **The `1B` Branch:** The loop moves to index 1 (which is `1B`). It wants to put `1B` into that very first slot.

                # If the code allows `1B` to go into that first slot, it will just generate `[1B, 1A, 2]` and `[1B, 2, 1A]`—the exact same permutations you just finished building.

                # Because `nums[i] == nums[i-1]` (both are `1`) AND `visited[i-1]` is `False` (meaning `1A` is sitting unused, having just vacated this exact level of the tree), the `continue` statement triggers. It skips `1B`, entirely pruning that duplicate branch.
                if idx > 0 and nums[idx] == nums[idx - 1] and not visited[idx - 1]:
                    continue

                visited[idx] = True
                path.append(choice)
                dfs_backtacking()
                path.pop()
                visited[idx] = False


        dfs_backtacking()
        return result