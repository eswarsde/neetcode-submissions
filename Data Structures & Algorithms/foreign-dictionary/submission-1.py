class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # We can model this question as a DAG graph
        # characters in this alien language is ordreed 
        # each given character may have a previous character and next character 
        # adjacency list is one way to represent that 
        

        # A string/word a is lexicographically smaller than a string b if either of the following is true:
          # Condition 1: The first letter where these worrds differ is smaller in a than in b.
          # Conidtion 2: a is a prefix of b and a.length < b.length => (ape < apes)
          # apple, ape => these words first differ at "p" and "e"

          # Input is lexicographically sorted

          # Step 1: convert the given input format into adjacency list
          # before that we need to all unique chars in the word list 

          adj_list = {char: set() for word in words for char in word}

          # Track prerequisites (incoming edges) for each character
          indegree = {c: 0 for c in adj_list}

          # take 2 words at a time and compare and find the first differing character 
          for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            # If w1 is longer than w2 and w2 is a prefix of w1, it's invalid
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            # Find the first differing character and create an edge
            for j in range(min_len):
                if w1[j] != w2[j]:
                    # Prevent duplicate edges from artificially inflating the indegree
                    if w2[j] not in adj_list[w1[j]]: 
                        adj_list[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break

          queue = deque([c for c in indegree if indegree[c] == 0])
          res = []

          while queue:
            curr_char = queue.popleft()
            res.append(curr_char)

            # Because this character is now placed, its neighbors have one less prerequisite
            for neighbor in adj_list[curr_char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)


          # Cycle detection: If we didn't process every character, there was a circular dependency
          if len(res) != len(indegree):
            return ""
        
          return "".join(res)




# V is the number of unique characters, 
# E is the number of edges and 
# N is the sum of lengths of all the strings.

