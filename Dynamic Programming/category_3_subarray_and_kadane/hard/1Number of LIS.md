## Number of Longest Increasing Subsequences
**Category:** **SUBSEQUENCE DP / LIS VARIANT**

**Problem:** Given integer array `nums`, return the **number** of longest increasing subsequences (not necessarily distinct indices).

**Example:**
```
Input: nums = [1,3,5,4,7]
Output: 2
Explanation: Two LIS of length 4:
[1,3,4,7] and [1,3,5,7]
```

```
Input: nums = [2,2,2,2,2]
Output: 5
Explanation: LIS length = 1, every element is a valid subsequence
```

```
Input: nums = [1,2,4,3,5,4,7,2]
Output: 3
```

---

### **Relation to LIS**
**Similar to:** **Longest Increasing Subsequence** but with **counting**
**How it's different:**
1. LIS: Find maximum length only
2. Number of LIS: Find **count** of subsequences achieving that max length
3. Need to track **both length AND count** at each position

**Key Insight:**
- `dp_len[i]` = length of LIS ending at i
- `dp_cnt[i]` = number of LIS ending at i with that length
- When extending, if dp_len[j]+1 > dp_len[i] → new length, reset count
- If dp_len[j]+1 == dp_len[i] → add to count

---

### DP Intuition
- **State:**
  - `length[i]` = LIS length ending at index i
  - `count[i]` = number of LIS ending at i with length = length[i]
- **Transition:**
  ```
  For each j < i:
    if nums[j] < nums[i]:
        if length[j] + 1 > length[i]:
            length[i] = length[j] + 1
            count[i] = count[j]
        elif length[j] + 1 == length[i]:
            count[i] += count[j]
  ```
- **Base:** `length[i] = 1`, `count[i] = 1`
- **Answer:** Sum of `count[i]` where `length[i] == max_len`

---

### 1. Recursive Solution
```python
def findNumberOfLIS(nums):
    n = len(nums)
    
    def dfs(i):
        if i == 0:
            return (1, 1)  # (length, count)
        
        max_len = 1
        total_cnt = 1
        
        for j in range(i):
            if nums[j] < nums[i]:
                len_j, cnt_j = dfs(j)
                if len_j + 1 > max_len:
                    max_len = len_j + 1
                    total_cnt = cnt_j
                elif len_j + 1 == max_len:
                    total_cnt += cnt_j
        
        return (max_len, total_cnt)
    
    result_len = 0
    result_cnt = 0
    
    for i in range(n):
        length, count = dfs(i)
        if length > result_len:
            result_len = length
            result_cnt = count
        elif length == result_len:
            result_cnt += count
    
    return result_cnt
```
**TC:** O(2ⁿ) | **SC:** O(n) recursion stack

---

### 2. Memoization (Top-Down DP)
```python
def findNumberOfLIS(nums):
    n = len(nums)
    memo_len = [-1] * n
    memo_cnt = [-1] * n
    
    def dfs(i):
        if memo_len[i] != -1:
            return (memo_len[i], memo_cnt[i])
        
        max_len = 1
        total_cnt = 1
        
        for j in range(i):
            if nums[j] < nums[i]:
                len_j, cnt_j = dfs(j)
                if len_j + 1 > max_len:
                    max_len = len_j + 1
                    total_cnt = cnt_j
                elif len_j + 1 == max_len:
                    total_cnt += cnt_j
        
        memo_len[i] = max_len
        memo_cnt[i] = total_cnt
        return (max_len, total_cnt)
    
    result_len = 0
    result_cnt = 0
    
    for i in range(n):
        length, count = dfs(i)
        if length > result_len:
            result_len = length
            result_cnt = count
        elif length == result_len:
            result_cnt += count
    
    return result_cnt
```
**TC:** O(n²) | **SC:** O(n)

---

### 3. Tabulation (Bottom-Up DP)
```python
def findNumberOfLIS(nums):
    n = len(nums)
    if n <= 1:
        return n
    
    length = [1] * n
    count = [1] * n
    
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                if length[j] + 1 > length[i]:
                    length[i] = length[j] + 1
                    count[i] = count[j]
                elif length[j] + 1 == length[i]:
                    count[i] += count[j]
    
    max_len = max(length)
    result = 0
    for i in range(n):
        if length[i] == max_len:
            result += count[i]
    
    return result
```
**TC:** O(n²) | **SC:** O(n)

---

### 4. Space Optimized (Still O(n))
```python
def findNumberOfLIS(nums):
    n = len(nums)
    if n <= 1:
        return n
    
    length = [1] * n
    count = [1] * n
    
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                if length[j] + 1 > length[i]:
                    length[i] = length[j] + 1
                    count[i] = count[j]
                elif length[j] + 1 == length[i]:
                    count[i] += count[j]
    
    max_len = 0
    result = 0
    for i in range(n):
        if length[i] > max_len:
            max_len = length[i]
            result = count[i]
        elif length[i] == max_len:
            result += count[i]
    
    return result
```
**TC:** O(n²) | **SC:** O(n)

---

