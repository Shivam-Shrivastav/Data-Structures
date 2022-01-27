// { Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
// User function Template for C++

class Solution{
public:
    vector<vector<int>> nQueen(int n) {
        // code here
        vector<vector<int>>answer;
        vector<vector<char>>grid(n,vector<char>(n,'.'));
        vector<int>tempAns;
        NQueens(tempAns,grid, 0, n, answer);
        return answer;
    }
    
    private:
    void NQueens(vector<int>&tempAns, vector<vector<char>>&grid, int row, int n, vector<vector<int>> &answer ){
        
        if(row == n){
            answer.push_back(tempAns);
            return;
        }
        
        for(int col = 0 ; col < n; col++)
        {
            if(isValid(row, col, grid, n))
            {
               grid[row][col]='Q';
               tempAns.push_back(col+1);
               NQueens(tempAns, grid, row+1, n, answer);
               tempAns.pop_back();
               grid[row][col]='.';
            }    
        }        
        return;
    }
    
    bool isValid(int row, int col, vector<vector<char>>&grid, int n ){
        return isRowValid(row, grid, n) && isColValid(col, grid, n) && AreDiagonalsValid(row, col, grid, n);
    }
    
    bool isRowValid(int row,vector<vector<char>>&grid, int n){
        for(int j = 0 ; j < n ; j++){
            if(grid[row][j]=='Q')
                return false;
        }
        return true;
    }
    
    bool isColValid(int col,vector<vector<char>>&grid, int n){
        for(int j = 0 ; j < n ; j++){
            if(grid[j][col]=='Q')
                return false;
        }
        return true;
    }
    
    bool AreDiagonalsValid(int row, int col, vector<vector<char>>&grid, int n){
        int i = row, j = col;
        
        while(i>=0 && j>=0) //Upper Left Diagonal
        {
            if(grid[i][j]=='Q')
                return false;
            
            i--,j--;
        }
        
        i = row, j = col;
        
        while(i>=0 && j<n) //Upper Right Diagonal
        {
            if(grid[i][j]=='Q')
                return false;
            
            i--,j++;
        }
        
        i = row, j = col;
        
        while(i<n && j<n) //Lower Right Diagonal
        {
            if(grid[i][j]=='Q')
                return false;
            
            i++,j++;
        }
        
        i = row, j = col;
        
        while(i<n && j>=0) //Lower Left Diagonal
        {
            if(grid[i][j]=='Q')
                return false;
            
            i++,j--;
        }
        return true;
        
    }
};

// { Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        
        Solution ob;
        vector<vector<int>> ans = ob.nQueen(n);
        if(ans.size() == 0)
            cout<<-1<<"\n";
        else {
            for(int i = 0;i < ans.size();i++){
                cout<<"[";
                for(int u: ans[i])
                    cout<<u<<" ";
                cout<<"] ";
            }
            cout<<endl;
        }
    }
    return 0;
}  // } Driver Code Ends