## 🚌 LeetCode: Bus Routes (Graph / BFS)

---

### 1. **Problem Statement with Example**

You are given an array `routes` where:

* `routes[i]` = list of bus stops that the **i-th bus** repeats forever.

You are also given:

* `source` stop
* `target` stop

👉 You can:

* Board any bus at the `source`
* Travel along that bus route
* Switch buses at common stops

**Goal:**
Return the **minimum number of buses** required to go from `source` to `target`.
Return `-1` if impossible.

**Constraints (important for approach):**

* `1 <= routes.length <= 500`
* Each route can have up to 10⁵ stops (total stops large)
* Stops values can be large (not continuous)

---

### 2. **Diagram**

```
routes = [
  [1, 2, 7],      (Bus 0)
  [3, 6, 7]       (Bus 1)
]

Graph view:

Stop → Buses:
1 → [0]
2 → [0]
7 → [0,1]  <-- INTERSECTION (switch point)
3 → [1]
6 → [1]

Path:
1 → (Bus 0) → 7 → (switch to Bus 1) → 6
```

---

### 3. **Example I/O**

#### ✅ Example 1

```
Input:
routes = [[1,2,7],[3,6,7]]
source = 1
target = 6

Output: 2
```

**Explanation:**

* Take Bus 0 → reach stop 7
* Switch to Bus 1 → reach stop 6

---

#### ⚠️ Edge Case

```
Input:
routes = [[1,2,3]]
source = 1
target = 3

Output: 1
```

**Explanation:**

* Same bus, no switching needed

---

#### ❌ Impossible Case

```
Input:
routes = [[1,2,3],[4,5,6]]
source = 1
target = 6

Output: -1
```

---

### 4. **Intuition & Pattern Recognition**

💡 Key signals:

* “Minimum buses” → shortest path → **BFS**
* You can switch buses → **graph traversal**
* But nodes are tricky:

  * Stops? OR buses?

👉 Trick:
Treat **buses as nodes**, not stops.

Why?

* We count buses, not stops
* Moving within a bus is free
* Switching buses = cost +1

---

### 🧠 What to say in interview:

> “I’ll model this as a graph where each bus is a node. Two buses are connected if they share a stop. Then I’ll BFS from all buses that include the source.”

---

### 5. **Simpler Version**

#### 🟢 Simpler Problem:

👉 "Find shortest path in graph"

Example:

* Nodes = buses
* Edge = common stop

---

#### 🔗 Related simpler LC problems:

* **Number of Provinces** → connected components
* **Rotting Oranges** → BFS levels
* **Word Ladder** → BFS with transformation

---

#### 🚀 Transition thinking:

* Simple BFS → nodes = stops ❌ (too big)
* Optimize → nodes = buses ✅

---

### 6. **Brute Force**

👉 Try all paths:

* From source → try all buses → explore all stops → repeat

❌ Very inefficient

**Time Complexity:**
`O(N * stops * stops)` (explosion)

---

### 7. **Optimal Solution (BFS on Buses)**

#### 🔥 Key Idea:

* Build: `stop → buses` mapping
* BFS on buses
* Track:

  * visited buses
  * visited stops

---

### ✅ Code (Python)

```python
from collections import defaultdict, deque

def numBusesToDestination(routes, source, target):
    if source == target:
        return 0

    # Map: stop -> buses
    stop_to_buses = defaultdict(list)
    for bus, stops in enumerate(routes):
        for stop in stops:
            stop_to_buses[stop].append(bus)

    queue = deque()
    visited_buses = set()
    visited_stops = set([source])

    # Start from all buses available at source
    for bus in stop_to_buses[source]:
        queue.append((bus, 1))  # (bus, count)
        visited_buses.add(bus)

    while queue:
        bus, count = queue.popleft()

        for stop in routes[bus]:
            if stop == target:
                return count

            if stop in visited_stops:
                continue

            visited_stops.add(stop)

            for next_bus in stop_to_buses[stop]:
                if next_bus not in visited_buses:
                    visited_buses.add(next_bus)
                    queue.append((next_bus, count + 1))

    return -1
```

---

### ⏱ Complexity

* **Time:** `O(N * K)`
  (N buses, K stops per bus)

* **Space:** `O(N * K)`

---

### 8. **Step-by-Step Trace**

#### Input:

```
routes = [[1,2,7],[3,6,7]]
source = 1
target = 6
```

---

| Step  | Queue            | Visited Buses | Visited Stops |
| ----- | ---------------- | ------------- | ------------- |
| Init  | [(0,1)]          | {0}           | {1}           |
| Pop   | (0,1)            |               |               |
|       | stops: 1,2,7     |               |               |
| Add   | bus 1 from 7     | {0,1}         | {1,2,7}       |
| Queue | [(1,2)]          |               |               |
| Pop   | (1,2)            |               |               |
|       | stops: 3,6,7     |               |               |
| Hit   | stop 6 == target |               |               |

✅ Return `2`

---

### 9. **Related Problems**

1. **Word Ladder**
   → BFS where nodes are words, edges are transformations

2. **Rotting Oranges**
   → Multi-source BFS, level = time

3. **Minimum Genetic Mutation**
   → BFS with transformation rules

4. **Number of Provinces**
   → Graph connected components

5. **Shortest Path in Binary Matrix**
   → Grid BFS shortest path

---

## 🔥 Final Interview Insight

👉 The hardest part is:

> **Choosing the right graph representation**

* If you think in **stops → TLE risk**
* If you think in **buses → clean BFS**

---

If you want, I can also show:

* Optimized version using **bidirectional BFS**
* OR **graph compression trick** used in top submissions
