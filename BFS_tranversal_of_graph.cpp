// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends


class Solution {
  public:
    // Function to return Breadth First Traversal of given graph.
    vector<int> bfsOfGraph(int V, vector<int> adj[]) {
        // Code here
         bool visted[V+1]={false};
       queue<int>q;
       int s=0;
       q.push(s);
       visted[s]=true;
       vector<int>v;
       while(q.empty()==false){
           int u=q.front();
           q.pop();
           v.push_back(u);
           for(auto x:adj[u]){
               if(visted[x]==false){
                   visted[x]=true;
                   q.push(x);
               }
           }
       }
       return v;
    }
};

// { Driver Code Starts.
int main() {
    int tc;
    cin >> tc;
    while (tc--) {
        int V, E;
        cin >> V >>

            E;

        vector<int> adj[V];

        for (int i = 0; i < E; i++) {
            int u, v;
            cin >> u >> v;
            adj[u].push_back(v);
            // 		adj[v].push_back(u);
        }
        // string s1;
        // cin>>s1;
        Solution obj;
        vector<int> ans = obj.bfsOfGraph(V, adj);
        for (int i = 0; i < ans.size(); i++) {
            cout << ans[i] << " ";
        }
        cout << endl;
    }
    return 0;
}  // } Driver Code Ends