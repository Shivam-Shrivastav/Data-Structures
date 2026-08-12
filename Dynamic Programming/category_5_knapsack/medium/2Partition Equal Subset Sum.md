## 416. Partition Equal Subset Sum
**Category:** **KNAPSACK / 0/1 KNAPSACK**

**Problem:** Given an integer array `nums`, return `true` if you can partition the array into two subsets with **equal sum**.

**Example:**
```
Input: nums = [1,5,11,5]
Output: true
Explanation: [1,5,5] and [11] both sum to 11
```

```
Input: nums = [1,2,3,5]
Output: false
Explanation: Can't split into two equal sum subsets
```

---

### **Relation to Knapsack Problems**
**Similar to:** **0/1 Knapsack** (each item used at most once)
**How it transforms:**
1. Calculate total sum = `sum(nums)`
2. If total sum is odd → impossible (`false`)
3. Target = `total_sum // 2`
4. Problem reduces to: Can we find subset that sums to `target`?

**Difference from Coin Change:**
- **Coin Change:** Unbounded items, counting/minimizing
- **Partition Sum:** 0/1 items, boolean (can/can't achieve sum)

**Key Insight:** 
- We need to check if there exists a subset with sum = target
- Classic subset sum problem
- Each number can be used at most once

---

### DP Intuition
- **State:** `dp[s]` = whether we can achieve sum `s` using some subset
- **Transition:**
  ```
  For each num in nums:
      for s from target down to num:
          dp[s] = dp[s] OR dp[s - num]
  ```
- **Base:** `dp[0] = true` (empty subset sums to 0)
- **Answer:** `dp[target]`

---

### 1. Recursive Solution
```python
def canPartition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    
    target = total // 2
    
    def dfs(i, remaining):
        if remaining == 0:
            return True
        if i >= len(nums) or remaining < 0:
            return False
        
        # Include or exclude current number
        include = dfs(i + 1, remaining - nums[i])
        exclude = dfs(i + 1, remaining)
        
        return include or exclude
    
    return dfs(0, target)
```
**TC:** O(2ⁿ) | **SC:** O(n) recursion stack

---

### 2. Memoization (Top-Down DP)
```python
def canPartition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    
    target = total // 2
    memo = {}
    
    def dfs(i, remaining):
        if remaining == 0:
            return True
        if i >= len(nums) or remaining < 0:
            return False
        if (i, remaining) in memo:
            return memo[(i, remaining)]
        
        include = dfs(i + 1, remaining - nums[i])
        exclude = dfs(i + 1, remaining)
        
        memo[(i, remaining)] = include or exclude
        return include or exclude
    
    return dfs(0, target)
```
**TC:** O(n × target) | **SC:** O(n × target)

---

### 3. Tabulation (2D DP)
```python
def canPartition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    
    target = total // 2
    n = len(nums)
    
    # dp[i][s] = can we achieve sum s using first i numbers
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    
    # Base: sum 0 always achievable
    for i in range(n + 1):
        dp[i][0] = True
    
    for i in range(1, n + 1):
        for s in range(1, target + 1):
            # Don't include current number
            dp[i][s] = dp[i-1][s]
            
            # Include current number if possible
            if s >= nums[i-1]:
                dp[i][s] = dp[i][s] or dp[i-1][s - nums[i-1]]
    
    return dp[n][target]
```
**TC:** O(n × target) | **SC:** O(n × target)

---

### 4. Space Optimized (1D DP)
```python
def canPartition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in nums:
        # Iterate backwards to avoid reusing the same number multiple times
        for s in range(target, num - 1, -1):
            if dp[s - num]:
                dp[s] = True
    
    return dp[target]
```
**TC:** O(n × target) | **SC:** O(target)

---

### 5. Bitmask Optimization
```python
def canPartition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    
    target = total // 2
    bits = 1  # bitmask representing achievable sums
    
    for num in nums:
        bits |= bits << num
    
    # Check if target bit is set
    return (bits >> target) & 1 == 1
```
**TC:** O(n × target) but faster in practice | **SC:** O(target) in bits

---

**Key Formula:**
```
dp[s] = dp[s] OR dp[s - num]  for s from target down to num
dp[0] = True
Answer = dp[target]
```

**Example Walkthrough:**
```
nums = [1,5,11,5], total = 22, target = 11

Initialize: dp = [T, F, F, F, F, F, F, F, F, F, F, F] (indices 0-11)

num = 1:
  s=11 down to 1: dp[11] |= dp[10] (F) → F
                 dp[10] |= dp[9] (F) → F
                 ...
                 dp[1] |= dp[0] (T) → T
  dp after: [T, T, F, F, F, F, F, F, F, F, F, F]

num = 5:
  s=11: dp[11] |= dp[6] (F) → F
  s=10: dp[10] |= dp[5] (F) → F
  s=9: dp[9] |= dp[4] (F) → F
  s=8: dp[8] |= dp[3] (F) → F
  s=7: dp[7] |= dp[2] (F) → F
  s=6: dp[6] |= dp[1] (T) → T
  s=5: dp[5] |= dp[0] (T) → T
  dp after: [T, T, F, F, T, T, T, F, F, F, F, F]

num = 11:
  s=11: dp[11] |= dp[0] (T) → T
  dp after: [T, T, F, F, T, T, T, F, F, F, F, T]

num = 5:
  s=11: dp[11] |= dp[6] (T) → T (already T)
  s=10: dp[10] |= dp[5] (T) → T
  s=9: dp[9] |= dp[4] (T) → T
  s=8: dp[8] |= dp[3] (F) → F
  s=7: dp[7] |= dp[2] (F) → F
  s=6: dp[6] |= dp[1] (T) → T (already T)
  s=5: dp[5] |= dp[0] (T) → T (already T)

Final dp[11] = True → can partition
```

**Comparison Table:**

| Aspect | Coin Change (Unbounded) | Partition Sum (0/1) |
|--------|------------------------|---------------------|
**Item usage** | Unlimited | At most once |
**DP direction** | Forward (coin outer) | Backward (num outer) |
**Operation** | `dp[a] += dp[a-coin]` | `dp[s] = dp[s] or dp[s-num]` |
**Initialization** | `dp[0]=1` | `dp[0]=True` |
**Return type** | Integer (count) | Boolean |

**0/1 Knapsack Family:**

| Problem | Type | DP Formula |
|---------|------|------------|
**Partition Equal Subset Sum** | Subset sum existence | `dp[s] = dp[s] or dp[s-num]` |
**Target Sum** | +/- assignment count | `dp[s] += dp[s-num]` |
**Last Stone Weight II** | Minimize difference | Similar to partition |
**Subset Sum** | Existence for given sum | Same as above |

**Edge Cases:**
- Single element → false (can't partition single element)
- Empty array → true? (empty can be partitioned)
- total sum odd → false
- target = 0 → true (empty subset)

**Why Backwards Iteration:**
```
Forward iteration would reuse same number multiple times:
dp[s] = dp[s] or dp[s-num] using updated dp[s-num] from same num

Backwards ensures we only consider each number once:
When updating dp[11] with num=5, dp[6] is from previous numbers only
```

**Bitmask Explanation:**
- Each bit position `s` represents whether sum `s` is achievable
- `bits << num` shifts all achievable sums by `num`
- OR combines original sums with new sums after adding `num`
- After processing all numbers, check if target bit is set

**Space-Time Tradeoff:**
- 1D DP: O(n × target) time, O(target) space
- Bitmask: Same time complexity but faster bitwise operations
- Both work for target up to ~10^4