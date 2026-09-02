class Solution:
	def preGreaterEle(self, arr):
		# code here
		n=len(arr)
		ans=[-1]*n
		stack=[]
		for i in range(0,n):
		    while stack and stack[-1]<=arr[i]:
		        stack.pop()
		    if stack:
		        ans[i]=stack[-1]
		    stack.append(arr[i])
		return ans