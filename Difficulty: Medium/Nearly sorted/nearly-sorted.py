import heapq

class Solution:
    def nearlySorted(self, arr, k):
        heap = []

        for x in arr[:k+1]:
            heapq.heappush(heap, x)

        index = 0

        for i in range(k+1, len(arr)):
            arr[index] = heapq.heappop(heap)
            index += 1
            heapq.heappush(heap, arr[i])

        while heap:
            arr[index] = heapq.heappop(heap)
            index += 1

        return arr
                
        