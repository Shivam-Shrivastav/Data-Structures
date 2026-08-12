## House Robber
**Problem:** You are a robber planning to rob houses along a street. Each house has money `nums[i]`. Adjacent houses have security systems connected - cannot rob two adjacent houses. Maximize total money.

**Example:**
```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money=2) and house 3 (money=2)
Total = 2 + 2 = 4
```

```
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (7) and house 3 (9) and house 5 (1)
Total = 7 + 9 + 1 = 12
```

---

### DP Intuition
- **Optimal Substructure:** At house i, choose max of:
  - Rob house i: money[i] + best up to i-2
  - Skip house i: best up to i-1
- **State:** `dp[i]` = max money robbing houses 0..i
- **Base:** 
  - dp[0] = nums[0]
  - dp[1] = max(nums[0], nums[1])

---

### 1. Recursive Solution
```python
def rob(nums):
    def dfs(i):
        if i < 0:
            return 0
        return max(dfs(i-1), nums[i] + dfs(i-2))
    
    return dfs(len(nums)-1)
```
**TC:** O(2ⁿ) | **SC:** O(n) recursion stack

---

### 2. Memoization (Top-Down DP)
```python
def rob(nums):
    n = len(nums)
    memo = [-1] * n
    
    def dfs(i):
        if i < 0:
            return 0
        if memo[i] != -1:
            return memo[i]
        memo[i] = max(dfs(i-1), nums[i] + dfs(i-2))
        return memo[i]
    
    return dfs(n-1)
```
**TC:** O(n) | **SC:** O(n)

---

### 3. Tabulation (Bottom-Up DP)
```python
def rob(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i-1], nums[i] + dp[i-2])
    
    return dp[n-1]
```
**TC:** O(n) | **SC:** O(n)

---

### 4. Space Optimized
```python
def rob(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    
    prev2, prev1 = nums[0], max(nums[0], nums[1])
    
    for i in range(2, n):
        curr = max(prev1, nums[i] + prev2)
        prev2, prev1 = prev1, curr
    
    return prev1
```
**TC:** O(n) | **SC:** O(1)

---

**Key Formula:**
```
dp[i] = max(dp[i-1], nums[i] + dp[i-2])
dp[0] = nums[0]
dp[1] = max(nums[0], nums[1])
```

**Example Walkthrough:**
```
nums = [2,7,9,3,1]
dp:
i=0: 2
i=1: max(2,7)=7
i=2: max(7, 9+2)=11
i=3: max(11, 3+7)=11
i=4: max(11, 1+11)=12
Answer = 12
```

**Alternative State Definition:**
Two states at each house:
- `rob[i]` = max money if rob house i
- `skip[i]` = max money if skip house i
```
rob[i] = nums[i] + skip[i-1]
skip[i] = max(rob[i-1], skip[i-1])
```

**Edge Cases:**
- Empty array → 0
- Single house → nums[0]
- Two houses → max(nums[0], nums[1])