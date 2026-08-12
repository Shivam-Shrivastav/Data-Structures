## 474. Ones and Zeroes
**Category:** **KNAPSACK / 0/1 KNAPSACK (MULTI-DIMENSIONAL)**

**Problem:** You are given an array of binary strings `strs` and two integers `m` and `n`. Return the size of the largest subset of `strs` such that the subset has **at most** `m` 0's and **at most** `n` 1's.

**Example:**
```
Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: Largest subset with at most 5 0's and 3 1's:
{"10", "0001", "1", "0"} → 0's: 1+3+0+1=5, 1's: 1+1+1+0=3
```

```
Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: {"10", "0"} → 0's: 1+1=2 > m? Wait no
Actually {"10", "1"} → 0's:1, 1's:2 > n? Let's check:
{"0", "1"} → 0's:1, 1's:1 → valid, size=2
```

---

### **Relation to Knapsack Problems**
**Similar to:** **Profitable Schemes** but with **two resource constraints**
**How it's different:**
1. **Profitable Schemes:** People (count) + Profit (value)
2. **Ones and Zeroes:** Zeros count + Ones count (both resources)
3. **Objective:** Maximize number of strings (not profit)

**Key Insight:** 
- Classic **2D 0/1 knapsack** where each item consumes two resources
- `dp[zeros][ones]` = max strings we can pick using exactly `zeros` zeros and `ones` ones
- For each string, we can take it or skip it
- Must iterate backwards on both dimensions

---

### DP Intuition
- **State:** `dp[z][o]` = maximum number of strings using exactly `z` zeros and `o` ones
- **Transition:**
  ```
  For each string with count0 zeros and count1 ones:
      for z from m down to count0:
          for o from n down to count1:
              dp[z][o] = max(dp[z][o], 1 + dp[z-count0][o-count1])
  ```
- **Base:** `dp[0][0] = 0` (empty subset)
- **Answer:** `max(dp[z][o] for z in 0..m, o in 0..n)`

---

### 1. Recursive Solution
```python
def findMaxForm(strs, m, n):
    # Precompute zeros and ones for each string
    counts = [(s.count('0'), s.count('1')) for s in strs]
    length = len(strs)
    
    def dfs(i, zeros_left, ones_left):
        if i == length:
            return 0
        
        # Skip current string
        max_len = dfs(i + 1, zeros_left, ones_left)
        
        # Take current string if possible
        z, o = counts[i]
        if zeros_left >= z and ones_left >= o:
            max_len = max(max_len, 1 + dfs(i + 1, zeros_left - z, ones_left - o))
        
        return max_len
    
    return dfs(0, m, n)
```
**TC:** O(2ˡᵉⁿᵍᵗʰ) | **SC:** O(length) recursion stack

---

### 2. Memoization (Top-Down DP)
```python
def findMaxForm(strs, m, n):
    counts = [(s.count('0'), s.count('1')) for s in strs]
    length = len(strs)
    memo = {}
    
    def dfs(i, zeros_left, ones_left):
        if i == length:
            return 0
        if (i, zeros_left, ones_left) in memo:
            return memo[(i, zeros_left, ones_left)]
        
        # Skip
        max_len = dfs(i + 1, zeros_left, ones_left)
        
        # Take
        z, o = counts[i]
        if zeros_left >= z and ones_left >= o:
            max_len = max(max_len, 1 + dfs(i + 1, zeros_left - z, ones_left - o))
        
        memo[(i, zeros_left, ones_left)] = max_len
        return max_len
    
    return dfs(0, m, n)
```
**TC:** O(length × m × n) | **SC:** O(length × m × n)

---

### 3. Tabulation (3D DP)
```python
def findMaxForm(strs, m, n):
    counts = [(s.count('0'), s.count('1')) for s in strs]
    length = len(strs)
    
    # dp[i][z][o] = max strings using first i strings, exactly z zeros, o ones
    dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(length + 1)]
    
    for i in range(1, length + 1):
        z, o = counts[i-1]
        for zeros in range(m + 1):
            for ones in range(n + 1):
                # Skip current string
                dp[i][zeros][ones] = dp[i-1][zeros][ones]
                
                # Take current string if possible
                if zeros >= z and ones >= o:
                    dp[i][zeros][ones] = max(dp[i][zeros][ones], 
                                             1 + dp[i-1][zeros - z][ones - o])
    
    return dp[length][m][n]
```
**TC:** O(length × m × n) | **SC:** O(length × m × n)

