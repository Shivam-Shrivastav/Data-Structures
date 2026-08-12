## 🧠 Minimum Height Trees (LeetCode)

---

## 1. **Problem Statement with Example**

You are given an **undirected tree** with `n` nodes labeled from `0` to `n-1` and `n-1` edges.

You can choose any node as root. The **height** of the tree is the number of edges on the longest path from root to a leaf.

👉 Return **all possible roots** that produce a tree with **minimum height**.

### Constraints:

* `1 ≤ n ≤ 2 * 10^4`
* Tree ⇒ connected + no cycles
* Exactly `n-1` edges

---

## 2. **Diagram (Core Idea: Peel from Leaves)**

```
Initial Tree:

        1
      / | \
     0  2  3
           |
           4

Leaves: [0,2,4]

Step 1 remove leaves → remaining:

        1
         \
          3

Leaves: [1,3]

Final centers → answer: [1,3]
```

👉 Think: **Trim leaves layer by layer → reach center(s)**

---

## 3. **Example I/O**

### Example 1:

```
Input:
n = 4
edges = [[1,0],[1,2],[1,3]]

Output:
[1]
```

Explanation:

* Root = 1 gives minimum height

---

### Example 2 (Edge Case):

```
Input:
n = 1
edges = []

Output:
[0]
```

Explanation:

* Only one node ⇒ it's the answer

---

## 4. **Intuition & Pattern Recognition**

### 🔥 Signals:

* Tree + “minimum height”
* Try all roots? ❌ too slow (O(n²))
* Think **center of tree**

### 💡 Key Insight:

* The root that minimizes height = **center of the tree**
* A tree has:

  * **1 center** (odd length path)
  * **2 centers** (even length path)

👉 How to find center?
➡️ **Topological BFS (like Kahn’s algorithm)**
➡️ Repeatedly remove **leaves (degree = 1)**

### 🧠 Interview thought:

> “This is like peeling an onion — remove outer layers until 1 or 2 nodes remain.”

---

## 5. **Simpler Version**

### Simplest problem:

👉 Find **center of a line (linked list)**

```
0 - 1 - 2 - 3 - 4
Center = 2
```

### Related simpler LeetCode:

* **Diameter of Binary Tree**
* **Find center using 2 BFS (tree diameter method)**

### Transition:

| Simpler             | This Problem                |
| ------------------- | --------------------------- |
| Find middle of path | Find center of general tree |
| Linear structure    | Graph structure             |
| Direct middle       | Need iterative leaf removal |

👉 Same idea: **center minimizes max distance**

---

## 6. **Brute Force**

### Idea:

* Try every node as root
* Compute height using BFS/DFS

### Complexity:

* Time: **O(n²)**
* Space: O(n)

```python
def findMinHeightTrees(n, edges):
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def height(root):
        visited = set([root])
        queue = deque([(root, 0)])
        max_h = 0
        
        while queue:
            node, h = queue.popleft()
            max_h = max(max_h, h)
            
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei, h + 1))
        
        return max_h

    min_height = float('inf')
    res = []

    for i in range(n):
        h = height(i)
        if h < min_height:
            min_height = h
            res = [i]
        elif h == min_height:
            res.append(i)

    return res
```

---

## 7. **Optimal Solution (Topological BFS)**

### 🚀 Idea:

* Build graph + degree array
* Push all **leaves (degree=1)** into queue
* Remove them layer by layer
* Stop when ≤ 2 nodes remain

### Complexity:

* Time: **O(n)**
* Space: O(n)

```python
def findMinHeightTrees(n, edges):
    if n == 1:
        return [0]

    from collections import defaultdict, deque

    graph = defaultdict(list)
    degree = [0] * n

    # Build graph
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        degree[u] += 1
        degree[v] += 1

    # Initial leaves
    leaves = deque()
    for i in range(n):
        if degree[i] == 1:
            leaves.append(i)

    remaining_nodes = n

    # Trim leaves
    while remaining_nodes > 2:
        size = len(leaves)
        remaining_nodes -= size

        for _ in range(size):
            leaf = leaves.popleft()

            for nei in graph[leaf]:
                degree[nei] -= 1
                if degree[nei] == 1:
                    leaves.append(nei)

    return list(leaves)
```

---

## 8. **Step-by-Step Trace**

### Input:

```
n = 6
edges = [[0,1],[0,2],[0,3],[3,4],[4,5]]
```

### Step-by-step:

| Step | Leaves         | Remaining Nodes | Action             |
| ---- | -------------- | --------------- | ------------------ |
| Init | [1,2,5]        | 6               | start              |
| 1    | remove [1,2,5] | 3               | new leaves → [0,4] |
| 2    | remove [0,4]   | 1               | remaining → [3]    |

### Output:

```
[3]
```

---

## 9. **Related Problems**

1. **Course Schedule**
   → Same topological sort idea but detects cycles.

2. **Find if Path Exists in Graph**
   → Basic graph traversal foundation.

3. **Tree Diameter**
   → Centers lie in the middle of diameter.

4. **Minimum Number of Vertices to Reach All Nodes**
   → Uses indegree logic similar to leaves.

5. **Longest Path in Tree**
   → Builds deeper intuition on tree structure.

---

## ⚡ Final Interview Takeaway

* Tree + minimum height ⇒ **center problem**
* Two approaches:

  * Diameter (2 BFS)
  * ✅ **Leaf trimming (Topological BFS)** ← best
* Stop when ≤ 2 nodes remain

---

If you want, I can also give you:
👉 Diameter-based solution (very useful in interviews)
👉 Pattern comparison with "Course Schedule" and "Topo Sort"
