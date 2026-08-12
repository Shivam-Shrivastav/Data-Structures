## Min Cost Climbing Stairs
**Problem:** Given an integer array `cost` where `cost[i]` is the cost to step on the i-th stair. Once you pay the cost, you can climb 1 or 2 steps. You can start from step 0 or step 1. Find minimum cost to reach the top (beyond the last stair).

**Example:**
```
Input: cost = [10, 15, 20]
Output: 15
Explanation:
Start at index 1 (cost[1] = 15), pay 15 → climb 2 steps → reach top.
Total cost = 15.
```

```
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: 1 → 1 → 1 → 1 → 1 → 1 (skip expensive 100s)
```

---

### DP Intuition
- **Goal:** Reach **beyond** the last stair (index n)
- **State:** `dp[i]` = min cost to reach step i
- **Transition:** 
  - To reach step i, either come from i-1 or i-2
  - But you **pay cost[i]** only when you **land on** step i
- **Key:** Final answer = min(cost to reach last stair, cost to reach second-last stair)
  Actually: `min(dp[n-1], dp[n-2])` where dp[i] includes cost[i]

Better formulation:
- `dp[i]` = min cost to reach step i **and pay cost[i]**
- `dp[i] = cost[i] + min(dp[i-1], dp[i-2])`
- Base: `dp[0] = cost[0]`, `dp[1] = cost[1]`
- Answer: `min(dp[n-1], dp[n-2])` (can jump to top from last or second-last)

---

### 1. Recursive Solution
```python
def minCostClimbingStairs(cost):
    n = len(cost)
    def dfs(i):
        if i <= 1:
            return cost[i] if i >= 0 else 0  # at step 0 or 1, pay its cost
        return cost[i] + min(dfs(i-1), dfs(i-2))
    # Can reach top from last or second-last
    return min(dfs(n-1), dfs(n-2))
```
**TC:** O(2ⁿ) | **SC:** O(n) recursion stack

---

### 2. Memoization (Top-Down DP)
```python
def minCostClimbingStairs(cost):
    n = len(cost)
    memo = {}
    def dfs(i):
        if i <= 1:
            return cost[i] if i >= 0 else 0
        if i in memo:
            return memo[i]
        memo[i] = cost[i] + min(dfs(i-1), dfs(i-2))
        return memo[i]
    return min(dfs(n-1), dfs(n-2))
```
**TC:** O(n) | **SC:** O(n)

---

### 3. Tabulation (Bottom-Up DP)
```python
def minCostClimbingStairs(cost):
    n = len(cost)
    if n == 0:
        return 0
    if n == 1:
        return cost[0]
    
    dp = [0] * n
    dp[0], dp[1] = cost[0], cost[1]
    
    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])
    
    return min(dp[n-1], dp[n-2])
```
**TC:** O(n) | **SC:** O(n)

---

### 4. Space Optimized
```python
def minCostClimbingStairs(cost):
    n = len(cost)
    if n <= 1:
        return 0 if n == 0 else min(cost[0], cost[1] if n > 1 else 0)
    
    prev2, prev1 = cost[0], cost[1]
    
    for i in range(2, n):
        curr = cost[i] + min(prev1, prev2)
        prev2, prev1 = prev1, curr
    
    return min(prev1, prev2)
```
**TC:** O(n) | **SC:** O(1)

---

**Alternative Intuition (Easier):**
- `dp[i]` = min cost to reach **step i** (without paying cost[i] yet)
- `dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])`
- Base: `dp[0] = 0`, `dp[1] = 0` (start from step 0 or 1 without paying)
- Answer: `dp[n]` (n = len(cost), top is beyond last index)

**Space-Optimized Version (Alternative):**
```python
def minCostClimbingStairs(cost):
    n = len(cost)
    if n == 1:
        return 0
    
    prev2, prev1 = 0, 0  # dp[0], dp[1]
    
    for i in range(2, n+1):
        curr = min(prev1 + cost[i-1], prev2 + cost[i-2])
        prev2, prev1 = prev1, curr
    
    return prev1
```