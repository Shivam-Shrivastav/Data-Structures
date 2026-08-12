## 188. Best Time to Buy and Sell Stock IV
**Category:** **BUY/SELL STOCK (STATE MACHINE)**

**Problem:** Stock prices array `prices[i]`. You can complete **at most k transactions** (buy→sell = 1 transaction). Must sell before buying again. Maximize profit.

**Example:**
```
Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy at 2, sell at 4 → profit=2
```

```
Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Transaction 1: Buy at 2, sell at 6 → profit=4
             Transaction 2: Buy at 0, sell at 3 → profit=3
             Total = 7
```

---

### **Relation to Stock Problems**
**Similar to:** **Stock III** (k=2) generalized to any k
**How it's different:**
1. **Stock III:** Fixed k=2 → 4 states
2. **Stock IV:** Any k → need **2k states** (hold[i], empty[i] for i=1..k)
3. **Optimization:** When k >= n/2, effectively unlimited (Stock II)

**Key Insight:** 
- Need to track profit after each transaction count
- Two arrays: `hold[j]` = max profit after jth buy (holding)
- `empty[j]` = max profit after jth sell (no shares, j transactions done)

---

### **State Machine Intuition**
For each transaction count t from 1 to k:
- **hold[t]**: Max profit after buying the t-th stock
- **empty[t]**: Max profit after selling the t-th stock

**Transitions:**
- `hold[t] = max(hold[t], empty[t-1] - price)`  # Buy using profit from t-1 transactions
- `empty[t] = max(empty[t], hold[t] + price)`   # Sell the t-th stock

---

### 1. Recursive Solution
```python
def maxProfit(k, prices):
    n = len(prices)
    
    def dfs(i, transactions, holding):
        if i >= n or transactions >= k:
            return 0
        
        if holding:
            # Can sell or do nothing
            sell = prices[i] + dfs(i+1, transactions+1, False)
            skip = dfs(i+1, transactions, True)
            return max(sell, skip)
        else:
            # Can buy or do nothing
            buy = -prices[i] + dfs(i+1, transactions, True)
            skip = dfs(i+1, transactions, False)
            return max(buy, skip)
    
    return dfs(0, 0, False)
```
**TC:** O(2ⁿ) | **SC:** O(n) recursion stack

---

### 2. Memoization (Top-Down DP)
```python
def maxProfit(k, prices):
    n = len(prices)
    memo = {}
    
    def dfs(i, transactions, holding):
        if i >= n or transactions >= k:
            return 0
        if (i, transactions, holding) in memo:
            return memo[(i, transactions, holding)]
        
        if holding:
            sell = prices[i] + dfs(i+1, transactions+1, False)
            skip = dfs(i+1, transactions, True)
            memo[(i, transactions, holding)] = max(sell, skip)
        else:
            buy = -prices[i] + dfs(i+1, transactions, True)
            skip = dfs(i+1, transactions, False)
            memo[(i, transactions, holding)] = max(buy, skip)
        
        return memo[(i, transactions, holding)]
    
    return dfs(0, 0, False)
```
**TC:** O(n × k × 2) = O(nk) | **SC:** O(nk)

---

### 3. Tabulation (2D DP)
```python
def maxProfit(k, prices):
    n = len(prices)
    if n <= 1 or k == 0:
        return 0
    
    # If k >= n/2, it's effectively unlimited transactions (Stock II)
    if k >= n // 2:
        profit = 0
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
    
    # dp[t][i] = max profit using at most t transactions up to day i
    dp = [[0] * n for _ in range(k+1)]
    
    for t in range(1, k+1):
        max_diff = -prices[0]  # max of (dp[t-1][j] - prices[j])
        for i in range(1, n):
            dp[t][i] = max(dp[t][i-1], prices[i] + max_diff)
            max_diff = max(max_diff, dp[t-1][i] - prices[i])
    
    return dp[k][n-1]
```
**TC:** O(kn) | **SC:** O(kn)

---

### 4. Space Optimized (2 arrays)
```python
def maxProfit(k, prices):
    n = len(prices)
    if n <= 1 or k == 0:
        return 0
    
    # If k >= n/2, it's effectively unlimited transactions
    if k >= n // 2:
        profit = 0
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
    
    # hold[j] = max profit after jth buy
    # empty[j] = max profit after jth sell
    hold = [-float('inf')] * (k+1)
    empty = [0] * (k+1)
    
    for price in prices:
        for j in range(1, k+1):
            # Update in reverse to use previous day's values
            empty[j] = max(empty[j], hold[j] + price)
            hold[j] = max(hold[j], empty[j-1] - price)
    
    return empty[k]
```
**TC:** O(kn) | **SC:** O(k)

---

### 5. 1D DP with Optimized Order
```python
def maxProfit(k, prices):
    n = len(prices)
    if n <= 1 or k == 0:
        return 0
    
    # If k >= n/2, it's effectively unlimited transactions
    if k >= n // 2:
        return sum(max(0, prices[i] - prices[i-1]) for i in range(1, n))
    
    # dp[j] = max profit with j transactions
    dp = [0] * (k+1)
    min_cost = [prices[0]] * (k+1)
    
    for i in range(1, n):
        for j in range(1, k+1):
            min_cost[j] = min(min_cost[j], prices[i] - dp[j-1])
            dp[j] = max(dp[j], prices[i] - min_cost[j])
    
    return dp[k]
```
**TC:** O(kn) | **SC:** O(k)

