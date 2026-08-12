## 123. Best Time to Buy and Sell Stock III
**Category:** **BUY/SELL STOCK (STATE MACHINE)**

**Problem:** Stock prices array `prices[i]`. You can complete **at most 2 transactions** (buy→sell = 1 transaction). Must sell before buying again. Maximize profit.

**Example:**
```
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Transaction 1: Buy at 0 (day3), sell at 3 (day5) → profit=3
             Transaction 2: Buy at 1 (day6), sell at 4 (day7) → profit=3
             Total = 6
```

```
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: One transaction: Buy at 1, sell at 5 → profit=4
             (Two transactions would split: 1→3 + 3→5 = 2+2=4, same)
```

```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: No profit possible
```

---

### **Relation to Stock Problems**
**Similar to:** **Stock II** (multiple) but with **limited transactions (k=2)**
**How it's different:**
1. **Stock I:** One transaction → track min price
2. **Stock II:** Unlimited → sum all uphill
3. **Stock III:** At most 2 → need to track **states for first and second transactions**

**Key Insight:** 
- Need to track profits after **0, 1, or 2 transactions**
- At each day, we can be in one of 4 states:
  - `hold1`: After 1st buy (have 1 share)
  - `empty1`: After 1st sell (no shares, 1 done)
  - `hold2`: After 2nd buy (have 1 share again)
  - `empty2`: After 2nd sell (no shares, 2 done)

---

### **State Machine Intuition**
**4 States:**
1. `hold1` = max profit after **buying first stock**
2. `empty1` = max profit after **selling first stock** (1 transaction done)
3. `hold2` = max profit after **buying second stock**
4. `empty2` = max profit after **selling second stock** (2 transactions done)

**Transitions:**
- `hold1`: either kept from yesterday, or bought today (`-prices[i]`)
- `empty1`: either kept from yesterday, or sold today (`hold1 + prices[i]`)
- `hold2`: either kept from yesterday, or bought today (`empty1 - prices[i]`)
- `empty2`: either kept from yesterday, or sold today (`hold2 + prices[i]`)

---

### 1. Recursive Solution
```python
def maxProfit(prices):
    n = len(prices)
    
    def dfs(i, transactions, holding):
        if i >= n or transactions >= 2:
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
def maxProfit(prices):
    n = len(prices)
    memo = {}
    
    def dfs(i, transactions, holding):
        if i >= n or transactions >= 2:
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
**TC:** O(n × 2 × 2) = O(n) | **SC:** O(n)

---

### 3. Tabulation (4-State DP)
```python
def maxProfit(prices):
    n = len(prices)
    if n <= 1:
        return 0
    
    # Initialize states
    hold1 = -prices[0]  # Bought first stock
    empty1 = 0           # Sold first stock
    hold2 = -prices[0]   # Bought second stock
    empty2 = 0           # Sold second stock
    
    for i in range(1, n):
        prev_hold1, prev_empty1 = hold1, empty1
        prev_hold2, prev_empty2 = hold2, empty2
        
        hold1 = max(prev_hold1, -prices[i])
        empty1 = max(prev_empty1, prev_hold1 + prices[i])
        hold2 = max(prev_hold2, prev_empty1 - prices[i])
        empty2 = max(prev_empty2, prev_hold2 + prices[i])
    
    return max(0, empty1, empty2)
```
**TC:** O(n) | **SC:** O(1)

---

### 4. Compact 4-State (In-place updates)
```python
def maxProfit(prices):
    if not prices:
        return 0
    
    hold1 = -float('inf')
    empty1 = 0
    hold2 = -float('inf')
    empty2 = 0
    
    for price in prices:
        # Order matters: use previous values
        empty2 = max(empty2, hold2 + price)
        hold2 = max(hold2, empty1 - price)
        empty1 = max(empty1, hold1 + price)
        hold1 = max(hold1, -price)
    
    return max(0, empty1, empty2)
```
**TC:** O(n) | **SC:** O(1)

---

### 5. Bidirectional DP (Alternative approach)
```python
def maxProfit(prices):
    n = len(prices)
    if n <= 1:
        return 0
    
    # Left to right: max profit with 1 transaction up to day i
    left = [0] * n
    min_price = prices[0]
    for i in range(1, n):
        min_price = min(min_price, prices[i])
        left[i] = max(left[i-1], prices[i] - min_price)
    
    # Right to left: max profit with 1 transaction from day i to end
    right = [0] * n
    max_price = prices[-1]
    for i in range(n-2, -1, -1):
        max_price = max(max_price, prices[i])
        right[i] = max(right[i+1], max_price - prices[i])
    
    # Combine: first transaction up to i, second from i+1 onward
    max_profit = 0
    for i in range(n):
        max_profit = max(max_profit, left[i] + (right[i+1] if i+1 < n else 0))
    
    return max_profit
