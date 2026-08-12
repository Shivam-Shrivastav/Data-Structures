## 518. Coin Change II
**Category:** **KNAPSACK / UNBOUNDED KNAPSACK (COUNTING)**

**Problem:** Given coins of different denominations and a total amount amount. Return the **number of combinations** that make up that amount. You have **unlimited supply** of each coin.

**Example:**
```
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: 5 = 5
             5 = 2+2+1
             5 = 2+1+1+1
             5 = 1+1+1+1+1
```

```
Input: amount = 3, coins = [2]
Output: 0
Explanation: Impossible to make amount 3 with only coin 2
```

```
Input: amount = 10, coins = [10]
Output: 1
Explanation: Only one combination: [10]
```

---

### **Relation to Coin Change I**
**Similar to:** **Coin Change I** but **count combinations** instead of min coins
**How it's different:**
1. **Coin Change I:** Minimize number of coins → `min(1 + dp[amt-coin])`
2. **Coin Change II:** Count combinations → `dp[amt] += dp[amt-coin]`
3. **Order matters:** Must avoid counting permutations as different

**Key Insight:** 
- To avoid counting permutations (1+2 vs 2+1 as same), **iterate coins first**
- Outer loop: coins
- Inner loop: amount from coin to target
- This ensures each combination is counted once

---

### DP Intuition
- **State:** `dp[i]` = number of combinations to make amount `i`
- **Transition:**
  ```
  For each coin c:
      for amount a from c to target:
          dp[a] += dp[a - c]
  ```
- **Base:** `dp[0] = 1` (one way to make amount 0: take no coins)
- **Answer:** `dp[amount]`

---

### 1. Recursive Solution
```python
def change(amount, coins):
    n = len(coins)
    
    def dfs(i, remaining):
        if remaining == 0:
            return 1
        if i >= n or remaining < 0:
            return 0
        
        # At index i, we can either:
        # 1. Use coin[i] (stay at i for unlimited usage)
        # 2. Skip coin[i] (move to next coin)
        use = dfs(i, remaining - coins[i])
        skip = dfs(i + 1, remaining)
        
        return use + skip
    
    return dfs(0, amount)
```
**TC:** O(2ⁿ⁺ᵃᵐᵒᵘⁿᵗ) | **SC:** O(n + amount) recursion stack

---

### 2. Memoization (Top-Down DP)
```python
def change(amount, coins):
    n = len(coins)
    memo = {}
    
    def dfs(i, remaining):
        if remaining == 0:
            return 1
        if i >= n or remaining < 0:
            return 0
        if (i, remaining) in memo:
            return memo[(i, remaining)]
        
        # Use coin[i] or skip it
        use = dfs(i, remaining - coins[i])
        skip = dfs(i + 1, remaining)
        
        memo[(i, remaining)] = use + skip
        return use + skip
    
    return dfs(0, amount)
```
**TC:** O(n × amount) | **SC:** O(n × amount)

---

### 3. Tabulation (2D DP)
```python
def change(amount, coins):
    n = len(coins)
    
    # dp[i][a] = combinations using first i coins to make amount a
    dp = [[0] * (amount + 1) for _ in range(n + 1)]
    
    # Base: 1 way to make amount 0 (use no coins)
    for i in range(n + 1):
        dp[i][0] = 1
    
    for i in range(1, n + 1):
        for a in range(1, amount + 1):
            # Don't use coin i-1
            dp[i][a] = dp[i-1][a]
            
            # Use coin i-1 (if possible)
            if a >= coins[i-1]:
                dp[i][a] += dp[i][a - coins[i-1]]
    
    return dp[n][amount]
```
**TC:** O(n × amount) | **SC:** O(n × amount)

---

### 4. Space Optimized (1D DP) - Classic Solution
```python
def change(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1
    
    for coin in coins:
        for a in range(coin, amount + 1):
            dp[a] += dp[a - coin]
    
    return dp[amount]
```
**TC:** O(n × amount) | **SC:** O(amount)

**Key: Outer loop coins, inner loop amount** (prevents permutations)

---

