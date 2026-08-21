class Solution:
    def solve(self, arr, target, n, count, dp):

        if n == 0:
            if target == 0:
                return 1
            return 0
        
        if dp[n][target] != -1:
            return dp[n][target]
    
        if arr[n-1] <= target:
            dp[n][target] = (
                self.solve(arr, target-arr[n-1], n-1, count, dp)
                + self.solve(arr, target, n-1, count, dp)
            )
        else:
            dp[n][target] = self.solve(arr, target, n-1, count, dp)
    
        return dp[n][target]

    
	def perfectSum(self, arr, target):
		# code here
		n = len(arr)
        count = 0
        dp = [[-1] * (target+1) for _ in range(n+1)]
        
        return self.solve(arr, target, n, count, dp)
		
		