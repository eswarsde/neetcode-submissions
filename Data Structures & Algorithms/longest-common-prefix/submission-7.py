from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # # Idea 1: Horizontal scanning

        # # Start by assuming the entire first word is the common prefix.
        prefix = strs[0]

        #  # Compare the prefix against every remaining word.
        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[0:len(prefix) - 1] # remove 1 character at a time until 

                if prefix == "":
                    return ""
        return prefix

        # Time complexity: O(n × m) - There are up to n words. For each word, startswith(prefix) may compare up to m characters
        # Space complexity: O(m)
#===================================================================================================
        # Idea 1: Vertical scanning
        # Use the first word as the reference.
        # Check its characters one position at a time.
        # For each character position:
        #   Compare that character with the character at the same position
        #   in every other word.
        # If a word is too short or the characters do not match,
        #   return everything before that position.
        # If every position matches, return the entire first word.

        prefix = strs[0]
        for character_index in range(len(prefix)):
            # Start by assuming the entire first word is the common prefix.
            prefix = strs[0]

             # Check each character position in the possible prefix.
            current_char = prefix[character_index]

            for word in strs[1:]: # start from word 2

                # The word is too short to contain this character,
                # or its character does not match the first word.
                if (character_index >= len(word) or word[character_index] != current_char):
                    return prefix[:character_index]

        # Every character in the first word matched.
        return prefix

        # Time complexity: O(n × m) # The outer loop checks each character position, The inner loop checks that position in every word (m character positions × n words)
        # Space complexity: O(1)
#===================================================================================================
        # Let:
        # n = number of strings
        # m = length of the first word
        #
        # Worst-case time: O(n * m)
        #
        # We may examine m character positions.
        # At each position, we may check all n strings.
        #
        #     m positions × n strings = O(n * m)
        #
        # Worst-case auxiliary space: O(1)
        #
        # first_word, word, current_char, and prefix_length use
        # only constant extra space.
        #
        # The returned slice first_word[:prefix_length] uses O(m)
        # space for the output string, but output space is normally
        # not counted as auxiliary space.

 #============================================================= 
         # Idea 2:
         # # Sort the strings alphabetically/lexicographically

        # After sorting, the first and last strings are the most different
        # strings in alphabetical order.

        #
        # Therefore, the common prefix shared by the first and last strings
        # must also be shared by every string between them.
        #
        # Compare the first and last strings character by character.
        # Return everything before the first mismatch.

        # strs.sort()

        # first_word = strs[0]
        # last_word = strs[-1]

        # # We can compare only while the index exists in both strings.
        # max_prefix_length = min(len(first_word), len(last_word))


        # for index in range(max_prefix_length):
        #     if first_word[index] != last_word[index]:
        #         return first_word[:index]

        # # No mismatch was found.
        # # Therefore, the entire shorter word is the common prefix.
        # return first_word[:max_prefix_length]

                # Let:
        # n = number of strings
        # m = maximum string length
        #
        # Worst-case time: O(n log n * m)
        #
        # Sorting performs O(n log n) string comparisons.
        # In the worst case, comparing two strings may inspect up to m characters.
        #
        # Therefore, sorting takes:
        #
        #     O(n log n * m)

        # Worst-case auxiliary space: O(n)
        #
        # Python's sorting algorithm may use up to O(n) temporary space.
        # first_word and last_word only reference existing strings.
        # The returned slice may use up to O(m) space.
        #
        # Including the returned string:
        #
        #     O(n + m)

        #=============================================================
       
       
        # Idea 1:
        # Find the shortest string the entire list.
        #
        # The longest common prefix cannot be longer than the shortest string,
        # so use the shortest string to generate possible prefixes.
        #
        # Try its prefixes from longest to shortest.
        # Return the first prefix that every string starts with.

        # shortest = min(strs, key=len)

        # # Try prefix lengths:
        # # len(shortest), len(shortest) - 1, ..., 1
        # for prefix_length in range(len(shortest), 0, -1):
        #     prefix = shortest[:prefix_length]

        #     found_in_all = True

        #     for word in strs:
        #         if not word.startswith(prefix):
        #             found_in_all = False
        #             break

        #     if found_in_all:
        #         return prefix

        # # No non-empty common prefix exists.
        # return ""

        # Let:
        # n = number of strings
        # m = length of the shortest string
        #
        # Worst-case time: O(n + n * m²)
        #
        # 1. Finding the shortest string:
        #
        #    min(strs, key=len) examines all n strings.
        #
        #    Time: O(n)
        #
        # 2. Generating and checking prefixes:
        #
        #    The shortest string has length m, so we may try m prefixes:
        #
        #        length m
        #        length m - 1
        #        length m - 2
        #        ...
        #        length 1
        #
        #    For every prefix:
        #
        #    - Creating shortest[:prefix_length] can take up to O(m).
        #    - We may check all n strings.
        #    - word.startswith(prefix) may compare up to O(m) characters.
        #
        #    Simple worst-case calculation:
        #
        #        m prefixes
        #        × n strings checked per prefix
        #        × up to m character comparisons
        #        = O(n * m²)
        #
        #    More precisely, the prefix lengths are:
        #
        #        m + (m - 1) + ... + 1
        #
        #    This sum is O(m²), so checking all n strings gives:
        #
        #        O(n * m²)
        #
        # 3. Total time:
        #
        #        O(n) + O(n * m²)
        #        = O(n + n * m²)
        #
        #    Usually simplified to:
        #
        #        O(n * m²)
        #
        #
        # Worst-case auxiliary space: O(m)
        #
        # shortest only references an existing string, so it does not create
        # a copy of that string.
        #
        # However, shortest[:prefix_length] creates a new prefix string.
        # The largest prefix can contain m characters, so it uses O(m) space.
        #
        # Only one prefix exists at a time, so the auxiliary space is O(m),
        # not O(m²).