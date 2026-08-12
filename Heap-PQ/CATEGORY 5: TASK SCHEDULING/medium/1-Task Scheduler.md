## 🧠 LeetCode: Task Scheduler (Heap Pattern)

---

## 1. **Problem Statement with Example**

You are given a list of tasks represented by uppercase letters (A–Z) and a non-negative integer `n` representing the cooldown period.

Each task takes **1 unit time**, but between two same tasks, there must be at least `n` units of time.

👉 Return the **minimum time required** to complete all tasks.

### Example:

```
tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
```

One optimal schedule:

```
A → B → idle → A → B → idle → A → B
```

### Constraints:

* 1 ≤ tasks.length ≤ 10^4
* tasks[i] ∈ 'A' to 'Z'
* 0 ≤ n ≤ 100

---

## 2. **Diagram (Greedy + Heap Scheduling)**

```
Tasks frequency:
A → 3
B → 3

Max Heap:
[3(A), 3(B)]

Cycle size = n + 1 = 3

Cycle 1: A B idle
Cycle 2: A B idle
Cycle 3: A B

Timeline:
| A | B | _ | A | B | _ | A | B |
```

---

## 3. **Example I/O**

### ✅ Typical Case

```
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
```

✔ Need idle slots due to cooldown

---

### ⚠️ Edge Case (No cooldown)

```
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
```

✔ No idle needed → just execute sequentially

---

## 4. **Intuition & Pattern Recognition**

### 🔍 Signals:

* “Cooldown” → scheduling problem
* “Most frequent tasks first” → **Max Heap / Greedy**
* Want to minimize idle → fill slots optimally

### 💡 Core Idea:

* Always pick the **most frequent task first**
* Execute tasks in **chunks of size (n+1)**
* Why? → ensures spacing between same tasks

👉 If you can’t fill the chunk → idle slots required

---

## 5. **Simpler Version**

### 🔹 Simplest Problem:

👉 No cooldown → just count tasks → answer = len(tasks)

### 🔹 Slightly Harder:

👉 Arrange tasks so no two adjacent same (n=1)

Related:

* **Reorganize String**

### 🔹 This Problem:

* Generalized version with **distance = n**
* Instead of adjacency → spacing constraint

---

## 6. **Brute Force**

### Idea:

* Simulate time step by step
* At each time → pick any valid task (not in cooldown)

### Issues:

* Need to track cooldown for each task
* Try all possibilities → inefficient

### Complexity:

* Time: **O(N²)**
* Space: **O(26)**

---

## 7. **Optimal Solution (Max Heap + Greedy)**

### 🚀 Approach:

1. Count frequencies
2. Push into **max heap**
3. Process in cycles of size `n+1`
4. Use temp list to store used tasks
5. Push back remaining tasks

---

### ✅ Code (Python)

```python
import heapq
from collections import Counter

def leastInterval(tasks, n):
    freq = Counter(tasks)
    
    # max heap (negative values because Python has min heap)
    max_heap = [-cnt for cnt in freq.values()]
    heapq.heapify(max_heap)
    
    time = 0
    
    while max_heap:
        temp = []
        cycle = n + 1
        
        for _ in range(cycle):
            if max_heap:
                count = heapq.heappop(max_heap)
                if count + 1 < 0:  # still remaining
                    temp.append(count + 1)
            time += 1
            
            if not max_heap and not temp:
                break
        
        for item in temp:
            heapq.heappush(max_heap, item)
    
    return time
```

---

### ⏱ Complexity:

* Time: **O(N log 26) ≈ O(N)**
* Space: **O(26)**

---

## 8. **Step-by-Step Trace**

### Input:

```
tasks = ["A","A","A","B","B","B"], n = 2
```

### Initial Heap:

```
[-3, -3]
```

---

### Cycle 1 (n+1 = 3)

| Step | Heap    | Action | Temp    | Time |
| ---- | ------- | ------ | ------- | ---- |
| 1    | [-3,-3] | pop A  | [-2]    | 1    |
| 2    | [-3]    | pop B  | [-2,-2] | 2    |
| 3    | []      | idle   |         | 3    |

Push back → [-2, -2]

---

### Cycle 2

| Step | Heap    | Action | Temp    | Time |
| ---- | ------- | ------ | ------- | ---- |
| 1    | [-2,-2] | pop A  | [-1]    | 4    |
| 2    | [-2]    | pop B  | [-1,-1] | 5    |
| 3    | []      | idle   |         | 6    |

Push back → [-1, -1]

---

### Cycle 3

| Step | Heap    | Action | Temp | Time |
| ---- | ------- | ------ | ---- | ---- |
| 1    | [-1,-1] | pop A  | []   | 7    |
| 2    | [-1]    | pop B  | []   | 8    |

✔ Done

---

## 9. **Related Problems**

1. **Reorganize String**
   → Arrange characters so no two adjacent same (n=1 version)

2. ****
   → Same problem (this one)

3. ****
   → Heap + greedy for spacing

4. ****
   → Exact generalization of this problem

5. ****
   → Same idea with frequencies

---

## 🔥 Interview Takeaway

* If you see:

  * **cooldown / distance constraint**
  * **frequencies matter**

👉 Think:

> “Max heap + process in chunks of (n+1)”

---

If you want, I can also show the **O(1) math formula solution (no heap)** — which is even more optimal for interviews.
