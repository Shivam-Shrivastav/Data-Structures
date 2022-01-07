class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxProfit = 0;
        int minbuy = INT_MAX;
        for(int i=0; i<prices.size(); i++){
            minbuy = min(minbuy, prices[i]);
            maxProfit = max(maxProfit, prices[i]-minbuy);
        }
        return maxProfit;
    }
        
};