# All Nodes Distance K in Binary Tree

LeetCode 863 — Tree + Graph Conversion + BFS/DFS

---

# 1. Problem Statement

Given:

* the `root` of a binary tree
* a `target` node
* an integer `k`

Return all node values that are exactly distance `k` away from the target node.

Distance means:

* number of edges between nodes.

---

## Example

```text id="6rqvxg"
            3
          /   \
         5     1
        / \   / \
       6   2 0   8
          / \
         7   4
```

Target:

```text id="9u4a2v"
5
```

K:

```text id="jlwm0i"
2
```

Nodes at distance 2:

```text id="jlwm2i"
7, 4, 1
```

Output:

```python id="jlwm4i"
[7,4,1]
```

---

## Constraints

* Number of nodes: `[1, 500]`
* `0 <= Node.val <= 500`
* target exists in tree

Important:

* movement allowed:

  * left
  * right
  * parent

This is the key twist.

---

# 2. Diagram

```text id="jlwm6i"
            3
          /   \
         5     1
        / \   / \
       6   2 0   8
          / \
         7   4
```

From target `5`:

```text id="jlwm8i"
Distance 1:
6, 2, 3

Distance 2:
7, 4, 1
```

Answer:

```text id="jlwm1i"
[7,4,1]
```

---

# 3. Example I/O

## Example 1

### Input

```text id="jlwm3i"
root = [3,5,1,6,2,0,8,null,null,7,4]
target = 5
k = 2
```

### Output

```python id="jlwm5i"
[7,4,1]
```

---

## Example 2

### Input

```text id="jlwm7i"
root = [1]
target = 1
k = 3
```

### Output

```python id="jlwm9i"
[]
```

No nodes that far away.

---

# 4. Intuition & Pattern Recognition

This LOOKS like tree DFS.

But real insight:

```text id="jlwm0j"
Once parent movement is allowed,
tree behaves like an UNDIRECTED GRAPH.
```

That changes everything.

---

# Key Observation

Normally tree traversal only goes:

```text id="jlwm2l"
parent -> child
```

But now we also need:

```text id="jlwm4l"
child -> parent
```

So:

* build parent pointers
  OR
* build graph adjacency list

Then:

* run BFS from target

---

# Pattern Recognition Signals

Keywords:

* “distance K”
* “nodes reachable”
* “can move upward”
* “all nodes at distance”

Usually means:

```text id="jlwm6l"
Graph BFS
```

even though input is tree.

---

# Why BFS?

Because BFS naturally explores:

* distance 1
* distance 2
* distance 3

level-by-level.

Exactly what we need.

---

# 5. Simpler Version

---

## Simpler Problem

### Binary Tree Level Order Traversal

BFS level traversal downward only.

---

## New Twist

Need upward traversal too.

So tree becomes:

```text id="jlwm8n"
Undirected graph
```

---

# Simpler Thinking Path

### Tree traversal

↓

### Need parent access

↓

### Add reverse edges

↓

### Run graph BFS from target

↓

### Stop at distance K

---

# 6. Brute Force

For every node:

1. compute distance to target
2. if distance == k → add answer

Distance computation repeatedly expensive.

---

# Complexity

Could become:

```text id="jlwm1o"
O(n^2)
```

---

# 7. Optimal Solution

# Step 1 — Build Parent Map

Store:

```python id="jlwm3o"
child -> parent
```

---

# Step 2 — BFS From Target

Now neighbors become:

* left child
* right child
* parent

---

# Optimal Code

```python id="jlwm5o"
from collections import deque

class Solution:

    def distanceK(self, root, target, k):

        # child -> parent mapping
        parent = {}

        # build parent pointers
        def dfs(node, par):

            if not node:
                return

            parent[node] = par

            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        # BFS from target
        q = deque([(target, 0)])

        visited = set([target])

        res = []

        while q:

            node, dist = q.popleft()

            # reached required distance
            if dist == k:
                res.append(node.val)

            # no need to explore further
            if dist > k:
                break

            neighbors = [
                node.left,
                node.right,
                parent[node]
            ]

            for nei in neighbors:

                if nei and nei not in visited:

                    visited.add(nei)

                    q.append((nei, dist + 1))

        return res
```

---

# Why Visited Set Needed?

Because graph now has cycles.

Example:

```text id="jlwm7o"
5 -> parent 3
3 -> child 5
```

Without visited:

* infinite loop.

---

# Complexity

## Time

```text id="jlwm9o"
O(n)
```

* build parent map → `O(n)`
* BFS traversal → `O(n)`

---

## Space

```text id="jlwm0l"
O(n)
```

Parent map + visited + queue.

---

# 8. Step-by-Step Trace

Input:

```text id="jlwm2p"
            3
          /   \
         5     1
        / \   / \
       6   2 0   8
          / \
         7   4
```

Target:

```text id="jlwm4p"
5
```

K:

```text id="jlwm6q"
2
```

---

# Parent Map

```text id="jlwm8q"
5 -> 3
6 -> 5
2 -> 5
1 -> 3
...
```

---

# BFS Start

Queue:

```text id="jlwm1r"
[(5,0)]
```

Visited:

```text id="jlwm3s"
{5}
```

---

## Distance 1

Neighbors of 5:

```text id="jlwm5s"
6,2,3
```

Queue:

```text id="jlwm7t"
[(6,1),(2,1),(3,1)]
```

---

## Distance 2

From 6:

* none

From 2:

* 7,4

From 3:

* 1

Queue:

```text id="jlwm9t"
[(7,2),(4,2),(1,2)]
```

Collect:

```text id="jlwm0v"
[7,4,1]
```

Done.

---

# 9. Related Problems

---

### Lowest Common Ancestor of a Binary Tree

Tree navigation between nodes.

---

### Binary Tree Level Order Traversal

Foundation BFS traversal.

---

### Find Leaves of Binary Tree

Bottom-up tree processing.

---

### Minimum Height Trees

Graph BFS over tree-like structures.

---

### Closest Leaf in a Binary Tree

Converts tree into graph for shortest path traversal.
