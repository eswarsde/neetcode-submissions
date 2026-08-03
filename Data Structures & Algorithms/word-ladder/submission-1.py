class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # minimum number of words within the transformation sequence needed to obtain the endWord, or 0 if no such sequence exists.
        # minimum - BFS ?? -> yes

        # how do i model this problem as a graph problem ?
        # I guess I can look at the output and see "cat" -> "bat" -> "bag" -> "sag" and see it's a graph
        # also there can be more than one word in the wordList that differs by one character -> which means there are more than one choice at that node.
        # also these graphs are bidrectional/undirected -> if we create a adj_list, it has to be bidrectional
        # a given beginWord can transformation into any of those listed of words as long as it satisifies the exactly one poistion change.. 
         

        # The Graph Mental Model
        #     The easiest way to visualize this problem is as an undirected graph:

        #     Nodes: Every valid word is a node in the graph.

        #     Edges: An edge connects two nodes if they differ by exactly one letter.


        # Step 1:
         # naive: compare every single word to every other word to find neighbors, the time complexity would be O(N^2 * M) (where N is the number of words and M is the word length)
         # better idea: To optimize this to O(N . M^2), we can use a wildcard pattern matching strategy. For every word, we replace each character with a wildcard (like *) to generate its intermediate states. For example, the word "cat" generates "*at", "c*t", and "ca*". We use these patterns as keys in a hash map, and the values are lists of all words that match that pattern.

         if endWord not in wordList:
            return 0

         wordList.append(beginWord)

         # adj maps a pattern to a list of actual words
         # # e.g., "*at" -> ["cat", "bat", "sat"]
         adj_list = collections.defaultdict(list)

         for word in wordList:
            for wild_card_index in range(len(word)):
                pattern = word[:wild_card_index] + "*" + word[wild_card_index+1:]
                adj_list[pattern].append(word)

         visited = set([beginWord])
         queue = deque([beginWord])
         result_len = 1 # 1 for the beginWord
         
         while queue:
            # level by level processing
            level_size = len(queue)

            for _ in range(level_size):
                word = queue.popleft()

                # Do something with poped node
                if word == endWord:
                    return result_len

                # Enqueue neighbors

                for wild_card_index in range(len(word)):
                    pattern = word[:wild_card_index] + "*" + word[wild_card_index+1:]
                    for neighbor in adj_list[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
            
            result_len +=1 # for eached poped word

         return 0

# Time complexity: O(m^2∗n)
# Space complexity: O(m^2∗n)
# Where 
#     n is the number of words and 
#     m is the length of the word.
                




        