### 5. If order mattered (permutations) - Different loop order
```python
def change_permutations(amount, coins):
    # This counts permutations (1+2 and 2+1 as different)
    dp = [0] * (amount + 1)
    dp[0] = 1
    
    for a in range(1, amount + 1):
        for coin in coins:
            if a >= coin:
                dp[a] += dp[a - coin]
    
    return dp[amount]
```
**TC:** O(n × amount) | **SC:** O(amount)

**Difference:** Outer loop amount, inner loop coins counts permutations

---

**Key Formula:**
```
dp[0] = 1
for coin in coins:
    for a in range(coin, amount + 1):
        dp[a] += dp[a - coin]
```

**Example Walkthrough:**
```
amount = 5, coins = [1,2,5]

Initialize: dp = [1,0,0,0,0,0]

coin = 1:
  a=1: dp[1] += dp[0] = 1 → dp=[1,1,0,0,0,0]
  a=2: dp[2] += dp[1] = 1 → dp=[1,1,1,0,0,0]
  a=3: dp[3] += dp[2] = 1 → dp=[1,1,1,1,0,0]
  a=4: dp[4] += dp[3] = 1 → dp=[1,1,1,1,1,0]
  a=5: dp[5] += dp[4] = 1 → dp=[1,1,1,1,1,1]

coin = 2:
  a=2: dp[2] += dp[0] = 1+1=2 → dp=[1,1,2,1,1,1]
  a=3: dp[3] += dp[1] = 1+1=2 → dp=[1,1,2,2,1,1]
  a=4: dp[4] += dp[2] = 1+2=3 → dp=[1,1,2,2,3,1]
  a=5: dp[5] += dp[3] = 1+2=3 → dp=[1,1,2,2,3,3]

coin = 5:
  a=5: dp[5] += dp[0] = 3+1=4 → dp=[1,1,2,2,3,4]

Answer = dp[5] = 4
```

**Comparison Table:**

| Aspect | Coin Change I (Min Coins) | Coin Change II (Combinations) |
|--------|--------------------------|------------------------------|
**Objective** | Minimize number of coins | Count number of combinations |
**DP Operation** | `min(1 + dp[a-coin])` | `dp[a] += dp[a-coin]` |
**Initialization** | `dp[0]=0`, rest = inf | `dp[0]=1`, rest = 0 |
**Loop Order** | Either order works | Must iterate coins first |
**Result if impossible** | -1 | 0 |

**Knapsack Family Counting Problems:**

| Problem | Type | DP Formula |
|---------|------|------------|
**Coin Change II** | Unbounded combinations | `dp[a] += dp[a-coin]` (coins outer) |
**Combination Sum IV** | Permutations | `dp[a] += dp[a-coin]` (amount outer) |
**Target Sum** | 0/1 ± assignment | `dp[s] += dp[s-num]` |
**Partition Equal Subset Sum** | 0/1 subset sum | `dp[s] = dp[s] or dp[s-num]` |

**Edge Cases:**
- amount = 0 → 1 (empty combination)
- coins empty → 1 if amount=0 else 0
- No combination possible → 0

**Why Loop Order Matters:**
```
Coins = [1,2], amount = 3

Outer coins (combinations):
  coin=1: dp[1]=1, dp[2]=1, dp[3]=1
  coin=2: dp[2]=2, dp[3]=2
  Result: 2 combinations [1,1,1] and [1,2]

Outer amount (permutations):
  a=1: dp[1] = dp[0] from coin=1 = 1
  a=2: dp[2] = dp[1] from coin=1 + dp[0] from coin=2 = 1+1=2
  a=3: dp[3] = dp[2] from coin=1 + dp[1] from coin=2 = 2+1=3
  Result: 3 permutations [1,1,1], [1,2], [2,1]
```

**Key Insight:**
- Outer loop on coins ensures we consider each coin type only once in a fixed order
- This prevents counting [1,2] and [2,1] as different
- Each combination is built by adding coins in the order they appear in coins array

**Space Optimization Note:**
- 1D DP works because we update dp[a] using dp[a-coin] from **same coin iteration**
- This is safe because we want to count multiple uses of same coin