## 🧠 **Ugly Number II (Using Heap)**

---

### 1. **Problem Statement with Example**

An **ugly number** is a positive number whose prime factors are limited to **2, 3, and 5**.

👉 Return the **n-th ugly number**

---

#### Example:

```python id="m0z8p4"
Input: n = 10
Output: 12

Ugly numbers:
[1,2,3,4,5,6,8,9,10,12,...]
```

#### Constraints:

* `1 <= n <= 1690`

---

### 2. **Diagram**

```text id="ywr5tc"
Start:
1

Generate:
1 × 2 = 2
1 × 3 = 3
1 × 5 = 5

Heap:
[2,3,5]

Then:
2 × 2 = 4
2 × 3 = 6
2 × 5 = 10

Heap evolves:
[3,4,5,6,10,...]
```

👉 Like **merging infinite sorted sequences**:

* Multiples of 2
* Multiples of 3
* Multiples of 5

---

### 3. **Example I/O**

#### ✅ Example 1

```python id="34h2vk"
Input: n = 5
Output: 5

Sequence:
[1,2,3,4,5]
```

#### ⚠️ Example 2 (Edge)

```python id="l5r2cx"
Input: n = 1
Output: 1
```

---

### 4. **Intuition & Pattern Recognition**

👉 Signals:

* Generate numbers in **sorted order**
* Each number produces more candidates
* Need **k-th smallest**

💡 Insight:

* Similar to:

  * merging sorted streams
  * BFS on number generation

🧠 Interview thought:

> “This is like generating numbers in increasing order → use min heap”

---

### 5. **Simpler Version**

#### Simpler Problems:

* Merge k Sorted Lists
  → heap merging multiple sorted streams

* Kth Smallest Number in Multiplication Table
  → k-th smallest via structure

---

#### Thinking flow:

```text id="3ns8f1"
Single sequence → Multiple generated sequences → Heap to merge
```

#### Difference:

* Here sequences are **generated dynamically**
* Risk of duplicates (very important!)

---

### 6. **Brute Force**

### Idea:

* Check each number if ugly
* Count until nth

```python id="htl83r"
def isUgly(num):
    for p in [2,3,5]:
        while num % p == 0:
            num //= p
    return num == 1

def nthUglyNumber(n):
    count = 0
    num = 1
    
    while True:
        if isUgly(num):
            count += 1
            if count == n:
                return num
        num += 1
```

#### Complexity:

* Very slow (`O(n * log num)`)

---

### 7. **Optimal Solution (Heap)** ⭐

---

### 🔑 Core Idea:

* Start with `1`
* Each time:

  * pop smallest
  * generate `×2, ×3, ×5`
* Avoid duplicates using `set`

---

### ✅ Code

```python id="bd2c0z"
import heapq

def nthUglyNumber(n):
    heap = [1]
    seen = set([1])
    
    for _ in range(n):
        num = heapq.heappop(heap)
        
        for factor in [2, 3, 5]:
            new_num = num * factor
            
            if new_num not in seen:
                seen.add(new_num)
                heapq.heappush(heap, new_num)
    
    return num
```

---

### Complexity:

* Time: `O(n log n)`
* Space: `O(n)`

---

### ⚠️ Key Pitfall

Without `set`:

```python id="y1n6ox"
2×3 = 6
3×2 = 6  ← duplicate
```

👉 Heap will explode → TLE

---

### 8. **Step-by-Step Trace**

#### Input:

```python id="pw0v0s"
n = 5
```

---

| Step | Heap            | Pop | Push    | Result |
| ---- | --------------- | --- | ------- | ------ |
| 1    | [1]             | 1   | 2,3,5   | 1      |
| 2    | [2,3,5]         | 2   | 4,6,10  | 2      |
| 3    | [3,4,5,6,10]    | 3   | 9,15    | 3      |
| 4    | [4,5,6,9,10,15] | 4   | 8,12,20 | 4      |
| 5    | [...]           | 5   | 25      | 5      |

---

### 9. **Related Problems**

1. Super Ugly Number
   → Same idea, more primes

2. Merge k Sorted Lists
   → Heap merging pattern

3. Kth Smallest Element in a Sorted Matrix
   → K-th smallest via heap

4. Find K Pairs with Smallest Sums
   → Heap with generated states

---

## ⚡ Final Interview Takeaway

* Pattern:

  ```
  Generate sorted sequence → Min Heap + Deduplication
  ```

* Core idea:

```python
num → num*2, num*3, num*5
```

* MUST:

  * Use `set` to avoid duplicates

---

## 🚀 Bonus (VERY IMPORTANT)

👉 Better solution exists (DP with 3 pointers) → `O(n)`

If interviewer pushes:

> “Can you optimize further?”

You should switch immediately.

---

If you want, I can break down:

* 🔥 **DP 3-pointer solution (most asked follow-up)**
* 🔥 Why heap is NOT optimal here (important insight)
* 🔥 Pattern mapping across all “k-th generated number” problems
