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