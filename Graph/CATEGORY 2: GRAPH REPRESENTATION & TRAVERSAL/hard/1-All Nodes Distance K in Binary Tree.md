## 🧠 LeetCode: **All Nodes Distance K in Binary Tree (Graph + Tree Hybrid)**

---

### 1. **Problem Statement with Example**

You are given:

* Root of a **binary tree**
* A **target node**
* An integer `K`

👉 Return all nodes that are exactly **distance K from the target node**.

Distance = number of edges.

---

#### Constraints:

* `1 <= n <= 500`
* Tree nodes are unique
* Target node exists in tree

---

### 2. **Diagram**

```text
        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4

Target = 5, K = 2

Nodes at distance 2:
→ 7, 4, 1
```

👉 Notice:

* Not just downward → also upward (parent!)

---

### 3. **Example I/O**

#### ✅ Example 1 (Typical)

```text
Input:
root = [3,5,1,6,2,0,8,null,null,7,4]
target = 5
K = 2

Output:
[7,4,1]
```

---

#### ⚠️ Example 2 (Edge Case)

```text
Input:
root = [1]
target = 1
K = 0

Output:
[1]
```

👉 Distance 0 → node itself

---

### 4. **Intuition & Pattern Recognition**

🔑 Key signals:

* “Distance from node” → BFS
* Need to move **up + down** → tree becomes graph
* Tree doesn’t have parent pointers → must build them

🧠 Interview thought:

> “Convert tree into graph (parent mapping), then BFS from target”

---

### 5. **Simpler Version**

#### 🟢 Simplest:

👉 “Find nodes at distance K from root”

* Just DFS downwards

---

#### Related simpler problems:

* **Binary Tree Level Order Traversal**
  → BFS level traversal

* **Path Sum**
  → Tree DFS traversal

---

#### Transition thinking:

| Problem         | Movement          |
| --------------- | ----------------- |
| Normal tree DFS | downward only     |
| This problem    | up + down (graph) |

---

### 6. **Brute Force**

Idea:

* For each node → compute distance from target
* Keep nodes where distance = K

👉 Time: **O(n²)** (repeated traversal)

---

### 7. **Optimal Solution (Graph + BFS)**

### Step 1: Build parent map

### Step 2: BFS from target

```python
from collections import deque

def distanceK(root, target, k):
    # Step 1: Build parent mapping
    parent = {}

    def dfs(node, par):
        if not node:
            return
        parent[node] = par
        dfs(node.left, node)
        dfs(node.right, node)

    dfs(root, None)

    # Step 2: BFS from target
    queue = deque([target])
    visited = set([target])
    dist = 0

    while queue:
        if dist == k:
            return [node.val for node in queue]

        for _ in range(len(queue)):
            node = queue.popleft()

            # neighbors: left, right, parent
            for nei in [node.left, node.right, parent[node]]:
                if nei and nei not in visited:
                    visited.add(nei)
                    queue.append(nei)

        dist += 1

    return []
```

---

### ✅ Complexity:

* Time: **O(n)**
* Space: **O(n)**

---

### 8. **Step-by-Step Trace**

Target = 5, K = 2

---

| Level | Queue   | Nodes     |
| ----- | ------- | --------- |
| 0     | [5]     | start     |
| 1     | [6,2,3] | neighbors |
| 2     | [7,4,1] | result    |

👉 Return `[7,4,1]`

---

### 9. **Related Problems**

* **Binary Tree Level Order Traversal**
  → BFS levels

* **Minimum Height Trees**
  → Graph BFS from nodes

* **Burning Tree**
  → Same idea (spread from target)

* **Closest Leaf in a Binary Tree**
  → Convert tree → graph

---

## ⚡ Final Interview Punchline

> “Convert tree into an undirected graph using parent mapping, then run BFS from the target node until distance K.”

---

If you want, I can give you a **one-line pattern trigger cheat sheet** for all graph problems (super useful before interviews).
