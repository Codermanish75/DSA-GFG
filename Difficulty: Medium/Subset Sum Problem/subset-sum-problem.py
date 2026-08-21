class Solution:
    # def subset_sum(self,arr,sum,n,dp):
    #     if n==0 and sum!=0:
    #         return False
    #     if sum==0:
    #         return True
    #     if dp[n][sum]!=-1:
    #         return dp[n][sum]
    #     if arr[n-1]<=sum:
    #         dp[n][sum]= (self.subset_sum(arr, sum - arr[n - 1], n - 1,dp) or
    #             self.subset_sum(arr, sum, n - 1,dp)
    #         )
        
    #     elif arr[n - 1] > sum:
    #         dp[n][sum]=self.subset_sum(arr, sum, n - 1,dp)
        
    #     return dp[n][sum]
            

        
        
        
        
    def isSubsetSum(self, arr: list[int], sum: int) -> bool:
        n=len(arr)
        dp=[[-1]*(sum+1) for _ in range(n+1)]
        # return self.subset_sum(arr,sum,n,dp)
        
        
        for i in range(n+1):
            for j in range(sum+1):
                if i==0 and j!=0:
                    dp[i][j]=False
                elif j==0:
                    dp[i][j]=True
                
        for i in range(1,n+1):
            for j in range(1,sum+1):
                if arr[i-1]<=j:
                    dp[i][j]=dp[i-1][j-arr[i-1]] or dp[i-1][j]
                elif arr[i-1]>j:
                    dp[i][j]=dp[i-1][j]
            
        return dp[n][sum]
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    