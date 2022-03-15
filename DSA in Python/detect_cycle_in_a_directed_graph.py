#User function Template for python3


class Solution:
    
    #Function to detect cycle in a directed graph.
    def solve(self, s, vis, order, adj):
        vis.add(s)
        order.add(s)
        for x in adj[s]:
            if x not in vis:
                conf = self.solve(x, vis, order, adj)
                if conf:
                    return True
            elif x in order:
                return True
        order.remove(s)
        return False
        
    def isCyclic(self, V, adj):
        # code here
        order = set()
        vis = set()
        for i in range(V):
            if i not in vis:
                c = self.solve(i, vis, order, adj)
                if c:
                    return True
        return False
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends