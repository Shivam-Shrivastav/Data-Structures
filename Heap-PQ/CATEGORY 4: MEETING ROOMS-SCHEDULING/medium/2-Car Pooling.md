## 🧠 LeetCode: **Car Pooling** (Heap / Sweep Line)

---

## 1. **Problem Statement**

You are given a list of trips:

```
trips[i] = [numPassengers, from, to]
```

* `numPassengers` people get in at location `from`
* They get off at location `to`
* Car moves in **one direction only (east)**

👉 You are given `capacity`

👉 Return **true** if you can pick up and drop off all passengers without exceeding capacity at any time.

---

### Constraints

* `1 <= trips.length <= 1000`
* `0 <= from < to <= 1000`
* `1 <= numPassengers <= 100`

---

## 2. **Diagram (Heap Timeline)**

```text
Trips:
[2,1,5], [3,3,7]

Location timeline:

0---1---2---3---4---5---6---7

At 1 → +2 passengers
At 3 → +3 passengers
At 5 → -2 passengers
At 7 → -3 passengers
```

👉 Track active passengers using **min-heap (drop times)**

---

## 3. **Example I/O**

### ✅ Example 1

```text
Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
```

✔ At location 3 → total = 5 > 4 → ❌

---

### ✅ Example 2

```text
Input: trips = [[2,1,5],[3,5,7]], capacity = 3
Output: true
```

✔ First group leaves before second enters

---

### ⚠️ Edge Case

```text
Input: [[3,2,7]], capacity = 3
Output: true
```

✔ Exactly fits capacity

---

## 4. **Intuition & Pattern Recognition**

### 🔑 Signals:

* Intervals `[from, to)`
* Need to track **overlapping load**
* Capacity constraint

👉 This is **interval overlap + running sum**

---

### 💡 Heap Approach Idea:

* Sort trips by start location
* Use **min-heap** storing `(end, passengers)`
* At each trip:

  * Remove finished trips
  * Add new passengers
  * Check capacity

---

### 🧠 Interview Thought:

> "This is like meeting rooms / overlapping intervals → track active intervals using heap"

---

## 5. **Simpler Version**

### 🔹 Simpler Problem:

👉 “Maximum number of overlapping intervals”

📌 Example:

* Find peak overlapping intervals

---

### 🔹 Related Problems:

* Meeting Rooms II
* Number of Platforms Required

---

### 🔥 Transition Thinking:

```text
Simpler:
→ count overlaps

This problem:
→ instead of count → sum of passengers
→ constraint: sum <= capacity
```

---

## 6. **Brute Force**

### Idea:

* For each location from 0 → 1000
* Track how many passengers are inside

### Complexity:

* Time: **O(n * maxLocation)**
* Space: O(1)

---

## 7. **Optimal Solution (Heap)**

### Steps:

1. Sort trips by `from`
2. Use min-heap (by `to`)
3. Track current passengers

---

### ✅ Code (Python)

```python
import heapq

def carPooling(trips, capacity):
    trips.sort(key=lambda x: x[1])  # sort by start
    
    min_heap = []  # (end, passengers)
    curr_passengers = 0
    
    for passengers, start, end in trips:
        
        # remove passengers who have reached destination
        while min_heap and min_heap[0][0] <= start:
            drop_end, drop_pass = heapq.heappop(min_heap)
            curr_passengers -= drop_pass
        
        # pick up new passengers
        curr_passengers += passengers
        
        # check capacity
        if curr_passengers > capacity:
            return False
        
        # push current trip
        heapq.heappush(min_heap, (end, passengers))
    
    return True
```

---

### ⏱ Complexity:

* Time: **O(n log n)**
* Space: **O(n)**

---

## 8. **Step-by-Step Trace**

### Input:

```text
trips = [[2,1,5],[3,3,7]], capacity = 4
```

---

| Step            | Action | Heap          | Current Passengers |
| --------------- | ------ | ------------- | ------------------ |
| Start           | —      | []            | 0                  |
| Trip1 (1→5, +2) | add    | [(5,2)]       | 2                  |
| Trip2 (3→7, +3) | add    | [(5,2),(7,3)] | 5 ❌                |

👉 Capacity exceeded → return False

---

## 9. **Related Problems**

### 🟢 Easy → Medium → Hard

1. **Meeting Rooms II**

   * Count overlapping intervals

2. **Number of Platforms**

   * Same idea in trains

3. **Maximum Number of Events That Can Be Attended**

   * Greedy + heap scheduling

4. **Minimum Number of Arrows to Burst Balloons**

   * Interval greedy

5. **Range Addition**

   * Difference array version of same idea

---

## 🧠 Final Interview Insight

👉 Core idea:

> "At any point, total active passengers must not exceed capacity"

👉 Pattern:

* Interval overlap + min heap (drop earliest first)

---

## ⚡ Bonus (Better Approach — No Heap)

👉 Use **difference array / prefix sum**

```python
def carPooling(trips, capacity):
    timeline = [0] * 1001
    
    for passengers, start, end in trips:
        timeline[start] += passengers
        timeline[end] -= passengers
    
    curr = 0
    for t in timeline:
        curr += t
        if curr > capacity:
            return False
    
    return True
```

### 🚀 Complexity:

* Time: **O(maxLocation) = O(1000)**
* Space: **O(1000)**

---

If you want, I can also:

* Compare **Heap vs Prefix Sum → when to use which (interview trick)**
* OR give a **mental shortcut to instantly recognize sweep-line problems**
