## 🧠 **Smallest Range Covering Elements from K Lists**

---

### 1. **Problem Statement with Example**

You are given `k` **sorted lists** of integers.

👉 Find the **smallest range [L, R]** such that:

* Each of the `k` lists contributes **at least one element inside the range**

---

#### Example:

```python id="g3x8pz"
Input:
nums = [
  [4,10,15,24,26],
  [0,9,12,20],
  [5,18,22,30]
]

Output: [20,24]
```

#### Why:

```text
List1 → 24
List2 → 20
List3 → 22
→ Range = [20,24]
```

---

### 2. **Diagram**

```text id="w5y9jm"
Lists:

L1:  4   10   15   24   26
L2:  0    9   12   20
L3:  5   18   22   30

We pick one from each:
(24,20,22)

Range:
min = 20, max = 24
```

👉 Maintain:

* Current **min (heap)**
* Current **max (variable)**

---

### 3. **Example I/O**

#### ✅ Example 1

```python id="vq4gk6"
Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
```

#### ⚠️ Example 2 (Edge)

```python id="u2d9o7"
Input: [[1],[2],[3]]
Output: [1,3]
```

---

### 4. **Intuition & Pattern Recognition**

👉 Signals:

* k sorted lists
* Need to cover all lists
* Optimize a range

💡 Key Insight:

* Always track:

  * **minimum element (heap)**
  * **maximum element (global)**

🧠 Interview thought:

> “This is like merging k lists but tracking a sliding window across lists”

---

### 5. **Simpler Version**

#### Simpler Problems:

* Merge k Sorted Lists
  → always pick smallest

* Find K Pairs with Smallest Sums
  → heap over combinations

---

#### Thinking flow:

```text id="7s2o6w"
Pick smallest → maintain max → update range → advance
```

#### Difference:

* Instead of building sorted list
* We maintain a **window covering all lists**

---

### 6. **Brute Force**

### Idea:

* Try all combinations (1 from each list)

```python id="qvlg0z"
# Exponential → not practical
```

❌ Impossible

---

### 7. **Optimal Solution (Heap)** ⭐

---

### 🔑 Core Idea:

1. Push first element from each list into heap
2. Track current **max**
3. Pop smallest → update range
4. Push next element from that list
5. Stop when any list ends

---

### ✅ Code

```python id="2pb0sd"
import heapq

def smallestRange(nums):
    heap = []
    current_max = float('-inf')
    
    # Step 1: initialize heap
    for i in range(len(nums)):
        val = nums[i][0]
        heapq.heappush(heap, (val, i, 0))
        current_max = max(current_max, val)
    
    best_range = [float('-inf'), float('inf')]
    
    while True:
        min_val, list_idx, idx = heapq.heappop(heap)
        
        # update best range
        if current_max - min_val < best_range[1] - best_range[0]:
            best_range = [min_val, current_max]
        
        # move forward in same list
        if idx + 1 == len(nums[list_idx]):
            break
        
        next_val = nums[list_idx][idx + 1]
        heapq.heappush(heap, (next_val, list_idx, idx + 1))
        
        current_max = max(current_max, next_val)
    
    return best_range
```

---

### Complexity:

* Time: `O(n log k)`
* Space: `O(k)`

---

### 8. **Step-by-Step Trace**

#### Input:

```python id="sfyfhq"
nums = [[4,10,15],[1,3,20],[5,6]]
```

---

#### Initial:

```text
Heap: [4,1,5]
Max = 5
Range = [1,5]
```

---

| Step | Pop | Push | New Max | Range  |
| ---- | --- | ---- | ------- | ------ |
| 1    | 1   | 3    | 5       | [3,5]  |
| 2    | 3   | 20   | 20      | [4,20] |
| 3    | 4   | 10   | 20      | [5,20] |

---

### 9. **Related Problems**

1. Merge k Sorted Lists
   → base heap merging

2. Kth Smallest Element in a Sorted Matrix
   → heap over sorted rows

3. Find K Pairs with Smallest Sums
   → heap + combinations

4. Ugly Number II
   → generate sorted stream

---

## ⚡ Final Interview Takeaway

### Pattern:

```
k sorted lists + global condition → Heap + Track max
```

---

### Core Loop:

```python id="0ygvnc"
min_val = heap.pop()
range = max - min
push next from same list
update max
```

---

### 🔥 Key Insight

> “You shrink the range from left (min), and expand from right (max) dynamically”

---

## 🚀 Mental Model

* Heap → gives smallest
* Variable → tracks largest
* Together → define current range

---

If you want next:

* 🔥 Why sliding window alone DOESN’T work here
* 🔥 Visual intuition (very powerful)
* 🔥 Common mistakes interviewers trap you with
