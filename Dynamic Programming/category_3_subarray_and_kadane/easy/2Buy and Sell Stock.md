## 121. Best Time to Buy and Sell Stock
**Category:** **SUBARRAY DP / KADANE'S VARIANT**

**Problem:** Given stock prices array `prices[i]`, choose **single day to buy** and **single later day to sell** to maximize profit. Return max profit (0 if no profit possible).

**Example:**
```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy at 1, sell at 6 → profit = 5
```

```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: No profit possible → return 0
```

---

### **Relation to Maximum Subarray**
**Similar to:** **Kadane's Algorithm on price differences**
**How it transforms:**
1. Create `diff` array where `diff[i] = prices[i] - prices[i-1]` for i≥1
2. **Maximum subarray sum** of `diff` = maximum profit from one transaction
3. Because profit = sum of consecutive day differences

**Difference from Maximum Subarray:**
- Maximum Subarray: find subarray with largest sum
- Stock: find max of (prices[j] - prices[i]) for j > i
- Can be solved with **single pass tracking min price**

---

### DP Intuition
1. **State:** Track minimum price seen so far
2. **Transition:** Profit = current price - min price so far
3. **Answer:** Max profit across all days

---

### 1. Recursive Solution
```python
def maxProfit(prices):
    n = len(prices)
    
    def dfs(i, min_price):
        if i >= n:
            return 0
        
        # Profit if sell at i
        profit = prices[i] - min_price
        # Update min_price for future
        new_min = min(min_price, prices[i])
        
        # Max of (sell today, don't sell today)
        return max(profit, dfs(i+1, new_min))
    
    return dfs(0, float('inf'))
```
**TC:** O(n) | **SC:** O(n) recursion stack

---

### 2. Memoization (not needed - no overlapping subproblems)
```python
def maxProfit(prices):
    n = len(prices)
    memo = {}
    
    def dfs(i, min_price):
        if i >= n:
            return 0
        if (i, min_price) in memo:
            return memo[(i, min_price)]
        
        profit = prices[i] - min_price
        new_min = min(min_price, prices[i])
        
        memo[(i, min_price)] = max(profit, dfs(i+1, new_min))
        return memo[(i, min_price)]
    
    return dfs(0, float('inf'))
```
**TC:** O(n) | **SC:** O(n²?) Actually state space large - not efficient

---

### 3. Tabulation (DP Array)
```python
def maxProfit(prices):
    n = len(prices)
    if n <= 1:
        return 0
    
    dp = [0] * n  # dp[i] = max profit ending at/on or before i
    min_price = prices[0]
    
    for i in range(1, n):
        min_price = min(min_price, prices[i-1])
        dp[i] = max(dp[i-1], prices[i] - min_price)
    
    return dp[n-1]
```
**TC:** O(n) | **SC:** O(n)

---

### 4. Space Optimized (Single Pass - Optimal)
```python
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    
    return max_profit
```
**TC:** O(n) | **SC:** O(1)

---

### 5. Kadane's on Differences
```python
def maxProfit(prices):
    if len(prices) <= 1:
        return 0
    
    curr_profit = 0
    max_profit = 0
    
    for i in range(1, len(prices)):
        diff = prices[i] - prices[i-1]
        curr_profit = max(diff, curr_profit + diff)
        max_profit = max(max_profit, curr_profit)
    
    return max_profit
```
**TC:** O(n) | **SC:** O(1)

---

**Key Formula:**
```
min_price = min(min_price, prices[i])
profit = max(profit, prices[i] - min_price)
```

**Transformation to Maximum Subarray:**
```
prices:  [7, 1, 5, 3, 6, 4]
diff:       [-6, 4, -2, 3, -2]
Kadane on diff: max subarray = [4, -2, 3] = 5
Profit: Buy at day of first diff's index, sell at last diff's index
```

**Example Walkthrough:**
```
prices = [7,1,5,3,6,4]
min_price = inf, profit = 0

i=0: price=7, min=7, profit=max(0,0)=0
i=1: price=1, min=1, profit=max(0,1-7= -6)=0
i=2: price=5, min=1, profit=max(0,5-1=4)=4
i=3: price=3, min=1, profit=max(4,3-1=2)=4
i=4: price=6, min=1, profit=max(4,6-1=5)=5
i=5: price=4, min=1, profit=max(5,4-1=3)=5
```

**Comparison Table:**

| Aspect | Maximum Subarray | Best Time to Buy/Sell Stock |
|--------|-----------------|----------------------------|
**Input** | Array of numbers | Array of prices |
**DP State** | Max sum ending at i | Min price seen so far |
**Subproblem** | Contiguous sum | Min prefix |
**Output** | Largest sum subarray | Max (price - min_prev) |
**Kadane's** | Direct application | On diff array |

**Variations of Stock Problems:**

| Variation | Key Difference | Solution |
|-----------|---------------|----------|
| **121. One Transaction** | Buy once, sell once | Track min price |
| **122. Multiple Transactions** | Buy/sell many times | Sum all positives |
| **123. Two Transactions** | At most 2 transactions | 4-state DP |
| **188. k Transactions** | At most k transactions | 2D DP |
| **309. Cooldown** | Can't buy next day after sell | State machine |
| **714. With Fee** | Pay fee per transaction | DP with fee |

**Edge Cases:**
- Empty array → 0
- Single element → 0
- Decreasing prices → 0
- All equal → 0

**Why Not Greedy?**
- Greedy: buy at global min, sell at global max
- But global max must come after global min
- DP/scan ensures this ordering constraint