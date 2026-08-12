# N-ary Tree Level Order Traversal

LeetCode 429 — Tree + BFS

---

# 1. Problem Statement

Given the `root` of an **N-ary tree**, return the **level order traversal** of its nodes' values.

An N-ary tree is a tree where each node can have:

* 0 children
* 1 child
* many children

Return:

* values level-by-level
* from left to right

---

## Example

```text id="o8v9jt"
            1
         /  |  \
        3   2   4
      /   \
     5     6
```

Output:

```python id="ynckdz"
[
  [1],
  [3,2,4],
  [5,6]
]
```

---

## Constraints

* Number of nodes: `[0, 10^4]`
* Tree height ≤ 1000

Important:

* Each node has a list of children
* Need level-wise traversal

---

# 2. Diagram

```text id="b55tp8"
Level 0:              1

Level 1:        3     2     4

Level 2:          5       6
```

Queue evolution:

```text id="vcjlwm"
[1]
↓
[3,2,4]
↓
[5,6]
```

---

# 3. Example I/O

## Example 1

### Input

```text id="5jlwm6"
root = [1,null,3,2,4,null,5,6]
```

### Output

```python id="aqnj6g"
[[1],[3,2,4],[5,6]]
```

---

## Example 2 (Edge Case)

### Input

```text id="s9nqzm"
root = []
```

### Output

```python id="iqy2nl"
[]
```

Empty tree.

---

# 4. Intuition & Pattern Recognition

This is the exact same pattern as:

### Binary Tree Level Order Traversal

The ONLY difference:

```text id="i5gmjn"
Instead of:
left + right

we now have:
children list
```

---

# Pattern Recognition Signals

Keywords:

* “Level order”
* “Level by level”
* “Breadth-first”

Immediately think:

```text id="66jlwm"
BFS + Queue
```

---

# Core Insight

At every level:

1. process current queue size
2. collect node values
3. push all children

---

# 5. Simpler Version

---

## Simpler Problem

### Binary Tree Level Order Traversal

Binary tree:

* max 2 children

N-ary tree:

* variable number of children

---

## Simpler Thinking Path

### Binary Tree BFS

```python id="93jlwm"
if node.left:
if node.right:
```

↓

### N-ary Tree BFS

```python id="kppjlwm"
for child in node.children:
```

Everything else same.

---

# 6. Brute Force

Actually BFS itself is already optimal.

A DFS solution exists but becomes awkward because:

* must track levels manually

BFS is natural.

---

# 7. Optimal Solution

## BFS Queue Solution

---

# Optimal Code

```python id="aofxlv"
from collections import deque

class Solution:
    def levelOrder(self, root):

        if not root:
            return []

        res = []

        q = deque([root])

        while q:

            level_size = len(q)

            level = []

            # process one level
            for _ in range(level_size):

                node = q.popleft()

                level.append(node.val)

                # add all children
                for child in node.children:
                    q.append(child)

            res.append(level)

        return res
```

---

# Complexity

## Time

```text id="jlwm5n"
O(n)
```

Every node visited once.

---

## Space

```text id="wjlwm3"
O(n)
```

Queue may hold entire level.

---

# 8. Step-by-Step Trace

Input:

```text id="i2pkq7"
            1
         /  |  \
        3   2   4
      /   \
     5     6
```

---

# Start

Queue:

```text id="1jlwm0"
[1]
```

Result:

```python id="1i3hmc"
[]
```

---

# Level 0

Process:

* 1

Push:

* 3,2,4

Queue:

```text id="vjlwm0"
[3,2,4]
```

Result:

```python id="h9yt6z"
[[1]]
```

---

# Level 1

Process:

* 3
* 2
* 4

Push children of 3:

* 5,6

Queue:

```text id="jlwm00"
[5,6]
```

Result:

```python id="3i0zjlwm"
[[1],[3,2,4]]
```

---

# Level 2

Process:

* 5
* 6

No children.

Queue empty.

Final:

```python id="yjlwm1"
[[1],[3,2,4],[5,6]]
```

---

# 9. Related Problems

---

### Binary Tree Level Order Traversal

Binary tree version of same BFS pattern.

---

### N-ary Tree Preorder Traversal

DFS traversal in N-ary trees.

---

### N-ary Tree Postorder Traversal

Postorder DFS variation.

---

### Maximum Depth of N-ary Tree

N-ary traversal with DFS/BFS.

---

### Binary Tree Zigzag Level Order Traversal

Advanced BFS level processing variation.
