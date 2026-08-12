# Lowest Common Ancestor of Deepest Leaves

LeetCode 1123 — Tree + DFS + Bottom-Up Recursion

---

# 1. Problem Statement

Given the `root` of a binary tree:

1. Find all deepest leaf nodes
2. Return their **Lowest Common Ancestor (LCA)**

The LCA is:

* the lowest node in the tree
* that has all deepest leaves in its subtree.

---

## Example

```text id="dyh7rq"
            3
          /   \
         5     1
        / \   / \
       6   2 0   8
          / \
         7   4
```

Deepest leaves:

```text id="jlwm4g"
7 and 4
```

Their LCA:

```text id="jlwm2c"
2
```

Answer:

```text id="jlwm7r"
2
```

---

## Constraints

* Number of nodes: `[1, 1000]`
* `0 <= Node.val <= 1000`

Important:

* deepest leaves may exist on:

  * left subtree
  * right subtree
  * both

Need:

* deepest subtree ancestor.

---

# 2. Diagram

```text id="jlwm0s"
                3
             /     \
            5       1
          /   \    / \
         6     2  0   8
              / \
             7   4
```

Depths:

```text id="jlwm6t"
7 -> depth 3
4 -> depth 3
```

LCA:

```text id="jlwm8t"
2
```

---

# Important Case

```text id="jlwm1f"
         1
       /   \
      2     3
```

Deepest leaves:

* 2
* 3

LCA becomes:

```text id="jlwm5m"
1
```

because deepest leaves split across both subtrees.

---

# 3. Example I/O

## Example 1

### Input

```text id="jlwm9j"
root = [3,5,1,6,2,0,8,null,null,7,4]
```

### Output

```text id="jlwm3h"
2
```

---

## Example 2

### Input

```text id="jlwm4r"
root = [1]
```

### Output

```text id="jlwm2m"
1
```

Single node is deepest leaf itself.

---

# 4. Intuition & Pattern Recognition

This problem combines:

1. deepest depth
2. LCA

The brilliant trick:

```text id="jlwm8r"
Compute BOTH together
in one DFS.
```

---

# Core Observation

At every node:

We ask:

* how deep is left subtree?
* how deep is right subtree?

---

## Cases

### Case 1

```text id="jlwm6b"
left depth > right depth
```

Deepest leaves entirely in left subtree.

Answer propagates from left.

---

### Case 2

```text id="jlwm5a"
right depth > left depth
```

Deepest leaves entirely in right subtree.

Answer propagates from right.

---

### Case 3

```text id="jlwm1d"
left depth == right depth
```

Deepest leaves exist in BOTH sides.

Current node becomes LCA.

---

# Pattern Recognition Signals

Keywords:

* “deepest leaves”
* “lowest common ancestor”
* “deepest subtree”

Usually suggests:

```text id="jlwm4u"
Postorder DFS
```

because:

* children information needed first.

---

# 5. Simpler Version

---

## Simpler Problem 1

### Maximum Depth of Binary Tree

Compute subtree depth.

---

## Simpler Problem 2

### Lowest Common Ancestor of a Binary Tree

Find ancestor using bottom-up recursion.

---

# This Problem = Combination

We simultaneously compute:

* subtree depth
* subtree LCA

---

# Simpler Thinking Path

### Step 1

Depth recursion:

```python id="jlwm9c"
depth = 1 + max(left,right)
```

↓

### Step 2

If depths equal:

* current node connects deepest leaves

↓

### Step 3

Current node becomes LCA.

---

# 6. Brute Force

## Naive Approach

1. Find deepest leaves
2. Store all deepest nodes
3. Compute pairwise LCA repeatedly

Complicated and inefficient.

---

# Complexity

Potentially:

```text id="jlwm0u"
O(n^2)
```

---

# 7. Optimal Solution

# Bottom-Up DFS

Return:

1. deepest depth
2. LCA node for that subtree

---

# Key DFS Meaning

```python id="jlwm7g"
dfs(node)
returns:
(depth, lca)
```

---

# Optimal Code

```python id="jlwm2h"
class Solution:

    def lcaDeepestLeaves(self, root):

        def dfs(node):

            if not node:
                return (0, None)

            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)

            # left subtree deeper
            if left_depth > right_depth:
                return (left_depth + 1, left_lca)

            # right subtree deeper
            if right_depth > left_depth:
                return (right_depth + 1, right_lca)

            # equal depth -> current node is LCA
            return (left_depth + 1, node)

        return dfs(root)[1]
```

---

# Why This Works

Suppose:

```text id="jlwm6g"
left depth = 5
right depth = 3
```

Then:

* all deepest leaves are inside left subtree
* left LCA remains answer

---

If:

```text id="jlwm3g"
left depth = right depth
```

Then:

* deepest leaves split across both sides
* current node becomes first common ancestor.

---

# Complexity

## Time

```text id="jlwm9f"
O(n)
```

Each node visited once.

---

## Space

```text id="jlwm5g"
O(h)
```

Recursion stack.

---

# 8. Step-by-Step Trace

Input:

```text id="jlwm4h"
            3
          /   \
         5     1
        / \   / \
       6   2 0   8
          / \
         7   4
```

---

# DFS Bottom-Up

---

## Leaves

```text id="jlwm0h"
6 -> (1,6)
7 -> (1,7)
4 -> (1,4)
0 -> (1,0)
8 -> (1,8)
```

---

## Node 2

Children:

```text id="jlwm7j"
7 -> depth 1
4 -> depth 1
```

Equal depth:

```text id="jlwm8k"
return (2, node 2)
```

---

## Node 5

Children:

```text id="jlwm3j"
6 -> depth 1
2 -> depth 2
```

Right deeper:

```text id="jlwm1j"
return (3, node 2)
```

---

## Node 1

Children equal:

```text id="jlwm2j"
return (2, node 1)
```

---

## Node 3

Children:

```text id="jlwm6j"
left depth = 3
right depth = 2
```

Left deeper:

```text id="jlwm5j"
return (4, node 2)
```

Final answer:

```text id="jlwm4k"
2
```

---

# 9. Related Problems

---

### Lowest Common Ancestor of a Binary Tree

Core LCA recursion pattern.

---

### Maximum Depth of Binary Tree

Depth computation foundation.

---

### Smallest Subtree with all the Deepest Nodes

Exact same problem statement internally.

---

### Diameter of Binary Tree

Postorder depth propagation.

---

### Balanced Binary Tree

Bottom-up subtree depth logic.
