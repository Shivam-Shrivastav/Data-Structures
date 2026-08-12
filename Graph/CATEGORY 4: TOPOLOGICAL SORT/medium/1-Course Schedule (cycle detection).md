## 📘 LeetCode: Course Schedule (Cycle Detection in Graph)

---

### 1. **Problem Statement with Example**

You are given:

* `numCourses` courses labeled from `0` to `n-1`
* `prerequisites[i] = [a, b]` → to take course `a`, you must first take `b`

👉 This forms a **directed graph**:

* Edge: `b → a`

**Goal:**
Return `True` if you can finish all courses, else `False`.

---

### 🔑 Key Constraint Insight:

* If there is a **cycle**, you cannot complete courses

---

### 2. **Diagram**

```id="2gb63p"
Example:
numCourses = 4
prerequisites = [[1,0],[2,1],[3,2]]

Graph:
0 → 1 → 2 → 3   (NO cycle → valid)

-------------------------

Cycle case:
[[1,0],[0,1]]

0 → 1
↑   ↓
← ← ←   (CYCLE)
```

---

### 3. **Example I/O**

#### ✅ Example 1

```id="9p22kb"
Input:
numCourses = 2
prerequisites = [[1,0]]

Output: True
```

**Explanation:**

* Take 0 → then 1

---

#### ❌ Example 2 (Cycle)

```id="d0lgi9"
Input:
numCourses = 2
prerequisites = [[1,0],[0,1]]

Output: False
```

**Explanation:**

* Circular dependency → impossible

---

#### ⚠️ Edge Case

```id="r0jvd6"
Input:
numCourses = 3
prerequisites = []

Output: True
```

---

### 4. **Intuition & Pattern Recognition**

💡 Key signals:

* Dependencies → directed graph
* “Can finish all?” → detect **cycle**

---

### 🧠 Two standard approaches:

#### 1. **DFS + Recursion Stack (Cycle Detection)**

#### 2. **BFS (Kahn’s Algorithm / Topological Sort)**

---

### 🔥 Interview line:

> “This reduces to detecting a cycle in a directed graph. If a cycle exists, topological ordering is impossible.”

---

### 5. **Simpler Version**

#### 🟢 Simpler Problem:

👉 Detect cycle in directed graph

---

#### Related simpler LC:

* **Graph Valid Tree** (cycle in undirected)
* **Number of Provinces** (connected components)

---

### 🚀 Thinking progression:

1. Try ordering courses
2. Realize → impossible if cycle
3. Convert → cycle detection problem

---

### 6. **Brute Force**

👉 Try all permutations of courses
Check if valid

❌ Time: `O(N!)` → impossible

---

### 7. **Optimal Solutions**

---

## ✅ Approach 1: DFS (Cycle Detection)

### 🔥 Idea:

* Use 3 states:

  * `0 = unvisited`
  * `1 = visiting` (in recursion stack)
  * `2 = visited`

👉 If we visit a node already in `visiting` → cycle

---

### ✅ Code (DFS)

```python id="ht7p64"
def canFinish(numCourses, prerequisites):
    graph = {i: [] for i in range(numCourses)}
    
    for a, b in prerequisites:
        graph[b].append(a)

    state = [0] * numCourses  # 0=unvisited,1=visiting,2=done

    def dfs(node):
        if state[node] == 1:
            return True   # cycle found
        if state[node] == 2:
            return False  # already safe

        state[node] = 1

        for nei in graph[node]:
            if dfs(nei):
                return True

        state[node] = 2
        return False

    for i in range(numCourses):
        if dfs(i):
            return False

    return True
```

---

## ✅ Approach 2: BFS (Kahn’s Algorithm)

### 🔥 Idea:

* Nodes with `in-degree = 0` can be taken first
* Remove them layer by layer
* If all nodes processed → no cycle

---

### ✅ Code (BFS)

```python id="1c69xt"
from collections import deque

def canFinish(numCourses, prerequisites):
    graph = {i: [] for i in range(numCourses)}
    in_degree = [0] * numCourses

    for a, b in prerequisites:
        graph[b].append(a)
        in_degree[a] += 1

    queue = deque()

    for i in range(numCourses):
        if in_degree[i] == 0:
            queue.append(i)

    visited = 0

    while queue:
        node = queue.popleft()
        visited += 1

        for nei in graph[node]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                queue.append(nei)

    return visited == numCourses
```

---

### ⏱ Complexity

* **Time:** `O(N + E)`
* **Space:** `O(N + E)`

---

### 8. **Step-by-Step Trace (BFS)**

#### Input:

```id="c2u7b9"
numCourses = 2
prereq = [[1,0]]
```

---

### Step 1:

```id="2pzz39"
graph = {0:[1], 1:[]}
in_degree = [0,1]
queue = [0]
```

---

### Step 2:

| Step | Queue | Node | visited | in_degree      |
| ---- | ----- | ---- | ------- | -------------- |
| 1    | [0]   | 0    | 1       | [0,1]          |
|      |       |      |         | → reduce 1 → 0 |
|      | [1]   |      |         |                |
| 2    | [1]   | 1    | 2       | [0,0]          |

---

### ✅ Result:

```id="5y4o3f"
visited == numCourses → True
```

---

### 9. **Related Problems**

1. **Course Schedule II**
   → Return actual topological order

2. **Alien Dictionary**
   → Topological sort on characters

3. **Minimum Height Trees**
   → Remove leaves layer by layer (similar BFS idea)

4. **Parallel Courses**
   → Levels in DAG (multi-source BFS)

5. **Detect Cycle in Directed Graph**
   → Same core problem

---

## 🔥 Final Interview Insight

👉 Always remember:

| Problem wording                | Pattern          |
| ------------------------------ | ---------------- |
| “Can finish all tasks”         | Cycle detection  |
| “Return order”                 | Topological sort |
| “Dependencies / prerequisites” | DAG              |

---

### 🧠 Golden rule:

> **Cycle present → impossible to complete**

---

If you want, I can also:

* Show **visual intuition difference between DFS vs BFS**
* OR give a **1-minute pattern recognition cheat sheet for graphs**
