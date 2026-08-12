## House Robber II
**Problem:** Same as House Robber but houses are arranged in a **circle**. First and last houses are adjacent.

**Example:**
```
Input: nums = [2,3,2]
Output: 3
Explanation: Cannot rob house 1 (2) and house 3 (2) - adjacent.
Rob only house 2 (3).
```

```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 2 (3) and house 4 (1) = 4
Not house 1 (1) and house 3 (3) = 4 (same but valid).
```

---

### DP Intuition
- **Key Insight:** Circle constraint means we have **two cases**:
  1. Rob houses 0..n-2 (exclude last)
  2. Rob houses 1..n-1 (exclude first)
- **Take max of both cases**
- Use same DP as House Robber for each linear case

---

### 1. Recursive Solution (with helper)
```python
def rob(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    
    def dfs(i, j):
        # Recursive for nums[i..j]
        if i > j:
            return 0
        return max(dfs(i, j-1), nums[j] + dfs(i, j-2))
    
    case1 = dfs(0, n-2)  # Exclude last
    case2 = dfs(1, n-1)  # Exclude first
    return max(case1, case2)
```
**TC:** O(2ⁿ) | **SC:** O(n) recursion stack

---

### 2. Memoization (with helper DP)
```python
def rob(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    
    def rob_linear(arr):
        # Standard House Robber DP
        if len(arr) == 0:
            return 0
        if len(arr) == 1:
            return arr[0]
        
        dp = [0] * len(arr)
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
        
        for i in range(2, len(arr)):
            dp[i] = max(dp[i-1], arr[i] + dp[i-2])
        
        return dp[-1]
    
    case1 = rob_linear(nums[:-1])  # Exclude last
    case2 = rob_linear(nums[1:])   # Exclude first
    return max(case1, case2)
```
**TC:** O(n) | **SC:** O(n)

---

### 3. Space Optimized (O(1) space per case)
```python
def rob(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])
    
    def rob_range(start, end):
        # Rob houses from start to end inclusive
        prev2, prev1 = 0, 0
        for i in range(start, end + 1):
            curr = max(prev1, nums[i] + prev2)
            prev2, prev1 = prev1, curr
        return prev1
    
    # Case 1: Rob houses 0 to n-2
    case1 = rob_range(0, n-2)
    # Case 2: Rob houses 1 to n-1
    case2 = rob_range(1, n-1)
    
    return max(case1, case2)
```
**TC:** O(n) | **SC:** O(1)

---

**Key Insight:**
```
Since first and last are adjacent, we have two possibilities:
1. Include first, exclude last → rob(nums[0..n-2])
2. Exclude first, include last → rob(nums[1..n-1])

Answer = max(case1, case2)
```

**Example Walkthrough:**
```
nums = [2,3,2]

Case 1 (houses 0..1): [2,3] → max(2,3)=3
Case 2 (houses 1..2): [3,2] → max(3,2)=3
Answer = max(3,3)=3
```

**Why Two Cases:**
- In circle, choosing first house blocks last house
- Choosing last house blocks first house
- Can't choose both, so try both scenarios

**Edge Cases:**
- n=0 → 0
- n=1 → nums[0]
- n=2 → max(nums[0], nums[1]) (can only rob one)
- n=3 → max(rob linear for first 2, rob linear for last 2)

**Alternative View:**
Three cases for small n:
- n=1: rob house 0
- n=2: rob max(house 0, house 1)
- n>=3: max(rob(0..n-2), rob(1..n-1))