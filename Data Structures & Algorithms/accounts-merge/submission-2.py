from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        # Step 1: Build adjacency list

        adjacency_list = defaultdict(list) # Stores emails connected to this email.
        email_to_name = {} # email_to_name[email]


        for account in accounts:
            name = account[0]
            first_email = account[1]

            # Ensure an account with only one email still appears in the graph
            adjacency_list[first_email]

            email_to_name[first_email] = name

            for email in account[2:]:
                email_to_name[email] = name

                # Undirected connection
                adjacency_list[first_email].append(email)
                adjacency_list[email].append(first_email)

        # Step 2: Traversal state
        visited = set()
        merged_accounts = []


        
        # Step 3: Collect one connected component
        def dfs(email, merged_emails):
            if email in visited:
                return

            visited.add(email)
            merged_emails.append(email)

            for neighbor in adjacency_list[email]:
                dfs(neighbor, merged_emails)
        

        for email in adjacency_list:
            if email not in visited:
                merged_emails = []
                dfs(email, merged_emails)

                merged_emails.sort()
                name = email_to_name[email]
                merged_account = [name] + merged_emails
                merged_accounts.append(merged_account)

        
        return merged_accounts



    #         To analyze the complexity, let's break down the operations. Let $N$ be the number of accounts and $K$ be the maximum number of emails in an account.

    # ### Time Complexity: $O(N \cdot K \cdot \log(N \cdot K))$

    # 1.  **Building the Graph:** We iterate through every email in every account once. Since there are $N$ accounts and up to $K$ emails per account, this takes **$O(N \cdot K)$**.
    # 2.  **DFS Traversal:** Each email is a node, and each account creates edges between emails. In the worst case, every email is visited once and every edge is traversed once. Total nodes/edges are proportional to $N \cdot K$, so this is **$O(N \cdot K)$**.
    # 3.  **Sorting:** This is the bottleneck. After merging, we sort the emails for each unique person. In the worst case (one person owns all emails), we sort $N \cdot K$ emails, which takes **$O(N \cdot K \cdot \log(N \cdot K))$**.

    # ### Space Complexity: $O(N \cdot K)$

    # 1.  **Adjacency List:** We store every email as a key, and for each account, we store edges. The number of entries is proportional to the total number of emails across all accounts: **$O(N \cdot K)$**.
    # 2.  **Mapping and Visited Set:** `emailToAcc` (or `email_to_name` in the DFS version) and the `visited` set both store at most every unique email, which is **$O(N \cdot K)$**.
    # 3.  **Recursion Stack (for DFS):** In the worst case of a skewed graph (one long chain of emails), the stack depth could reach **$O(N \cdot K)$**.

    # ### Summary Table

    # | Operation | Complexity |
    # | :--- | :--- |
    # | **Total Time** | $O(N \cdot K \cdot \log(N \cdot K))$ |
    # | **Total Space** | $O(N \cdot K)$ |

    # **Note on Union Find:**
    # If you use the **Union-Find** approach (provided in the reference solution), the complexity remains effectively the same because the sorting step still dominates the $O(N \cdot K \cdot \alpha(N))$ time required for Union-Find operations.