#User function Template for python3


class Solution:
    
    #Function to find largest rectangular area possible in a given histogram.
    def getMaxArea(self,histogram):
        #code here
        arr = histogram
        arr.extend([0,-1])
        print(arr)
        stack = [-1]
        print(stack)
        ans = 0
        for i in range(len(arr)-1):
            while arr[stack[-1]]>=arr[i]:
                ans = max(ans,arr[stack.pop()]*(i-stack[-1]-1))
            stack.append(i)
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

# by Jinay Shah 

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.getMaxArea(a))
# } Driver Code Ends