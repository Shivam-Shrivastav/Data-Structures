## 🧠 LeetCode: **Minimum Cost of a Path With Special Roads**

---

### 1. **Problem Statement with Example**

You are given:

* `start = (sx, sy)`
* `target = (tx, ty)`
* A list of **special roads**:

Each special road:

```
[x1, y1, x2, y2, cost]
```

* You can go from `(x1, y1)` → `(x2, y2)` at given `cost`

👉 Otherwise, you can move anywhere using **Manhattan distance**:

```
cost = |x1 - x2| + |y1 - y2|
```

🎯 Return the **minimum cost** to reach `target`.

---

### 2. **Diagram**

```
Start → (1,1)
Target → (4,5)

Special Road:
(1,2) → (3,5) cost = 2

Normal move:
(1,1) → (4,5) = 7

Better:
(1,1) → (1,2) = 1
(1,2) → (3,5) = 2 (special)
(3,5) → (4,5) = 1

Total = 4 ✅
```

---

### 3. **Example I/O**

#### Example 1:

```
Input:
start = [1,1]
target = [4,5]
specialRoads = [[1,2,3,5,2]]

Output: 4
```

---

#### Edge Case:

```
Input:
start = [0,0]
target = [5,5]
specialRoads = []

Output: 10
```

👉 No special roads → pure Manhattan distance

---

### 4. **Intuition & Pattern Recognition**

🚨 Key signals:

* Points in coordinate space
* Weighted edges (normal move + special roads)
* Need **minimum cost**

👉 This is:

> **Dijkstra on implicit graph**

---

### 🔥 Interview Thought

> "Nodes are coordinates, edges are either Manhattan distance or special roads → shortest path → Dijkstra"

---

### 5. **Simpler Version**

#### Step 1:

👉 Only Manhattan movement
→ direct answer

#### Step 2:

👉 Add shortcuts (special roads)
→ graph shortest path

---

### Related simpler problems:

* Network Delay Time
  → Classic Dijkstra

* Cheapest Flights Within K Stops
  → Graph with special edges

---

### Bridge Thinking:

```
Without special roads:
→ direct distance

With special roads:
→ graph with shortcuts
→ choose optimal combination
```

---

### 6. **Brute Force**

* Try all combinations of special roads
* Explore all paths

❌ Exponential → not feasible

---

### 7. **Optimal Solution (Dijkstra)**

### 💡 Key Idea:

* Treat **each point as node**
* Important nodes:

  * start
  * target
  * all special road endpoints

---

### Transitions:

From current `(x, y)`:

1. Go directly to target
2. Try every special road:

   * move to `(x1,y1)` using Manhattan
   * then take special road

---

### Code (Python)

```python
import heapq

def minimumCost(start, target, specialRoads):
    # remove useless roads
    filtered = []
    for x1, y1, x2, y2, cost in specialRoads:
        if cost < abs(x1 - x2) + abs(y1 - y2):
            filtered.append((x1, y1, x2, y2, cost))
    
    heap = [(0, start[0], start[1])]
    dist = {}
    
    while heap:
        cost, x, y = heapq.heappop(heap)
        
        if (x, y) in dist:
            continue
        dist[(x, y)] = cost
        
        # go directly to target
        direct = cost + abs(x - target[0]) + abs(y - target[1])
        if target not in dist:
            heapq.heappush(heap, (direct, target[0], target[1]))
        
        # try special roads
        for x1, y1, x2, y2, c in filtered:
            new_cost = cost + abs(x - x1) + abs(y - y1) + c
            
            if (x2, y2) not in dist:
                heapq.heappush(heap, (new_cost, x2, y2))
    
    return dist[target]
```

---

### ⏱ Complexity:

* Time: `O(N log N)` where N = number of roads
* Space: `O(N)`

---

### 8. **Step-by-Step Trace**

Example:

```
start = (1,1)
target = (4,5)
road = (1,2 → 3,5, cost=2)
```

| Step | Position | Cost | Action       |
| ---- | -------- | ---- | ------------ |
| 1    | (1,1)    | 0    | start        |
| 2    | (1,2)    | 1    | move         |
| 3    | (3,5)    | 3    | special road |
| 4    | (4,5)    | 4    | final        |

---

### 9. **Related Problems**

1. Network Delay Time
   → Basic Dijkstra

2. Cheapest Flights Within K Stops
   → Graph with constraints

3. Path With Minimum Effort
   → Modified Dijkstra

4. Swim in Rising Water
   → Minimax path

5. Minimum Cost to Make at Least One Valid Path in a Grid
   → 0-1 BFS

---

## 🚀 Final Interview Summary

* Recognize:

  ```
  coordinates + weighted paths
  → graph shortest path
  ```
* Trick:

  ```
  don't build full graph
  → compute edges on the fly
  ```
* Optimization:

  ```
  ignore useless roads
  ```

---

If you want next level:
👉 How to reduce nodes further (important optimization insight)
👉 Compare with A* (very strong interview impression)
