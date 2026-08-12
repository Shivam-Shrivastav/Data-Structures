## 🧠 **Kth Smallest Element in a Sorted Matrix**

---

### 1. **Problem Statement with Example**

You are given an `n x n` matrix where:

* Each **row is sorted**
* Each **column is sorted**

👉 Return the **k-th smallest element** in the matrix.

---

#### Example:

```python
Input:
matrix = [
  [1,  5,  9],
  [10, 11, 13],
  [12, 13, 15]
]
k = 8

Output: 13
```

#### Constraints:

* `n <= 300`
* Matrix sorted row-wise & column-wise
* `1 <= k <= n^2`

---

### 2. **Diagram**

```text
Matrix:

[ 1   5   9 ]
[10  11  13]
[12  13  15]

Sorted order:
[1,5,9,10,11,12,13,13,15]

We don't flatten → exploit structure
```

👉 Think: **multiple sorted lists (rows)**

---

### 3. **Example I/O**

#### ✅ Example 1

```python
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
```

#### ⚠️ Example 2 (Edge)

```python
Input: matrix = [[-5]], k = 1
Output: -5
```

---

### 4. **Intuition & Pattern Recognition**

👉 Signals:

* Sorted rows AND columns
* k-th smallest → classic pattern

💡 Two strong approaches:

1. Heap (merge sorted rows)
2. Binary search on answer (optimal)

🧠 Interview thought:

> “This is like merging k sorted lists OR binary search on value space”

---

### 5. **Simpler Version**

#### Simpler Problems:

* Merge k Sorted Lists
  → each row = sorted list

* Kth Smallest Number in Multiplication Table
  → count ≤ mid trick

---

#### Thinking flow:

```text
Sorted arrays → Matrix → Count-based binary search
```

#### Difference:

* Here rows + columns sorted → enables faster counting

---

### 6. **Brute Force**

### Idea:

* Flatten matrix
* Sort

```python
def kthSmallest(matrix, k):
    arr = []
    
    for row in matrix:
        arr.extend(row)
    
    arr.sort()
    return arr[k-1]
```

#### Complexity:

* Time: `O(n^2 log n)`
* Space: `O(n^2)`

---

### 7. **Optimal Solutions**

---

## ⭐ Approach 1: Heap (Merge Rows)

---

### 🔑 Idea:

* Push first element of each row
* Always pop smallest
* Push next element in same row

---

### ✅ Code (Heap)

```python
import heapq

def kthSmallest(matrix, k):
    n = len(matrix)
    heap = []
    
    # push first column
    for r in range(n):
        heapq.heappush(heap, (matrix[r][0], r, 0))
    
    for _ in range(k-1):
        val, r, c = heapq.heappop(heap)
        
        if c + 1 < n:
            heapq.heappush(heap, (matrix[r][c+1], r, c+1))
    
    return heap[0][0]
```

---

### Complexity:

* Time: `O(k log n)`
* Space: `O(n)`

---

## ⭐⭐ Approach 2: Binary Search (BEST)

---

### 🔑 Core Idea:

* Binary search on value range
* Count how many elements ≤ mid

---

### 🔥 Counting Trick (from bottom-left)

```text
Start from bottom-left:
If matrix[r][c] <= mid → move right
Else → move up
```

---

### ✅ Code

```python
def kthSmallest(matrix, k):
    n = len(matrix)
    
    def countLessEqual(mid):
        count = 0
        r, c = n - 1, 0
        
        while r >= 0 and c < n:
            if matrix[r][c] <= mid:
                count += (r + 1)
                c += 1
            else:
                r -= 1
        
        return count
    
    left, right = matrix[0][0], matrix[-1][-1]
    
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

* Time: `O(n log range)`
* Space: `O(1)`

---

### 8. **Step-by-Step Trace (Binary Search)**

#### Input:

```python
matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
```

---

| Step | mid | count ≤ mid | Action     |
| ---- | --- | ----------- | ---------- |
| 1    | 8   | 2           | left = 9   |
| 2    | 12  | 6           | left = 13  |
| 3    | 14  | 8           | right = 14 |
| 4    | 13  | 8           | right = 13 |

➡️ Answer = 13

---

### 9. **Related Problems**

1. Find K Pairs with Smallest Sums
   → matrix + heap expansion

2. Kth Smallest Number in Multiplication Table
   → binary search + counting

3. Kth Smallest Prime Fraction
   → pairs + heap

4. Ugly Number II
   → generate sorted sequence

---

## ⚡ Final Interview Takeaway

### Two approaches:

#### Heap:

```
Merge sorted rows → O(k log n)
```

#### Binary Search (BEST):

```
If you can count ≤ mid → binary search answer
```

---

## 🔥 Mental Shortcut

> “Sorted matrix + k-th smallest → either heap OR binary search”

---

If you want:

* 🔥 When heap beats binary search (important nuance)
* 🔥 How to derive bottom-left counting in interview
* 🔥 Pattern unification across ALL k-th problems
