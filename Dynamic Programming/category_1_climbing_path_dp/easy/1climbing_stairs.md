## Climbing Stairs
**Problem:** Climb to nth stair using 1 or 2 steps at a time. Count distinct ways.

---

### DP Intuition
- **Optimal Substructure:** Ways to reach step `n` = ways to reach `(n-1)` + ways to reach `(n-2)`
- **Base:** 0 ways to reach step 0? Actually `n=0 → 1 way` (stand there), `n=1 → 1 way`
- **State:** `dp[i]` = distinct ways to reach step `i`

---

### 1. Recursive Solution
```python
def climbStairs(n):
    if n <= 1:
        return 1
    return climbStairs(n-1) + climbStairs(n-2)
```
**TC:** O(2ⁿ) | **SC:** O(n) recursion stack

---

### 2. Memoization (Top-Down DP)
```python
def climbStairs(n):
    memo = {}
    def dfs(i):
        if i <= 1:
            return 1
        if i in memo:
            return memo[i]
        memo[i] = dfs(i-1) + dfs(i-2)
        return memo[i]
    return dfs(n)
```
**TC:** O(n) | **SC:** O(n)

---

### 3. Tabulation (Bottom-Up DP)
```python
def climbStairs(n):
    if n <= 1:
        return 1
    dp = [0]*(n+1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```
**TC:** O(n) | **SC:** O(n)

---

### 4. Space Optimized (Fibonacci-like)
```python
def climbStairs(n):
    if n <= 1:
        return 1
    prev2, prev1 = 1, 1  # for n=0 and n=1
    for i in range(2, n+1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr
    return prev1
```
**TC:** O(n) | **SC:** O(1)

---

**Formula:**  
It's basically Fibonacci:  
`F(0) = 1, F(1) = 1, F(n) = F(n-1) + F(n-2)`  
Answer = `F(n)`