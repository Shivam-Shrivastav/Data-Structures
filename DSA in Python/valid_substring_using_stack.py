#User function Template for python3

class Solution:
    def findMaxLen(ob, S):
        # code here 
        count = 0
        i = 0
        stack = [-1]
        # stack.append(-1)
        while i<len(S):
            if S[i]=="(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack)==0:
                    stack.append(i)
                else:
                    count = max(count, i - stack[-1])
            i+=1
        return count
            
        
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        
        ob = Solution()
        print(ob.findMaxLen(S))
# } Driver Code Ends