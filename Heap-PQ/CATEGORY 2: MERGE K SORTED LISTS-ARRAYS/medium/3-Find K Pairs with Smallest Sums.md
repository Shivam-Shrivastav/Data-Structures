## 🧠 **Find K Pairs with Smallest Sums**

---

### 1. **Problem Statement with Example**

You are given two **sorted arrays** `nums1` and `nums2`.

👉 A pair `(u, v)` consists of:

* `u ∈ nums1`
* `v ∈ nums2`

👉 Return the **k pairs with the smallest sums**.

---

#### Example:

```python id="a1p9zx"
Input:
nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3

Output:
[[1,2],[1,4],[1,6]]
```

#### Why:

All pairs:

```
(1,2)=3
(1,4)=5
(1,6)=7
(7,2)=9 ...
```

Smallest 3 → `[1,2], [1,4], [1,6]`

---

### 2. **Diagram**

```text id="7mwxj1"
Matrix of sums:

        2   4   6
      -------------
1  |   3   5   7
7  |   9  11  13
11 |  13  15  17

We explore like:
Start at (0,0) → push neighbors → heap
```

👉 This is like a **sorted matrix problem**

---

### 3. **Example I/O**

#### ✅ Example 1

```python id="1qf6qx"
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
```

#### ⚠️ Example 2 (Edge)

```python id="1f3r6g"
Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
```

---

### 4. **Intuition & Pattern Recognition**

👉 Signals:

* Two sorted arrays
* Pair combinations → `n * m`
* Need smallest k → not all

💡 Key Insight:

* Think of matrix:

  * rows = nums1
  * cols = nums2
* Each row sorted

🧠 Interview thought:

> “This is like k-way merge on sorted rows → use min heap”

---

### 5. **Simpler Version**

#### Simpler Problems:

* Merge k Sorted Lists
  → merging multiple sorted streams

* Kth Smallest Element in a Sorted Matrix
  → grid with sorted rows/cols

---

#### Thinking flow:

```text id="s1qg8n"
Pairs → Matrix → Sorted rows → Heap traversal
```

#### Difference:

* Here we generate neighbors `(i, j+1)` or `(i+1, j)`

---

### 6. **Brute Force**

### Idea:

* Generate all pairs
* Sort

```python id="1r3glj"
def kSmallestPairs(nums1, nums2, k):
    arr = []
    
    for a in nums1:
        for b in nums2:
            arr.append([a, b])
    
    arr.sort(key=lambda x: x[0] + x[1])
    return arr[:k]
```

#### Complexity:

* Time: `O(n*m log(n*m))`
* Space: `O(n*m)`

❌ Too slow

---

### 7. **Optimal Solution (Heap)** ⭐

---

### 🔑 Core Idea:

* Start with smallest pair `(0,0)`
* Push neighbors carefully
* Avoid duplicates using visited OR optimized push

---

### 🔥 Optimization Trick:

👉 Only push `(i, 0)` initially for first `k` rows

---

### ✅ Code

```python id="o4kn6k"
import heapq
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        if not nums1 or not nums2 or not k:
            return res
        
        heap = []
        visited = set()
        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))
        visited.add((0, 0))
        
        while k and heap:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            
            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))
            
            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))
            
            k -= 1
        
        return res
```

---

### Complexity:

* Time: `O(k log k)`
* Space: `O(k)`

---

### 8. **Step-by-Step Trace**

#### Input:

```python id="bq3n9c"
nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
```

---

#### Initial Heap:

```
(1+2,0,0)
(7+2,1,0)
(11+2,2,0)
```

---

#### Steps:

| Step | Pop   | Push  | Result              |
| ---- | ----- | ----- | ------------------- |
| 1    | (1,2) | (1,4) | [[1,2]]             |
| 2    | (1,4) | (1,6) | [[1,2],[1,4]]       |
| 3    | (1,6) | —     | [[1,2],[1,4],[1,6]] |

---

### 9. **Related Problems**

1. Kth Smallest Element in a Sorted Matrix
   → same matrix + heap idea

2. Merge k Sorted Lists
   → merging sorted streams

3. Kth Smallest Prime Fraction
   → pair generation + heap

4. Ugly Number II
   → generate sorted sequence

---

## ⚡ Final Interview Takeaway

* Pattern:

  ```
  k smallest combinations → Min Heap + Controlled Expansion
  ```

* Core idea:

```python
(i, j) → (i, j+1)
```

* Avoid:

  * generating all pairs ❌
  * duplicate pushes ❌

---

## 🔥 Mental Shortcut

> “Sorted arrays + pair sums + k smallest → heap with index tracking”

---

If you want next:

* 🔥 Why **binary search ALSO works here** (advanced)
* 🔥 Full graph/BFS interpretation (very powerful)
* 🔥 Common mistakes interviewers trap you with
