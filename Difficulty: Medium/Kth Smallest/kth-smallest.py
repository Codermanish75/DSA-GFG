import heapq
class Solution:
    def kthSmallest(self, arr, k):
        # Code here
        heap=[]
        for x in arr:
            heapq.heappush(heap,-x)
            
            if len(heap)>k:
                heapq.heappop(heap)
            
        return -heap[0]
            
        
