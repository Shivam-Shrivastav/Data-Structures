## Maximum Product Subarray
**Category:** **SUBARRAY DP / KADANE'S VARIANT**

**Problem:** Find contiguous subarray with largest product in integer array (can contain negative numbers and zeros).

**Example:**
```
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has product = 6
```

```
Input: nums = [-2,0,-1]
Output: 0
Explanation: Can't get positive product, max is 0
```

```
Input: nums = [-2,3,-4]
Output: 24
Explanation: [-2,3,-4] product = 24
```

---

### **Relation to Maximum Subarray**
**Similar to:** **Kadane's Algorithm** but with product instead of sum
**How it's different:**
1. **Negative × Negative = Positive** - can't just drop negative prefixes
2. Need to track **both max and min** product ending at i
3. Min product becomes max when multiplied by negative number

**Key Insight:** 
- When current number is **negative**, swap max and min
- Zero resets the subarray

---

### DP Intuition
- **State:**
  - `max_prod[i]` = max product subarray **ending at i**
  - `min_prod[i]` = min product subarray **ending at i** (most negative)
- **Transition:**
  ```
  max_prod[i] = max(nums[i], max_prod[i-1]*nums[i], min_prod[i-1]*nums[i])
  min_prod[i] = min(nums[i], max_prod[i-1]*nums[i], min_prod[i-1]*nums[i])
  ```
- **Answer:** `max(max_prod[0..n-1])`

---

### 1. Recursive Solution
```python
def maxProduct(nums):
    n = len(nums)
    
    def dfs(i):
        if i == 0:
            return nums[0], nums[0]  # (max_prod, min_prod)
        
        prev_max, prev_min = dfs(i-1)
        
        curr_max = max(nums[i], prev_max * nums[i], prev_min * nums[i])
        curr_min = min(nums[i], prev_max * nums[i], prev_min * nums[i])
        
        return curr_max, curr_min
    
    # Need to track global max
    global_max = float('-inf')
    for i in range(n):
        curr_max, _ = dfs(i)
        global_max = max(global_max, curr_max)
    
    return global_max
```
**TC:** O(n²) | **SC:** O(n) recursion stack (overlapping not reused)

---

### 2. Memoization
```python
def maxProduct(nums):
    n = len(nums)
    memo_max = [None] * n
    memo_min = [None] * n
    
    def dfs(i):
        if i == 0:
            memo_max[i] = nums[0]
            memo_min[i] = nums[0]
            return nums[0], nums[0]
        
        if memo_max[i] is not None:
            return memo_max[i], memo_min[i]
        
        prev_max, prev_min = dfs(i-1)
        
        memo_max[i] = max(nums[i], prev_max * nums[i], prev_min * nums[i])
        memo_min[i] = min(nums[i], prev_max * nums[i], prev_min * nums[i])
        
        return memo_max[i], memo_min[i]
    
    # Compute all
    for i in range(n):
        dfs(i)
    
    return max(memo_max)
```
**TC:** O(n) | **SC:** O(n)

---

### 3. Tabulation (DP Array)
```python
def maxProduct(nums):
    n = len(nums)
    
    max_dp = [0] * n
    min_dp = [0] * n
    
    max_dp[0] = nums[0]
    min_dp[0] = nums[0]
    result = nums[0]
    
    for i in range(1, n):
        max_dp[i] = max(nums[i], max_dp[i-1] * nums[i], min_dp[i-1] * nums[i])
        min_dp[i] = min(nums[i], max_dp[i-1] * nums[i], min_dp[i-1] * nums[i])
        result = max(result, max_dp[i])
    
    return result
```
**TC:** O(n) | **SC:** O(n)

---

### 4. Space Optimized (Classic Solution)
```python
def maxProduct(nums):
    if not nums:
        return 0
    
    max_prod = nums[0]
    min_prod = nums[0]
    result = nums[0]
    
    for i in range(1, len(nums)):
        # If current number is negative, swap max and min
        if nums[i] < 0:
            max_prod, min_prod = min_prod, max_prod
        
        max_prod = max(nums[i], max_prod * nums[i])
        min_prod = min(nums[i], min_prod * nums[i])
        
        result = max(result, max_prod)
    
    return result
```
**TC:** O(n) | **SC:** O(1)

---

### 5. Alternative: Two-Pass (No Swap)
```python
def maxProduct(nums):
    # Forward pass
    curr = 1
    max_forward = float('-inf')
    for num in nums:
        curr *= num
        max_forward = max(max_forward, curr)
        if curr == 0:
            curr = 1
    
    # Backward pass
    curr = 1
    max_backward = float('-inf')
    for num in reversed(nums):
        curr *= num
        max_backward = max(max_backward, curr)
        if curr == 0:
            curr = 1
    
    return max(max_forward, max_backward)
```
**TC:** O(n) | **SC:** O(1)

---

**Key Formula:**
```
max_prod[i] = max(nums[i], max_prod[i-1]*nums[i], min_prod[i-1]*nums[i])
min_prod[i] = min(nums[i], max_prod[i-1]*nums[i], min_prod[i-1]*nums[i])
```

**Example Walkthrough:**
```
nums = [2,3,-2,4]

i=0: max=2, min=2, result=2
i=1: 
    max = max(3, 2*3=6, 2*3=6) = 6
    min = min(3, 2*3=6, 2*3=6) = 3
    result = max(2,6)=6
i=2: num=-2 (negative)
    max = max(-2, 6*-2=-12, 3*-2=-6) = -2
    min = min(-2, 6*-2=-12, 3*-2=-6) = -12
    result = max(6,-2)=6
i=3:
    max = max(4, -2*4=-8, -12*4=-48) = 4
    min = min(4, -2*4=-8, -12*4=-48) = -48
    result = max(6,4)=6
Answer = 6
```

```
nums = [-2,3,-4]

i=0: max=-2, min=-2, result=-2
i=1: num=3
    max = max(3, -2*3=-6, -2*3=-6) = 3
    min = min(3, -2*3=-6, -2*3=-6) = -6
    result = max(-2,3)=3
i=2: num=-4 (negative)
    swap max=3, min=-6
    max = max(-4, -6*-4=24, 3*-4=-12) = 24
    min = min(-4, -6*-4=24, 3*-4=-12) = -12
    result = max(3,24)=24
Answer = 24
```

**Comparison Table:**

| Aspect | Maximum Subarray (Sum) | Maximum Product Subarray |
|--------|----------------------|------------------------|
**DP State** | Single value (max) | Two values (max, min) |
**Effect of negative** | Just ignore | Can flip max↔min |
**Effect of zero** | Reset to 0 | Reset product to 0 |
**Transition** | `max(nums[i], prev+nums[i])` | `max/min of 3 choices` |
**Space** | O(1) | O(1) |
**Intuition** | Drop negative prefix | Keep negative for later |

**Why Two States are Needed:**
```
Example: [-2, 3, -4]
- If only track max: 
  i=1: max(3, -2*3=-6) = 3
  i=2: max(-4, 3*-4=-12) = -4 ❌
- With min tracking:
  min at i=1 = -6
  i=2: -6*-4=24 ✅
```

**Edge Cases:**
- Single element → that element
- All positive → entire array
- All negative → largest single element (least negative)
- Contains zero → subarray avoiding zero or zero itself

**Common Patterns:**
- **Negative numbers:** Need min tracking
- **Zeros:** Natural reset points
- **Ones:** Don't affect product but break subarrays