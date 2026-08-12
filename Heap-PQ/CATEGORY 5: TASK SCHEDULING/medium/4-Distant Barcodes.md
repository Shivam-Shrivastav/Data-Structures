## 🧠 LeetCode: Distant Barcodes (Heap Pattern)

---

## 1. **Problem Statement with Example**

You are given an array `barcodes` where each element represents a barcode value.

👉 Rearrange the array so that **no two adjacent elements are equal**.

Return any valid arrangement.

---

### Example:

```text
barcodes = [1,1,1,2,2,2]
Output: [1,2,1,2,1,2]
```

---

### Constraints:

* 1 ≤ barcodes.length ≤ 10⁴
* 1 ≤ barcodes[i] ≤ 10⁴

---

## 2. **Diagram (Heap Greedy)**

```text
Input:
[1,1,1,2,2,2]

Frequencies:
1 → 3
2 → 3

Max Heap:
[3(1), 3(2)]

Process:
Step 1: pick 1,2
Step 2: pick 1,2
Step 3: pick 1,2

Result:
1 2 1 2 1 2
```

👉 Same as **Reorganize String**, just integers instead of chars

---

## 3. **Example I/O**

### ✅ Typical Case

```text
Input: [1,1,1,2,2,3]
Output: [1,2,1,2,1,3]
```

---

### ⚠️ Edge Case

```text
Input: [1]
Output: [1]
```

---

### ❗ Always Possible?

✔ Yes — problem guarantees a solution exists

---

## 4. **Intuition & Pattern Recognition**

### 🔍 Signals:

* “no adjacent equal” → **adjacency constraint**
* “rearrange array” → **greedy**
* “frequency matters” → **max heap**

---

### 💡 Core Idea:

👉 Always pick **top 2 most frequent elements**

Why?

* Avoids placing same element consecutively
* Distributes high-frequency elements

---

### 🧠 Interview Thought:

> “This is literally Reorganize String but with numbers.”

---

## 5. **Simpler Version**

### 🔹 Base Problem:

👉 Avoid adjacent duplicates

Same as:

* ****

---

### 🔹 More Complex:

👉 k distance apart

* ****

---

### 🔹 Even More:

👉 cooldown scheduling

* ****

---

### 🔥 Transition Thinking:

```
Reorganize String → no adjacent
Distant Barcodes → same
k-distance → gap ≥ k
Task Scheduler → gap via time
```

---

## 6. **Brute Force**

### Idea:

* Try all permutations
* Check validity

### Complexity:

* Time: **O(N!)** ❌
* Space: **O(N)**

---

## 7. **Optimal Solution (Max Heap)**

### 🚀 Approach:

1. Count frequencies
2. Build max heap `(freq, value)`
3. While heap has ≥ 2 elements:

   * Pop top 2
   * Append both
   * Push back if remaining
4. Handle last element

---

### ✅ Code (Python)

```python
import heapq
from collections import Counter

def rearrangeBarcodes(barcodes):
    freq = Counter(barcodes)
    
    max_heap = [(-cnt, val) for val, cnt in freq.items()]
    heapq.heapify(max_heap)
    
    result = []
    
    while len(max_heap) >= 2:
        count1, val1 = heapq.heappop(max_heap)
        count2, val2 = heapq.heappop(max_heap)
        
        result.append(val1)
        result.append(val2)
        
        if count1 + 1 < 0:
            heapq.heappush(max_heap, (count1 + 1, val1))
        if count2 + 1 < 0:
            heapq.heappush(max_heap, (count2 + 1, val2))
    
    if max_heap:
        result.append(max_heap[0][1])
    
    return result
```

---

### ⏱ Complexity:

* Time: **O(N log K)** (K = unique elements)
* Space: **O(K)**

---

## 8. **Step-by-Step Trace**

### Input:

```text
[1,1,1,2,2,2]
```

---

### Initial Heap:

```text
[(-3,1), (-3,2)]
```

---

### Steps:

| Step | Heap | Pick | Result        |
| ---- | ---- | ---- | ------------- |
| 1    | 1,2  | 1,2  | [1,2]         |
| 2    | 1,2  | 1,2  | [1,2,1,2]     |
| 3    | 1,2  | 1,2  | [1,2,1,2,1,2] |

✔ Done

---

## 9. **Related Problems**

1. ****
   → Exact same logic (string version)

2. ****
   → Generalized spacing

3. ****
   → Scheduling version

4. ****
   → Avoid repeated patterns

---

## 🔥 Interview Takeaway

👉 If you see:

* “no two adjacent equal”
* “rearrange”

Think:

> **Max Heap + pick top 2 elements**

---

## ⚡ Bonus (Even Better Approach — No Heap)

👉 Greedy placement:

1. Place most frequent element at **even indices**
2. Fill remaining elements

### Why it works:

* Even spacing guarantees no adjacency conflict

👉 This is **O(N)** and often preferred in interviews

---

If you want, I can give you a **single reusable template** that solves:

* Reorganize String
* Distant Barcodes
* k Distance Apart
* Task Scheduler

…with just small tweaks.
