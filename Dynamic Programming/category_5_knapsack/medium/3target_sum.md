## 494. Target Sum
**Category:** **KNAPSACK / 0/1 KNAPSACK (COUNTING)**

**Problem:** Given integer array `nums` and target sum `target`, assign `+` or `-` to each number to make sum equal to target. Return number of different ways.

**Example:**
```
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: 
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
```

```
Input: nums = [1], target = 1
Output: 1
Explanation: +1 = 1
```

---

### **Relation to Knapsack Problems**
**Similar to:** **Partition Equal Subset Sum** but with **target** and **counting**
**How it transforms:**
1. Let sum of all numbers = `total`
2. If we assign `+` to some subset P and `-` to others N:
   ```
   sum(P) - sum(N) = target
   sum(P) - (total - sum(P)) = target
   2 * sum(P) = target + total
   sum(P) = (target + total) / 2
   ```
3. Problem reduces to: Count subsets with sum = `(target + total) // 2`

**Difference from Partition Sum:**
- **Partition:** Find if subset exists with sum = total/2
- **Target Sum:** Count subsets with sum = S (derived from target)

**Key Insight:** 
- Must be integer: `(target + total)` must be even
- Absolute target ≤ total (otherwise impossible)
- Then it's exactly **count subsets with given sum**

---

### DP Intuition
- **State:** `dp[s]` = number of ways to achieve sum `s`
- **Transition:**
  ```
  For each num in nums:
      for s from target_sum down to num:
          dp[s] += dp[s - num]
  ```
- **Base:** `dp[0] = 1` (empty subset)
- **Target sum to find:** `S = (target + total) // 2`
- **Answer:** `dp[S]` if valid, else 0

---

### 1. Recursive Solution
```python
def findTargetSumWays(nums, target):
    n = len(nums)
    
    def dfs(i, curr_sum):
        if i == n:
            return 1 if curr_sum == target else 0
        
        # Add + or - to current number
        add_plus = dfs(i + 1, curr_sum + nums[i])
        add_minus = dfs(i + 1, curr_sum - nums[i])
        
        return add_plus + add_minus
    
    return dfs(0, 0)
```
**TC:** O(2ⁿ) | **SC:** O(n) recursion stack

---

### 2. Memoization (Top-Down DP)
```python
def findTargetSumWays(nums, target):
    n = len(nums)
    memo = {}
    
    def dfs(i, curr_sum):
        if i == n:
            return 1 if curr_sum == target else 0
        if (i, curr_sum) in memo:
            return memo[(i, curr_sum)]
        
        add_plus = dfs(i + 1, curr_sum + nums[i])
        add_minus = dfs(i + 1, curr_sum - nums[i])
        
        memo[(i, curr_sum)] = add_plus + add_minus
        return add_plus + add_minus
    
    return dfs(0, 0)
```
**TC:** O(n × range) | **SC:** O(n × range) where range = 2*total+1

---

### 3. 2D Tabulation
```python
def findTargetSumWays(nums, target):
    total = sum(nums)
    
    # Range of possible sums: -total to total
    offset = total  # to handle negative indices
    dp = [[0] * (2*total + 1) for _ in range(len(nums) + 1)]
    dp[0][offset] = 1  # sum 0 at start
    
    for i in range(len(nums)):
        for s in range(-total, total + 1):
            if dp[i][s + offset] > 0:
                # Add +nums[i]
                dp[i+1][s + nums[i] + offset] += dp[i][s + offset]
                # Add -nums[i]
                dp[i+1][s - nums[i] + offset] += dp[i][s + offset]
    
    return dp[len(nums)][target + offset] if abs(target) <= total else 0
```
**TC:** O(n × total) | **SC:** O(n × total)

---

### 4. Space Optimized 2-row DP
```python
def findTargetSumWays(nums, target):
    total = sum(nums)
    if abs(target) > total:
        return 0
    
    offset = total
    dp = [0] * (2*total + 1)
    dp[offset] = 1
    
    for num in nums:
        next_dp = [0] * (2*total + 1)
        for s in range(-total, total + 1):
            if dp[s + offset] > 0:
                next_dp[s + num + offset] += dp[s + offset]
                next_dp[s - num + offset] += dp[s + offset]
        dp = next_dp
    
    return dp[target + offset]
```
**TC:** O(n × total) | **SC:** O(total)

---

