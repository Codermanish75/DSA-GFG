class Solution:
    def solve(self,arr,i,j,dp):
        if i>=j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        mini = float('inf')
        for k in range(i,j):
            temp=self.solve(arr,i,k,dp)+self.solve(arr,k+1,j,dp)+arr[i-1]*arr[k]*arr[j]
            
            mini=min(mini,temp)
        
        dp[i][j] = mini

        return dp[i][j]

    def matrixMultiplication(self, arr):
        # code here
        n=len(arr)
        dp = [[-1] * n for _ in range(n)]
        return self.solve(arr,1,n-1,dp)
        