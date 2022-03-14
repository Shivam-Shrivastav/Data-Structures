#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def solve(self, s, visited, ans, adj):
        visited.add(s)
        ans.append(s)
        for i in adj[s]:
            if i not in visited:
                self.solve(i, visited, ans, adj)
            
    def dfsOfGraph(self, V, adj):
        # code here
        visited = set()
        ans = []
        s = 0
        self.solve(s, visited, ans, adj)
        return ans

#{ 
#  Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends