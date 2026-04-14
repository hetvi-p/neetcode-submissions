class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
            
        res = [h[1] for h in heap]
        
        return res

        

            




                                 
        