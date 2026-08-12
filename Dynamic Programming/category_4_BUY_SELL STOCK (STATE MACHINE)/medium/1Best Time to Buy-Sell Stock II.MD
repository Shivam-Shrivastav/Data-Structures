## 122. Best Time to Buy and Sell Stock II
**Category:** **BUY/SELL STOCK (STATE MACHINE)**

**Problem:** You have stock prices array `prices[i]`. You can complete **as many transactions as you like** (buy one, sell one, repeat). However, you must sell before buying again. Maximize profit.

**Example:**
```
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy at 1 (day2), sell at 5 (day3) → profit=4
             Buy at 3 (day4), sell at 6 (day5) → profit=3
             Total = 7
```

```
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy at 1, sell at 5 → profit=4
```

```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: No profit possible
```

---

### **Relation to Stock Problems**
**Similar to:** **Stock I** (one transaction) but with **multiple transactions allowed**
**How it's different:**
1. **Stock I:** Only one transaction → track min price
2. **Stock II:** Multiple transactions → sum all upward moves
3. **Stock III/IV:** Limited transactions → state machine with k transactions

**Key Insight:** 
- You can buy and sell multiple times
- Equivalent to **summing all positive differences** between consecutive days
- **Greedy works:** Every time price increases from previous day, capture profit

---

### **State Machine Intuition**
Two states at each day:
1. **HOLD** state: You have 1 share of stock
2. **EMPTY** state: You have 0 shares (cash only)

Transitions:
- `EMPTY` → `HOLD`: Buy stock (pay `prices[i]`)
- `HOLD` → `EMPTY`: Sell stock (gain `prices[i]`)
- Can stay in same state

**DP State:** `dp[i][state]` = max profit at day i in given state

---

### 1. Recursive Solution
```python
def maxProfit(prices):
    n = len(prices)
    
    def dfs(i, holding):
        if i >= n:
            return 0
        
        if holding:
            # Can sell or do nothing
            sell = prices[i] + dfs(i+1, False)
            skip = dfs(i+1, True)
            return max(sell, skip)
        else:
            # Can buy or do nothing
            buy = -prices[i] + dfs(i+1, True)
            skip = dfs(i+1, False)
            return max(buy, skip)
    
    return dfs(0, False)
```
**TC:** O(2ⁿ) | **SC:** O(n) recursion stack

---

### 2. Memoization (Top-Down DP)
```python
def maxProfit(prices):
    n = len(prices)
    memo = {}
    
    def dfs(i, holding):
        if i >= n:
            return 0
        if (i, holding) in memo:
            return memo[(i, holding)]
        
        if holding:
            # Can sell or do nothing
            sell = prices[i] + dfs(i+1, False)
            skip = dfs(i+1, True)
            memo[(i, holding)] = max(sell, skip)
        else:
            # Can buy or do nothing
            buy = -prices[i] + dfs(i+1, True)
            skip = dfs(i+1, False)
            memo[(i, holding)] = max(buy, skip)
        
        return memo[(i, holding)]
    
    return dfs(0, False)
```
**TC:** O(n) | **SC:** O(n)

---

### 3. Tabulation (Bottom-Up DP)
```python
def maxProfit(prices):
    n = len(prices)
    if n <= 1:
        return 0
    
    # dp[i][0] = max profit at day i with 0 shares (empty)
    # dp[i][1] = max profit at day i with 1 share (holding)
    dp = [[0, 0] for _ in range(n)]
    
    dp[0][0] = 0
    dp[0][1] = -prices[0]  # Bought on day 0
    
    for i in range(1, n):
        # Empty today: either was empty yesterday, or sold today
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        # Holding today: either was holding yesterday, or bought today
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
    
    return dp[n-1][0]
```
**TC:** O(n) | **SC:** O(n)

---

### 4. Space Optimized (State Machine)
```python
def maxProfit(prices):
    n = len(prices)
    if n <= 1:
        return 0
    
    empty = 0
    hold = -prices[0]
    
    for i in range(1, n):
        prev_empty = empty
        empty = max(empty, hold + prices[i])
        hold = max(hold, prev_empty - prices[i])
    
    return empty
```
**TC:** O(n) | **SC:** O(1)

---

### 5. Greedy Solution (Sum All Uphill)
```python
def maxProfit(prices):
    profit = 0
    
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    
    return profit
```
**TC:** O(n) | **SC:** O(1)

---

**Key Formula (State Machine):**
```
empty[i] = max(empty[i-1], hold[i-1] + prices[i])
hold[i] = max(hold[i-1], empty[i-1] - prices[i])
empty[0] = 0
hold[0] = -prices[0]
Answer = empty[n-1]
```

**Greedy Formula:**
```
profit = sum(max(0, prices[i] - prices[i-1]))
```

**Example Walkthrough (State Machine):**
```
prices = [7,1,5,3,6,4]

Day 0: empty=0, hold=-7

Day 1 (price=1):
  empty = max(0, -7+1=-6) = 0
  hold = max(-7, 0-1=-1) = -1  ← better to buy today

Day 2 (price=5):
  empty = max(0, -1+5=4) = 4
  hold = max(-1, 0-5=-5) = -1  ← still better to keep

Day 3 (price=3):
  empty = max(4, -1+3=2) = 4
  hold = max(-1, 4-3=1) = 1   ← buy again? wait

Day 4 (price=6):
  empty = max(4, 1+6=7) = 7
  hold = max(1, 4-6=-2) = 1

Day 5 (price=4):
  empty = max(7, 1+4=5) = 7
  hold = max(1, 7-4=3) = 3

Answer = 7
```

**Example Walkthrough (Greedy):**
```
prices = [7,1,5,3,6,4]
diffs:    -6, +4, -2, +3, -2
sum all positive: 4 + 3 = 7
```

**Comparison Table:**

| Aspect | Stock I (One Transaction) | Stock II (Multiple) |
|--------|--------------------------|---------------------|
**Transactions** | At most 1 | Unlimited |
**DP States** | Min price + max profit | Empty/Hold states |
**Greedy possible?** | No (need correct order) | Yes (sum uphill) |
**Time Complexity** | O(n) | O(n) |
**Space** | O(1) | O(1) |
**Intuition** | Buy low, sell high once | Capture every rise |

**State Machine Pattern for Stock Problems:**

| Problem | States | Transition |
|---------|--------|------------|
**121. One Transaction** | min_price, max_profit | Track min, calc profit |
**122. Unlimited** | empty, hold | empty/hold with no limit |
**123. Two Transactions** | empty1, hold1, empty2, hold2 | 4 states |
**188. k Transactions** | empty[k+1], hold[k+1] | 2(k+1) states |
**309. Cooldown** | empty, hold, cooldown | 3 states |
**714. With Fee** | empty, hold | Add fee on sell |

**Edge Cases:**
- Empty array → 0
- Single element → 0
- Strictly decreasing → 0
- Strictly increasing → prices[-1] - prices[0]

**Why Greedy Works:**
- Multiple transactions mean we can capture every upward move
- Valley-to-peak profit = sum of all step-up profits
- No penalty for multiple transactions
- Equivalent to: buy at every local min, sell at every local max

**Key Insight:**
```
Profit = (5-1) + (6-3) = 4 + 3 = 7
       = (1→5) + (3→6)
       = sum of all upward steps
```