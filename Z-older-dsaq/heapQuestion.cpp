multiset<int,greater<int>> m;
        vector<int> vec;
        
        for(int i=0;i<k;i++)
        {
            m.insert(arr[i]);
        }
        
        vec.push_back(*m.begin());
        
        for(int i=k;i<n;i++)
        {
            m.erase(m.find(arr[i-k]));
            m.insert(arr[i]);
            vec.push_back(*m.begin());
        }
        
        return vec;