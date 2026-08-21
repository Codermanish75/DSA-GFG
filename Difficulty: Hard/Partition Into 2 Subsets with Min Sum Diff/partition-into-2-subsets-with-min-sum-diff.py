class Solution:
    def solve(self,arr,total,n,dp):
        if n==0 and total!=0:
            return 
        if total==0:
            return True
        if dp[n][total]!=-1:
            return dp[n][total]
        if arr[n-1]<=total:
            dp[n][total] =(self.solve(arr,total-arr[n-1],n-1,dp) or self.solve(arr,total,n-1,dp))
        else:
            dp[n][total] =self.solve(arr,total,n-1,dp)
        return dp[n][total]
    
    def minDifference(self, arr: list[int]) -> int:
        # code here
        total=sum(arr)
        n=len(arr)
        half=total//2
        dp=[[-1]*(half+1) for _ in range(n+1)]
        for s in range(half,-1,-1):
            if self.solve(arr,s,n,dp):
                return total-2*s
            