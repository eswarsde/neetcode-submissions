class Solution:
    def climbStairs(self, n: int) -> int:

        # permutation - order matters
        # combination -> order doesn't matters
        # in this the order matters, first we can take 2 steps and then 1 steps
        # we need to find number of unique ways

        # approach 2 => DFS -> at each junction we have 2 choices to make 
           # count when we reach n(top of the staris)
           # prune if we overshoot the top of the stairs
        # https://docs.google.com/document/d/1B7atdVTcNhbl2O7Naio7nLGzH4dk3m9I86ltvIneHr0/edit?tab=t.0



        # 0️⃣ WHAT IS THE QUESTION AT MY(Node) LEVEL?
        #    Question: "How many total distinct ways can I reach the top of the stairs 
        #    from my current position?"

        # 1️⃣ TOP-DOWN: Do I need info from ancestors?
        #    Yes. I need to know where I currently am on the staircase. 
        #    → PARAMETER: `reamaining_steps` (or current step `i`).

        # 2️⃣ BOTTOM-UP: What must dfs(child) return so that I can answer MY question?
        #    One value. Each child must return an integer representing the 
        #    number of valid ways to reach the top from their position.
        #    → RETURN TYPE: `int`

        # 3️⃣ THE SPLIT CHECK: Is "what I return to my parent" == "the final answer"?
        #    Same! The total ways from step 0 is exactly what `dfs` returns. 
        #    → No global tracker (`self.ans`) is needed. We just return the result upward.

        # 4️⃣ COMBINE: At my node, using (params + child returns):
        #    - What value do I return upward? 
        #      `take_one = dfs(reamaining_steps - 1)`
        #      `take_two = dfs(reamaining_steps - 2)`
        #      `return take_one + take_two`
        #    - Do I return BEFORE or AFTER visiting children? 
        #      AFTER. This is Pure Postorder Aggregation. You must wait for the children 
        #      to give you their answers before you can sum them up and return your own.
        #      *(Note: This is also where you check/update your Memoization cache!)*

        # 5️⃣ BASE CASE: What does a leaf return so the combine step works?
        #    - Perfect landing (Target Reached): If `reamaining_steps == 0`, return `1` 
        #      (this counts as 1 valid path).
        #    - Overshoot (Pruning): If `reamaining_steps < 0`, return `0` 
        #      (this is a dead end, adding 0 won't affect the parent's sum).

        # 6️⃣ INITIAL CALL: What state does root receive?
        #    `dfs(n)` (passing in the total number of stairs as our starting `reamaining_steps`).
        #    We just directly `return dfs(n)` as our final answer.

        # momoize using 2 ways
        # 
        # from functools import cache
        # @cache

        # option 2: use memo
        memo = {}
        def dfs(reamaining_steps):

            if reamaining_steps == 0:
                return 1

            if reamaining_steps < 0:
                return 0

            if reamaining_steps in memo:
                return memo[reamaining_steps]
            
            one_step_num_ways_to_reach_top = dfs(reamaining_steps -1) 
            two_step_num_ways_to_reach_top = dfs(reamaining_steps - 2)
            memo[reamaining_steps] = one_step_num_ways_to_reach_top + two_step_num_ways_to_reach_top

            return one_step_num_ways_to_reach_top + two_step_num_ways_to_reach_top

        
        return dfs(n)













        