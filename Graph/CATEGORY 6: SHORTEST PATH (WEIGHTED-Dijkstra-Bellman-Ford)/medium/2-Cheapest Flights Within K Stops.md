## 🔹 Problem: Cheapest Flights Within K Stops

---

### 1. **Problem Statement with Example**

You are given:

* `n` cities labeled `0 → n-1`
* `flights[i] = (u, v, price)` → flight from `u` to `v`
* `src`, `dst`, and `k` (max stops allowed)

👉 Return the **minimum cost** from `src` to `dst` with **at most `k` stops**.
If not possible → return `-1`.

#### Constraints:

* `1 ≤ n ≤ 100`
* `0 ≤ flights.length ≤ n²`
* `0 ≤ k < n`

---

### 2. **Diagram**

```
Flights:
0 → 1 (100)
1 → 2 (100)
0 → 2 (500)

Graph:

     100        100
0 --------> 1 --------> 2
 \                        ^
  \________500___________/

Paths from 0 → 2:
- Direct: cost = 500
- Via 1: cost = 200 (1 stop) ✅
```

---

### 3. **Example I/O**

#### Example 1 (Typical)

```
Input:
n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1

Output: 200
```

---

#### Example 2 (Edge Case)

```
Input:
n = 3
flights = [[0,1,100],[1,2,100]]
src = 0, dst = 2, k = 0

Output: -1
```

👉 Cannot use 1 stop → no path

---

### 4. **Intuition & Pattern Recognition**

💡 Key signals:

* Weighted graph
* Shortest path
* **Constraint on number of stops (k)**

👉 This breaks vanilla Dijkstra ❌

---

### Why normal Dijkstra fails?

Dijkstra minimizes **cost only**,
but here we must also track **stops**.

👉 A cheaper path might use **more stops (invalid)**

---

### Correct pattern:

👉 **Dijkstra with state OR BFS + cost tracking**

State = `(node, cost, stops)`

---

### 5. **Simpler Version**

#### Step 1: No stop constraint

👉 Classic shortest path → Dijkstra

#### Step 2: Add constraint

👉 Now we must track stops → **extra dimension**

---

### Simpler related problems:

* **Network Delay Time** → pure Dijkstra
* **Minimum Obstacle Removal** → 0-1 BFS
* **This problem** → Dijkstra + constraint

---

### Thinking shift:

```
Normal: dist[node]
Now: dist[node][stops]
```

---

### 6. **Brute Force**

👉 Try all paths up to k stops (DFS)

* Explore all possible paths
* Track min cost

❌ Time: Exponential
❌ Not feasible

---

### 7. **Optimal Solution (Modified Dijkstra / BFS)**

👉 Best interview approach: **BFS + pruning**

```python
from collections import defaultdict, deque

def findCheapestPrice(n, flights, src, dst, k):
    graph = defaultdict(list)
    
    for u, v, w in flights:
        graph[u].append((v, w))
    
    # (node, cost, stops)
    queue = deque([(src, 0, 0)])
    
    # min cost to reach node with <= stops
    dist = [float('inf')] * n
    dist[src] = 0
    
    while queue:
        node, cost, stops = queue.popleft()
        
        if stops > k:
            continue
        
        for nei, price in graph[node]:
            new_cost = cost + price
            
            # only proceed if better cost
            if new_cost < dist[nei]:
                dist[nei] = new_cost
                queue.append((nei, new_cost, stops + 1))
    
    return dist[dst] if dist[dst] != float('inf') else -1
```

---

### ⚠️ Important Note:

* This works because:

  * We limit stops
  * We prune worse paths

---

### Alternative (Safer): Dijkstra with stops

```python
import heapq
from collections import defaultdict

def findCheapestPrice(n, flights, src, dst, k):
    graph = defaultdict(list)
    
    for u, v, w in flights:
        graph[u].append((v, w))
    
    heap = [(0, src, 0)]  # (cost, node, stops)
    
    while heap:
        cost, node, stops = heapq.heappop(heap)
        
        if node == dst:
            return cost
        
        if stops > k:
            continue
        
        for nei, price in graph[node]:
            heapq.heappush(heap, (cost + price, nei, stops + 1))
    
    return -1
```

---

### Complexity:

* Time: **O(E log V)** (heap version)
* Space: **O(V + E)**

---

### 8. **Step-by-Step Trace**

Input:

```
0 → 1 (100)
1 → 2 (100)
0 → 2 (500)
k = 1
```

| Step | Heap                  | Node        | Cost | Stops |
| ---- | --------------------- | ----------- | ---- | ----- |
| 1    | [(0,0,0)]             | start       | 0    | 0     |
| 2    | [(100,1,1),(500,2,1)] | from 0      |      |       |
| 3    | [(200,2,2),(500,2,1)] | from 1      |      |       |
| 4    | pop (200,2,2)         | reached dst |      |       |

✅ Answer = 200

---

### 9. **Related Problems**

1. **Network Delay Time**
   → Classic Dijkstra (no constraints)

2. **Minimum Cost to Reach Destination in Time**
   → Dijkstra with time constraint

3. **Shortest Path with Alternating Colors**
   → BFS + state

4. **Minimum Obstacle Removal to Reach Corner**
   → 0-1 BFS

5. **Bellman-Ford (conceptual)**
   → Useful when constraints like `k` exist

---

## 🔥 Interview One-Liner

👉 *“This is a shortest path problem with an additional constraint (k stops), so I’ll use Dijkstra with (node, cost, stops) as state.”*

---

If you want, I can also show:

* 🔥 Why Bellman-Ford is actually the **cleanest theoretical solution** here
* 🔥 Common bug: using only `dist[node]` instead of tracking stops
