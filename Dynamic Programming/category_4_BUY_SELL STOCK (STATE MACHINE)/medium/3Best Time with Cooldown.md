## 309. Best Time to Buy and Sell Stock with Cooldown
**Category:** **BUY/SELL STOCK (STATE MACHINE)**

**Problem:** Stock prices array `prices[i]`. You can complete as many transactions as you like, but **after selling, you cannot buy the next day** (cooldown of 1 day). Maximize profit.

**Example:**
```
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: Transactions: Buy at 1, sell at 2 → profit=1
             Cooldown at 3 (can't buy)
             Buy at 0, sell at 2 → profit=2
             Total = 3
```

```
Input: prices = [1]
Output: 0
Explanation: No transaction possible
```

```
Input: prices = [1,2,4]
Output: 3
Explanation: Buy at 1, sell at 4 → profit=3
```

---

### **Relation to Stock Problems**
**Similar to:** **Stock II** (unlimited transactions) but with **cooldown constraint**
**How it's different:**
1. **Stock II:** Can buy immediately after selling
2. **With Cooldown:** Must wait 1 day after selling before next buy
3. **Need 3 states:** hold, empty, cooldown

**Key Insight:** 
- After selling, you enter cooldown state for one day
- From cooldown, you can only transition to empty (can't buy directly)
- This creates a 3-state machine

---

### **State Machine Intuition**
**3 States:**
1. **HOLD** = You have 1 share of stock
2. **EMPTY** = You have 0 shares, can buy
3. **COOLDOWN** = You just sold, can't do anything today

**Transitions:**
- **HOLD → HOLD:** Keep holding
- **HOLD → COOLDOWN:** Sell stock (gain `prices[i]`)
- **EMPTY → EMPTY:** Stay empty
- **EMPTY → HOLD:** Buy stock (pay `prices[i]`)
- **COOLDOWN → EMPTY:** Cooldown ends, can buy tomorrow
- **COOLDOWN → COOLDOWN:** Stay in cooldown? No, must go to empty next day

---

### 1. Recursive Solution
```python
def maxProfit(prices):
    n = len(prices)
    
    def dfs(i, state):
        # state: 0=empty, 1=holding, 2=cooldown
        if i >= n:
            return 0
        
        if state == 0:  # Empty - can buy or skip
            buy = -prices[i] + dfs(i+1, 1)
            skip = dfs(i+1, 0)
            return max(buy, skip)
        
        elif state == 1:  # Holding - can sell or skip
            sell = prices[i] + dfs(i+1, 2)  # Sell -> cooldown
            skip = dfs(i+1, 1)
            return max(sell, skip)
        
        else:  # Cooldown - must skip (can't do anything)
            return dfs(i+1, 0)  # Cooldown ends, back to empty
    
    return dfs(0, 0)
```
**TC:** O(2ⁿ) | **SC:** O(n) recursion stack

---

### 2. Memoization (Top-Down DP)
```python
def maxProfit(prices):
    n = len(prices)
    memo = {}
    
    def dfs(i, state):
        # state: 0=empty, 1=holding, 2=cooldown
        if i >= n:
            return 0
        if (i, state) in memo:
            return memo[(i, state)]
        
        if state == 0:  # Empty
            buy = -prices[i] + dfs(i+1, 1)
            skip = dfs(i+1, 0)
            memo[(i, state)] = max(buy, skip)
        
        elif state == 1:  # Holding
            sell = prices[i] + dfs(i+1, 2)
            skip = dfs(i+1, 1)
            memo[(i, state)] = max(sell, skip)
        
        else:  # Cooldown
            memo[(i, state)] = dfs(i+1, 0)
        
        return memo[(i, state)]
    
    return dfs(0, 0)
```
**TC:** O(n × 3) = O(n) | **SC:** O(n)

---

### 3. Tabulation (3-State DP)
```python
def maxProfit(prices):
    n = len(prices)
    if n <= 1:
        return 0
    
    # dp[i][0] = empty, dp[i][1] = hold, dp[i][2] = cooldown
    dp = [[0, 0, 0] for _ in range(n)]
    
    dp[0][0] = 0           # Empty on day 0
    dp[0][1] = -prices[0]  # Bought on day 0
    dp[0][2] = 0           # Can't be in cooldown on day 0
    
    for i in range(1, n):
        # Empty today: either was empty yesterday, or came from cooldown
        dp[i][0] = max(dp[i-1][0], dp[i-1][2])
        
        # Hold today: either was holding yesterday, or bought today (from empty)
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        
        # Cooldown today: sold yesterday (from hold)
        dp[i][2] = dp[i-1][1] + prices[i]
    
    # Max profit on last day: either empty or cooldown (can't be holding)
    return max(dp[n-1][0], dp[n-1][2])
```
**TC:** O(n) | **SC:** O(n)

---

### 4. Space Optimized (3 variables)
```python
def maxProfit(prices):
    n = len(prices)
    if n <= 1:
        return 0
    
    empty = 0
    hold = -prices[0]
    cooldown = 0
    
    for i in range(1, n):
        prev_empty = empty
        prev_hold = hold
        prev_cooldown = cooldown
        
        empty = max(prev_empty, prev_cooldown)
        hold = max(prev_hold, prev_empty - prices[i])
        cooldown = prev_hold + prices[i]
    
    return max(empty, cooldown)
```
**TC:** O(n) | **SC:** O(1)

---

### 5. Alternative: 2-State with Cool Variable
```python
def maxProfit(prices):
    n = len(prices)
    if n <= 1:
        return 0
    
    # cash: max profit with 0 shares (can buy today)
    # hold: max profit with 1 share
    # cool: max profit with 0 shares but in cooldown (can't buy today)
    cash = 0
    hold = -prices[0]
    cool = 0
    
    for i in range(1, n):
        prev_cash = cash
        
        cash = max(cash, cool)  # Stay empty or come from cooldown
        cool = hold + prices[i]  # Sell today -> go to cooldown
        hold = max(hold, prev_cash - prices[i])  # Keep holding or buy today
    
    return max(cash, cool)
```
**TC:** O(n) | **SC:** O(1)

---

**Key Formula (3-State Machine):**
```
empty[i] = max(empty[i-1], cooldown[i-1])
hold[i] = max(hold[i-1], empty[i-1] - prices[i])
cooldown[i] = hold[i-1] + prices[i]
```

**Example Walkthrough (3-State):**
```
prices = [1,2,3,0,2]

Initialize:
day 0: empty=0, hold=-1, cooldown=0

day 1 (price=2):
  empty = max(0, 0) = 0
  hold = max(-1, 0-2=-2) = -1
  cooldown = -1+2=1

day 2 (price=3):
  empty = max(0, 1) = 1
  hold = max(-1, 0-3=-3) = -1
  cooldown = -1+3=2

day 3 (price=0):
  empty = max(1, 2) = 2
  hold = max(-1, 1-0=1) = 1
  cooldown = -1+0=-1

day 4 (price=2):
  empty = max(2, -1) = 2
  hold = max(1, 2-2=0) = 1
  cooldown = 1+2=3

result = max(empty=2, cooldown=3) = 3
```

**State Machine Diagram:**
```
           Buy (-price)
    EMPTY ------------> HOLD
      ^                   |
      |                   | Sell (+price)
      |                   v
      |<---- COOLDOWN <---|
      |   (next day)      |
      |___________________|
```

**Comparison Table:**

| Aspect | Stock II (Unlimited) | Stock with Cooldown |
|--------|---------------------|---------------------|
**States** | empty, hold | empty, hold, cooldown |
**After Sell** | Can buy next day | Must cooldown 1 day |
**Transitions** | 2 states × 2 options | 3 states with restrictions |
**Greedy?** | Yes (sum uphill) | No (need state) |
**Space** | O(1) | O(1) |

**Edge Cases:**
- Empty array → 0
- Single element → 0
- Strictly decreasing → 0
- Strictly increasing → can do one transaction

**Why Cooldown Complicates:**
- Can't just sum all positive differences
- Need to decide whether to skip some profits to allow better timing
- Example: [1,2,3,0,2] - if you capture 1→2, you miss 3→? but 0→2 works

**Key Insight:**
- Cooldown forces you to choose between consecutive profits
- Sometimes better to skip a small profit to capture two larger ones
- State machine naturally handles this trade-off