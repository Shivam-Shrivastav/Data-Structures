## 🧠 LeetCode: **Meeting Rooms III** (Heap + Simulation)

---

## 1. **Problem Statement**

You are given:

* `n` rooms labeled `0 → n-1`
* `meetings[i] = [start, end]`

Rules:

* Each meeting must be assigned a room
* If multiple rooms are free → pick **smallest room index**
* If no room is free → delay meeting until earliest room becomes free
* Delayed meeting keeps same duration

👉 Return the **room number that hosted the most meetings**
(if tie → smallest index)

---

### Constraints

* `1 <= n <= 100`
* `1 <= meetings.length <= 10^5`
* `0 <= start < end <= 10^9`

---

## 2. **Diagram (Two Heaps)**

```text
Rooms: 0, 1

Meetings:
[0,10], [1,5], [2,7], [3,4]

Time →
0----1----2----3----4----5----7----10

Heap1 (free rooms): [0,1]
Heap2 (busy rooms): [(endTime, room)]
```

---

### Flow:

```text
Time 0:
→ assign room 0 → busy = [(10,0)]

Time 1:
→ assign room 1 → busy = [(5,1),(10,0)]

Time 2:
→ no free room → wait till room 1 free at 5
→ new end = 5 + duration(5) = 10
```

---

## 3. **Example I/O**

### ✅ Example 1

```text
Input:
n = 2
meetings = [[0,10],[1,5],[2,7],[3,4]]

Output: 0
```

✔ Room 0 handles most meetings

---

### ⚠️ Example 2 (Tie case)

```text
Input:
n = 2
meetings = [[0,5],[5,10]]

Output: 0
```

✔ Both rooms same → return smallest index

---

### ⚠️ Edge Case

```text
n = 1
meetings = [[0,10],[1,2],[3,4]]

Output: 0
```

✔ Only one room → everything delayed

---

## 4. **Intuition & Pattern Recognition**

### 🔑 Signals:

* Resource allocation (rooms)
* Time simulation
* Need earliest available resource

👉 Classic **two heap problem**

---

### 💡 Key Idea:

We maintain:

1. **Free rooms heap** → min heap of room indices
2. **Busy rooms heap** → min heap of `(endTime, room)`

---

### 🧠 Interview Thought:

> "Always assign meeting to earliest available room → if none free, delay using earliest finishing room"

---

## 5. **Simpler Version**

### 🔹 Simpler Problems:

1. **Meeting Rooms I**

   * Check if overlap exists

2. **Meeting Rooms II**

   * Minimum number of rooms required

---

### 🔥 Transition Thinking:

```text
Meeting Rooms II:
→ count overlapping intervals

Meeting Rooms III:
→ simulate assignment
→ track WHICH room is used
→ handle delays
```

---

### 🔑 Key Upgrade:

* Not just count → track room usage
* Need **which room frees first → heap**

---

## 6. **Brute Force**

### Idea:

* Try assigning each meeting to every room
* Simulate delays manually

### Complexity:

* Time: **O(n * meetings)** ❌ too slow

---

## 7. **Optimal Solution (Two Heaps)**

---

### ✅ Code (Python)

```python
import heapq

def mostBooked(n, meetings):
    meetings.sort()
    
    free_rooms = list(range(n))  # available rooms
    heapq.heapify(free_rooms)
    
    busy_rooms = []  # (end_time, room)
    
    count = [0] * n  # meeting count per room
    
    for start, end in meetings:
        
        # free rooms that have finished before current meeting
        while busy_rooms and busy_rooms[0][0] <= start:
            end_time, room = heapq.heappop(busy_rooms)
            heapq.heappush(free_rooms, room)
        
        if free_rooms:
            # assign available room
            room = heapq.heappop(free_rooms)
            heapq.heappush(busy_rooms, (end, room))
        
        else:
            # delay meeting
            end_time, room = heapq.heappop(busy_rooms)
            duration = end - start
            new_end = end_time + duration
            heapq.heappush(busy_rooms, (new_end, room))
        
        count[room] += 1
    
    # return room with max meetings (smallest index if tie)
    return count.index(max(count))
```

---

### ⏱ Complexity:

* Time: **O(m log n)**
* Space: **O(n)**

---

## 8. **Step-by-Step Trace**

### Input:

```text
n = 2
meetings = [[0,10],[1,5],[2,7],[3,4]]
```

---

| Step   | Action         | Free Rooms | Busy Rooms      | Count |
| ------ | -------------- | ---------- | --------------- | ----- |
| Start  | —              | [0,1]      | []              | [0,0] |
| [0,10] | assign room 0  | [1]        | [(10,0)]        | [1,0] |
| [1,5]  | assign room 1  | []         | [(5,1),(10,0)]  | [1,1] |
| [2,7]  | delay → room 1 | []         | [(10,0),(10,1)] | [1,2] |
| [3,4]  | delay → room 0 | []         | [(10,1),(11,0)] | [2,2] |

---

👉 Final count = `[2,2]` → return `0`

---

## 9. **Related Problems**

1. **Meeting Rooms II**

   * Same heap idea, but counting rooms

2. **Car Pooling**

   * Interval overlap + heap

3. **Maximum Number of Events That Can Be Attended**

   * Greedy + heap scheduling

4. **Task Scheduler**

   * Scheduling with constraints

5. **Process Tasks Using Servers**

   * Very similar → assign tasks to servers

---

## 🧠 Final Interview Insight

👉 Core idea:

> "Use one heap for free resources, one for busy resources sorted by earliest release time"

---

### 🔥 Pattern Summary:

* Two Heaps:

  * Free → min(room index)
  * Busy → min(end time)

---

If you want, I can:

* Show **why sorting by start time is critical**
* OR give a **template to solve ANY “resource allocation with delay” problem**
