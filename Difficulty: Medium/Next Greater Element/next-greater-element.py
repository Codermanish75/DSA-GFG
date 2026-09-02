class Solution:
    def nextLargerElement(self, arr):
        # n=len(arr)
        # ans=[]
        # for i in range(0,n):
        #     found=-1
        #     for j in range(i+1,n):
        #         if arr[j]>arr[i]:
        #             found=arr[j]
        #             break
        #     ans.append(found)
        # return ans
        
        n=len(arr)
        stack=[]
        ans=[-1]*n
        for i in range(n-1,-1,-1):
            while stack and stack[-1]<=arr[i]:
                stack.pop()
            if stack:
                ans[i]=stack[-1]
            stack.append(arr[i])
        return ans
                    
                    
            
                    
       
        