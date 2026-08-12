## 🧠 **Find the Kth Smallest Sum of a Matrix With Sorted Rows**

---

### 1. **Problem Statement with Example**

You are given a matrix `mat` of size `m x n` where:

* Each **row is sorted in non-decreasing order**
* You must pick **exactly one element from each row**

👉 Return the **k-th smallest possible sum**

---

#### Example:

```python
Input:
mat = [
  [1,3,11],
  [2,4,6]
]
k = 5

All sums:
1+2=3
1+4=5
1+6=7
3+2=5
3+4=7
3+6=9
11+2=13
...

Sorted:
[3,5,5,7,7,9,...]

Output: 7
```

---

#### Constraints:

* `1 <= m, n <= 40`
* `1 <= k <= min(200, n^m)`

---

### 2. **Diagram**

```text
Matrix:

[1   3   11]
[2   4    6]

Think:
Row1 choices → combine with Row2

Combinations:

(0,0) → 1+2 = 3
(0,1) → 1+4 = 5
(1,0) → 3+2 = 5
...

Like exploring a grid of combinations
```

👉 This is **multi-dimensional merging problem**

---

### 3. **Example I/O**

#### ✅ Example 1

```python
Input: mat = [[1,3,11],[2,4,6]], k = 5
Output: 7
```

#### ⚠️ Example 2 (Edge)

```python
Input: mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
Output: 9
```

---

### 4. **Intuition & Pattern Recognition**

👉 Signals:

* Pick one element per row → combinations explode
* Need k-th smallest → not all

💡 Key Insight:

* Each row acts like a **dimension**
* Combine rows **progressively**

🧠 Interview thought:

> “This is like merging rows one by one using heap → k smallest combinations”

---

### 5. **Simpler Version**

#### Step-by-step thinking:

1. One row → trivial

2. Two rows → pair sums →
   👉 Find K Pairs with Smallest Sums

3. Extend to m rows → iterative merging

---

#### Thinking flow:

```text
2 arrays → k smallest pairs → extend row by row
```

---

### 6. **Brute Force**

### Idea:

* Generate all combinations

```python
# exponential → O(n^m)
```

❌ Impossible

---

### 7. **Optimal Solution (Heap + Iterative Merge)** ⭐

---

### 🔑 Core Idea:

* Start with first row
* Merge with next row → keep only k smallest sums
* Repeat

---

### Step:

```
current_sums = row1

for next_row:
    merge current_sums + next_row
    keep k smallest
```

---

### ✅ Code

```python
import heapq

def kthSmallest(mat, k):
    
    def merge(arr1, arr2):
        heap = []
        res = []
        
        # initialize heap
        for i in range(min(k, len(arr1))):
            heapq.heappush(heap, (arr1[i] + arr2[0], i, 0))
        
        while heap and len(res) < k:
            total, i, j = heapq.heappop(heap)
            res.append(total)
            
            if j + 1 < len(arr2):
                heapq.heappush(heap, (arr1[i] + arr2[j+1], i, j+1))
        
        return res
    
    curr = mat[0]
    
    for i in range(1, len(mat)):
        curr = merge(curr, mat[i])
    
    return curr[k-1]
```

---

### Complexity:

* Time: `O(m * k log k)`
* Space: `O(k)`

---

### 8. **Step-by-Step Trace**

#### Input:

```python
mat = [[1,3],[2,4]]
k = 3
```

---

### Step 1:

```text
curr = [1,3]
```

---

### Step 2 (merge with [2,4]):

| Pair | Sum |
| ---- | --- |
| 1+2  | 3   |
| 1+4  | 5   |
| 3+2  | 5   |

Sorted → `[3,5,5]`

---

### Answer = 5

---

### 9. **Related Problems**

1. Find K Pairs with Smallest Sums
   → exact base problem

2. Kth Smallest Element in a Sorted Matrix
   → k-th smallest in structured grid

3. Smallest Range Covering Elements from K Lists
   → heap across k lists

4. Ugly Number II
   → generate sorted sequence

---

## ⚡ Final Interview Takeaway

### Pattern:

```text
k smallest combinations across multiple arrays → Heap + incremental merging
```

---

### Core trick:

```python
Only keep k smallest at each step
```

---

### Mental Shortcut

> “Multiple rows → reduce to 2-row problem repeatedly (LC 373)”

---

## 🔥 Key Insight

* You NEVER build all combinations
* You always:

  ```
  prune to k → merge → prune → merge
  ```

---

If you want next:

* 🔥 Why BFS / state-space also works here
* 🔥 Visual intuition (graph traversal view)
* 🔥 Common pitfalls (VERY important for interviews)
