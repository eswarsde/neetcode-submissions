import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        happy_string = []
        
        heap = []
        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(heap, (-c, 'c'))

        while heap:
            count1, ch1 = heapq.heappop(heap)
            # if it is safe to append these to happyString, go on 
            # else pop the second highest and append

            # Check if adding char1 would cause three in a row
            if len(happy_string)>=2 and ch1 == happy_string[-1] and ch1 == happy_string[-2]:
                # We can't use char1. We need the second most frequent character.
                if not heap:
                    break
                
                # Use the second character instead
                count2, ch2 = heapq.heappop(heap)
                happy_string.append(ch2)
                count2 +=1

                if count2 < 0:
                    heapq.heappush(heap, (count2, ch2))              
                
                #We didn't use char1, so push it back into the heap untouched
                heapq.heappush(heap, (count1, ch1))

            else:
                happy_string.append(ch1)
                count1 +=1

                if count1 < 0:
                    heapq.heappush(heap, (count1, ch1))

        return "".join(happy_string)
        