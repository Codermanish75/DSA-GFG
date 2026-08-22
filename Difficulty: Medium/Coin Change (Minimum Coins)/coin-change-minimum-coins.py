class Solution:
    def solve(self,arr,sum,n,dp):
        
        if sum==0:
            return 0
            
        if n==0:
            return float('inf')
    
        if dp[n][sum]!=-1:
            return dp[n][sum]
    
        if arr[n-1]<=sum:
            dp[n][sum]= min(self.solve(arr,sum-arr[n-1],n,dp)+1,self.solve(arr,sum,n-1,dp))
        else:
            dp[n][sum]= (self.solve(arr,sum,n-1,dp))
    
        return dp[n][sum]    

    def minCoins(self, coins: list[int], sum: int) -> int:
        n=len(coins)
        dp=[[-1]*(sum+1) for _ in range(n+1)]
        ans= self.solve(coins,sum,n,dp)
        if ans == float('inf'):
            return -1
        return ans
        
        
        
        