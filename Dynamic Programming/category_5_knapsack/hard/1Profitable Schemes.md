## 879. Profitable Schemes
**Category:** **KNAPSACK / 0/1 KNAPSACK (MULTI-DIMENSIONAL)**

**Problem:** You have `n` members in a gang and a list of crimes. The i-th crime requires `group[i]` members and generates `profit[i]` profit. A member can only be in one crime. Find the **number of subsets** of crimes that:
1. Use **at most** `n` total members
2. Generate **at least** `minProfit` total profit

Return answer modulo 10⁹+7.

**Example:**
```
Input: n = 5, minProfit = 3, group = [2,2], profit = [2,3]
Output: 2
Explanation: 
- Crime 0: needs 2 people, gives 2 profit
- Crime 1: needs 2 people, gives 3 profit
Valid schemes: {crime1} (profit=3), {crime0,crime1} (profit=5, people=4)
```

```
Input: n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
Output: 7
Explanation: Any non-empty subset works → 2³ - 1 = 7
```

---

### **Relation to Knapsack Problems**
**Similar to:** **0/1 Knapsack** but with **two constraints**:
1. **Weight dimension:** members used ≤ n
2. **Value dimension:** profit earned ≥ minProfit

**How it's different:**
1. **Standard 0/1 Knapsack:** One constraint (weight ≤ capacity), maximize value
2. **Partition Sum:** One constraint (sum = target), boolean
3. **Profitable Schemes:** Two constraints + counting + profit is **lower bound** (≥) not upper bound

**Key Insight:** 
- Classic **multi-dimensional 0/1 knapsack counting problem**
- `dp[people][profit]` = number of ways to use exactly `people` members and earn exactly `profit`
- Profit dimension capped at `minProfit` (any profit ≥ minProfit is treated as minProfit)
- Iterate crimes in outer loop, update backwards to avoid reuse

---

### DP Intuition
- **State:** `dp[p][prof]` = number of schemes using exactly `p` people and earning exactly `prof` profit
- **Transition:**
  ```
  For each crime (g, pr):
      for p from n down to g:
          for prof from minProfit down to 0:
              new_prof = min(prof + pr, minProfit)
              dp[p][new_prof] += dp[p-g][prof]
  ```
- **Base:** `dp[0][0] = 1` (empty scheme)
- **Answer:** Sum of `dp[p][minProfit]` for all p from 0 to n

---

### 1. Recursive Solution
```python
def profitableSchemes(n, minProfit, group, profit):
    m = len(group)
    MOD = 10**9 + 7
    
    def dfs(i, people, prof):
        if i == m:
            return 1 if prof >= minProfit else 0
        
        # Option 1: Skip current crime
        total = dfs(i + 1, people, prof)
        
        # Option 2: Take current crime (if enough people)
        if people + group[i] <= n:
            total += dfs(i + 1, people + group[i], prof + profit[i])
        
        return total % MOD
    
    return dfs(0, 0, 0)
```
**TC:** O(2ᵐ) | **SC:** O(m) recursion stack

---

### 2. Memoization (Top-Down DP)
```python
def profitableSchemes(n, minProfit, group, profit):
    m = len(group)
    MOD = 10**9 + 7
    memo = {}
    
    def dfs(i, people, prof):
        if i == m:
            return 1 if prof >= minProfit else 0
        if (i, people, min(prof, minProfit)) in memo:
            return memo[(i, people, min(prof, minProfit))]
        
        # Skip
        total = dfs(i + 1, people, prof)
        
        # Take
        if people + group[i] <= n:
            total += dfs(i + 1, people + group[i], prof + profit[i])
        
        memo[(i, people, min(prof, minProfit))] = total % MOD
        return total % MOD
    
    return dfs(0, 0, 0)
```
**TC:** O(m × n × minProfit) | **SC:** O(m × n × minProfit)

---

### 3. Tabulation (3D DP)
```python
def profitableSchemes(n, minProfit, group, profit):
    m = len(group)
    MOD = 10**9 + 7
    
    # dp[i][p][prof] = ways using first i crimes, exactly p people, exactly prof profit
    dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(m + 1)]
    dp[0][0][0] = 1
    
    for i in range(1, m + 1):
        g = group[i-1]
        pr = profit[i-1]
        for p in range(n + 1):
            for prof in range(minProfit + 1):
                # Skip current crime
                dp[i][p][prof] = dp[i-1][p][prof]
                
                # Take current crime
                if p >= g:
                    prev_prof = max(0, prof - pr)
                    dp[i][p][prof] = (dp[i][p][prof] + dp[i-1][p-g][prev_prof]) % MOD
    
    # Sum all schemes with profit >= minProfit
    result = 0
    for p in range(n + 1):
        result = (result + dp[m][p][minProfit]) % MOD
    return result
```
**TC:** O(m × n × minProfit) | **SC:** O(m × n × minProfit)

---

