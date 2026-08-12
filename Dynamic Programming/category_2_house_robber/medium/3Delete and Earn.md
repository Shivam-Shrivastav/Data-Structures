## Delete and Earn
**Problem:** Given array `nums`, you can:
1. Pick `nums[i]` and earn `nums[i]` points
2. Delete **ALL** elements equal to `nums[i]-1` and `nums[i]+1`
Find maximum points.

**Example:**
```
Input: nums = [3,4,2]
Output: 6
Explanation: Delete 4 to earn 4 points → delete 3 and 5 (none)
Delete 2 to earn 2 points → total = 4+2=6
```

```
Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: Delete 3 → earn 3×3=9 points
Delete 2 and 4 (2+4=6) less than 9
```

---

### **Relation to House Robber**
**Similar to:** **House Robber** (cannot pick adjacent numbers)
**How it transforms:**
1. Convert to `freq` array where `freq[x] = sum of all x in nums`
2. Now problem: pick numbers for max sum, cannot pick adjacent numbers
   (if pick x, cannot pick x-1 or x+1)
3. This is exactly **House Robber** on the freq array

**Difference from House Robber:**
- House Robber: predefined array, cannot pick adjacent indices
- Delete and Earn: need to **first transform** to freq/sum array
- Numbers can be sparse, need to find max number

---

### DP Intuition
1. Find max number `max_num` in nums
2. Create `sums` array where `sums[num] = num × count(num)`
3. Apply **House Robber DP** on sums array

---

### 1. Recursive Solution
```python
def deleteAndEarn(nums):
    if not nums:
        return 0
    
    max_num = max(nums)
    sums = [0] * (max_num + 1)
    
    # Build sums array
    for num in nums:
        sums[num] += num
    
    # Recursive House Robber
    def dfs(i):
        if i < 0:
            return 0
        return max(dfs(i-1), sums[i] + dfs(i-2))
    
    return dfs(max_num)
```
**TC:** O(2ⁿ) | **SC:** O(n) recursion stack

---

### 2. Memoization (Top-Down DP)
```python
def deleteAndEarn(nums):
    if not nums:
        return 0
    
    max_num = max(nums)
    sums = [0] * (max_num + 1)
    
    for num in nums:
        sums[num] += num
    
    memo = [-1] * (max_num + 1)
    
    def dfs(i):
        if i < 0:
            return 0
        if memo[i] != -1:
            return memo[i]
        memo[i] = max(dfs(i-1), sums[i] + dfs(i-2))
        return memo[i]
    
    return dfs(max_num)
```
**TC:** O(max_num) | **SC:** O(max_num)

---

### 3. Tabulation (Bottom-Up DP)
```python
def deleteAndEarn(nums):
    if not nums:
        return 0
    
    max_num = max(nums)
    sums = [0] * (max_num + 1)
    
    for num in nums:
        sums[num] += num
    
    # House Robber DP
    if max_num == 0:
        return sums[0]
    
    dp = [0] * (max_num + 1)
    dp[0] = sums[0]
    dp[1] = max(sums[0], sums[1])
    
    for i in range(2, max_num + 1):
        dp[i] = max(dp[i-1], sums[i] + dp[i-2])
    
    return dp[max_num]
```
**TC:** O(max_num + n) | **SC:** O(max_num)

---

### 4. Space Optimized
```python
def deleteAndEarn(nums):
    if not nums:
        return 0
    
    max_num = max(nums)
    sums = [0] * (max_num + 1)
    
    for num in nums:
        sums[num] += num
    
    # House Robber space optimized
    if max_num == 0:
        return sums[0]
    
    prev2, prev1 = sums[0], max(sums[0], sums[1])
    
    for i in range(2, max_num + 1):
        curr = max(prev1, sums[i] + prev2)
        prev2, prev1 = prev1, curr
    
    return prev1
```
**TC:** O(max_num + n) | **SC:** O(max_num) for sums array

---

### 5. Optimized with Dictionary (Sparse Numbers)
```python
def deleteAndEarn(nums):
    from collections import Counter
    
    count = Counter(nums)
    nums_sorted = sorted(set(nums))
    
    if not nums_sorted:
        return 0
    
    # House Robber on sorted unique numbers
    prev2, prev1 = 0, 0
    prev_num = -1
    
    for num in nums_sorted:
        curr_earn = num * count[num]
        
        if prev_num == num - 1:
            # Adjacent numbers
            curr = max(prev1, curr_earn + prev2)
        else:
            # Not adjacent, can take both
            curr = curr_earn + prev1
        
        prev2, prev1 = prev1, curr
        prev_num = num
    
    return prev1
```
**TC:** O(n log n) | **SC:** O(n)

---

**Key Transformation:**
```
Original: [2,2,3,3,3,4]
Transform to sums: [0,0,4,9,4] (index=num, value=sum)
Apply House Robber: max(4,9,4+9?) → Actually:
dp[0]=0, dp[1]=0, dp[2]=4, dp[3]=max(4,9)=9, dp[4]=max(9,4+4)=9
```

**Why it's House Robber:**
```
Numbers:     1   2   3   4   5
If pick 3 → cannot pick 2 or 4
This is exactly "cannot pick adjacent"
```

**Edge Cases:**
- Empty array → 0
- All same numbers → sum all of them
- Consecutive numbers [1,2,3,4] → like House Robber
- Sparse numbers [1,100,1000] → take all (no adjacency)

**Comparison Table:**
| Aspect | House Robber | Delete and Earn |
|--------|-------------|-----------------|
**Input** | Array of values | Array with duplicates |
**Constraint** | Cannot pick adjacent indices | Cannot pick adjacent values |
**Transformation** | None needed | Convert to freq/sum array |
**DP Relation** | Base problem | Reduced to House Robber |