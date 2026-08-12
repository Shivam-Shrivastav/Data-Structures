## 🧠 LeetCode: **Maximum Number of Events That Can Be Attended** (Heap / Greedy)

---

## 1. **Problem Statement**

You are given an array `events`, where
`events[i] = [startDay, endDay]`.

* Each event can be attended **only once**
* You can attend **at most one event per day**
* You can attend an event on any day in `[startDay, endDay]`

👉 Return the **maximum number of events you can attend**

### Constraints

* `1 <= events.length <= 10^5`
* `1 <= startDay <= endDay <= 10^5`

---

## 2. **Diagram (Timeline + Min Heap)**

```
Events:
[1,2], [2,3], [3,4]

Day:   1    2    3    4
       |----|----|----|

Heap (stores end days):

Day 1 → add [1,2] → heap = [2]
        attend → pop → heap = []

Day 2 → add [2,3] → heap = [3]
        attend → pop

Day 3 → add [3,4] → heap = [4]
        attend → pop
```

👉 Always attend event that **ends earliest**

---

## 3. **Example I/O**

### ✅ Example 1 (Typical)

```
Input: events = [[1,2],[2,3],[3,4]]
Output: 3
```

✔ Attend one event per day sequentially

---

### ⚠️ Example 2 (Overlap Case)

```
Input: events = [[1,2],[1,2],[1,2]]
Output: 2
```

✔ Only 2 days available → max 2 events

---

### ⚠️ Edge Case

```
Input: [[1,100000]]
Output: 1
```

✔ Only one event → attend once

---

## 4. **Intuition & Pattern Recognition**

### 🔑 Signals:

* Interval scheduling problem
* Choose **maximum number of non-conflicting choices**
* Flexible scheduling within range

👉 Classic greedy + heap

---

### 💡 Key Idea:

* Process **day by day**
* Add all events starting today
* Remove expired events
* Attend event with **smallest end day**

👉 Why?

* Ends earliest → frees future days

---

### 🧠 Interview Thought:

> "I should always pick the event that finishes earliest among available ones → min heap"

---

## 5. **Simpler Version**

### 🔹 Simpler Problem:

👉 “Maximum number of non-overlapping intervals”

Example:
Pick intervals such that no overlap → sort by end

📌 Related: **Activity Selection Problem**

---

### 🔹 Difference:

| Simpler           | This Problem                 |
| ----------------- | ---------------------------- |
| Fixed interval    | Flexible day inside interval |
| Greedy on sorting | Need dynamic choice per day  |
| No heap           | Heap required                |

---

### 🔥 Transition Thinking:

```
Simpler: pick by earliest end

This problem:
→ same idea BUT
→ events can be attended on ANY valid day
→ need dynamic tracking → heap
```

---

## 6. **Brute Force**

### Idea:

* For each day, try all events
* Pick unused valid event

### Complexity:

* Time: **O(n * maxDay)** ❌ too slow
* Space: O(n)

---

## 7. **Optimal Solution (Heap + Greedy)**

### Steps:

1. Sort events by start day
2. Iterate day from 1 → maxDay
3. Add all events starting today to heap (store endDay)
4. Remove expired events (`end < day`)
5. Attend event with smallest endDay

---

### ✅ Code (Python)

```python
import heapq

def maxEvents(events):
    events.sort()  # sort by start day
    min_heap = []
    
    day = 0
    i = 0
    n = len(events)
    attended = 0
    
    while i < n or min_heap:
        # move to next available day
        if not min_heap:
            day = events[i][0]
        
        # add all events starting today
        while i < n and events[i][0] == day:
            heapq.heappush(min_heap, events[i][1])  # push end day
            i += 1
        
        # remove expired events
        while min_heap and min_heap[0] < day:
            heapq.heappop(min_heap)
        
        # attend event
        if min_heap:
            heapq.heappop(min_heap)
            attended += 1
        
        day += 1
    
    return attended
```

---

### ⏱ Complexity:

* Time: **O(n log n)**
* Space: **O(n)**

---

## 8. **Step-by-Step Trace**

### Input:

```
events = [[1,2],[2,3],[3,4]]
```

| Day | Heap (end days) | Action | Attended |
| --- | --------------- | ------ | -------- |
| 1   | [2]             | attend | 1        |
| 2   | [3]             | attend | 2        |
| 3   | [4]             | attend | 3        |

---

### 🔍 Another Case:

```
[[1,2],[1,2],[1,2]]
```

| Day | Heap    | Action | Attended |
| --- | ------- | ------ | -------- |
| 1   | [2,2,2] | attend | 1        |
| 2   | [2,2]   | attend | 2        |
| 3   | []      | stop   | 2        |

---

## 9. **Related Problems**

### 🟢 Easy → Medium → Hard progression

1. **Meeting Rooms II**

   * Count minimum rooms → similar heap usage

2. **Non-overlapping Intervals**

   * Greedy by end time → base idea

3. **Minimum Number of Arrows to Burst Balloons**

   * Interval merging with greedy

4. **Task Scheduler**

   * Greedy + priority queue scheduling

5. **Course Schedule III**

   * Heap + greedy with deadlines

---

## 🧠 Final Interview Insight

👉 Core idea:

> "Among all available events today → attend the one that ends earliest"

👉 Pattern:

* Interval scheduling + Min Heap
* Dynamic greedy decision

---

If you want, I can also show:

* **Why sorting by start (not end) is necessary here**
* OR a **dry run visualization trick to remember this forever**
