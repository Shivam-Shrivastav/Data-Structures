## 🔹 Problem: Network Delay Time

---

### 1. **Problem Statement with Example**

You are given:

* `times[i] = (u, v, w)` → signal from node `u` to `v` takes `w` time
* `n` nodes labeled `1 → n`
* A starting node `k`

👉 Return the **minimum time** for all nodes to receive the signal.
If impossible → return `-1`.

---

### 2. **Diagram**

```
Edges:
1 → 2 (1)
1 → 3 (4)
2 → 3 (2)

Graph:

     (1)
   /     \
  2       3
   \     ^
    (2) (4)

Shortest paths from node 1:
1 → 2 = 1
1 → 3 = min(4, 1+2) = 3
```

---

### 3. **Example I/O**

#### Example 1 (Typical)

```
Input:
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4, k = 2

Output: 2
```

Explanation:

* 2 → 1 = 1
* 2 → 3 = 1
* 2 → 4 = 2
  👉 Max time = 2

---

#### Example 2 (Edge Case)

```
Input:
times = [[1,2,1]]
n = 2, k = 2

Output: -1
```

👉 Node 1 never receives signal

---

### 4. **Intuition & Pattern Recognition**

💡 Key signals:

* Directed graph
* Weighted edges
* Need **shortest time to all nodes**

👉 This is classic: **Single Source Shortest Path**

---

### Pattern decision:

| Condition        | Algorithm      |
| ---------------- | -------------- |
| Unweighted graph | BFS            |
| Weights = 0/1    | 0-1 BFS        |
| Positive weights | **Dijkstra ✅** |

---

### Interview Thinking:

👉 “I need shortest path from one node to all → Dijkstra”

---

### 5. **Simpler Version**

#### Step 1: BFS version

👉 If all weights = 1
→ just BFS

#### Step 2: Weighted version

👉 Now weights differ
→ BFS breaks

#### Step 3: General solution

👉 Use **Dijkstra (min heap)**

---

### Related simpler LeetCode:

* **Shortest Path in Binary Matrix** → BFS
* **Minimum Obstacle Removal** → 0-1 BFS
* **This problem** → full Dijkstra

---

### 6. **Brute Force**

👉 Try all paths (DFS)

* Explore every possible path
* Track minimum distance

❌ Time: Exponential
❌ Not feasible

---

### 7. **Optimal Solution (Dijkstra)**

```python
import heapq
from collections import defaultdict

def networkDelayTime(times, n, k):
    graph = defaultdict(list)
    
    # build adjacency list
    for u, v, w in times:
        graph[u].append((v, w))
    
    min_heap = [(0, k)]  # (time, node)
    dist = {}
    
    while min_heap:
        time, node = heapq.heappop(min_heap)
        
        # already visited with shorter path
        if node in dist:
            continue
        
        dist[node] = time
        
        for nei, wt in graph[node]:
            if nei not in dist:
                heapq.heappush(min_heap, (time + wt, nei))
    
    # if not all nodes reached
    if len(dist) != n:
        return -1
    
    return max(dist.values())
```

---

### Complexity:

* Time: **O(E log V)**
* Space: **O(V + E)**

---

### 8. **Step-by-Step Trace**

Input:

```
times = [[2,1,1],[2,3,1],[3,4,1]]
k = 2
```

| Step | Heap          | Node    | Dist Map          |
| ---- | ------------- | ------- | ----------------- |
| 1    | [(0,2)]       | start   | {}                |
| 2    | [(1,1),(1,3)] | visit 2 | {2:0}             |
| 3    | [(1,3)]       | visit 1 | {2:0,1:1}         |
| 4    | [(2,4)]       | visit 3 | {2:0,1:1,3:1}     |
| 5    | []            | visit 4 | {2:0,1:1,3:1,4:2} |

👉 Answer = max = **2**

---

### 9. **Related Problems**

1. **Cheapest Flights Within K Stops**
   → Dijkstra + constraint (stops)

2. **Path With Minimum Effort**
   → Minimize max edge → modified Dijkstra

3. **Swim in Rising Water**
   → Grid + priority queue

4. **Minimum Cost to Reach City With Discounts**
   → Dijkstra + state

5. **Minimum Obstacle Removal to Reach Corner**
   → Special case → 0-1 BFS

---

## 🔥 Interview One-Liner

👉 *“This is a single-source shortest path problem with positive weights, so I’ll use Dijkstra’s algorithm with a min-heap.”*

---

If you want next level:

* I can show **when NOT to use Dijkstra (Bellman-Ford cases)**
* Or give a **mental template to identify graph patterns instantly**
