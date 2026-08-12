## 🧠 LeetCode: **All Paths From Source to Target (Graph Pattern)**

---

### 1. **Problem Statement with Example**

You are given a **Directed Acyclic Graph (DAG)** with `n` nodes labeled `0` to `n-1`.

* Graph is given as adjacency list:
  `graph[i] = list of nodes you can go from node i`

👉 Find **all possible paths** from node `0` (source) to node `n-1` (target).

---

#### Constraints:

* `2 <= n <= 15` (small → allows exponential solutions)
* DAG (no cycles)

---

### 2. **Diagram**

```text
graph = [[1,2],[3],[3],[]]

        0
       / \
      1   2
       \ /
        3

Paths:
0 → 1 → 3
0 → 2 → 3
```

---

### 3. **Example I/O**

#### ✅ Example 1 (Typical)

```text
Input:
graph = [[1,2],[3],[3],[]]

Output:
[[0,1,3],[0,2,3]]
```

---

#### ⚠️ Example 2 (Edge Case)

```text
Input:
graph = [[1],[]]

Output:
[[0,1]]
```

👉 Only one path exists

---

### 4. **Intuition & Pattern Recognition**

🔑 Key signals:

* “All paths” → **enumeration problem**
* DAG → no cycles → safe DFS
* Small constraints → exponential allowed

🧠 Interview thinking:

> “This is DFS + backtracking to explore all possible paths”

---

### 5. **Simpler Version**

#### 🟢 Simplest:

👉 “Is there a path from source to target?”

* Just DFS → return True/False

---

#### Related simpler problems:

* **Find if Path Exists in Graph**
  → Only check existence

* **Path Sum**
  → DFS path check in tree

---

#### Transition thinking:

| Problem     | Goal               |
| ----------- | ------------------ |
| Path exists | Stop early         |
| All paths   | Explore everything |

---

### 6. **Brute Force**

Idea:

* Try all possible paths using DFS
* Store each valid path

👉 This itself is the optimal approach due to constraints

---

### 7. **Optimal Solution (DFS + Backtracking)**

```python
def allPathsSourceTarget(graph):
    res = []
    path = [0]  # start from source

    def dfs(node):
        # If target reached → store path
        if node == len(graph) - 1:
            res.append(path[:])   # copy path
            return

        # Explore neighbors
        for nei in graph[node]:
            path.append(nei)      # choose
            dfs(nei)              # explore
            path.pop()            # backtrack

    dfs(0)
    return res
```

---

### ✅ Complexity:

* Time: **O(2^n * n)** (all paths)
* Space: **O(n)** recursion + path

---

### 8. **Step-by-Step Trace**

Input:

```text
[[1,2],[3],[3],[]]
```

---

| Step | Node | Path    | Action         |
| ---- | ---- | ------- | -------------- |
| 1    | 0    | [0]     | start          |
| 2    | 1    | [0,1]   | go to 1        |
| 3    | 3    | [0,1,3] | target → store |
| 4    | back | [0,1]   | pop            |
| 5    | back | [0]     | pop            |
| 6    | 2    | [0,2]   | go to 2        |
| 7    | 3    | [0,2,3] | target → store |

---

Final:

```text
[[0,1,3],[0,2,3]]
```

---

### 9. **Related Problems**

* **Path Sum II**
  → All root-to-leaf paths with condition

* **Word Search**
  → Backtracking path exploration

* **Subsets**
  → Generate all combinations (same pattern)

* **Permutations**
  → Backtracking enumeration

---

## ⚡ Final Interview Punchline

> “Since we need all paths in a DAG, use DFS + backtracking. Maintain a path list, explore all neighbors, and backtrack after recursion.”

---

If you want, I can give you a **universal backtracking template** that works for 90% of problems like this.
