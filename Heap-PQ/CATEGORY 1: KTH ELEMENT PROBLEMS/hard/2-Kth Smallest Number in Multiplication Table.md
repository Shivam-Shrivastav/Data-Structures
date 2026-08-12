## 🧠 **Kth Smallest Number in Multiplication Table**

---

### 1. **Problem Statement with Example**

Given two integers `m` and `n`, representing an `m x n` multiplication table:

* Each cell `(i, j)` contains value: `i * j`
* Find the **k-th smallest number** in this table.

#### Example:

```
Input: m = 3, n = 3, k = 5

Multiplication Table:
1 2 3
2 4 6
3 6 9

Output: 3
```

#### Constraints:

* `1 <= m, n <= 3 * 10^4`
* `1 <= k <= m * n`

---

### 2. **Diagram**

```
Matrix (m x n):

      1   2   3   4
  -------------------
1 |   1   2   3   4
2 |   2   4   6   8
3 |   3   6   9  12

Sorted order:
[1,2,2,3,3,4,4,6,6,8,9,12]
```

---

### 3. **Example I/O**

#### ✅ Example 1 (Typical)

```
Input: m = 3, n = 3, k = 5
Output: 3

Sorted:
[1,2,2,3,3,4,6,6,9]
→ 5th = 3
```

#### ⚠️ Example 2 (Edge Case)

```
Input: m = 1, n = 10, k = 7
Output: 7

Table:
[1,2,3,4,5,6,7,8,9,10]
```

---

### 4. **Intuition & Pattern Recognition**

👉 Signals:

* Sorted structure hidden in matrix
* Each row is **sorted**
* Want **k-th smallest → typical heap OR binary search on answer**

💡 Key Insight:

* Row `i` → multiples of `i`: `i, 2i, 3i...`
* Instead of building full matrix → too big

🧠 Interview thought:

> “This is like merging `m` sorted lists → Heap OR binary search on value space.”

---

### 5. **Simpler Version**

#### Simpler Problem:

* Merge k sorted arrays → use min heap
  👉 Merge k Sorted Lists

#### Connection:

* Each row = sorted list
* We want k-th smallest across all rows

#### Difference:

* Lists are **implicit** (not stored)
* Very large → can't push all elements

➡️ Leads to:

* Either **Heap (optimized)**
* Or **Binary Search on Answer (best)**

---

### 6. **Brute Force**

### Idea:

* Generate full matrix
* Flatten + sort

```python
def findKthNumber(m, n, k):
    arr = []
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            arr.append(i*j)
    
    arr.sort()
    return arr[k-1]
```

#### Complexity:

* Time: `O(m * n log(m*n))`
* Space: `O(m * n)`

❌ Impossible for large constraints

---

### 7. **Optimal Solution (Binary Search on Answer)** ⭐

👉 This is the **real optimal**, even though heap is intuitive.

#### Key Idea:

* Guess a number `mid`
* Count how many numbers ≤ `mid`

```
count += min(n, mid // i)
```

---

### ✅ Code

```python
def findKthNumber(m, n, k):
    def countLessEqual(x):
        count = 0
        for i in range(1, m + 1):
            count += min(n, x // i)  # numbers ≤ x in row i
        return count

    left, right = 1, m * n

    while left < right:
        mid = (left + right) // 2
        
        if countLessEqual(mid) >= k:
            right = mid
        else:
            left = mid + 1

    return left
```

---

### Complexity:

* Time: `O(m log(m*n))`
* Space: `O(1)`

---

### 🔥 Heap Approach (Interview Mention)

```python
import heapq

def findKthNumber(m, n, k):
    heap = []
    
    # push first column
    for i in range(1, m+1):
        heapq.heappush(heap, (i, i, 1))  # value, row, col
    
    for _ in range(k-1):
        val, r, c = heapq.heappop(heap)
        
        if c < n:
            heapq.heappush(heap, (r*(c+1), r, c+1))
    
    return heap[0][0]
```

### Complexity:

* Time: `O(k log m)`
* Space: `O(m)`

---

### 8. **Step-by-Step Trace (Binary Search)**

#### Example:

```
m=3, n=3, k=5
```

| Step | mid | count ≤ mid | Action    |
| ---- | --- | ----------- | --------- |
| 1    | 5   | 6           | right = 5 |
| 2    | 3   | 5           | right = 3 |
| 3    | 2   | 3           | left = 3  |

➡️ Answer = 3

---

### 9. **Related Problems**

1. Kth Smallest Element in a Sorted Matrix
   → Same idea: binary search on value

2. Find K Pairs with Smallest Sums
   → Heap merging sorted pairs

3. Kth Smallest Prime Fraction
   → Binary search + counting

4. Ugly Number II
   → Multiple sorted streams + heap

5. Smallest Range Covering Elements from K Lists
   → Heap + k sorted lists

---

## ⚡ Final Interview Takeaway

* **Heap thinking:** merge sorted rows
* **But optimal:** binary search on answer
* Core trick:

```
count += min(n, mid // i)
```

---

If you want, I can also show **why binary search works mathematically (very important for interviews)** or how to **derive this from scratch under pressure**.
