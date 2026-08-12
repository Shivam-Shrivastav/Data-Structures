// { Driver Code Starts
#include <bits/stdc++.h> 
using namespace std; 

 // } Driver Code Ends
class Solution
{   
    public: 
    //Function to return a list of integers denoting spiral traversal of matrix.
    vector<int> spirallyTraverse(vector<vector<int> > matrix, int r, int c) 
    {
        // code here 
        int T,B,L,R,dir;
    T=0;
    B=matrix.size()-1;
    L=0;
    R=matrix[0].size()-1;
    dir=0;
    int i;
    vector<int> ans;
    
    while(T<=B && L<=R)
    {
        if(dir==0)
        {
            for(i=L;i<=R;i++)
                ans.push_back(matrix[T][i]);
            T++;
        }
        else if(dir==1)
        {
            for(i=T;i<=B;i++)
                ans.push_back(matrix[i][R]);
            R--;
        }
        else if(dir==2)
        {
            for(i=R;i>=L;i--)
                ans.push_back(matrix[B][i]);
            B--;
        }
        else if(dir==3)
        {
            for(i=B;i>=T;i--)
                ans.push_back(matrix[i][L]);
            L++;
        }
        dir=(dir+1)%4;
    }
    return ans;
}
};

// { Driver Code Starts.
int main() {
    int t;
    cin>>t;
    
    while(t--) 
    {
        int r,c;
        cin>>r>>c;
        vector<vector<int> > matrix(r); 

        for(int i=0; i<r; i++)
        {
            matrix[i].assign(c, 0);
            for( int j=0; j<c; j++)
            {
                cin>>matrix[i][j];
            }
        }

        Solution ob;
        vector<int> result = ob.spirallyTraverse(matrix, r, c);
        for (int i = 0; i < result.size(); ++i)
                cout<<result[i]<<" ";
        cout<<endl;
    }
    return 0;
}  // } Driver Code Ends