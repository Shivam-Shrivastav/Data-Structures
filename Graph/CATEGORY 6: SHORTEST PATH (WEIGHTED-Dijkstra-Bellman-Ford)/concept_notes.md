# Weighted Graph Pattern: Dijkstra & Bellman-Ford

---

# 1. Pattern in One Minute

### Core Idea

This pattern solves **Single Source Shortest Path (SSSP)** in a **weighted graph**.

There are two major algorithms:

| Algorithm        | Handles Negative Weights | Detects Negative Cycle | Time               |
| ---------------- | ------------------------ | ---------------------- | ------------------ |
| **Dijkstra**     | ❌ No                     | ❌                      | **O((V+E) log V)** |
| **Bellman-Ford** | ✅ Yes                    | ✅                      | **O(VE)**          |

---

### Why does this pattern exist?

BFS works only when every edge has the same weight.

Once edge costs differ, we need algorithms that minimize

> total path cost

instead of

> number of edges.

---

### Immediately think of it when

* shortest path
* minimum cost
* cheapest route
* weighted graph
* network delay
* flight prices
* road distances

---

# 2. Recognition Signals

## Use Dijkstra when

✓ Edge weights are **non-negative**

✓ Need shortest distance

✓ Weighted graph

✓ Fast solution required

Examples

* Network Delay Time
* Path With Minimum Effort
* Cheapest route (without negative cost)

---

## Use Bellman-Ford when

✓ Negative edge weights exist

✓ Need to detect negative cycle

✓ Currency arbitrage

✓ Graph may contain penalties

---

## Don't use these when

* Graph unweighted → BFS
* All-pairs shortest path → Floyd Warshall
* Need MST → Prim/Kruskal

---

# 3. Mental Model

## Dijkstra

Imagine water spreading.

The closest node is finalized first.

```
Start

0

↓

2

↓

5

↓

7
```

Once a node becomes the smallest available distance,

its answer never changes.

Repeat

> Pick closest unfinished node.

Relax all neighbors.

---

### Why it fails on negative edges

A shorter path may appear later because of

```
5
↓

-10
```

which breaks the greedy property.

---

## Bellman-Ford

Instead of greedily picking nodes,

keep improving every edge.

```
Repeat V-1 times

u ----3----> v

if dist[u]+3 < dist[v]

update
```

Every iteration allows shortest paths with one more edge.

After V−1 iterations,

all shortest paths are found.

One more iteration

↓

Still changes?

↓

Negative cycle exists.

---

# 4. Boilerplate Templates

## Dijkstra

```python
from heapq import heappush, heappop

def dijkstra(n, graph, src):
    INF = float('inf')
    dist = [INF] * n
    dist[src] = 0

    pq = [(0, src)]   # (distance, node)

    while pq:
        d, node = heappop(pq)

        if d > dist[node]:
            continue

        for nei, wt in graph[node]:
            nd = d + wt

            if nd < dist[nei]:
                dist[nei] = nd
                heappush(pq, (nd, nei))

    return dist
```

---

## Bellman-Ford

```python
def bellman_ford(n, edges, src):
    INF = float('inf')
    dist = [INF] * n
    dist[src] = 0

    for _ in range(n - 1):
        updated = False

        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True

        if not updated:
            break

    # Detect negative cycle
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            return None  # Negative cycle

    return dist
```

---

# 5. Variations

| Variation            | Change                                               |
| -------------------- | ---------------------------------------------------- |
| Directed graph       | Use given direction only                             |
| Undirected graph     | Add both edges                                       |
| Return shortest path | Store `parent[]`                                     |
| Multi-source         | Push all sources with distance 0                     |
| Count shortest paths | Maintain `ways[]` alongside `dist[]`                 |
| 0-1 BFS              | Replace heap with deque when weights are only 0 or 1 |
| K shortest paths     | Store multiple distances per node                    |
| A* Search            | Add heuristic to priority                            |

---

# 6. Common Pitfalls

### Dijkstra

❌ Using it with negative weights

---

❌ Marking visited too early

Better:

```python
if curr_dist > dist[node]:
    continue
```

instead of a simple `visited` array.

---

❌ Forgetting stale heap entries

Always skip outdated distances.

---

❌ Wrong priority

Heap must store

```
(distance, node)
```

not

```
(node, distance)
```

---

### Bellman-Ford

❌ Forgetting

```
dist[u] != INF
```

before relaxing.

---

❌ Running only once.

Need

```
V-1 iterations
```

---

❌ Missing the final negative-cycle check.

---

# 7. Interview Checklist

### Use Dijkstra if

✓ Weighted graph

✓ Shortest path

✓ All edge weights ≥ 0

✓ Need fastest solution

---

### Use Bellman-Ford if

✓ Negative edges

✓ Detect negative cycle

✓ Shortest path still required

---

### Complexity

| Algorithm       | Time               | Space  |
| --------------- | ------------------ | ------ |
| Dijkstra (Heap) | **O((V+E) log V)** | O(V+E) |
| Bellman-Ford    | **O(VE)**          | O(V)   |

---

# 8. Must-Do Problems

## ⭐ Top 3 (Enough for Revision)

1. ⭐ **743. Network Delay Time** *(Dijkstra)*
2. ⭐ **1631. Path With Minimum Effort** *(Dijkstra variant)*
3. ⭐ **787. Cheapest Flights Within K Stops** *(Bellman-Ford / Modified Dijkstra)*

---

## Easy

* None commonly used specifically for this pattern.

---

## Medium

* **743. Network Delay Time** ⭐
* **1631. Path With Minimum Effort** ⭐
* **787. Cheapest Flights Within K Stops** ⭐
* **1514. Path with Maximum Probability**
* **1976. Number of Ways to Arrive at Destination**

---

## Hard

* **882. Reachable Nodes In Subdivided Graph**
* **2699. Modify Graph Edge Weights**

---

# 9. 30-Second Cheat Sheet

### Recognition

* Weighted graph
* Shortest path
* Cheapest route
* Minimum travel cost

---

### Core Idea

* **Dijkstra** → Greedily finalize the nearest node (non-negative weights only).
* **Bellman-Ford** → Relax every edge repeatedly; supports negative weights and detects negative cycles.

---

### Templates

* **Dijkstra:** Min-heap + distance array + edge relaxation.
* **Bellman-Ford:** Relax all edges **V−1** times, then do one extra pass to detect negative cycles.

---

### Complexity

* **Dijkstra:** `O((V + E) log V)`
* **Bellman-Ford:** `O(VE)`

---

### Common Variations

* 0-1 BFS
* Multi-source shortest path
* Path reconstruction with `parent[]`
* Counting shortest paths
* K-shortest paths
* A* search

---

### Pitfalls

* ❌ Dijkstra with negative weights
* ❌ Not skipping stale heap entries
* ❌ Forgetting `dist[u] != INF` in Bellman-Ford
* ❌ Skipping the negative-cycle detection pass
