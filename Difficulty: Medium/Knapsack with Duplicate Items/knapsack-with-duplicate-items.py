class Solution:
    def solve(self,val,wt,capacity,n,dp):
        if n==0 or capacity==0:
            return 0
        if dp[n][capacity]!=-1:
            return dp[n][capacity]
        if wt[n-1]<=capacity:
            dp[n][capacity]=max(val[n-1]+self.solve(val,wt,capacity-wt[n-1],n,dp),self.solve(val,wt,capacity,n-1,dp))
        else:
            dp[n][capacity]=self.solve(val,wt,capacity,n-1,dp)
        return dp[n][capacity]
            
    
    
    def knapSack(self, val, wt, capacity):
        # code here
        n=len(val)
        dp=[[-1]*(capacity+1) for _ in range(n+1)]
        return self.solve(val,wt,capacity,n,dp)