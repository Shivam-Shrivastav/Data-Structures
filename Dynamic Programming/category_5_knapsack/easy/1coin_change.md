## 322. Coin Change
**Category:** **KNAPSACK / UNBOUNDED KNAPSACK**

**Problem:** Given coins of different denominations and a total amount amount. Find the **fewest number of coins** needed to make that amount. If impossible, return -1. You have **unlimited supply** of each coin.

**Example:**
```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```

```
Input: coins = [2], amount = 3
Output: -1
Explanation: Impossible to make amount 3 with only coin 2
```

```
Input: coins = [1], amount = 0
Output: 0
Explanation: No coins needed
```

---

### **Relation to Knapsack Problems**
**Similar to:** **Unbounded Knapsack** (items can be used unlimited times)
**How it's different:**
1. **0/1 Knapsack:** Each item used at most once
2. **Unbounded Knapsack:** Each item can be used multiple times
3. **Coin Change:** Minimize number of items, not maximize value

**Key Insight:** 
- At each amount, we try every coin denomination
- If we use coin `c`, remaining amount = `amount - c`
- Need 1 (this coin) + minimum coins for remaining amount

---

### DP Intuition
- **State:** `dp[i]` = minimum coins needed to make amount `i`
- **Transition:**
  ```
  For each coin c:
      if i >= c:
          dp[i] = min(dp[i], 1 + dp[i-c])
  ```
- **Base:** `dp[0] = 0` (0 coins needed for amount 0)
- **Initialize:** `dp[i] = infinity` (impossible amount)
- **Answer:** `dp[amount]` or -1 if infinity

---

### 1. Recursive Solution
```python
def coinChange(coins, amount):
    def dfs(remaining):
        if remaining < 0:
            return float('inf')
        if remaining == 0:
            return 0
        
        min_coins = float('inf')
        for coin in coins:
            res = dfs(remaining - coin)
            if res != float('inf'):
                min_coins = min(min_coins, 1 + res)
        
        return min_coins
    
    result = dfs(amount)
    return -1 if result == float('inf') else result
```
**TC:** O(amountᵏ) where k = len(coins) | **SC:** O(amount) recursion stack

---

### 2. Memoization (Top-Down DP)
```python
def coinChange(coins, amount):
    memo = {}
    
    def dfs(remaining):
        if remaining < 0:
            return float('inf')
        if remaining == 0:
            return 0
        if remaining in memo:
            return memo[remaining]
        
        min_coins = float('inf')
        for coin in coins:
            res = dfs(remaining - coin)
            if res != float('inf'):
                min_coins = min(min_coins, 1 + res)
        
        memo[remaining] = min_coins
        return min_coins
    
    result = dfs(amount)
    return -1 if result == float('inf') else result
```
**TC:** O(amount × k) | **SC:** O(amount)

---

### 3. Tabulation (Bottom-Up DP)
```python
def coinChange(coins, amount):
    # Initialize dp array with infinity
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], 1 + dp[i - coin])
    
    return -1 if dp[amount] == float('inf') else dp[amount]
```
**TC:** O(amount × k) | **SC:** O(amount)

---

### 4. BFS Solution (Alternative approach)
```python
from collections import deque

def coinChange(coins, amount):
    if amount == 0:
        return 0
    
    queue = deque([(0, 0)])  # (current_amount, steps)
    visited = [False] * (amount + 1)
    visited[0] = True
    
    while queue:
        curr, steps = queue.popleft()
        
        for coin in coins:
            next_amount = curr + coin
            if next_amount == amount:
                return steps + 1
            if next_amount < amount and not visited[next_amount]:
                visited[next_amount] = True
                queue.append((next_amount, steps + 1))
    
    return -1
```
**TC:** O(amount × k) | **SC:** O(amount)

---

### 5. Optimized DP (Early break)
```python
def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coins.sort()  # Sort coins for early break
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin > i:  # Coin too large, break early
                break
            dp[i] = min(dp[i], 1 + dp[i - coin])
    
    return -1 if dp[amount] == float('inf') else dp[amount]
```
**TC:** O(amount × k) but faster in practice | **SC:** O(amount)

---

**Key Formula:**
```
dp[i] = min(dp[i], 1 + dp[i - coin]) for all coin in coins where i >= coin
dp[0] = 0
Answer = dp[amount] or -1 if infinity
```

**Example Walkthrough:**
```
coins = [1,2,5], amount = 11

dp[0] = 0

i=1: try coin=1 → dp[1] = min(inf, 1+dp[0]=1) = 1
     coin=2 → i<2 skip, coin=5 → skip
     dp[1]=1

i=2: coin=1 → dp[2] = min(inf, 1+dp[1]=2) = 2
     coin=2 → dp[2] = min(2, 1+dp[0]=1) = 1
     dp[2]=1

i=3: coin=1 → dp[3] = min(inf, 1+dp[2]=2) = 2
     coin=2 → dp[3] = min(2, 1+dp[1]=2) = 2
     dp[3]=2

i=4: coin=1 → dp[4] = min(inf, 1+dp[3]=3) = 3
     coin=2 → dp[4] = min(3, 1+dp[2]=2) = 2
     dp[4]=2

i=5: coin=1 → dp[5] = min(inf, 1+dp[4]=3) = 3
     coin=2 → dp[5] = min(3, 1+dp[3]=3) = 3
     coin=5 → dp[5] = min(3, 1+dp[0]=1) = 1
     dp[5]=1

... continue ...

i=11: dp[11] = min(1+dp[10]=1+2=3, 1+dp[9]=1+3=4, 1+dp[6]=1+2=3) = 3
Answer = 3
```

**Comparison Table:**

| Aspect | 0/1 Knapsack | Unbounded Knapsack | Coin Change |
|--------|--------------|-------------------|-------------|
**Item usage** | At most once | Unlimited | Unlimited |
**Objective** | Maximize value | Maximize value | Minimize count |
**DP direction** | i from high to low | i from low to high | i from low to high |
**Transition** | `dp[i][w] = max(val + dp[i-1][w-wt], dp[i-1][w])` | `dp[w] = max(val + dp[w-wt], dp[w])` | `dp[a] = min(1 + dp[a-coin], dp[a])` |
**State** | 2D often | 1D forward | 1D forward |

**Knapsack Family:**

| Problem | Type | Key Difference |
|---------|------|---------------|
**0/1 Knapsack** | Classic | Each item once |
**Unbounded Knapsack** | Unlimited items | Can reuse items |
**Coin Change (min coins)** | Minimization | Fewest coins |
**Coin Change 2 (combinations)** | Counting | Number of ways |
**Partition Equal Subset Sum** | 0/1 | Can we sum to target? |
**Target Sum** | 0/1 | +/- assignment count |

**Edge Cases:**
- amount = 0 → 0
- coins empty → -1 (unless amount=0)
- coin > amount → skip
- No combination possible → -1

**Why BFS Works:**
- Each coin addition is like moving to next level
- BFS finds shortest path (minimum coins) in unweighted graph
- Nodes = amounts, Edges = coins

**Key Insight for Optimization:**
- Sort coins to break early when coin > i
- BFS can be faster when amount is large relative to coin values
- DP order matters: iterate coins outer loop for counting combinations