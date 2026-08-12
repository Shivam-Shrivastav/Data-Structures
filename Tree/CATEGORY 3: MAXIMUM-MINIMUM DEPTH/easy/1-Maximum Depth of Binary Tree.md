# Maximum Depth of Binary Tree

LeetCode 104 — Tree + DFS/BFS

---

# 1. Problem Statement

Given the `root` of a binary tree, return its **maximum depth**.

Maximum depth means:

```text
Number of nodes
along the longest path
from root to leaf.
```

A leaf node:

* has no children

---

## Example

```text id="6g4e6h"
        3
      /   \
     9     20
          /  \
         15   7
```

Longest path:

```text id="bjlwm1"
3 -> 20 -> 15
```

Depth:

```text id="ytjlwm"
3
```

---

## Constraints

* Number of nodes: `[0, 10^4]`
* `-100 <= Node.val <= 100`

Important:

* Empty tree depth = 0
* Need longest root-to-leaf path

---

# 2. Diagram

```text id="0q3jlwm"
Depth 1:          3

Depth 2:      9       20

Depth 3:            15    7
```

Maximum depth:

```text id="djlwm3"
3
```

---

# 3. Example I/O

## Example 1

### Input

```text id="x7kq2w"
root = [3,9,20,null,null,15,7]
```

### Output

```text id="jlwm2m"
3
```

---

## Example 2

### Input

```text id="tq2l5r"
root = [1,null,2]
```

Tree:

```text id="jlwm9v"
1
 \
  2
```

### Output

```text id="5mjlwm"
2
```

---

## Edge Case

### Input

```text id="xjlwm1"
root = []
```

### Output

```text id="jlwm4x"
0
```

---

# 4. Intuition & Pattern Recognition

This is one of the most classic DFS tree problems.

Key observation:

```text
Depth of current node
=
1 + max(left depth, right depth)
```

This is the entire problem.

---

# Pattern Recognition Signals

Keywords:

* “Maximum depth”
* “Height”
* “Longest root-to-leaf”

Immediately think:

```text id="sjlwm6"
Tree recursion
```

because:

* subtrees solve same problem recursively

---

# Recursive Structure

Suppose:

```text id="jlwm88"
        1
       / \
      2   3
```

If:

* left subtree depth = 5
* right subtree depth = 2

Then:

```text
root depth = 1 + max(5,2)
```

---

# 5. Simpler Version

---

## Simplest Tree

```text id="jlwm7k"
    1
```

Depth:

```text
1
```

---

## Slightly Bigger

```text id="jlwm8n"
    1
   /
  2
```

Depth:

```text
1 + depth(2)
```

---

## Core Recursive Thinking

Every node asks:

```text
"What is the deepest subtree below me?"
```

Then adds itself:

```text
1 + deeper side
```

---

## Related Simpler Problem

### Minimum Depth of Binary Tree

Same idea:

* instead of max
* use min carefully

---

# 6. Brute Force

You could:

1. generate all root-to-leaf paths
2. compute lengths
3. take maximum

Very inefficient.

---

## Complexity

Could become:

```text
O(n^2)
```

depending on path copying.

---

# 7. Optimal Solution

## DFS Recursive Solution

This is the cleanest interview solution.

---

# Optimal Code (DFS)

```python id="jlwm55"
class Solution:
    def maxDepth(self, root):

        # empty tree
        if not root:
            return 0

        # compute left subtree depth
        left_depth = self.maxDepth(root.left)

        # compute right subtree depth
        right_depth = self.maxDepth(root.right)

        # current node contributes +1
        return 1 + max(left_depth, right_depth)
```

---

# Why This Works

Each node:

* recursively asks children for depths
* chooses deeper side
* adds itself

This naturally propagates upward.

---

# Complexity

## Time

```text id="vjlwm6"
O(n)
```

Every node visited once.

---

## Space

```text id="9jlwm2"
O(h)
```

Recursion stack.

Worst case:

* skewed tree → `O(n)`

Balanced tree:

* `O(log n)`

---

# BFS Alternative

You can also solve using level-order traversal.

Each level increases depth by 1.

---

## BFS Code

```python id="jlwm6w"
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

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return depth
```

---

# DFS vs BFS

| Approach      | Space |
| ------------- | ----- |
| DFS recursion | O(h)  |
| BFS queue     | O(w)  |

Usually DFS preferred for interviews because cleaner.

---

# 8. Step-by-Step Trace

Input:

```text id="jlwm5t"
        3
      /   \
     9     20
          /  \
         15   7
```

---

# Recursive Calls

---

## Node 9

```text
left = 0
right = 0

depth = 1
```

---

## Node 15

```text
depth = 1
```

---

## Node 7

```text
depth = 1
```

---

## Node 20

```text
left = 1
right = 1

depth = 1 + max(1,1)
      = 2
```

---

## Node 3

```text
left = 1
right = 2

depth = 1 + max(1,2)
      = 3
```

Final answer:

```text
3
```

---

# 9. Related Problems

---

### Minimum Depth of Binary Tree

Similar recursion but careful leaf handling needed.

---

### Diameter of Binary Tree

Uses subtree depths to compute longest path.

---

### Balanced Binary Tree

Checks subtree height differences.

---

### Maximum Depth of N-ary Tree

Same idea generalized to N children.

---

### Binary Tree Level Order Traversal

BFS alternative for computing depth.
