## 🧠 LeetCode: **Clone Graph (Graph Pattern)**

---

### 1. **Problem Statement with Example**

You are given a reference to a node in a **connected undirected graph**.

Each node contains:

* `val` (unique integer)
* `neighbors` (list of adjacent nodes)

👉 You must return a **deep copy (clone)** of the graph.

#### Constraints:

* Number of nodes ≤ 100
* Graph is connected
* No duplicate edges, no self-loops

---

### 2. **Diagram**

```text
Original Graph:

    1
   / \
  2---3
   \
    4

Clone Graph (new nodes, same structure):

    1'
   / \
  2'--3'
   \
    4'
```

👉 Same structure, **different memory nodes**

---

### 3. **Example I/O**

#### ✅ Example 1 (Typical)

```text
Input (Adj List):
1: [2,3]
2: [1,3,4]
3: [1,2]
4: [2]

Output:
Deep copy of same structure
```

Explanation:

* Each node recreated
* Connections preserved

---

#### ⚠️ Example 2 (Edge Case)

```text
Input:
[]

Output:
[]
```

👉 Empty graph → return `None`

---

### 4. **Intuition & Pattern Recognition**

🔑 Key signals:

* Graph traversal (DFS/BFS)
* Need to **copy nodes + edges**
* Cycles exist → must avoid infinite loop

🧠 Interview thought:

> “While traversing, create a clone and store mapping (original → clone)”

---

### 5. **Simpler Version**

#### 🟢 Simplest idea:

👉 Copy a **tree (no cycles)**

* Just DFS and create nodes → no need for visited map

---

#### Related simpler problems:

* **Find if Path Exists in Graph**
  → Only traversal (no cloning)

* **Binary Tree Clone**
  → Tree cloning (no cycles → easier)

---

#### Transition thinking:

| Case  | Need hashmap?           |
| ----- | ----------------------- |
| Tree  | ❌ No                    |
| Graph | ✅ Yes (to avoid cycles) |

---

### 6. **Brute Force**

❌ Not practical:

* If you try cloning without tracking visited → infinite loop in cyclic graph

---

### 7. **Optimal Solution (DFS + HashMap)**

```python
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []

def cloneGraph(node):
    if not node:
        return None

    old_to_new = {}  # map original → clone

    def dfs(curr):
        # If already cloned → return it
        if curr in old_to_new:
            return old_to_new[curr]

        # Create clone node
        copy = Node(curr.val)
        old_to_new[curr] = copy

        # Clone neighbors recursively
        for nei in curr.neighbors:
            copy.neighbors.append(dfs(nei))

        return copy

    return dfs(node)
```

---

### ✅ Complexity:

* Time: **O(V + E)**
* Space: **O(V)** (map + recursion)

---

### 🔁 Alternative: BFS

```python
from collections import deque

def cloneGraph(node):
    if not node:
        return None

    old_to_new = {node: Node(node.val)}
    queue = deque([node])

    while queue:
        curr = queue.popleft()

        for nei in curr.neighbors:
            if nei not in old_to_new:
                old_to_new[nei] = Node(nei.val)
                queue.append(nei)

            # connect cloned nodes
            old_to_new[curr].neighbors.append(old_to_new[nei])

    return old_to_new[node]
```

---

### 8. **Step-by-Step Trace**

Start at node `1`

| Step | Current | Action    | Map                   |
| ---- | ------- | --------- | --------------------- |
| 1    | 1       | create 1' | {1 → 1'}              |
| 2    | 2       | create 2' | {1→1', 2→2'}          |
| 3    | 3       | create 3' | {1→1',2→2',3→3'}      |
| 4    | 4       | create 4' | {1→1',2→2',3→3',4→4'} |

Then:

* Add edges accordingly

---

### 9. **Related Problems**

* **Copy List with Random Pointer**
  → Same idea (mapping old → new)

* **Number of Provinces**
  → Graph traversal but counting components

* **Course Schedule**
  → Cycle detection in graph

* **Graph Valid Tree**
  → Validate graph structure

---

## ⚡ Final Interview Punchline

> “Use DFS/BFS with a hashmap (old → new). This avoids cycles and ensures each node is cloned exactly once.”

---

If you want, I can give you a **super short template to remember this pattern in 10 seconds during interview**.
