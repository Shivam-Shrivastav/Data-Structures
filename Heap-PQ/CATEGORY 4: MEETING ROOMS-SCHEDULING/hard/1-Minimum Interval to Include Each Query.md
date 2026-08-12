## 🧠 LeetCode: **Minimum Interval to Include Each Query** (Heap + Sweep Line)

---

## 1. **Problem Statement**

You are given:

* `intervals[i] = [left, right]`
* `queries[j]`

👉 For each query, find the **size of the smallest interval** such that:

```text
left ≤ query ≤ right
```

👉 If no such interval exists → return `-1`

👉 Return answers in **same order as queries**

---

### Constraints

* `1 <= intervals.length, queries.length <= 10^5`
* `1 <= left ≤ right <= 10^7`

---

## 2. **Diagram (Sorted Sweep + Heap)**

```text
Intervals:
[1,4], [2,4], [3,6], [4,4]

Queries:
2, 3, 4

Sorted queries → process left → right
```

---

### Heap stores:

```text
(size, right)
where size = right - left + 1
```

---

### Flow:

```text
Query = 2:
→ add intervals starting ≤ 2 → [1,4], [2,4]
→ heap = [(4,4),(3,4)]
→ answer = 3

Query = 3:
→ add [3,6]
→ heap = [(3,4),(4,4),(4,6)]
→ answer = 3

Query = 4:
→ add [4,4]
→ heap = [(1,4),(3,4),(4,6)]
→ answer = 1
```

---

## 3. **Example I/O**

### ✅ Example 1

```text
Input:
intervals = [[1,4],[2,4],[3,6],[4,4]]
queries = [2,3,4]

Output:
[3,3,1]
```

✔ Smallest valid interval per query

---

### ⚠️ Example 2

```text
Input:
intervals = [[2,3],[2,5],[1,8],[20,25]]
queries = [2,19,5,22]

Output:
[2,-1,4,6]
```

✔ Query 19 → no interval → -1

---

### ⚠️ Edge Case

```text
intervals = [[5,5]]
queries = [1,5]

Output:
[-1,1]
```

---

## 4. **Intuition & Pattern Recognition**

### 🔑 Signals:

* Queries + intervals
* Need **smallest interval covering a point**
* Offline processing (queries independent)

👉 Classic **Sweep Line + Heap**

---

### 💡 Key Idea:

1. Sort intervals by `left`
2. Sort queries
3. For each query:

   * Add all intervals where `left ≤ query`
   * Remove intervals where `right < query`
   * Top of heap = smallest valid interval

---

### 🧠 Interview Thought:

> "For each query, dynamically maintain valid intervals → pick smallest → heap"

---

## 5. **Simpler Version**

### 🔹 Simpler Problem:

👉 “Check if a query lies inside any interval”

→ Just scan all intervals

---

### 🔹 Slightly harder:

👉 “Find any interval containing query”

→ still brute force

---

### 🔥 Transition Thinking:

```text
Simpler:
→ check existence

This problem:
→ need MINIMUM sized interval
→ dynamic filtering → heap needed
```

---

### 🔑 Core Leap:

* Not just existence → optimization (min size)
* Not static → queries processed in sorted order

---

## 6. **Brute Force**

### Idea:

* For each query:

  * Check all intervals
  * Find smallest valid

### Complexity:

* Time: **O(n * q)** ❌ too slow

---

## 7. **Optimal Solution (Heap + Sorting)**

---

### ✅ Code (Python)

```python
import heapq

def minInterval(intervals, queries):
    intervals.sort()
    
    # store (query, index)
    sorted_queries = sorted((q, i) for i, q in enumerate(queries))
    
    result = [-1] * len(queries)
    min_heap = []  # (size, right)
    
    i = 0
    n = len(intervals)
    
    for q, idx in sorted_queries:
        
        # add all intervals starting before query
        while i < n and intervals[i][0] <= q:
            left, right = intervals[i]
            size = right - left + 1
            heapq.heappush(min_heap, (size, right))
            i += 1
        
        # remove invalid intervals
        while min_heap and min_heap[0][1] < q:
            heapq.heappop(min_heap)
        
        # answer
        if min_heap:
            result[idx] = min_heap[0][0]
    
    return result
```

---

### ⏱ Complexity:

* Time: **O((n + q) log n)**
* Space: **O(n)**

---

## 8. **Step-by-Step Trace**

### Input:

```text
intervals = [[1,4],[2,4],[3,6],[4,4]]
queries = [2,3,4]
```

---

### Sorted:

```text
queries → [(2,0),(3,1),(4,2)]
```

---

| Query | Heap (size,right)   | Action | Answer |
| ----- | ------------------- | ------ | ------ |
| 2     | [(3,4),(4,4)]       | pick 3 | 3      |
| 3     | [(3,4),(4,4),(4,6)] | pick 3 | 3      |
| 4     | [(1,4),(3,4),(4,6)] | pick 1 | 1      |

---

## 9. **Related Problems**

1. **Maximum Number of Events That Can Be Attended**

   * Similar: process timeline + heap

2. **Car Pooling**

   * Interval overlap tracking

3. **Meeting Rooms II**

   * Active intervals via heap

4. **Find Right Interval**

   * Binary search on intervals

5. **Range Module**

   * Interval queries and updates

---

## 🧠 Final Interview Insight

👉 Core idea:

> "For each query, maintain all valid intervals and pick smallest → min heap"

---

### 🔥 Pattern Template

```text
1. Sort intervals
2. Sort queries
3. Sweep queries:
   → add valid intervals
   → remove invalid ones
   → heap top = answer
```

---

If you want, I can:

* 🔥 Compare this with **binary search + segment tree approach**
* OR give a **cheat sheet for all “query + interval” problems**
