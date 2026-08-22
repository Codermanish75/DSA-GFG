class Solution:
    def solve(self,arr,sum,n,dp):
        if n==0:
            if sum==0:
                return 1
            return 0
            
        if dp[n][sum]!=-1:
            return dp[n][sum]
        
        if arr[n-1]<=sum:
            dp[n][sum]= (self.solve(arr,sum-arr[n-1],n,dp)+self.solve(arr,sum,n-1,dp))
        else:
            dp[n][sum]= (self.solve(arr,sum,n-1,dp))
        
        return dp[n][sum]    
            
            
    def count(self, coins: list[int], sum: int) -> int:
        # code here
        n=len(coins)
        dp=[[-1]*(sum+1) for _ in range(n+1)]
        return self.solve(coins,sum,n,dp)
    