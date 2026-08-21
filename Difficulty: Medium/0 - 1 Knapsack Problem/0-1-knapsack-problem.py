class Solution:
    # def solve(self,W,val,wt,n,dp):
    #     if (n==0 or W==0):
    #         return 0
    #     if dp[n][W]!=-1:
    #         return dp[n][W]
            
    #     if wt[n-1]<=W:
    #         dp[n][W]= max(val[n-1]+self.solve(W-wt[n-1],val,wt,n-1,dp),self.solve(W,val,wt,n-1,dp))
    #     elif wt[n-1]>W:
    #         dp[n][W]= self.solve(W,val,wt,n-1,dp)
        
    #     return dp[n][W]       
    
    
    def knapsack(self, W: int, val: list[int], wt: list[int]) -> int:
        n=len(wt)
        dp = [[-1] * (W + 1) for _ in range(n + 1)]
        # return self.solve(W,val,wt,n,dp)
        
        for i in range(n+1):
            for j in range(W+1):
                if i==0 or j==0:
                    dp[i][j]=0
        
        
        for i in range(1,n+1):
            for j in range(1,W+1):
                if wt[i-1]<=j:
                    dp[i][j]=max(val[i-1]+dp[i-1][j-wt[i-1]],dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
                    
        return dp[n][W]
                    
        # code here
        