---

### 4. Space Optimized (2D DP) - Optimal
```python
def findMaxForm(strs, m, n):
    # dp[z][o] = max strings using exactly z zeros and o ones
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for s in strs:
        zeros = s.count('0')
        ones = len(s) - zeros
        
        # Iterate backwards to avoid reusing same string
        for z in range(m, zeros - 1, -1):
            for o in range(n, ones - 1, -1):
                dp[z][o] = max(dp[z][o], 1 + dp[z - zeros][o - ones])
    
    return dp[m][n]
```
**TC:** O(length × m × n) | **SC:** O(m × n)

---

### 5. Alternative: Using coordinate compression
```python
def findMaxForm(strs, m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for s in strs:
        zeros = s.count('0')
        ones = len(s) - zeros
        
        # Update in reverse
        for i in range(m, zeros - 1, -1):
            for j in range(n, ones - 1, -1):
                dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
    
    return dp[m][n]
```

---

**Key Formula:**
```
dp[z][o] = max(dp[z][o], 1 + dp[z - zeros][o - ones])
for z from m down to zeros, o from n down to ones
```

**Example Walkthrough:**
```
strs = ["10", "0001", "111001", "1", "0"], m=5, n=3

Initialize: dp[0..5][0..3] = 0

String "10": zeros=1, ones=1
  z=5..1, o=3..1:
    dp[5][3] = max(0, 1+dp[4][2]=0) = 0
    dp[5][2] = max(0, 1+dp[4][1]=0) = 0
    ...
    dp[1][1] = max(0, 1+dp[0][0]=1) = 1

String "0001": zeros=3, ones=1
  z=5..3, o=3..1:
    dp[5][3] = max(0, 1+dp[2][2]=0) = 0
    dp[5][2] = max(0, 1+dp[2][1]=0) = 0
    dp[4][3] = max(0, 1+dp[1][2]=0) = 0
    dp[4][2] = max(0, 1+dp[1][1]=1) = 1
    dp[3][3] = max(0, 1+dp[0][2]=0) = 0
    dp[3][2] = max(0, 1+dp[0][1]=0) = 0
    dp[3][1] = max(0, 1+dp[0][0]=1) = 1

Continue processing all strings...

Final dp[5][3] will be maximum size achievable
```

**Comparison Table:**

| Aspect | Profitable Schemes | Ones and Zeroes |
|--------|-------------------|-----------------|
**Constraints** | People ≤ n, Profit ≥ minProfit | Zeros ≤ m, Ones ≤ n |
**Resources** | 2 (people count, profit) | 2 (zeros count, ones count) |
**Objective** | Count subsets | Maximize subset size |
**DP Operation** | Add counts | Max size |
**Profit handling** | Cap at minProfit | No capping needed |
**Answer** | Sum of dp[p][minProfit] | dp[m][n] |

**Multi-dimensional Knapsack Family:**

| Problem | Resources | Objective |
|---------|-----------|-----------|
**0/1 Knapsack** | Weight | Max value |
**Profitable Schemes** | People, Profit (≥) | Count subsets |
**Ones and Zeroes** | Zeros, Ones (≤) | Max subset size |
**Shopping Offers** | Multiple items | Min cost |

**Edge Cases:**
- m = 0, n = 0 → 0 (can't pick any string with non-zero zeros/ones)
- All strings empty → length of strs (if m,n ≥ 0)
- Single string → 1 if fits, else 0

**Why Backward Iteration:**
```
Forward: dp[z][o] would use dp[z-zeros][o-ones] that might have already 
         included the current string (multiple uses)
Backward: Ensures each string used at most once
```

**Time Complexity Analysis:**
- O(length × m × n) is typical
- For m=n=100, length=200 → ~2 million operations (feasible)
- Can't optimize further due to 2D nature

**Space-Time Tradeoff:**
- 3D DP: O(length × m × n) space (too large for typical constraints)
- 2D DP: O(m × n) space (optimal)
- 2D with backward iteration is standard solution