#User function Template for python3

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here 
        # The condition for celebrity is that it doesn't know anyone but everyone knows him
        # We have to do something with this statement
        # From the matrix let C be the celebrity and i be the normal people
        # Therefore for the celebrity codition M[c][i] == 0 and M[i][c] ==1
        
        c = 0
        for i in range(1, n):
            if M[c][i] == 1:# C know i but i doesn't know C hence C is not celebrity but i may be a celebrity
                c = i # Therefore let C = i
        
        # Above loop will let us find the person which doesn't know only one person
        # We have to make sure that he/she doesn't know anyone there
        
        for i in range(0, n):
            if M[c][i]==1 or M[i][c]==0 and c!=i:
                return -1
    
        return c
                
                
        


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m,n))
# } Driver Code Ends