### 5. Subset Sum Transformation (Optimal)
```python
def findTargetSumWays(nums, target):
    total = sum(nums)
    
    # Check if valid transformation exists
    if (target + total) % 2 != 0 or abs(target) > total:
        return 0
    
    subset_sum = (target + total) // 2
    
    # Count subsets with sum = subset_sum
    dp = [0] * (subset_sum + 1)
    dp[0] = 1
    
    for num in nums:
        for s in range(subset_sum, num - 1, -1):
            dp[s] += dp[s - num]
    
    return dp[subset_sum]
```
**TC:** O(n × subset_sum) | **SC:** O(subset_sum)

---

**Key Transformation:**
```
Let P = set of numbers with + sign
Let N = set with - sign

sum(P) - sum(N) = target
sum(P) - (total - sum(P)) = target
2*sum(P) = target + total
sum(P) = (target + total) / 2

Problem becomes: Count subsets with sum = (target + total)/2
```

**Example Walkthrough (Subset Sum Method):**
```
nums = [1,1,1,1,1], target = 3
total = 5
(target + total) = 8, /2 = 4

Need subsets with sum = 4

dp[0] = 1

num=1:
  s=4 down to 1: dp[4]+=dp[3]=0 → 0
                 dp[3]+=dp[2]=0 → 0
                 dp[2]+=dp[1]=0 → 0
                 dp[1]+=dp[0]=1 → 1
dp = [1,1,0,0,0]

num=1:
  s=4: dp[4]+=dp[3]=0 → 0
  s=3: dp[3]+=dp[2]=0 → 0
  s=2: dp[2]+=dp[1]=1 → 1
  s=1: dp[1]+=dp[0]=1+1=2 → 2
dp = [1,2,1,0,0]

num=1:
  s=4: dp[4]+=dp[3]=0 → 0
  s=3: dp[3]+=dp[2]=1 → 1
  s=2: dp[2]+=dp[1]=2 → 3
  s=1: dp[1]+=dp[0]=2+1=3 → 3
dp = [1,3,3,1,0]

num=1:
  s=4: dp[4]+=dp[3]=1 → 1
  s=3: dp[3]+=dp[2]=3 → 4
  s=2: dp[2]+=dp[1]=3 → 6
  s=1: dp[1]+=dp[0]=3+1=4 → 4
dp = [1,4,6,4,1]

num=1:
  s=4: dp[4]+=dp[3]=4 → 5
  s=3: dp[3]+=dp[2]=6 → 10
  s=2: dp[2]+=dp[1]=4 → 10
  s=1: dp[1]+=dp[0]=4+1=5 → 5
dp = [1,5,10,10,5]

dp[4] = 5 → Answer = 5
```

**Example Walkthrough (2D State Machine):**
```
nums = [1,1,1], target = 1
total = 3, offset = 3

Initialize: dp[0][3] = 1 (sum 0 at start)

i=0, num=1:
  from sum 0: +1 → sum 1, -1 → sum -1
  dp[1][4] += 1, dp[1][2] += 1

i=1, num=1:
  from sum 1: +1 → sum 2, -1 → sum 0
  from sum -1: +1 → sum 0, -1 → sum -2
  dp[2][5] += 1, dp[2][3] += 2, dp[2][1] += 1

i=2, num=1:
  from sums: track counts...
Final: dp[3][4] (target=1 + offset=3 = 4) = 3
```

**Comparison Table:**

| Aspect | Partition Sum | Target Sum |
|--------|--------------|------------|
**Problem** | Can we split equally? | How many +/- assignments? |
**Transformation** | target = total/2 | target = (target+total)/2 |
**DP Type** | Existence (boolean) | Counting (integer) |
**Operation** | `dp[s] = dp[s] or dp[s-num]` | `dp[s] += dp[s-num]` |
**Base** | `dp[0] = True` | `dp[0] = 1` |
**Return** | Boolean | Integer count |

**Knapsack Counting Family:**

| Problem | Type | DP Formula |
|---------|------|------------|
**Coin Change II** | Unbounded combinations | `dp[a] += dp[a-coin]` (coins outer) |
**Target Sum** | 0/1 assignments | `dp[s] += dp[s-num]` (subset sum transform) |
**Combination Sum IV** | Permutations | `dp[a] += dp[a-coin]` (amount outer) |

**Edge Cases:**
- Empty array → 1 if target=0 else 0
- target > total → 0
- (target + total) odd → 0
- target = 0 with all zeros → 2ⁿ ways? Actually careful with zeros

**Handling Zeros:**
```
If nums contains zeros, each zero can be +0 or -0 (both same)
For k zeros, they contribute 2^k factor
Subset sum method with zeros needs special handling
```

**Why Subset Sum Transformation Works:**
- Reduces 2ⁿ possibilities to knapsack counting
- Much faster: O(n × subset_sum) vs O(2ⁿ)
- Works because each number must be either + or -
- The transformation is mathematical equivalence