```
**TC:** O(n) | **SC:** O(n)

---

**Key Formula (4-State Machine):**
```
hold1 = max(hold1, -price)           # Buy first
empty1 = max(empty1, hold1 + price)  # Sell first
hold2 = max(hold2, empty1 - price)   # Buy second
empty2 = max(empty2, hold2 + price)  # Sell second
```

**Example Walkthrough (4-State):**
```
prices = [3,3,5,0,0,3,1,4]

Initialize: hold1=-inf, empty1=0, hold2=-inf, empty2=0

Day 0 (3):
  hold1 = max(-inf, -3) = -3
  empty1 = max(0, -3+3=0) = 0
  hold2 = max(-inf, 0-3=-3) = -3
  empty2 = max(0, -3+3=0) = 0

Day 1 (3):
  empty2 = max(0, -3+3=0) = 0
  hold2 = max(-3, 0-3=-3) = -3
  empty1 = max(0, -3+3=0) = 0
  hold1 = max(-3, -3) = -3

Day 2 (5):
  empty2 = max(0, -3+5=2) = 2
  hold2 = max(-3, 0-5=-5) = -3
  empty1 = max(0, -3+5=2) = 2
  hold1 = max(-3, -5) = -3

Day 3 (0):
  empty2 = max(2, -3+0=-3) = 2
  hold2 = max(-3, 2-0=2) = 2
  empty1 = max(2, -3+0=-3) = 2
  hold1 = max(-3, -0=0) = 0

... continue ...

Final: empty2 = 6
```

**Example Walkthrough (Bidirectional):**
```
prices = [3,3,5,0,0,3,1,4]

left (max profit up to i):
i=0: 0
i=1: max(0, 3-3=0)=0
i=2: max(0, 5-3=2)=2
i=3: max(2, 0-0=0)=2
i=4: max(2, 0-0=0)=2
i=5: max(2, 3-0=3)=3
i=6: max(3, 1-0=1)=3
i=7: max(3, 4-0=4)=4

right (max profit from i):
i=7: 0
i=6: max(0, 4-1=3)=3
i=5: max(3, 4-3=1)=3
i=4: max(3, 4-0=4)=4
i=3: max(4, 4-0=4)=4
i=2: max(4, 5-5=0)=4
i=1: max(4, 5-3=2)=4
i=0: max(4, 5-3=2)=4

Combine:
i=0: left[0]=0 + right[1]=4 = 4
i=1: left[1]=0 + right[2]=4 = 4
i=2: left[2]=2 + right[3]=4 = 6
i=3: left[3]=2 + right[4]=4 = 6
i=4: left[4]=2 + right[5]=3 = 5
i=5: left[5]=3 + right[6]=3 = 6
i=6: left[6]=3 + right[7]=0 = 3
i=7: left[7]=4 + 0 = 4
max = 6
```

**Comparison Table:**

| Aspect | Stock I (1 tx) | Stock II (∞) | Stock III (2 tx) |
|--------|----------------|--------------|------------------|
**States** | min_price | empty, hold | hold1, empty1, hold2, empty2 |
**Greedy?** | No | Yes | No |
**DP Approach** | Single pass | 2 states | 4 states / bidirectional |
**Time** | O(n) | O(n) | O(n) |
**Space** | O(1) | O(1) | O(1) |

**State Machine Progression:**

```
Stock I:     empty → hold → empty
              (1 tx)

Stock II:    empty ⇄ hold  (unlimited)

Stock III:   empty1 ⇄ hold1 → empty1 ⇄ hold2 → empty2
              (tx1)          (tx2)

Stock IV:    empty[0..k] ⇄ hold[0..k]
              (k transactions)
```

**Edge Cases:**
- Empty array → 0
- Single element → 0
- Strictly decreasing → 0
- Strictly increasing → prices[-1] - prices[0]

**Key Insight for Stock III:**
- Two transactions = find two non-overlapping profitable periods
- Bidirectional: best in first i days + best in remaining days
- State machine: track all possible states after each transaction