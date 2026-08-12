// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;
vector<int> find(int a[], int n , int x );

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,x;
        cin>>n>>x;
        int arr[n],i;
        for(i=0;i<n;i++)
        cin>>arr[i];
        vector<int> ans;
        ans=find(arr,n,x);
        cout<<ans[0]<<" "<<ans[1]<<endl;
    }
    return 0;
}


// } Driver Code Ends


vector<int> find(int arr[], int n , int x )
{
    // code here
    int a,b;
    bool flag1=false;
    bool flag2=false;
    for(int i=0;i<n;i++){
        if(arr[i]==x){
           a=i;
           flag1=true;
           break;
        }
    }
    if(flag1==false){
        a=-1;
    }
    for(int i=n-1;i>=0;i--){
        if(arr[i]==x){
            b=i;
            flag2=true;
            break;
        }
    }
    if(flag2==false){
        b=-1;
    }
    return {a,b};
    
}