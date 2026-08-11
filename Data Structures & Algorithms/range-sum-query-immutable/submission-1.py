class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sum = [0]* (len(nums)+1)
        for idx, num in enumerate(nums):
            self.prefix_sum[idx + 1] = self.prefix_sum[idx] + num
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]
        

# Space complexity: O(n)
# time complexity: O(n) for pre-compute and O(1) for ramge sum 

# Your NumArray object will be instantiated and called as such:
# if __name__ == "__main__":
#     obj = NumArray([1,2,3,4,3,1,2,9, 10, 12])
#     param_1 = obj.sumRange(1, 3)