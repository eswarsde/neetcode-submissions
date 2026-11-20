class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = [[] for i in range(len(nums) + 1)]
        cnt = {}
        for num in nums:
            cnt[num] = 1 + cnt.get(num, 0)
        for num, c in cnt.items():
            freq[c].append(num)
        for i in range(len(freq) - 1, 0, -1 ):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res