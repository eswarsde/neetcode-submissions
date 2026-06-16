class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Store the index corresponding to the value in the second list.
        valueToPos = {}
        for i in range(len(nums2)):
            valueToPos[nums2[i]] = i

        # List to store the anagram mappings.
        mappings = [0] * len(nums1)
        for i in range(len(nums1)):
            mappings[i] = valueToPos[nums1[i]]

        return mappings