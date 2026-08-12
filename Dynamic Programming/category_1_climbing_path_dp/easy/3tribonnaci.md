## N-th Tribonacci Number
**Problem:** The Tribonacci sequence Tₙ is defined as:
- T₀ = 0, T₁ = 1, T₂ = 1
- Tₙ₊₃ = Tₙ + Tₙ₊₁ + Tₙ₊₂ for n ≥ 0

Return the value of Tₙ.

**Example:**
```
Input: n = 4
Output: 4
Explanation:
T₃ = T₀ + T₁ + T₂ = 0 + 1 + 1 = 2
T₄ = T₁ + T₂ + T₃ = 1 + 1 + 2 = 4
```

```
Input: n = 25
Output: 1389537
```

---

### DP Intuition
- **Simple extension of Fibonacci:** Sum of last 3 terms instead of 2
- **Optimal Substructure:** Tₙ = Tₙ₋₁ + Tₙ₋₂ + Tₙ₋₃
- **Base Cases:** T₀ = 0, T₁ = 1, T₂ = 1
- **State:** `dp[i]` = Tᵢ (i-th Tribonacci number)

---

### 1. Recursive Solution
```python
def tribonacci(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
```
**TC:** O(3ⁿ) | **SC:** O(n) recursion stack

---

### 2. Memoization (Top-Down DP)
```python
def tribonacci(n):
    memo = {}
    def dfs(i):
        if i == 0:
            return 0
        if i <= 2:
            return 1
        if i in memo:
            return memo[i]
        memo[i] = dfs(i-1) + dfs(i-2) + dfs(i-3)
        return memo[i]
    return dfs(n)
```
**TC:** O(n) | **SC:** O(n)

---

### 3. Tabulation (Bottom-Up DP)
```python
def tribonacci(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    
    dp = [0] * (n+1)
    dp[0], dp[1], dp[2] = 0, 1, 1
    
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    return dp[n]
```
**TC:** O(n) | **SC:** O(n)

---

### 4. Space Optimized
```python
def tribonacci(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    
    a, b, c = 0, 1, 1  # T₀, T₁, T₂
    
    for i in range(3, n+1):
        d = a + b + c
        a, b, c = b, c, d
    
    return c
```
**TC:** O(n) | **SC:** O(1)

---

**Formula:**
```
Base: T₀ = 0, T₁ = 1, T₂ = 1
Recurrence: Tₙ = Tₙ₋₁ + Tₙ₋₂ + Tₙ₋₃ for n ≥ 3
```

**Edge Cases:**
- n = 0 → return 0
- n = 1 or 2 → return 1
- n can be up to 37 (in original constraints)

**Quick Sequence:**
```
T₀ = 0
T₁ = 1
T₂ = 1
T₃ = 0+1+1 = 2
T₄ = 1+1+2 = 4
T₅ = 1+2+4 = 7
T₆ = 2+4+7 = 13
```