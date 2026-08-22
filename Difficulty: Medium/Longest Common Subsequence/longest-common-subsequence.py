class Solution:
    def solve(self,s1,s2,n,m,dp):
        if n==0 or m==0:
            return 0
        if dp[n][m]!=-1:
            return dp[n][m]
        if s1[n-1]==s2[m-1]:
            dp[n][m]= (1+self.solve(s1,s2,n-1,m-1,dp))
        else:
            dp[n][m]= max(self.solve(s1,s2,n,m-1,dp),self.solve(s1,s2,n-1,m,dp))
        return dp[n][m]
    
    def lcs(self, s1, s2):
        # code here
        n=len(s1)
        m=len(s2)
        dp=[[-1]*(m+1) for _ in range(n+1)]
        return self.solve(s1,s2,n,m,dp)