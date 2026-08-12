## 📘 LeetCode: Course Schedule II (Topological Sort)

---

### 1. **Problem Statement with Example**

You are given:

* `numCourses` courses labeled `0 → n-1`
* `prerequisites[i] = [a, b]` meaning:
  👉 To take course `a`, you must first take `b`
  👉 Directed edge: `b → a`

**Goal:**
Return **any valid order** of courses such that all prerequisites are satisfied.
If impossible (cycle exists), return `[]`.

---

### 🔑 Key Insight:

* You must produce a **Topological Ordering**
* If cycle exists → no valid ordering

---

### 2. **Diagram**

```text
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]

Graph:

      0
     / \
    1   2
     \ /
      3

Valid orders:
[0,1,2,3]
[0,2,1,3]
```

---

### 3. **Example I/O**

#### ✅ Example 1

```text
Input:
numCourses = 2
prerequisites = [[1,0]]

Output: [0,1]
```

---

#### ✅ Example 2

```text
Input:
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]

Output: [0,1,2,3]  (or [0,2,1,3])
```

---

#### ❌ Example (Cycle)

```text
Input:
numCourses = 2
prerequisites = [[1,0],[0,1]]

Output: []
```

---

### 4. **Intuition & Pattern Recognition**

💡 Key signals:

* “Return order” → not just possible/impossible
* Dependencies → directed graph
* Ordering constraint → **Topological Sort**

---

### 🧠 Interview line:

> “This is a classic topological sorting problem. I’ll use Kahn’s Algorithm (BFS) to generate the order while detecting cycles.”

---

### 5. **Simpler Version**

#### 🟢 Simpler Problems:

1. **Course Schedule I**
   → Just detect cycle (True/False)

2. **Find nodes with zero in-degree**
   → Starting points of topo sort

---

### 🚀 Thinking progression:

* Course Schedule I → detect cycle
* Course Schedule II → build ordering

👉 Same logic + store result

---

### 6. **Brute Force**

👉 Try all permutations of courses
Check valid ordering

❌ Time: `O(N!)` → infeasible

---

### 7. **Optimal Solution (BFS - Kahn’s Algorithm)**

---

### 🔥 Idea:

1. Build:

   * Graph (adj list)
   * In-degree array

2. Start with nodes having `in-degree = 0`

3. Process:

   * Remove node
   * Reduce neighbors' in-degree
   * Add new zero in-degree nodes

4. If all nodes processed → valid order
   Else → cycle → return `[]`

---

### ✅ Code (Python)

```python
from collections import deque

def findOrder(numCourses, prerequisites):
    graph = {i: [] for i in range(numCourses)}
    in_degree = [0] * numCourses

    # Build graph
    for a, b in prerequisites:
        graph[b].append(a)
        in_degree[a] += 1

    # Queue for nodes with no prerequisites
    queue = deque()
    for i in range(numCourses):
        if in_degree[i] == 0:
            queue.append(i)

    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        # Reduce dependency
        for nei in graph[node]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                queue.append(nei)

    # If cycle exists
    if len(order) != numCourses:
        return []

    return order
```

---

### ⏱ Complexity

* **Time:** `O(N + E)`
* **Space:** `O(N + E)`

---

### 8. **Step-by-Step Trace**

#### Input:

```text
numCourses = 4
prereq = [[1,0],[2,0],[3,1],[3,2]]
```

---

### Step 1: Build

```text
graph:
0 → [1,2]
1 → [3]
2 → [3]
3 → []

in_degree:
[0,1,1,2]
```

---

### Step 2: Initialize queue

```text
queue = [0]
order = []
```

---

### Step 3: BFS

| Step | Queue | Pop | Order     | in_degree update |
| ---- | ----- | --- | --------- | ---------------- |
| 1    | [0]   | 0   | [0]       | 1→0, 2→0         |
|      |       |     |           | queue → [1,2]    |
| 2    | [1,2] | 1   | [0,1]     | 3→1              |
| 3    | [2]   | 2   | [0,1,2]   | 3→0              |
|      |       |     |           | queue → [3]      |
| 4    | [3]   | 3   | [0,1,2,3] |                  |

---

### ✅ Result:

```text
[0,1,2,3]
```

---

### 9. **Related Problems**

1. **Course Schedule I**
   → Same problem without order (cycle detection)

2. **Alien Dictionary**
   → Topological sort on characters

3. **Parallel Courses**
   → Count levels in DAG

4. **Minimum Height Trees**
   → Reverse topological (remove leaves)

5. **Find Eventual Safe States**
   → Reverse graph + topo logic

---

## 🔥 Final Interview Insight

👉 Core difference:

| Problem            | Goal         |
| ------------------ | ------------ |
| Course Schedule I  | Detect cycle |
| Course Schedule II | Return order |

---

### 🧠 Golden Rule:

> **Topological sort = BFS on in-degree OR DFS postorder**

---

### ⚡ Pro Tip:

* Use **BFS (Kahn)** → cleaner, easier in interviews
* Use **DFS topo** → useful when recursion preferred

---

If you want next:

* I can give **DFS topological sort version**
* OR **trick to instantly identify topo problems in interviews**
