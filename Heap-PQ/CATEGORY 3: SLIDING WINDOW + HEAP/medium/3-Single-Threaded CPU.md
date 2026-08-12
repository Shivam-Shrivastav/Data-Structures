## ⚙️ Single-Threaded CPU (Heap + Sorting Pattern)

---

## 1. Problem Statement with Example

You are given `tasks`, where each task is:

```
tasks[i] = [enqueueTime, processingTime]
```

CPU rules:

* CPU is **single-threaded**
* It can process **only one task at a time**
* If idle → pick available task with:

  1. **smallest processingTime**
  2. if tie → **smallest index**
* If no task is available → jump time to next task

👉 Return the **order of processing indices**

---

### Example

```text
Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
Output: [0,2,3,1]
```

---

## 2. Diagram

```text
Tasks (enqueue, process, index):
[1,2,0], [2,4,1], [3,2,2], [4,1,3]

Time = 1 → task 0 available → pick it → finish at 3

Time = 3 → tasks 1 & 2 available  
Pick smallest processing → task 2 → finish at 5

Time = 5 → tasks 1 & 3 available  
Pick smallest → task 3 → finish at 6

Time = 6 → task 1 → finish

Order: [0,2,3,1]
```

---

## 3. Example I/O

### Example 1 (Typical)

```text
Input: [[1,2],[2,4],[3,2],[4,1]]
Output: [0,2,3,1]
```

### Example 2 (CPU idle case)

```text
Input: [[5,2],[6,1]]
Output: [0,1]

Explanation:
CPU jumps from time 0 → 5
```

---

## 4. Intuition & Pattern Recognition

### 🔑 Key Signals:

* “Process tasks in order of priority” → **Heap**
* “Tasks arrive over time” → **Sorting + Simulation**
* “Always pick best available task” → **Min Heap**

### 🧠 Interview Thought:

> “This is like scheduling → sort by arrival + heap for processing priority”

---

## 5. Simpler Version

### Simpler Problem:

👉 “Given all tasks available at once, pick smallest processing time”

→ Just use a heap

### Build-up Thinking:

```text
No arrival time → simple heap  
With arrival time → need sorting + simulation  
Dynamic arrival → push into heap as time progresses
```

### Related Simpler Problems:

* **Kth Smallest Element**
* **Merge K Sorted Lists**
* **Task Scheduler (LC)**

---

## 6. Brute Force

### Idea:

* At every time:

  * scan all tasks
  * find best available

```python
def getOrder(tasks):
    n = len(tasks)
    used = [False]*n
    time = 0
    res = []

    while len(res) < n:
        best = -1
        for i in range(n):
            if not used[i] and tasks[i][0] <= time:
                if best == -1 or tasks[i][1] < tasks[best][1] or \
                   (tasks[i][1] == tasks[best][1] and i < best):
                    best = i

        if best == -1:
            time += 1
        else:
            used[best] = True
            time += tasks[best][1]
            res.append(best)

    return res
```

### Complexity

* Time: **O(n²)**
* Space: **O(n)**

---

## 7. Optimal Solution (Sort + Min Heap)

### Idea:

1. Add index to tasks
2. Sort by `enqueueTime`
3. Use min heap → `(processingTime, index)`
4. Simulate time

---

### Code

```python
import heapq

def getOrder(tasks):
    # attach index
    tasks = [(e, p, i) for i, (e, p) in enumerate(tasks)]
    tasks.sort()  # sort by enqueue time

    res = []
    heap = []
    time = 0
    i = 0
    n = len(tasks)

    while i < n or heap:
        # if no available tasks → jump time
        if not heap and time < tasks[i][0]:
            time = tasks[i][0]

        # push all available tasks
        while i < n and tasks[i][0] <= time:
            e, p, idx = tasks[i]
            heapq.heappush(heap, (p, idx))
            i += 1

        # process next task
        p, idx = heapq.heappop(heap)
        time += p
        res.append(idx)

    return res
```

---

### Complexity

* Time: **O(n log n)**
* Space: **O(n)**

---

## 8. Step-by-Step Trace

### Input:

```text
tasks = [[1,2],[2,4],[3,2],[4,1]]
```

### After sorting:

```text
[(1,2,0), (2,4,1), (3,2,2), (4,1,3)]
```

---

| Time | Available Tasks | Heap        | Pick | Result    |
| ---- | --------------- | ----------- | ---- | --------- |
| 1    | [0]             | (2,0)       | 0    | [0]       |
| 3    | [1,2]           | (2,2),(4,1) | 2    | [0,2]     |
| 5    | [1,3]           | (1,3),(4,1) | 3    | [0,2,3]   |
| 6    | [1]             | (4,1)       | 1    | [0,2,3,1] |

---

## 9. Related Problems

1. **Task Scheduler**
   → Scheduling + greedy decisions

2. **Meeting Rooms II**
   → Heap for overlapping intervals

3. **Merge K Sorted Lists**
   → Always pick smallest available

4. **Kth Smallest Element in Matrix**
   → Heap-based selection

5. **Process Tasks Using Servers**
   → Similar scheduling + multiple heaps

---

## ⚠️ Final Interview Notes

### 🔥 Core Pattern:

👉 **Sort + Heap + Simulation**

### Key Observations:

* Sort by arrival time
* Heap decides **which task next**
* Time moves dynamically

### Common Mistakes:

* Not jumping time when heap is empty ❌
* Forgetting index tie-breaker ❌
* Not pushing all available tasks ❌

---

If you want, I can also give:

* 🔥 **Dry run trick to derive solution in interview (very important)**
* OR compare with **Process Tasks Using Servers (harder version)**
