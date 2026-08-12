# Maximum Depth of N-ary Tree

LeetCode 559 — Tree + DFS/BFS

---

# 1. Problem Statement

Given the `root` of an **N-ary tree**, return its **maximum depth**.

Maximum depth:

```text id="gklp3d"
Number of nodes
along the longest path
from root to leaf.
```

An N-ary tree:

* each node can have multiple children

---

## Example

```text id="n2l7sa"
            1
         /  |  \
        3   2   4
      /   \
     5     6
```

Longest path:

```text id="7m0f14"
1 -> 3 -> 5
```

Depth:

```text id="v0ecyj"
3
```

---

## Constraints

* Number of nodes: `[0, 10^4]`
* Tree depth ≤ 1000

Important:

* children stored as list
* need deepest subtree

---

# 2. Diagram

```text id="mrjlwm"
Depth 1:                1

Depth 2:         3      2      4

Depth 3:            5      6
```

Maximum depth:

```text id="jlwm6y"
3
```

---

# 3. Example I/O

## Example 1

### Input

```text id="jlwm8e"
root = [1,null,3,2,4,null,5,6]
```

### Output

```text id="jlwm4q"
3
```

---

## Example 2 (Edge Case)

### Input

```text id="jlwm1t"
root = []
```

### Output

```text id="jlwm5b"
0
```

---

# 4. Intuition & Pattern Recognition

This is the N-ary version of:

### Maximum Depth of Binary Tree

Binary tree:

```python id="jlwm7v"
1 + max(left_depth, right_depth)
```

N-ary tree:

```python id="jlwm2o"
1 + max(depth of all children)
```

Same exact recursive pattern.

---

# Pattern Recognition Signals

Keywords:

* “Maximum depth”
* “Height”
* “Longest path”
* “Tree”

Immediately think:

```text id="jlwm9o"
DFS recursion
```

because:

* subtree problem repeats identically.

---

# Core Recursive Insight

Each node asks:

```text id="jlwm3k"
"What is the deepest child subtree?"
```

Then:

```text id="jlwm0y"
depth = 1 + deepest child
```

---

# 5. Simpler Version

---

## Simpler Problem

### Maximum Depth of Binary Tree

Binary tree:

* only 2 recursive calls

---

## N-ary Generalization

Instead of:

```python id="jlwm8m"
max(left, right)
```

we now do:

```python id="jlwm6m"
max(all child depths)
```

---

# Simpler Thinking Path

### Binary Tree

```python id="jlwm7z"
depth = 1 + max(left,right)
```

↓

### N-ary Tree

```python id="jlwm1w"
depth = 1 + max(child1, child2, ...)
```

Only difference:

* loop over children.

---

# 6. Brute Force

Generate every root-to-leaf path:

* compute lengths
* take maximum

Unnecessary.

---

# Complexity

Potentially inefficient due to path copying.

---

# 7. Optimal Solution

# DFS Recursive Solution

---

# Optimal Code (DFS)

```python id="jlwm0n"
class Solution:
    def maxDepth(self, root):

        # empty tree
        if not root:
            return 0

        # if leaf node
        if not root.children:
            return 1

        max_child_depth = 0

        # compute deepest child subtree
        for child in root.children:

            child_depth = self.maxDepth(child)

            max_child_depth = max(
                max_child_depth,
                child_depth
            )

        return 1 + max_child_depth
```

---

# Cleaner Python Version

```python id="jlwm3r"
class Solution:
    def maxDepth(self, root):

        if not root:
            return 0

        return 1 + max(
            (self.maxDepth(child) for child in root.children),
            default=0
        )
```

---

# Why `default=0`?

For leaf nodes:

```python id="jlwm4v"
root.children = []
```

then:

```python id="jlwm5y"
max([])
```

would crash.

So:

```python id="jlwm7y"
default=0
```

means:

* no child depth
* leaf contributes only itself

---

# Complexity

## Time

```text id="jlwm2v"
O(n)
```

Every node visited once.

---

## Space

```text id="jlwm9v"
O(h)
```

Recursion stack depth.

Worst case:

* skewed tree → `O(n)`

---

# BFS Alternative

Can also solve level-by-level.

---

# BFS Code

```python id="jlwm8u"
from collections import deque

class Solution:
    def maxDepth(self, root):

        if not root:
            return 0

        q = deque([root])

        depth = 0

        while q:

            depth += 1

            for _ in range(len(q)):

                node = q.popleft()

                for child in node.children:
                    q.append(child)

        return depth
```

---

# DFS vs BFS

| Approach | Space |
| -------- | ----- |
| DFS      | O(h)  |
| BFS      | O(w)  |

Usually DFS cleaner.

---

# 8. Step-by-Step Trace

Input:

```text id="jlwm3b"
            1
         /  |  \
        3   2   4
      /   \
     5     6
```

---

# Recursive Calls

---

## Node 5

```text id="jlwm4m"
leaf → depth = 1
```

---

## Node 6

```text id="jlwm0q"
leaf → depth = 1
```

---

## Node 3

Children depths:

```text id="jlwm6v"
5 -> 1
6 -> 1
```

So:

```text id="jlwm2q"
depth = 1 + max(1,1)
      = 2
```

---

## Nodes 2 and 4

```text id="jlwm1q"
leaf → depth = 1
```

---

## Node 1

Children depths:

```text id="jlwm5z"
3 -> 2
2 -> 1
4 -> 1
```

So:

```text id="jlwm8z"
depth = 1 + max(2,1,1)
      = 3
```

Final answer:

```text id="jlwm9m"
3
```

---

# 9. Related Problems

---

### Maximum Depth of Binary Tree

Binary tree version of same recursion.

---

### Minimum Depth of Binary Tree

Shortest root-to-leaf depth variation.

---

### N-ary Tree Level Order Traversal

BFS traversal in N-ary trees.

---

### Balanced Binary Tree

Uses subtree heights recursively.

---

### Diameter of Binary Tree

Advanced depth-based recursion problem.