### 4. Space Optimized (2D DP) - Optimal
```python
def profitableSchemes(n, minProfit, group, profit):
    MOD = 10**9 + 7
    
    # dp[p][prof] = ways to use exactly p people with exactly prof profit
    dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    for g, pr in zip(group, profit):
        # Iterate backwards to avoid reusing same crime
        for p in range(n, g - 1, -1):
            for prof in range(minProfit, -1, -1):
                new_prof = min(prof + pr, minProfit)
                dp[p][new_prof] = (dp[p][new_prof] + dp[p-g][prof]) % MOD
    
    # Sum all schemes with profit >= minProfit
    result = 0
    for p in range(n + 1):
        result = (result + dp[p][minProfit]) % MOD
    return result
```
**TC:** O(m × n × minProfit) | **SC:** O(n × minProfit)

---

### 5. Alternative: Sum over all profit levels
```python
def profitableSchemes(n, minProfit, group, profit):
    MOD = 10**9 + 7
    
    dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    for g, pr in zip(group, profit):
        for p in range(n, g - 1, -1):
            for prof in range(minProfit, -1, -1):
                new_prof = min(prof + pr, minProfit)
                dp[p][new_prof] = (dp[p][new_prof] + dp[p-g][prof]) % MOD
    
    # Sum all p where profit >= minProfit
    return sum(dp[p][minProfit] for p in range(n + 1)) % MOD
```

---

**Key Formula:**
```
dp[p][prof] += dp[p-g][prof - pr]  (if prof ≥ pr)
dp[p][prof] += dp[p-g][0] + ...? Actually we use capping:
new_prof = min(prof + pr, minProfit)
dp[p][new_prof] += dp[p-g][prof]
```

**Example Walkthrough:**
```
n = 5, minProfit = 3, group = [2,2], profit = [2,3]

Initialize: dp[0][0] = 1

Crime 0 (g=2, pr=2):
  p=5 down to 2:
    prof=3: new_prof = min(3+2,3)=3 → dp[5][3] += dp[3][3]=0
    prof=2: new_prof = min(2+2,3)=3 → dp[4][3] += dp[2][2]=0
    prof=1: new_prof = min(1+2,3)=3 → dp[3][3] += dp[1][1]=0
    prof=0: new_prof = min(0+2,3)=2 → dp[2][2] += dp[0][0]=1
  After crime 0: dp[2][2] = 1

Crime 1 (g=2, pr=3):
  p=5 down to 2:
    prof=3: new_prof = min(3+3,3)=3 → dp[5][3] += dp[3][3]=0
           dp[4][3] += dp[2][3]=0
           dp[3][3] += dp[1][3]=0
           dp[2][3] += dp[0][3]=0
    prof=2: new_prof = min(2+3,3)=3 → dp[4][3] += dp[2][2]=1 → dp[4][3]=1
           dp[3][3] += dp[1][2]=0
           dp[2][3] += dp[0][2]=0
    prof=1: new_prof = min(1+3,3)=3 → dp[3][3] += dp[1][1]=0
    prof=0: new_prof = min(0+3,3)=3 → dp[2][3] += dp[0][0]=1 → dp[2][3]=1

Final dp[][3]:
p=0:0, p=1:0, p=2:1, p=3:0, p=4:1, p=5:0
Sum = 2
```

**Comparison Table:**

| Aspect | 0/1 Knapsack | Partition Sum | Profitable Schemes |
|--------|--------------|---------------|-------------------|
**Constraints** | Weight ≤ capacity | Sum = target | Members ≤ n, Profit ≥ minProfit |
**Dimensions** | 1 (weight) | 1 (sum) | 2 (people, profit) |
**Profit handling** | Maximize | Exact match | Lower bound (cap at minProfit) |
**DP direction** | Backward | Backward | Backward (both dims) |
**Result** | Max value | Boolean | Count modulo |

**Multi-dimensional Knapsack Family:**

| Problem | Dimensions | Type |
|---------|-----------|------|
**0/1 Knapsack** | 1D (weight) | Maximize value |
**Partition Sum** | 1D (sum) | Existence |
**Target Sum** | 1D (sum) | Count assignments |
**Profitable Schemes** | 2D (people, profit) | Count subsets |
**Ones and Zeroes** | 2D (zeros, ones) | Max subset size |

**Edge Cases:**
- minProfit = 0 → Empty scheme counts (return 1 initially plus others)
- n = 0 → Only empty scheme if minProfit=0 else 0
- No crimes → 1 if minProfit=0 else 0

**Why Profit Capping Works:**
- Once profit ≥ minProfit, exact value doesn't matter for final count
- Capping reduces state space from O(sum(profit)) to O(minProfit)
- Any profit ≥ minProfit maps to minProfit index

**Why Backward Iteration:**
- Ensures each crime used at most once
- When updating dp[p][prof], we use dp[p-g][prof] from **previous crimes only**
- Forward iteration would allow reusing same crime multiple times