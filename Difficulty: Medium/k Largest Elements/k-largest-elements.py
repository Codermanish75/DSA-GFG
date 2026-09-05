import heapq
class Solution:
	def kLargest(self, arr, k):
		# code here
		heap=[]
		for x in arr:
		    heapq.heappush(heap,x)
		    if len(heap)>k:
		        heapq.heappop(heap)
		return sorted(heap , reverse=True)
		