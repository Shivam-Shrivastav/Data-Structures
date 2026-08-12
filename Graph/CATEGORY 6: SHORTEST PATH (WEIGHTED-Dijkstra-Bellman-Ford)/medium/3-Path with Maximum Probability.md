## 🔹 Problem: Path with Maximum Probability

---

### 1. **Problem Statement with Example**

You are given:

* `n` nodes (0 → n-1)
* `edges[i] = (u, v)` → undirected edge
* `succProb[i]` → probability of success for that edge
* `start`, `end`

👉 Return the **maximum probability** of reaching `end` from `start`.

* If no path exists → return `0`

#### Key twist:

* Instead of **sum**, we maximize **product of probabilities**

---

### 2. **Diagram**

```
Edges:
0 --(0.5)-- 1 --(0.5)-- 2
 \                         ^
  \------(0.2)------------/

Paths from 0 → 2:

1. 0 → 2 = 0.2
2. 0 → 1 → 2 = 0.5 * 0.5 = 0.25 ✅
```

👉 Choose path with **maximum product**

---

### 3. **Example I/O**

#### Example 1 (Typical)

```
Input:
n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0, end = 2

Output: 0.25
```

---

#### Example 2 (Edge Case)

```
Input:
n = 3
edges = [[0,1]]
succProb = [0.5]
start = 0, end = 2

Output: 0.0
```

👉 No path exists

---

### 4. **Intuition & Pattern Recognition**

💡 Key signals:

* Graph
* Weighted edges
* Need **optimal path**
* But operation = **multiplication**

---

### Trick 🔥

👉 Convert thinking:

| Normal shortest path | This problem     |
| -------------------- | ---------------- |
| Minimize sum         | Maximize product |

---

### Key insight:

👉 Use **Dijkstra but maximize instead of minimize**

* Instead of min heap → use **max heap**
* Instead of distance → store **probability**

---

### Interview thought:

👉 *“This is a variation of Dijkstra where I maximize probability instead of minimizing distance.”*

---

### 5. **Simpler Version**

#### Step 1: BFS

* If all probabilities = same → BFS

#### Step 2: Dijkstra (sum)

* Minimize cost

#### Step 3: This problem

* Maximize product → **modified Dijkstra**

---

### Related simpler problems:

* **Network Delay Time** → sum minimization
* **Swim in Rising Water** → max-edge minimization
* **This problem** → product maximization

---

### 6. **Brute Force**

👉 Try all paths

* Compute product for each
* Take maximum

❌ Time: Exponential
❌ Not feasible

---

### 7. **Optimal Solution (Max Heap Dijkstra)**

```python
import heapq
from collections import defaultdict

def maxProbability(n, edges, succProb, start, end):
    graph = defaultdict(list)
    
    # build graph
    for (u, v), p in zip(edges, succProb):
        graph[u].append((v, p))
        graph[v].append((u, p))
    
    # max heap → use negative probability
    heap = [(-1.0, start)]  # (probability, node)
    
    prob = [0.0] * n
    prob[start] = 1.0
    
    while heap:
        curr_prob, node = heapq.heappop(heap)
        curr_prob = -curr_prob
        
        # early stop
        if node == end:
            return curr_prob
        
        for nei, edge_prob in graph[node]:
            new_prob = curr_prob * edge_prob
            
            # relax condition (maximize)
            if new_prob > prob[nei]:
                prob[nei] = new_prob
                heapq.heappush(heap, (-new_prob, nei))
    
    return 0.0
```

---

### Complexity:

* Time: **O(E log V)**
* Space: **O(V + E)**

---

### 8. **Step-by-Step Trace**

Input:

```
0 --0.5-- 1 --0.5-- 2
 \--------0.2-------/
```

| Step | Heap               | Node        | Prob |
| ---- | ------------------ | ----------- | ---- |
| 1    | [(1.0,0)]          | start       | 1.0  |
| 2    | [(0.5,1),(0.2,2)]  | from 0      |      |
| 3    | [(0.25,2),(0.2,2)] | from 1      |      |
| 4    | pop (0.25,2)       | reached end |      |

✅ Answer = **0.25**

---

### 9. **Related Problems**

1. **Network Delay Time**
   → Minimize sum (classic Dijkstra)

2. **Path With Minimum Effort**
   → Minimize max edge

3. **Swim in Rising Water**
   → Minimize max weight

4. **Cheapest Flights Within K Stops**
   → Dijkstra + constraint

5. **Minimum Obstacle Removal to Reach Corner**
   → 0-1 BFS

---

## 🔥 Interview One-Liner

👉 *“This is a Dijkstra variant where instead of minimizing distance, I maximize probability using a max heap.”*

---

### 🧠 Extra Insight (VERY IMPORTANT)

👉 You can also transform:

```
maximize (p1 * p2 * p3)
= minimize (-log p1 + -log p2 + -log p3)
```

➡️ Converts to standard Dijkstra

---

If you want next level:

* I can give you a **1-page cheat sheet for all graph shortest path patterns**
* Or a **decision tree to pick BFS vs 0-1 BFS vs Dijkstra instantly**
