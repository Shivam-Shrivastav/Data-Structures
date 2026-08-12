## Maximum Subarray (Kadane's Algorithm)
**Category:** **SUBARRAY DP** (contiguous elements)

**Problem:** Find contiguous subarray with largest sum in given integer array.

**Example:**
```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has sum = 6
```

```
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: [5,4,-1,7,8] has sum = 23
```

---

### **DP Intuition**
- **State:** `dp[i]` = maximum subarray sum **ending at index i**
- **Transition:** Either extend previous subarray or start new subarray at i
  `dp[i] = max(nums[i], dp[i-1] + nums[i])`
- **Answer:** `max(dp[0..n-1])`

**Key Insight:** Subarray must be contiguous, so each position either:
1. Starts a new subarray: `nums[i]`
2. Extends previous subarray: `dp[i-1] + nums[i]`

---

### 1. Recursive Solution
```python
def maxSubArray(nums):
    n = len(nums)
    
    def dfs(i):
        if i == 0:
            return nums[0]
        
        # Max sum ending at i
        prev_sum = dfs(i-1)
        curr_sum = max(nums[i], prev_sum + nums[i])
        return curr_sum
    
    # Need to track global max during recursion
    global_max = float('-inf')
    for i in range(n):
        global_max = max(global_max, dfs(i))
    return global_max
```
**TC:** O(n²) | **SC:** O(n) recursion stack (overlapping subproblems not reused)

---

### 2. Memoization
```python
def maxSubArray(nums):
    n = len(nums)
    memo = [-float('inf')] * n
    
    def dfs(i):
        if i == 0:
            memo[i] = nums[0]
            return nums[0]
        if memo[i] != -float('inf'):
            return memo[i]
        
        prev_sum = dfs(i-1)
        memo[i] = max(nums[i], prev_sum + nums[i])
        return memo[i]
    
    # Compute all ending positions
    for i in range(n):
        dfs(i)
    
    return max(memo)
```
**TC:** O(n) | **SC:** O(n)

---

### 3. Tabulation (Kadane's Algorithm)
```python
def maxSubArray(nums):
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    
    for i in range(1, n):
        dp[i] = max(nums[i], dp[i-1] + nums[i])
    
    return max(dp)
```
**TC:** O(n) | **SC:** O(n)

---

### 4. Space Optimized (Classic Kadane's)
```python
def maxSubArray(nums):
    curr_sum = nums[0]
    max_sum = nums[0]
    
    for i in range(1, len(nums)):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(max_sum, curr_sum)
    
    return max_sum
```
**TC:** O(n) | **SC:** O(1)

---

### 5. Return Subarray Indices
```python
def maxSubArray(nums):
    curr_sum = nums[0]
    max_sum = nums[0]
    start = end = 0
    temp_start = 0
    
    for i in range(1, len(nums)):
        if nums[i] > curr_sum + nums[i]:
            curr_sum = nums[i]
            temp_start = i
        else:
            curr_sum = curr_sum + nums[i]
        
        if curr_sum > max_sum:
            max_sum = curr_sum
            start = temp_start
            end = i
    
    return max_sum, nums[start:end+1]
```

---

**Key Formula:**
```
dp[i] = max(nums[i], dp[i-1] + nums[i])
dp[0] = nums[0]
Answer = max(dp[0], dp[1], ..., dp[n-1])
```

**Example Walkthrough:**
```
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
dp:
i=0: -2
i=1: max(1, -2+1=-1) = 1
i=2: max(-3, 1-3=-2) = -2
i=3: max(4, -2+4=2) = 4
i=4: max(-1, 4-1=3) = 3
i=5: max(2, 3+2=5) = 5
i=6: max(1, 5+1=6) = 6
i=7: max(-5, 6-5=1) = 1
i=8: max(4, 1+4=5) = 5
max(dp) = 6 at i=6
```

**Variations of Subarray DP:**

| Variation | Key Difference | Solution |
|-----------|---------------|----------|
| **Maximum Subarray** | Any subarray | Kadane's |
| **Maximum Subarray with at least k elements** | Length constraint | Sliding window + prefix sums |
| **Maximum Product Subarray** | Product instead of sum | Track min/max |
| **Circular Subarray** | Wrap around | max(Kadane, total - min subarray) |
| **Maximum Subarray Sum with one deletion** | Can delete one element | DP with 2 states |

**Edge Cases:**
- All negative → largest single element
- Single element → that element
- All positive → entire array

**Why Kadane's Works:**
- If previous sum is negative, it will only reduce current sum
- Better to start fresh at current element
- Greedy + DP combined