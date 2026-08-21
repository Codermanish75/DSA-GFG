class Solution:
    # def solve(self,arr,total,n,dp):
    #     if n==0 and total!=0:
    #         return False
            
    #     if total==0:
    #         return True
            
    #     if dp[n][total]!=-1:
    #         return dp[n][total]
        
    #     if arr[n-1]<=total:
    #         dp[n][total]=(self.solve(arr,total-arr[n-1],n-1,dp) or
    #         self.solve(arr,total,n-1,dp))
    #     elif arr[n-1]>total:
    #         dp[n][total]= self.solve(arr,total,n-1,dp)
    #     return dp[n][total]
    
    def equalPartition(self, arr):
        # code here
        total=sum(arr)
        if total%2!=0:
            return False
        total=total//2
        n=len(arr)
        dp=[[-1]*(total+1) for _ in range(n+1)]
        # return self.solve(arr,total,n,dp)
        for i in range(n+1):
            for j in range(total+1):
                if i==0 and j!=0:
                    dp[i][j]=False
                if j==0:
                    dp[i][j]=True
        
        for i in range(1,n+1):
            for j in range(1,total+1):
                if arr[i-1]<=j:
                    dp[i][j]=dp[i-1][j-arr[i-1]] or dp[i-1][j]
                elif arr[i-1]>j:
                    dp[i][j]=dp[i-1][j]
                    
        return dp[n][total]
            
        