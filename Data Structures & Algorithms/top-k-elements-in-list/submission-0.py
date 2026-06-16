class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = {}

        ## O(n)
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1

        # O(n)
        bucket = [[] for i in range(len(nums) + 1)]

        # O(n)
        for key, value in counter.items():
            bucket[value].append(key)

        res = []
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
               
        

        


            



            




        
        