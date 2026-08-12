## 🟢 LeetCode: Minimum Number of Vertices to Reach All Nodes (Graph / In-degree)

---

### 1. **Problem Statement with Example**

You are given:

* `n` nodes labeled from `0` to `n-1`
* A list of **directed edges** where `edges[i] = [u, v]` means `u → v`

👉 You can start from some vertices and traverse along directed edges.

**Goal:**
Return the **minimum set of vertices** from which all nodes in the graph can be reached.

---

### 🔑 Key Constraint Insight:

* Graph is a **Directed Acyclic Graph (DAG)**

---

### 2. **Diagram**

```id="b9zav5"
n = 6
edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]

Graph:

0 → 1
↓
2 → 5

3 → 4 → 2

Observation:
- Nodes with NO incoming edges → 0, 3
```

---

### 3. **Example I/O**

#### ✅ Example 1

```id="ps5bga"
Input:
n = 6
edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]

Output: [0,3]
```

**Explanation:**

* From `0` → reach {1,2,5}
* From `3` → reach {4,2,5}
* Together → cover all nodes

---

#### ⚠️ Edge Case

```id="ubnbo9"
Input:
n = 3
edges = []

Output: [0,1,2]
```

**Explanation:**

* No edges → each node isolated → must include all

---

### 4. **Intuition & Pattern Recognition**

💡 Key signals:

* "Minimum vertices to reach all nodes"
* Directed graph
* Reachability

👉 Think:

> “Which nodes are NOT reachable from others?”

---

### 🧠 Key Observation:

👉 Nodes with **in-degree = 0** must be included

Why?

* No one points to them → cannot be reached from anywhere else
* So we must start from them

---

### 🔥 Interview line:

> “In a DAG, any node with zero in-degree must be part of the answer, since no other node can reach it.”

---

### 5. **Simpler Version**

#### 🟢 Simpler Problem:

👉 “Find nodes with no incoming edges”

---

#### Related simpler LC:

* **Find Center of Star Graph**
* **Course Schedule (in-degree usage)**
* **Topological Sort (Kahn's Algorithm)**

---

### 🚀 Thinking Progression:

1. Try DFS from each node ❌ (too slow)
2. Realize reachability depends on incoming edges
3. Simplify → just find nodes with **in-degree 0**

---

### 6. **Brute Force**

👉 For each node:

* Run DFS/BFS
* Track coverage

❌ Time Complexity:
`O(N * (N + E))`

Too slow

---

### 7. **Optimal Solution (In-degree Trick)**

#### 🔥 Idea:

* Count in-degree of each node
* Return nodes with in-degree = 0

---

### ✅ Code (Python)

```python id="b2wuxc"
def findSmallestSetOfVertices(n, edges):
    in_degree = [0] * n

    # Count incoming edges
    for u, v in edges:
        in_degree[v] += 1

    # Nodes with zero in-degree
    result = []
    for i in range(n):
        if in_degree[i] == 0:
            result.append(i)

    return result
```

---

### ⏱ Complexity

* **Time:** `O(N + E)`
* **Space:** `O(N)`

---

### 8. **Step-by-Step Trace**

#### Input:

```id="qjtxsy"
n = 6
edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
```

---

### Step 1: Initialize

```
in_degree = [0,0,0,0,0,0]
```

---

### Step 2: Process edges

| Edge  | Update         | in_degree     |
| ----- | -------------- | ------------- |
| 0 → 1 | in_degree[1]++ | [0,1,0,0,0,0] |
| 0 → 2 | in_degree[2]++ | [0,1,1,0,0,0] |
| 2 → 5 | in_degree[5]++ | [0,1,1,0,0,1] |
| 3 → 4 | in_degree[4]++ | [0,1,1,0,1,1] |
| 4 → 2 | in_degree[2]++ | [0,1,2,0,1,1] |

---

### Step 3: Pick zero in-degree nodes

```
Nodes: 0 and 3
```

---

### ✅ Result:

```
[0, 3]
```

---

### 9. **Related Problems**

1. **Course Schedule**
   → Detect cycle using in-degree (Kahn's BFS)

2. **Course Schedule II**
   → Return topological order

3. **Find Center of Star Graph**
   → Identify node with max degree

4. **All Ancestors of a Node in DAG**
   → Reverse thinking of reachability

5. **Number of Provinces**
   → Undirected connectivity

---

## 🔥 Final Interview Insight

👉 This problem looks like traversal… but it's NOT.

> The moment you see **“minimum starting nodes in DAG” → think IN-DEGREE**

---

If you want, I can also show:

* Why this fails in **graphs with cycles**
* OR convert this into a **topological sort intuition** for deeper understanding
