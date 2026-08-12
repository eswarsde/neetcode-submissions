class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        vowels = set("aeiou")
        prefix_counts = [0] * (len(words) + 1)

        running_sum = 0

        for idx, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                running_sum += 1
            prefix_counts[idx + 1] = running_sum


        result = [0] * len(queries)
        for i, query in enumerate(queries):
            left, right = query

            result[i] = prefix_counts[right + 1] - prefix_counts[left]

        return result


