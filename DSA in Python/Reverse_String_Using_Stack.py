#{ 
#Driver Code Starts

 # } Driver Code Ends
def reverse(S):
    
    #Add code here
    stack = []
    l = len(S) - 1
    while l>=0:
        stack.append(S[l])
        l-=1
    S = ''.join(stack)
    return S

#{ 
#Driver Code Starts.
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
#} Driver Code Ends