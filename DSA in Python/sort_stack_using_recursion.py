class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    
    def merger(self,temp,s) :
        if len(s)==0 or temp>s[-1] :
            
            return s.append(temp)
        else :
            temp1 = s.pop()
            self.merger(temp,s)
            return s.append(temp1)
    def sorted(self, s):
        if len(s)==0 :
            return
        temp = s.pop()
        self.sorted(s)
        return self.merger(temp,s)      
        


#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


# } Driver Code Ends