### 5. Segment Tree Optimization (O(n log n))
```python
def findNumberOfLIS(nums):
    # Coordinate compression
    sorted_unique = sorted(set(nums))
    coord = {v: i+1 for i, v in enumerate(sorted_unique)}  # 1-indexed
    
    n = len(sorted_unique)
    length_seg = [0] * (4 * n)
    count_seg = [0] * (4 * n)
    
    def query(node, l, r, ql, qr):
        if ql > r or qr < l:
            return (0, 0)  # (max_len, total_count)
        if ql <= l and r <= qr:
            return (length_seg[node], count_seg[node])
        
        mid = (l + r) // 2
        left_len, left_cnt = query(node*2, l, mid, ql, qr)
        right_len, right_cnt = query(node*2+1, mid+1, r, ql, qr)
        
        if left_len > right_len:
            return (left_len, left_cnt)
        elif right_len > left_len:
            return (right_len, right_cnt)
        else:
            return (left_len, left_cnt + right_cnt)
    
    def update(node, l, r, pos, length_val, count_val):
        if l == r:
            if length_val > length_seg[node]:
                length_seg[node] = length_val
                count_seg[node] = count_val
            elif length_val == length_seg[node]:
                count_seg[node] += count_val
            return
        
        mid = (l + r) // 2
        if pos <= mid:
            update(node*2, l, mid, pos, length_val, count_val)
        else:
            update(node*2+1, mid+1, r, pos, length_val, count_val)
        
        left_len, left_cnt = length_seg[node*2], count_seg[node*2]
        right_len, right_cnt = length_seg[node*2+1], count_seg[node*2+1]
        
        if left_len > right_len:
            length_seg[node] = left_len
            count_seg[node] = left_cnt
        elif right_len > left_len:
            length_seg[node] = right_len
            count_seg[node] = right_cnt
        else:
            length_seg[node] = left_len
            count_seg[node] = left_cnt + right_cnt
    
    for num in nums:
        idx = coord[num]
        # Query all values < num (indices 1 to idx-1)
        max_len, total_cnt = query(1, 1, n, 1, idx-1)
        
        if max_len == 0:
            update(1, 1, n, idx, 1, 1)
        else:
            update(1, 1, n, idx, max_len + 1, total_cnt)
    
    return count_seg[1]
```
**TC:** O(n log n) | **SC:** O(n)

---

**Key Formula:**
```
For each i:
    length[i] = 1
    count[i] = 1
    
    For j < i:
        if nums[j] < nums[i]:
            if length[j] + 1 > length[i]:
                length[i] = length[j] + 1
                count[i] = count[j]
            elif length[j] + 1 == length[i]:
                count[i] += count[j]
```

**Example Walkthrough:**
```
nums = [1,3,5,4,7]

Initialize: length=[1,1,1,1,1], count=[1,1,1,1,1]

i=1 (3): j=0: 1<3, len[0]+1=2 > len[1]=1 → len[1]=2, cnt[1]=1
i=2 (5): j=0: 1<5, len[0]+1=2 > len[2]=1 → len[2]=2, cnt[2]=1
         j=1: 3<5, len[1]+1=3 > len[2]=2 → len[2]=3, cnt[2]=1
i=3 (4): j=0: 1<4, len[0]+1=2 > len[3]=1 → len[3]=2, cnt[3]=1
         j=1: 3<4, len[1]+1=3 > len[3]=2 → len[3]=3, cnt[3]=1
         j=2: 5<4? no
i=4 (7): j=0: 1<7, len[0]+1=2 > len[4]=1 → len[4]=2, cnt[4]=1
         j=1: 3<7, len[1]+1=3 > len[4]=2 → len[4]=3, cnt[4]=1
         j=2: 5<7, len[2]+1=4 > len[4]=3 → len[4]=4, cnt[4]=1
         j=3: 4<7, len[3]+1=4 == len[4]=4 → cnt[4] += 1 = 2

Final:
length = [1,2,3,3,4]
count  = [1,1,1,1,2]
max_len = 4, count[4]=2 → answer = 2
```

**Comparison Table:**

| Aspect | LIS | Number of LIS |
|--------|-----|---------------|
**DP State** | Single array (length) | Two arrays (length, count) |
**Transition** | Max length only | Length + count aggregation |
**Same length case** | Ignore | Add counts |
**Answer** | max(length) | sum(count where length=max_len) |
**Complexity** | O(n²)/O(n log n) | O(n²)/O(n log n) |

**Variations:**

| Variation | Key Difference | Solution |
|-----------|---------------|----------|
**LIS Length** | Find max length only | Standard LIS |
**Number of LIS** | Count sequences with max length | DP with length+count |
**Number of all increasing subsequences** | Count all, not just longest | DP sum all counts |
**LIS with maximum sum** | Maximize sum instead of length | DP with sum tracking |
**LIS reconstruction** | Print one LIS | Track prev indices |
**All LIS** | Print all LIS | Backtracking + DP |

**Edge Cases:**
- Empty array → 0
- Single element → 1
- All decreasing → n (each element is length 1)
- All equal → n (each element is length 1)

**Why Two Arrays:**
- Length tells us if we found a **longer** subsequence
- Count accumulates when we find **another** subsequence of same length
- Need both to correctly handle multiple paths to same length

**Key Insight:**
- This is essentially **counting number of longest paths in a DAG**
- Nodes = indices, edges = i→j if i<j and nums[i]<nums[j]
- DP finds longest path length and count of such paths