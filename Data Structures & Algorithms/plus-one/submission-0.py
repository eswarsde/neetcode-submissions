class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
              # Walk from the last digit to the first because addition starts at the ones place.
        # range(start, stop, step): start at len(digits) - 1, stop before -1, move by -1.
        for i in range(len(digits) - 1, -1, -1):
            # If this digit is not 9, we can add 1 here and stop.
            # No further carry is needed, so we return immediately.
            if digits[i] < 9:
                digits[i] += 1
                return digits

            # If the digit is 9, adding 1 makes it 0 and carries to the left.
            digits[i] = 0

        # If we finished the loop, every digit was 9.
        # Example: [9, 9] -> [0, 0], but we still have one carry left,
        # so the correct result is a new leading 1 followed by all zeros.
        return [1] + digits
        