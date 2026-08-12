# Minimum Depth of Binary Tree

LeetCode 111 — Tree + DFS/BFS

---

# 1. Problem Statement

Given the `root` of a binary tree, return its **minimum depth**.

Minimum depth means:

```text id="9b3b9q"
Number of nodes
along the shortest path
from root to the nearest leaf node.
```

A leaf node:

* has NO left child
* has NO right child

---

## Example

```text id="ywkx7y"
        3
      /   \
     9     20
          /  \
         15   7
```

Nearest leaf:

```text id="jlwmd2"
3 -> 9
```

Minimum depth:

```text id="jlwmx4"
2
```

---

## Constraints

* Number of nodes: `[0, 10^5]`
* `-1000 <= Node.val <= 1000`

Important:

* Leaf definition matters
* Missing child handling is the trick

---

# 2. Diagram

```text id="jlwm2s"
Depth 1:           3

Depth 2:      9         20

Depth 3:               15    7
```

Nearest leaf:

* `9`

Minimum depth:

```text id="jlwm5r"
2
```

---

# 3. Example I/O

## Example 1

### Input

```text id="jlwm8q"
root = [3,9,20,null,null,15,7]
```

### Output

```text id="jlwm3n"
2
```

---

## Example 2

### Input

```text id="jlwm7f"
root = [2,null,3,null,4,null,5,null,6]
```

Tree:

```text id="jlwm1g"
2
 \
  3
   \
    4
     \
      5
       \
        6
```

### Output

```text id="jlwm9d"
5
```

Only one root-to-leaf path exists.

---

# 4. Intuition & Pattern Recognition

This looks extremely similar to:

### Maximum Depth of Binary Tree

BUT there is one dangerous trap.

---

# The Trap

Many people incorrectly write:

```python id="jlwm1v"
return 1 + min(left, right)
```

This FAILS.

---

## Why?

Consider:

```text id="jlwm8b"
    1
   /
  2
```

Depth should be:

```text id="jlwm7m"
2
```

But:

```python id="jlwm0w"
left = 1
right = 0

1 + min(1,0) = 1
```

WRONG.

Because:

* missing child is NOT a valid path to leaf.

---

# Core Insight

If one child is missing:

* MUST go through existing child.

---

# Pattern Recognition Signals

Keywords:

* “nearest leaf”
* “shortest root-to-leaf”
* “minimum depth”

This often suggests:

```text id="jlwm5w"
BFS
```

because:

* first leaf encountered in BFS
  = shortest path automatically.

---

# 5. Simpler Version

---

## Simplest Tree

```text id="jlwm3u"
    1
```

Depth:

```text id="jlwm0m"
1
```

---

## One Child Case

```text id="jlwm6z"
    1
   /
  2
```

Cannot use:

```python id="jlwm1e"
min(left,right)
```

Need:

```text id="jlwm4p"
follow existing subtree only
```

---

# Simpler Thinking Path

### Maximum Depth

```python id="jlwm7x"
1 + max(left,right)
```

↓

### Minimum Depth

Would seem:

```python id="jlwm4t"
1 + min(left,right)
```

↓

BUT:

* null child invalidates path

↓

Need special handling.

---

# 6. Brute Force

Generate all root-to-leaf paths:

1. compute lengths
2. take minimum

Inefficient.

---

# Complexity

Potentially:

```text id="jlwm9x"
O(n^2)
```

with path copying.

---

# 7. Optimal Solutions

---

# Approach 1 — DFS Recursive

## Key Logic

### Case 1

Leaf node:

```python id="jlwm6q"
return 1
```

---

### Case 2

One child missing:

Must use other child.

---

# Optimal DFS Code

```python id="jlwm9r"
class Solution:
    def minDepth(self, root):

        if not root:
            return 0

        # leaf node
        if not root.left and not root.right:
            return 1

        # if left missing, go right
        if not root.left:
            return 1 + self.minDepth(root.right)

        # if right missing, go left
        if not root.right:
            return 1 + self.minDepth(root.left)

        # both exist
        return 1 + min(
            self.minDepth(root.left),
            self.minDepth(root.right)
        )
```

---

# Complexity

## Time

```text id="jlwm4a"
O(n)
```

---

## Space

```text id="jlwm7q"
O(h)
```

Recursion stack.

---

# Approach 2 — BFS (Best Interview Insight)

BFS naturally finds:

* shortest path first

So:

* first leaf encountered
  = minimum depth

---

# Optimal BFS Code

```python id="jlwm2r"
from collections import deque

class Solution:
    def minDepth(self, root):

        if not root:
            return 0

        q = deque([(root, 1)])

        while q:

            node, depth = q.popleft()

            # first leaf found
            if not node.left and not node.right:
                return depth

            if node.left:
                q.append((node.left, depth + 1))

            if node.right:
                q.append((node.right, depth + 1))
```

---

# Why BFS is Elegant

Because BFS explores:

```text id="jlwm8x"
level-by-level
```

First leaf reached:

* automatically shortest root-to-leaf path.

No tricky recursion edge cases.

---

# 8. Step-by-Step Trace

Input:

```text id="jlwm3y"
        3
      /   \
     9     20
          /  \
         15   7
```

---

# BFS Trace

Queue:

```text id="jlwm5u"
[(3,1)]
```

---

## Process 3

Push:

```text id="jlwm0r"
(9,2)
(20,2)
```

Queue:

```text id="jlwm2u"
[(9,2), (20,2)]
```

---

## Process 9

Check:

```text id="jlwm8s"
9 is leaf
```

Return:

```text id="jlwm6e"
2
```

Done immediately.

---

# 9. Related Problems

---

### Maximum Depth of Binary Tree

Classic counterpart using max depth.

---

### Binary Tree Level Order Traversal

BFS foundation for shortest-depth logic.

---

### Balanced Binary Tree

Uses subtree depth recursion.

---

### Diameter of Binary Tree

Uses recursive depth calculations.

---

### Maximum Depth of N-ary Tree

Generalized depth computation for N-ary trees.