---

**Key Formula (Optimized 2D DP):**
```
For each transaction count t:
    max_diff = max(max_diff, dp[t-1][i] - prices[i])
    dp[t][i] = max(dp[t][i-1], prices[i] + max_diff)
```

**Key Formula (State Machine):**
```
empty[j] = max(empty[j], hold[j] + price)
hold[j] = max(hold[j], empty[j-1] - price)
```

**Example Walkthrough (State Machine):**
```
k=2, prices = [3,2,6,5,0,3]

Initialize: hold=[-inf,-inf,-inf], empty=[0,0,0]

price=3:
  j=1: empty[1]=max(0, -inf+3) = 0
       hold[1]=max(-inf, 0-3=-3) = -3
  j=2: empty[2]=max(0, -inf+3) = 0
       hold[2]=max(-inf, 0-3=-3) = -3

price=2:
  j=1: empty[1]=max(0, -3+2=-1) = 0
       hold[1]=max(-3, 0-2=-2) = -2
  j=2: empty[2]=max(0, -3+2=-1) = 0
       hold[2]=max(-3, 0-2=-2) = -2

price=6:
  j=1: empty[1]=max(0, -2+6=4) = 4
       hold[1]=max(-2, 0-6=-6) = -2
  j=2: empty[2]=max(0, -2+6=4) = 4
       hold[2]=max(-2, 4-6=-2) = -2

price=5:
  j=1: empty[1]=max(4, -2+5=3) = 4
       hold[1]=max(-2, 0-5=-5) = -2
  j=2: empty[2]=max(4, -2+5=3) = 4
       hold[2]=max(-2, 4-5=-1) = -1

price=0:
  j=1: empty[1]=max(4, -2+0=-2) = 4
       hold[1]=max(-2, 0-0=0) = 0
  j=2: empty[2]=max(4, -1+0=-1) = 4
       hold[2]=max(-1, 4-0=4) = 4

price=3:
  j=1: empty[1]=max(4, 0+3=3) = 4
       hold[1]=max(0, 0-3=-3) = 0
  j=2: empty[2]=max(4, 4+3=7) = 7
       hold[2]=max(4, 4-3=1) = 4

result = empty[2] = 7
```

**Example Walkthrough (2D DP):**
```
k=2, prices = [3,2,6,5,0,3]

t=1:
  max_diff = -3
  i=1: dp[1][1] = max(0, 2 + (-3) = -1) = 0, max_diff = max(-3, 0-2=-2) = -2
  i=2: dp[1][2] = max(0, 6 + (-2) = 4) = 4, max_diff = max(-2, 0-6=-6) = -2
  i=3: dp[1][3] = max(4, 5 + (-2) = 3) = 4, max_diff = max(-2, 0-5=-5) = -2
  i=4: dp[1][4] = max(4, 0 + (-2) = -2) = 4, max_diff = max(-2, 0-0=0) = 0
  i=5: dp[1][5] = max(4, 3 + 0 = 3) = 4

t=2:
  max_diff = -3 (dp[1][0]-3 = 0-3=-3)
  i=1: dp[2][1] = max(0, 2 + (-3) = -1) = 0, max_diff = max(-3, dp[1][1]-2=0-2=-2) = -2
  i=2: dp[2][2] = max(0, 6 + (-2) = 4) = 4, max_diff = max(-2, dp[1][2]-6=4-6=-2) = -2
  i=3: dp[2][3] = max(4, 5 + (-2) = 3) = 4, max_diff = max(-2, dp[1][3]-5=4-5=-1) = -1
  i=4: dp[2][4] = max(4, 0 + (-1) = -1) = 4, max_diff = max(-1, dp[1][4]-0=4-0=4) = 4
  i=5: dp[2][5] = max(4, 3 + 4 = 7) = 7

result = dp[2][5] = 7
```

**Optimization Trick:**
```
If k >= n/2, it's equivalent to unlimited transactions
Because you can't do more than n/2 transactions (each requires 2 days)
```

**Comparison Table:**

| Aspect | Stock III (k=2) | Stock IV (general k) |
|--------|-----------------|---------------------|
**States** | 4 states (hold1,empty1,hold2,empty2) | 2k states |
**Optimization** | Fixed k, simple | Need k >= n/2 check |
**DP Complexity** | O(n) | O(kn) |
**Space** | O(1) | O(k) optimized |
**When k large** | N/A | Use Stock II logic |

**State Machine Generalization:**

```
For t = 1 to k:
    hold[t] = max(hold[t], empty[t-1] - price)
    empty[t] = max(empty[t], hold[t] + price)
```

**Edge Cases:**
- k = 0 → 0
- n ≤ 1 → 0
- k >= n/2 → use Stock II (sum all positive diffs)
- Strictly decreasing → 0

**Key Insight:**
- The problem reduces to finding k non-overlapping profitable segments
- Dynamic programming naturally finds optimal combination
- When k is large enough, constraint becomes irrelevant