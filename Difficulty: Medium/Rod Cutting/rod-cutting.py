class Solution:
    def solve(self, arr, n, length, dp):
        if n==0 or length==0:
            return 0
        if dp[n][length]!=-1:
            return dp[n][length]
        
        if n<=length:
            dp[n][length]=max(arr[n-1]+self.solve(arr,n,length-n,dp),self.solve(arr,n-1,length,dp))
        else:
            dp[n][length]=self.solve(arr,n-1,length,dp)
            
            
        return dp[n][length]
        
    def cutRod(self, price: list[int]) -> int:
        n=len(price)
        dp=[[-1]*(n+1) for _ in range(n+1)]
        return self.solve(price,n,n,dp)
        
    