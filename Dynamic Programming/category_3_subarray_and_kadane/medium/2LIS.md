## Longest Increasing Subsequence
**Category:** **SUBSEQUENCE DP** (non-contiguous, order preserved)

**Problem:** Given integer array `nums`, find length of longest strictly increasing subsequence (not necessarily contiguous).

**Example:**
```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: [2,3,7,101] or [2,5,7,101] length = 4
```

```
Input: nums = [0,1,0,3,2,3]
Output: 4
Explanation: [0,1,2,3] length = 4
```

```
Input: nums = [7,7,7,7,7,7]
Output: 1
Explanation: Strictly increasing → all equal = 1
```

---

### **Relation to Subarray Problems**
**Similar to:** **Maximum Subarray** but for **SUBSEQUENCE** (not contiguous)
**How it's different:**
1. **Subarray:** Contiguous elements → transition from i-1 only
2. **Subsequence:** Can skip elements → transition from **any previous j < i**
3. **State:** `dp[i]` = LIS ending at index i (must include nums[i])

**Key Insight:** 
- At position i, can extend any previous increasing subsequence ending at j where nums[j] < nums[i]
- Need to check **all previous positions**, not just i-1

---

### DP Intuition
- **State:** `dp[i]` = length of LIS **ending at index i** (including nums[i])
- **Transition:**
  ```
  dp[i] = max(1, max(dp[j] + 1 for all j < i if nums[j] < nums[i]))
  ```
- **Answer:** `max(dp[0..n-1])`

---

### 1. Recursive Solution
```python
def lengthOfLIS(nums):
    n = len(nums)
    
    def dfs(i):
        if i == 0:
            return 1
        
        max_len = 1
        for j in range(i):
            if nums[j] < nums[i]:
                max_len = max(max_len, dfs(j) + 1)
        
        return max_len
    
    result = 0
    for i in range(n):
        result = max(result, dfs(i))
    return result
```
**TC:** O(2ⁿ) | **SC:** O(n) recursion stack

---

### 2. Memoization (Top-Down DP)
```python
def lengthOfLIS(nums):
    n = len(nums)
    memo = [-1] * n
    
    def dfs(i):
        if memo[i] != -1:
            return memo[i]
        
        max_len = 1
        for j in range(i):
            if nums[j] < nums[i]:
                max_len = max(max_len, dfs(j) + 1)
        
        memo[i] = max_len
        return max_len
    
    result = 0
    for i in range(n):
        result = max(result, dfs(i))
    return result
```
**TC:** O(n²) | **SC:** O(n)

---

### 3. Tabulation (Bottom-Up DP) - O(n²)
```python
def lengthOfLIS(nums):
    n = len(nums)
    dp = [1] * n  # Each element is at least length 1
    
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)
```
**TC:** O(n²) | **SC:** O(n)

---

### 4. Patience Sorting - O(n log n)
```python
def lengthOfLIS(nums):
    import bisect
    
    piles = []  # stores smallest tail of increasing subsequence of each length
    
    for num in nums:
        pos = bisect.bisect_left(piles, num)
        if pos == len(piles):
            piles.append(num)
        else:
            piles[pos] = num
    
    return len(piles)
```
**TC:** O(n log n) | **SC:** O(n)

**Intuition:** Maintain piles where each pile's top card is smallest possible tail for subsequence of that length.

---

### 5. Print LIS (Reconstruction)
```python
def lengthOfLIS(nums):
    n = len(nums)
    dp = [1] * n
    prev = [-1] * n  # stores previous index in LIS
    
    max_len = 1
    last_idx = 0
    
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j
        
        if dp[i] > max_len:
            max_len = dp[i]
            last_idx = i
    
    # Reconstruct LIS
    lis = []
    while last_idx != -1:
        lis.append(nums[last_idx])
        last_idx = prev[last_idx]
    
    lis.reverse()
    print("LIS:", lis)
    return max_len
```

---

**Key Formula:**
```
dp[i] = 1 + max(dp[j]) for all j < i with nums[j] < nums[i]
dp[0] = 1
Answer = max(dp)
```

**Example Walkthrough (DP O(n²)):**
```
nums = [10, 9, 2, 5, 3, 7, 101, 18]
dp:
i=0: dp[0]=1
i=1: no j with nums[j]<9 → dp[1]=1
i=2: no j with nums[j]<2 → dp[2]=1
i=3: j=2 (2<5) → dp[3]=dp[2]+1=2
i=4: j=2 (2<3) → dp[4]=dp[2]+1=2
i=5: j=2 (2<7) → dp[5]=dp[2]+1=2
     j=3 (5<7) → dp[5]=max(2, dp[3]+1=3) = 3
     j=4 (3<7) → dp[5]=max(3, dp[4]+1=3) = 3
i=6: j=5 (7<101) → dp[6]=dp[5]+1=4
i=7: j=5 (7<18) → dp[7]=dp[5]+1=4
     j=6 (101<18?) no
max(dp) = 4
```

**Patience Sorting Example:**
```
nums = [10,9,2,5,3,7,101,18]
10  → [10]
9   → [9]      # replace 10
2   → [2]      # replace 9
5   → [2,5]
3   → [2,3]    # replace 5
7   → [2,3,7]
101 → [2,3,7,101]
18  → [2,3,7,18]  # replace 101
length = 4
```

**Comparison Table:**

| Aspect | Maximum Subarray | LIS |
|--------|-----------------|-----|
**Contiguous?** | ✅ Yes | ❌ No |
**DP Transition** | From i-1 only | From all j < i |
**Time Complexity** | O(n) | O(n²) or O(n log n) |
**Space Complexity** | O(1) | O(n) |
**Greedy possible?** | Yes (Kadane's) | Yes (Patience) |
**State Definition** | Max sum ending at i | Max length ending at i |

**Variations of LIS:**

| Variation | Key Difference | Solution |
|-----------|---------------|----------|
| **LIS (strict)** | nums[i] > nums[j] | Standard DP |
| **Non-decreasing** | nums[i] ≥ nums[j] | Change condition |
| **Longest Bitonic** | Increasing then decreasing | LIS left + LIS right |
| **Number of LIS** | Count distinct LIS | DP + count array |
| **Minimum deletions** | n - LIS length | Convert to LIS |
| **Russian Doll Envelopes** | 2D sort + LIS on second dim | Patience on 2nd dim |

**Edge Cases:**
- Empty array → 0
- Single element → 1
- All decreasing → 1
- All equal → 1

**Why Not Greedy (Simple)?**
- Greedy "take smallest possible" works for length but not reconstruction
- Patience sorting is greedy on tails, optimal for length

**Key Insight for O(n log n):**
- Maintain tails[i] = smallest ending value for LIS of length i+1
- Binary search to find where current number fits
- Greedy: smaller tail is always better