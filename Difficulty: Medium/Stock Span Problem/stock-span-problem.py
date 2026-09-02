class Solution:
    def calculateSpan(self, arr):
        # code here
        n=len(arr)
        ans=[-1]*n
        stack=[]
        for i in range(n):
            while stack and arr[i]>=stack[-1][0]:
                stack.pop()
            if stack:
                ans[i]=stack[-1][1]
            stack.append((arr[i],i))
        for i in range(n):
            ans[i]=i-ans[i]
        return ans