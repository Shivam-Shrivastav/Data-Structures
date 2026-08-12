## 🧠 LeetCode: **Number of Provinces (Graph Pattern)**

---

### 1. **Problem Statement with Example**

You are given an `n x n` adjacency matrix `isConnected`, where:

* `isConnected[i][j] = 1` → city `i` and city `j` are directly connected
* `isConnected[i][j] = 0` → not directly connected

A **province** is a group of directly or indirectly connected cities.

👉 Return the **number of provinces**.

#### Constraints:

* `1 <= n <= 200`
* `isConnected[i][i] = 1`
* Matrix is symmetric → undirected graph

---

### 2. **Diagram**

Think of it as an **undirected graph**:

```
Example:

isConnected =
[ [1,1,0],
  [1,1,0],
  [0,0,1] ]

Graph:

  0 —— 1      2

Province 1: {0,1}
Province 2: {2}
```

👉 Each **connected component = 1 province**

---

### 3. **Example I/O**

#### ✅ Example 1 (Typical)

```
Input:
isConnected = [[1,1,0],
               [1,1,0],
               [0,0,1]]

Output: 2
```

Explanation:

* Cities 0 & 1 connected → 1 province
* City 2 alone → 1 province

---

#### ⚠️ Example 2 (Edge Case)

```
Input:
isConnected = [[1,0,0],
               [0,1,0],
               [0,0,1]]

Output: 3
```

Explanation:

* No connections → each city is its own province

---

### 4. **Intuition & Pattern Recognition**

🔑 Key signals:

* Adjacency matrix → graph representation
* Need to count **groups** → connected components
* “Direct or indirect connection” → DFS/BFS/Union-Find

🧠 What to think in interview:

> “This is a connected components problem in an undirected graph.”

---

### 5. **Simpler Version**

#### 🟢 Simpler problem:

👉 “Count number of connected components in a graph given edges list”

Example:

```
n = 5
edges = [[0,1], [1,2], [3,4]]
```

Same idea → 2 components

---

#### Related simpler LeetCode problems:

* **Find if Path Exists in Graph**
  → Just check if ONE path exists (not counting all components)

* **Number of Connected Components in an Undirected Graph**
  → EXACT same problem but with edge list instead of matrix

---

#### Transition thinking:

* Path exists → traverse once
* Count components → traverse multiple times

---

### 6. **Brute Force**

Idea:

* For each node, try to explore all reachable nodes without marking visited properly → redundant traversal

```python
def findCircleNum(isConnected):
    n = len(isConnected)
    visited = set()
    provinces = 0

    def dfs(i):
        for j in range(n):
            if isConnected[i][j] == 1 and j not in visited:
                visited.add(j)
                dfs(j)

    for i in range(n):
        if i not in visited:
            provinces += 1
            visited.add(i)
            dfs(i)

    return provinces
```

👉 Time: **O(n²)**
👉 Space: **O(n)**

(Note: Even optimal is similar, but brute idea = no clear structure / repeated thinking)

---

### 7. **Optimal Solution (DFS)**

```python
def findCircleNum(isConnected):
    n = len(isConnected)
    visited = set()
    provinces = 0

    def dfs(city):
        for nei in range(n):
            # If connected AND not visited
            if isConnected[city][nei] == 1 and nei not in visited:
                visited.add(nei)
                dfs(nei)

    for i in range(n):
        if i not in visited:
            provinces += 1          # New province found
            visited.add(i)
            dfs(i)                  # Explore entire component

    return provinces
```

---

### ✅ Complexity:

* Time: **O(n²)** (scan matrix)
* Space: **O(n)** (visited + recursion)

---

### 🔁 Alternative: Union-Find (Advanced)

* Treat each city as separate
* Union connected ones
* Count unique parents

---

### 8. **Step-by-Step Trace**

Input:

```
[[1,1,0],
 [1,1,0],
 [0,0,1]]
```

| Step | i | visited | provinces | Action          |
| ---- | - | ------- | --------- | --------------- |
| 1    | 0 | {0}     | 1         | start DFS       |
|      |   | {0,1}   |           | visit 1         |
| 2    | 1 | {0,1}   | 1         | already visited |
| 3    | 2 | {0,1,2} | 2         | new DFS         |

👉 Final = **2**

---

### 9. **Related Problems**

* **Number of Islands**
  → Grid version of connected components

* **Max Area of Island**
  → Instead of count → maximize size

* **Surrounded Regions**
  → Boundary-based DFS variation

* **Accounts Merge**
  → Union-Find on real-world grouping

---

## ⚡ Final Interview Punchline

> “This is a classic connected components problem in an undirected graph represented as an adjacency matrix. Use DFS/BFS or Union-Find to count components.”

---

If you want, I can also give you **Union-Find version with path compression** (very interview impressive).
