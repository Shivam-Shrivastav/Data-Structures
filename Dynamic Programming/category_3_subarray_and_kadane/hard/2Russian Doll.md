## Russian Doll Envelopes
**Category:** **SUBSEQUENCE DP / 2D LIS VARIANT**

**Problem:** You have envelopes with (width, height). An envelope can fit into another if both width and height are **strictly smaller**. Find maximum number of envelopes you can Russian doll (nest).

**Example:**
```
Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: [2,3] → [5,4] → [6,7] (3 envelopes)
```

```
Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1
Explanation: Can't nest equal dimensions (strictly smaller required)
```

---

### **Relation to LIS**
**Similar to:** **Longest Increasing Subsequence** in 2D
**How it transforms:**
1. **Sort by width ascending**, if tie → **height descending**
2. Then find **LIS on heights** (strict increasing)

**Why sort height descending when width equal?**
- If same width, can't nest (width not strictly smaller)
- Descending heights ensures we don't count same-width envelopes together
- LIS on heights will pick at most one from each width group

**Difference from LIS:**
- LIS: 1D array, single condition
- Russian Doll: 2D, both dimensions must be strictly smaller
- Requires clever sorting to reduce to 1D LIS

---

### DP Intuition
1. **Sorting Trick:** 
   - Sort by width ascending
   - When widths equal, sort by height descending
2. **Extract heights array**
3. **Apply LIS** on heights (strict increasing)
4. **Answer:** Length of LIS

---

### 1. Brute Force Recursive
```python
def maxEnvelopes(envelopes):
    if not envelopes:
        return 0
    
    n = len(envelopes)
    envelopes.sort()  # sort by width then height
    
    def dfs(i):
        # LIS ending at i
        max_len = 1
        for j in range(i):
            if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
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
def maxEnvelopes(envelopes):
    if not envelopes:
        return 0
    
    n = len(envelopes)
    envelopes.sort()
    memo = [-1] * n
    
    def dfs(i):
        if memo[i] != -1:
            return memo[i]
        
        max_len = 1
        for j in range(i):
            if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
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

### 3. Tabulation (O(n²) DP)
```python
def maxEnvelopes(envelopes):
    if not envelopes:
        return 0
    
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    n = len(envelopes)
    dp = [1] * n
    
    for i in range(n):
        for j in range(i):
            if envelopes[j][1] < envelopes[i][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)
```
**TC:** O(n²) | **SC:** O(n)

---

### 4. Patience Sorting (O(n log n)) - Optimal
```python
def maxEnvelopes(envelopes):
    import bisect
    
    if not envelopes:
        return 0
    
    # Sort width ascending, height descending
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    
    # LIS on heights using patience sorting
    piles = []
    for _, h in envelopes:
        pos = bisect.bisect_left(piles, h)
        if pos == len(piles):
            piles.append(h)
        else:
            piles[pos] = h
    
    return len(piles)
```
**TC:** O(n log n) | **SC:** O(n)

---

### 5. With Reconstruction
```python
def maxEnvelopes(envelopes):
    import bisect
    
    if not envelopes:
        return 0
    
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    
    piles = []  # tails of increasing subsequences
    prev = {}   # for reconstruction (index -> previous index)
    indices = []  # store which envelope at each tail
    
    for i, (_, h) in enumerate(envelopes):
        pos = bisect.bisect_left(piles, h)
        
        if pos == len(piles):
            piles.append(h)
            indices.append(i)
        else:
            piles[pos] = h
            indices[pos] = i
        
        # Track previous element for reconstruction
        if pos > 0:
            prev[i] = indices[pos-1]
    
    # Reconstruct sequence
    if not piles:
        return 0
    
    last_idx = indices[-1]
    sequence = []
    while last_idx in prev:
        sequence.append(envelopes[last_idx])
        last_idx = prev[last_idx]
    sequence.append(envelopes[last_idx])
    sequence.reverse()
    
    print("Nesting sequence:", sequence)
    return len(piles)
```

---

**Key Transformation:**
```
Original: [[5,4],[6,4],[6,7],[2,3]]

Step 1: Sort by width asc, height desc
        [(2,3), (5,4), (6,7), (6,4)]  ← height desc for equal width

Step 2: Extract heights
        [3, 4, 7, 4]

Step 3: LIS on heights (strict)
        [3, 4, 7] length = 3
```

**Why Height Descending for Equal Width:**
```
If we sort height ascending for equal width:
[(6,4), (6,7)] → heights [4,7] → LIS = 2 ❌
But can't nest (6,4) in (6,7) - same width!

If we sort height descending:
[(6,7), (6,4)] → heights [7,4] → LIS = 1 ✅
Correctly counts only one from same width
```

**Example Walkthrough (Patience Sorting):**
```
envelopes = [[5,4],[6,4],[6,7],[2,3]]

After sorting: [(2,3), (5,4), (6,7), (6,4)]

Heights = [3, 4, 7, 4]

piles = []
3 → [3]
4 → [3,4]
7 → [3,4,7]
4 → bisect_left([3,4,7],4)=1 → [3,4,7]  # replace 4 at pos1
length = 3 ✅
```

**Comparison Table:**

| Aspect | LIS (1D) | Russian Doll Envelopes (2D) |
|--------|---------|---------------------------|
**Input** | 1D array | 2D array (w,h) |
**Condition** | nums[i] > nums[j] | w1<w2 AND h1<h2 |
**Sorting** | Not needed | Required (w asc, h desc) |
**Reduction** | Direct | 2D → 1D via sorting |
**DP Complexity** | O(n²) | O(n²) |
**Optimal** | O(n log n) | O(n log n) |

**Variations:**

| Variation | Key Difference | Solution |
|-----------|---------------|----------|
**1D LIS** | Single dimension | Standard LIS |
**2D LIS** | Both dimensions increasing | Sort + LIS on 2nd |
**3D LIS** | Box stacking (w,d,h) | Sort 2D, LIS on 3rd |
**Non-strict** | w1≤w2 AND h1≤h2 | Modify sort & LIS condition |
**Max sum** | Maximize sum instead of count | DP with sum tracking |

**Edge Cases:**
- Empty array → 0
- Single envelope → 1
- All same dimensions → 1
- One dimension increasing, other decreasing → careful with tie-breaking

**Key Insight for O(n log n):**
- **Sorting is the DP optimization** for 2D LIS
- Width sorted ascending ensures we only check forward
- Height descending for ties prevents invalid nests
- Problem reduces to: "Can we find strictly increasing height sequence?"
- Patience sorting on heights gives LIS length

**Why Greedy Works Here:**
- After sorting, any valid nesting must have increasing heights
- Smaller height at same LIS length is always better
- Patience sorting finds optimal LIS length greedily