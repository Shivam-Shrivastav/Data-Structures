## 🧠 **K-th Smallest Prime Fraction**

---

### 1. **Problem Statement with Example**

You are given a **sorted array** `arr` of **distinct primes** (and 1).

👉 Consider all fractions of the form:

[
\frac{arr[i]}{arr[j]} \quad \text{where } i < j
]

👉 Return the **k-th smallest fraction**.

---

#### Example:

```python
Input: arr = [1,2,3,5], k = 3

Fractions:
1/2 = 0.5
1/3 = 0.33
1/5 = 0.2
2/3 = 0.66
2/5 = 0.4
3/5 = 0.6

Sorted:
[1/5, 1/3, 2/5, 1/2, 3/5, 2/3]

Output: [2,5]
```

---

#### Constraints:

* `2 <= arr.length <= 1000`
* `arr[0] = 1`, rest are primes
* `1 <= k <= n*(n-1)/2`

---

### 2. **Diagram**

```text
Fraction Matrix:

        2     3     5
      -----------------
1 |   1/2   1/3   1/5
2 |         2/3   2/5
3 |               3/5

Each row is sorted (increasing denominator → smaller fraction)
```

👉 Think of it as a **sorted matrix of fractions**

---

### 3. **Example I/O**

#### ✅ Example 1

```python
Input: arr = [1,2,3,5], k = 3
Output: [2,5]
```

#### ⚠️ Example 2 (Edge)

```python
Input: arr = [1,7], k = 1
Output: [1,7]
```

---

### 4. **Intuition & Pattern Recognition**

👉 Signals:

* k-th smallest
* Pair combinations `(i, j)`
* Values derived from indices

💡 Key Insight:

* Treat as **matrix problem**
* Each row = fractions with same numerator

🧠 Interview thought:

> “This is like k-th smallest in sorted matrix OR k smallest pairs → use heap or binary search”

---

### 5. **Simpler Version**

#### Related problems:

* Find K Pairs with Smallest Sums
  → pair generation with heap

* Kth Smallest Element in a Sorted Matrix
  → matrix + heap/binary search

---

#### Thinking flow:

```text
Pairs → Fractions → Sorted matrix → Heap/Binary Search
```

#### Difference:

* Instead of sum → we compare fractions

---

### 6. **Brute Force**

### Idea:

* Generate all fractions
* Sort

```python
def kthSmallestPrimeFraction(arr, k):
    fractions = []
    
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            fractions.append((arr[i]/arr[j], arr[i], arr[j]))
    
    fractions.sort()
    return [fractions[k-1][1], fractions[k-1][2]]
```

#### Complexity:

* Time: `O(n^2 log n)`
* Space: `O(n^2)`

❌ Too slow

---

### 7. **Optimal Solutions**

---

## ⭐ Approach 1: Heap (Best for understanding)

---

### 🔑 Core Idea:

* Treat rows like sorted lists:

  * Fix numerator `i`
  * Move denominator `j`

---

### Initialization:

* Push `(i, n-1)` → smallest fraction per numerator

---

### ✅ Code

```python
import heapq

def kthSmallestPrimeFraction(arr, k):
    n = len(arr)
    heap = []
    
    # push smallest fractions for each numerator
    for i in range(n - 1):
        heapq.heappush(heap, (arr[i] / arr[-1], i, n - 1))
    
    for _ in range(k - 1):
        val, i, j = heapq.heappop(heap)
        
        if j - 1 > i:
            heapq.heappush(heap, (arr[i] / arr[j - 1], i, j - 1))
    
    _, i, j = heapq.heappop(heap)
    return [arr[i], arr[j]]
```

---

### Complexity:

* Time: `O(k log n)`
* Space: `O(n)`

---

## ⭐⭐ Approach 2: Binary Search (Advanced)

---

### 🔑 Idea:

* Binary search on fraction value
* Count how many fractions ≤ mid

---

### Trick:

* Use two pointers to count efficiently

---

### ✅ Code

```python
def kthSmallestPrimeFraction(arr, k):
    n = len(arr)
    
    def countLessEqual(x):
        count = 0
        best_num, best_den = 0, 1
        j = 1
        
        for i in range(n):
            while j < n and arr[i] > x * arr[j]:
                j += 1
            
            if j == n:
                break
            
            count += (n - j)
            
            if arr[i] * best_den > best_num * arr[j]:
                best_num, best_den = arr[i], arr[j]
        
        return count, best_num, best_den
    
    left, right = 0, 1
    
    while True:
        mid = (left + right) / 2
        count, num, den = countLessEqual(mid)
        
        if count == k:
            return [num, den]
        elif count < k:
            left = mid
        else:
            right = mid
```

---

### Complexity:

* Time: `O(n log range)`
* Space: `O(1)`

---

### 8. **Step-by-Step Trace (Heap)**

#### Input:

```python
arr = [1,2,3,5], k = 3
```

---

#### Initial Heap:

```text
1/5, 2/5, 3/5
```

---

| Step | Pop | Push | Result    |
| ---- | --- | ---- | --------- |
| 1    | 1/5 | 1/3  | [1/5]     |
| 2    | 1/3 | 1/2  | [1/5,1/3] |
| 3    | 2/5 | —    | answer    |

---

### Final → `[2,5]`

---

### 9. **Related Problems**

1. Find K Pairs with Smallest Sums
   → pair-based heap

2. Kth Smallest Element in a Sorted Matrix
   → matrix + heap

3. Ugly Number II
   → generate sorted sequence

4. Kth Smallest Number in Multiplication Table
   → binary search + counting

---

## ⚡ Final Interview Takeaway

### Pattern:

```text
k-th smallest over combinations → Heap OR Binary Search
```

---

### Key Insight:

* Treat fractions as **sorted matrix**
* Use indices instead of generating all

---

### Mental Shortcut

> “Pairs + sorted + k-th → heap with index movement OR count-based binary search”

---

If you want:

* 🔥 How to derive binary search counting (very tricky but powerful)
* 🔥 Why float comparison is dangerous (important!)
* 🔥 How this connects to ALL fraction-based problems
