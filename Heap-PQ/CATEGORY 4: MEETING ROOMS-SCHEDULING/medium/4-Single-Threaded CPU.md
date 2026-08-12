## 🧠 LeetCode: **Single-Threaded CPU** (Heap / Simulation)

---

## 1. **Problem Statement**

You are given tasks:

```text
tasks[i] = [enqueueTime, processingTime]
```

CPU rules:

* CPU is **single-threaded**
* Picks task with:

  1. **Smallest processing time**
  2. If tie → **smallest index**
* If CPU is idle → jump to next available task time
* Once started → task runs to completion (no preemption)

👉 Return the **order of task execution (indices)**

---

### Constraints

* `1 <= tasks.length <= 10^5`
* `0 <= enqueueTime, processingTime <= 10^9`

---

## 2. **Diagram (Timeline + Heap)**

```text
Tasks:
[1,2], [2,4], [3,2], [4,1]

Time →
1----2----3----4----5----6----7

Heap stores: (processingTime, index)
```

---

### Flow:

```text
Time 1:
→ add task0 → heap=[(2,0)]
→ process → time=3

Time 3:
→ add task1, task2
→ heap=[(2,2),(4,1)]
→ pick smallest → task2
```

---

## 3. **Example I/O**

### ✅ Example 1

```text
Input:
tasks = [[1,2],[2,4],[3,2],[4,1]]

Output:
[0,2,3,1]
```

✔ CPU always picks shortest available job

---

### ⚠️ Example 2

```text
Input:
tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]

Output:
[4,3,2,0,1]
```

✔ All arrive same time → sort by processing time

---

### ⚠️ Edge Case

```text
Input:
[[10,3]]
Output:
[0]
```

✔ CPU waits till time 10

---

## 4. **Intuition & Pattern Recognition**

### 🔑 Signals:

* Tasks arriving over time
* Always pick **minimum processing time**
* Simulation required

👉 Classic **Shortest Job First (SJF)** scheduling

---

### 💡 Key Idea:

* Sort tasks by enqueue time
* Use **min heap** → `(processingTime, index)`
* Simulate time:

  * Add available tasks
  * Pick shortest job
  * If none → jump time

---

### 🧠 Interview Thought:

> "This is scheduling with arrival times → use heap to pick best available task"

---

## 5. **Simpler Version**

### 🔹 Simpler Problem:

👉 “Pick smallest element from array”

OR

👉 All tasks available at time 0

---

### 🔹 Related:

* Sort by processing time → done

---

### 🔥 Transition Thinking:

```text
Simpler:
→ all tasks available → just sort

This problem:
→ tasks arrive over time
→ need dynamic selection → heap
```

---

## 6. **Brute Force**

### Idea:

* At every time, scan all tasks to find best one

### Complexity:

* Time: **O(n^2)** ❌ too slow

---

## 7. **Optimal Solution (Heap + Simulation)**

---

### ✅ Code (Python)

```python
import heapq

def getOrder(tasks):
    n = len(tasks)
    
    # attach index
    indexed_tasks = [(et, pt, i) for i, (et, pt) in enumerate(tasks)]
    indexed_tasks.sort()
    
    result = []
    min_heap = []  # (processingTime, index)
    
    time = 0
    i = 0
    
    while i < n or min_heap:
        
        # if no task available → jump time
        if not min_heap and time < indexed_tasks[i][0]:
            time = indexed_tasks[i][0]
        
        # add all available tasks
        while i < n and indexed_tasks[i][0] <= time:
            et, pt, idx = indexed_tasks[i]
            heapq.heappush(min_heap, (pt, idx))
            i += 1
        
        # process next task
        pt, idx = heapq.heappop(min_heap)
        time += pt
        result.append(idx)
    
    return result
```

---

### ⏱ Complexity:

* Time: **O(n log n)**
* Space: **O(n)**

---

## 8. **Step-by-Step Trace**

### Input:

```text
tasks = [[1,2],[2,4],[3,2],[4,1]]
```

---

| Step  | Time          | Heap      | Action    | Result |
| ----- | ------------- | --------- | --------- | ------ |
| Start | 0             | []        | jump → 1  | []     |
| t=1   | [(2,0)]       | run task0 | [0]       |        |
| t=3   | [(2,2),(4,1)] | run task2 | [0,2]     |        |
| t=5   | [(1,3),(4,1)] | run task3 | [0,2,3]   |        |
| t=6   | [(4,1)]       | run task1 | [0,2,3,1] |        |

---

## 9. **Related Problems**

1. **Process Tasks Using Servers**

   * Same pattern: assign tasks using heap

2. **Meeting Rooms III**

   * Resource allocation + heap

3. **Task Scheduler**

   * CPU scheduling variant

4. **Maximum Number of Events That Can Be Attended**

   * Time + greedy + heap

5. **Car Pooling**

   * Sweep line + heap

---

## 🧠 Final Interview Insight

👉 Core idea:

> "At any time, choose the shortest available job → heap"

---

### 🔥 Pattern Template (IMPORTANT)

```text
1. Sort by arrival time
2. Use heap for best candidate
3. If heap empty → jump time
4. Process → update time
```

---

If you want, I can give:

* 🔥 A **unified template for ALL heap scheduling problems**
* OR a **pattern cheat sheet to instantly classify these problems in interviews**
