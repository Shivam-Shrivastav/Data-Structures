# Smallest Subtree with all the Deepest Nodes

LeetCode 865 — Tree + DFS + Bottom-Up Recursion

---

# 1. Problem Statement

Given the `root` of a binary tree:

Return the **smallest subtree** that contains **all the deepest nodes**.

The answer should be:

* the root node of that subtree.

---

## Example

```text id="o0rmtw"
            3
          /   \
         5     1
        / \   / \
       6   2 0   8
          / \
         7   4
```

Deepest nodes:

```text id="jlwm1s"
7 and 4
```

Smallest subtree containing both:

```text id="jlwm3t"
      2
     / \
    7   4
```

Answer:

```text id="jlwm5t"
2
```

---

## Constraints

* Number of nodes: `[1, 500]`
* All node values unique

Important:

* deepest nodes may exist:

  * entirely on left
  * entirely on right
  * split across both sides

---

# 2. Diagram

```text id="jlwm7u"
                3
             /     \
            5       1
          /   \    / \
         6     2  0   8
              / \
             7   4
```

Deepest depth:

```text id="jlwm9u"
7 -> depth 3
4 -> depth 3
```

Smallest subtree containing both:

```text id="jlwm0x"
2
```

---

# Important Alternate Case

```text id="jlwm2x"
         1
       /   \
      2     3
```

Deepest nodes:

* 2
* 3

Smallest subtree:

```text id="jlwm4x"
1
```

because deepest nodes split across both sides.

---

# 3. Example I/O

## Example 1

### Input

```text id="jlwm6y"
root = [3,5,1,6,2,0,8,null,null,7,4]
```

### Output

```text id="jlwm8y"
2
```

---

## Example 2

### Input

```text id="jlwm1y"
root = [1]
```

### Output

```text id="jlwm3z"
1
```

Single node itself.

---

# 4. Intuition & Pattern Recognition

This is secretly:

### Lowest Common Ancestor of Deepest Leaves

They are effectively the SAME problem.

---

# Core Insight

At every node:

* compare left subtree depth
* compare right subtree depth

---

# Cases

---

## Case 1

```text id="jlwm5z"
left depth > right depth
```

All deepest nodes lie in left subtree.

Return:

* left answer

---

## Case 2

```text id="jlwm7z"
right depth > left depth
```

All deepest nodes lie in right subtree.

Return:

* right answer

---

## Case 3

```text id="jlwm0aa"
left depth == right depth
```

Deepest nodes split across both sides.

Current node becomes:

* smallest subtree root
* LCA of deepest nodes

---

# Pattern Recognition Signals

Keywords:

* “deepest nodes”
* “smallest subtree”
* “contains all”

Usually means:

```text id="jlwm2aa"
Bottom-up DFS
```

because:

* subtree information required first.

---

# 5. Simpler Version

---

## Simpler Problem 1

### Maximum Depth of Binary Tree

Compute subtree depths.

---

## Simpler Problem 2

### Lowest Common Ancestor of a Binary Tree

Find common ancestor using postorder recursion.

---

# This Problem Combines Both

Need:

1. subtree depth
2. subtree root containing deepest nodes

---

# Simpler Thinking Path

### Step 1

Compute subtree depths

↓

### Step 2

Deeper side contains deepest nodes

↓

### Step 3

Equal depth means:

* deepest nodes exist on both sides
* current node becomes answer

---

# 6. Brute Force

## Naive Method

1. Find deepest nodes
2. Compute pairwise LCAs
3. Merge answers

Complicated and inefficient.

---

# Complexity

Could become:

```text id="jlwm4aa"
O(n^2)
```

---

# 7. Optimal Solution

# Bottom-Up DFS

Return:

1. maximum depth
2. subtree root containing deepest nodes

---

# DFS Meaning

```python id="jlwm6aa"
dfs(node)
returns:
(depth, subtree_root)
```

---

# Optimal Code

```python id="jlwm8aa"
class Solution:

    def subtreeWithAllDeepest(self, root):

        def dfs(node):

            if not node:
                return (0, None)

            left_depth, left_node = dfs(node.left)
            right_depth, right_node = dfs(node.right)

            # left subtree deeper
            if left_depth > right_depth:
                return (left_depth + 1, left_node)

            # right subtree deeper
            if right_depth > left_depth:
                return (right_depth + 1, right_node)

            # equal depth -> current node
            return (left_depth + 1, node)

        return dfs(root)[1]
```

---

# Why This Works

Suppose:

```text id="jlwm1ab"
left depth = 5
right depth = 3
```

Then:

* all deepest nodes entirely in left subtree
* left subtree answer propagates upward

---

If:

```text id="jlwm3ab"
left depth == right depth
```

Then:

* deepest nodes exist on both sides
* current node becomes smallest connecting subtree

---

# Complexity

## Time

```text id="jlwm5ab"
O(n)
```

Every node visited once.

---

## Space

```text id="jlwm7ab"
O(h)
```

Recursion stack.

Worst case:

* skewed tree → `O(n)`

Balanced:

* `O(log n)`

---

# 8. Step-by-Step Trace

Input:

```text id="jlwm9ab"
            3
          /   \
         5     1
        / \   / \
       6   2 0   8
          / \
         7   4
```

---

# Bottom-Up DFS

---

## Leaves

```text id="jlwm0ac"
6 -> (1,6)
7 -> (1,7)
4 -> (1,4)
0 -> (1,0)
8 -> (1,8)
```

---

## Node 2

Children:

```text id="jlwm2ac"
7 depth = 1
4 depth = 1
```

Equal:

```text id="jlwm4ac"
return (2, node 2)
```

---

## Node 5

Children:

```text id="jlwm6ac"
6 depth = 1
2 depth = 2
```

Right deeper:

```text id="jlwm8ac"
return (3, node 2)
```

---

## Node 1

Equal children:

```text id="jlwm1ad"
return (2, node 1)
```

---

## Node 3

Children:

```text id="jlwm3ad"
left depth = 3
right depth = 2
```

Left deeper:

```text id="jlwm5ad"
return (4, node 2)
```

Final answer:

```text id="jlwm7ad"
2
```

---

# 9. Related Problems

---

### Lowest Common Ancestor of Deepest Leaves

Essentially identical problem.

---

### Lowest Common Ancestor of a Binary Tree

Core ancestor recursion pattern.

---

### Maximum Depth of Binary Tree

Subtree depth computation.

---

### Diameter of Binary Tree

Bottom-up depth propagation.

---

### Balanced Binary Tree

Postorder subtree height logic.
