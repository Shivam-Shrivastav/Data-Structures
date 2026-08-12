#User function Template for python3

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # code here
        s = 0
        vis =  [False] * V
        queue = []
        ans = []
        vis[s] = True
        queue.append(s)
        while queue:
            u = queue[0]
            queue.pop(0)
            ans.append(u)
            for i in adj[u]:
                if vis[i] == False:
                    vis[i] = True
                    queue.append(i)
        return ans
        
        
        
#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends