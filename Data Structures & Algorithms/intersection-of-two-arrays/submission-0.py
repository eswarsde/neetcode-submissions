class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # If either array is empty, there cannot be any common values.
        if len(nums1) == 0 or len(nums2) == 0:
            # Return early for this edge case.
            return []

        # Store all unique values from nums1.
        # This turns repeated membership checks into O(1) average time.
        seen1 = set(nums1)

        # Store the intersection here as a set so duplicates are removed automatically.
        ans = set()

        # Scan the second array and keep values that also appear in nums1.
        for value in nums2:
            # If value is present in nums1, it belongs in the intersection.
            if value in seen1:
                # Add it to the answer set; duplicates do nothing.
                ans.add(value)

        # Convert the set result to a list because the function expects a list[int].
        return list(ans)
        