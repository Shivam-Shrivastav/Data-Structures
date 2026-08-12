# 98. Validate Binary Search Tree

## 1. Problem Statement with Example

Given the `root` of a binary tree, determine whether it is a **valid Binary Search Tree (BST)**.

A BST follows these rules:

1. Left subtree of a node contains only values **smaller** than the node.
2. Right subtree contains only values **greater** than the node.
3. Both left and right subtrees must also themselves be BSTs.

Return `True` if valid, otherwise `False`.

---

## Constraints

* Number of nodes: `1 <= n <= 10^4`
* `-2^31 <= Node.val <= 2^31 - 1`

---

## Example

### Valid BST

```text id="iq23h7"
        2
       / \
      1   3
```

Output:

```text id="gh2d64"
True
```

---

### Invalid BST

```text id="85od2f"
         5
        / \
       1   4
          / \
         3   6
```

Output:

```text id="x1sznk"
False
```

Why?

```text id="f4m6n6"
3 is inside right subtree of 5
but 3 < 5
```

So BST property breaks globally.

---

# 2. Diagram

## Common Mistake

Many people only compare:

```text id="bt9yie"
node.left < node
node.right > node
```

But BST condition is GLOBAL.

---

## Invalid Example

```text id="1t23sv"
         10
        /  \
       5    15
           /  \
          6    20
```

Looks locally valid:

```text id="nzz3m6"
6 < 15
20 > 15
```

BUT:

```text id="2drz2x"
6 is in right subtree of 10
therefore must be > 10
```

Tree is invalid.

---

# 3. Example I/O

## Example 1

### Input

```text id="wvwjlwm"
root = [2,1,3]
```

### Output

```text id="tp0dxy"
True
```

---

## Example 2

### Input

```text id="otj77g"
root = [5,1,4,null,null,3,6]
```

### Output

```text id="l7c8g9"
False
```

---

## Edge Case

### Input

```text id="pqis8d"
root = [2147483647]
```

### Output

```text id="2k0vv0"
True
```

---

# 4. Intuition & Pattern Recognition

This is one of the most important BST interview problems.

---

# Key Insight

Each node is not only constrained by parent.

It is constrained by:

* all ancestors above it.

---

## Example

For node `6` here:

```text id="4krq0q"
         10
           \
            15
           /
          6
```

`6` must satisfy BOTH:

```text id="a5v7w4"
6 < 15
6 > 10
```

So each node needs:

* lower bound
* upper bound

---

# Pattern Recognition

Whenever you see:

```text id="1ajb5h"
BST validation
```

Think:

> DFS with min/max bounds.

---

# Why Bounds Work

For every node:

* valid range is inherited from ancestors.

Example:

```text id="5v6k1w"
Left subtree:
(-inf, parent.val)

Right subtree:
(parent.val, +inf)
```

As recursion continues:

* bounds become tighter.

---

# 5. Simpler Version

# Simplest Question

## Search in a BST

There:

* you use BST ordering property.

Here:

* you verify the entire tree follows that property.

---

# Another Simpler Insight

## Inorder Traversal of BST

A valid BST produces:

```text id="i8o93e"
strictly increasing inorder traversal
```

Example:

```text id="e4zq8f"
1 2 3 4 5
```

If sequence breaks:

* not BST.

---

# Thinking Evolution

## Step 1

Understand local BST rule.

---

## Step 2

Realize local checking is insufficient.

---

## Step 3

Pass valid ranges downward recursively.

---

# Related Simpler Problems

### 1. Search in a BST

Basic BST property usage.

### 2. Insert into BST

Maintaining BST property.

### 3. Inorder Traversal

Understanding sorted BST traversal.

### 4. Lowest Common Ancestor in BST

Uses BST ordering.

### 5. Balanced Binary Tree

Recursive tree validation pattern.

---

# 6. Brute Force

## Naive Idea

For every node:

* find max in left subtree
* find min in right subtree
* validate

Then recurse.

---

# Complexity

### Time

```text id="52q06f"
O(N^2)
```

Repeated subtree scans.

---

# Brute Force Code

```python id="7rqvkn"
class Solution:
    def isValidBST(self, root):

        def maxValue(node):
            while node.right:
                node = node.right
            return node.val

        def minValue(node):
            while node.left:
                node = node.left
            return node.val

        if not root:
            return True

        if root.left and maxValue(root.left) >= root.val:
            return False

        if root.right and minValue(root.right) <= root.val:
            return False

        return (
            self.isValidBST(root.left) and
            self.isValidBST(root.right)
        )
```

---

# 7. Optimal Solution

# Core Idea

Pass:

* lower bound
* upper bound

during DFS.

---

# Python Code

```python id="s3mljlwm"
class Solution:
    def isValidBST(self, root):

        def dfs(node, low, high):

            # Empty tree is valid
            if not node:
                return True

            # Node violates BST range
            if not (low < node.val < high):
                return False

            # Left subtree:
            # values must be smaller than current node
            left = dfs(node.left, low, node.val)

            # Right subtree:
            # values must be greater than current node
            right = dfs(node.right, node.val, high)

            return left and right

        return dfs(root, float('-inf'), float('inf'))
```

---

# Complexity

### Time

```text id="98x4v8"
O(N)
```

Each node visited once.

---

### Space

```text id="jz2t4o"
O(H)
```

Recursion stack.

Balanced tree:

```text id="yuklzm"
O(log N)
```

Worst skewed:

```text id="k7l5cz"
O(N)
```

---

# Alternative Optimal Solution

## Inorder Traversal

Since inorder of BST is strictly increasing.

---

## Code

```python id="qkg1i8"
class Solution:
    def isValidBST(self, root):

        self.prev = float('-inf')

        def inorder(node):

            if not node:
                return True

            if not inorder(node.left):
                return False

            # Current value must be greater
            if node.val <= self.prev:
                return False

            self.prev = node.val

            return inorder(node.right)

        return inorder(root)
```

---

# 8. Step-by-Step Trace

Example:

```text id="2oaqh4"
        5
       / \
      1   7
         / \
        6   8
```

---

# Start

```text id="6qjlwm"
dfs(5, -inf, inf)
```

Valid:

```text id="sffpws"
-inf < 5 < inf
```

---

# Left Subtree

```text id="9nt29z"
dfs(1, -inf, 5)
```

Valid:

```text id="ry87a2"
-inf < 1 < 5
```

---

# Right Subtree

```text id="5ytz2g"
dfs(7, 5, inf)
```

Valid:

```text id="g1kpcl"
5 < 7 < inf
```

---

# Node 6

```text id="3hspb8"
dfs(6, 5, 7)
```

Valid:

```text id="5 < 6 < 7"
```

---

# Node 8

```text id="r0sdc6"
dfs(8, 7, inf)
```

Valid.

---

Final Result:

```text id="7u0hx4"
True
```

---

# Invalid Example Trace

```text id="7gpjlwm"
        10
          \
           15
          /
         6
```

For node `6`:

```text id="3mjlwm"
dfs(6, 10, 15)
```

Check:

```text id="mjlwmk"
10 < 6 < 15
```

Fails ❌

---

# 9. Related Problems

### 1. Search in a BST

Basic BST traversal logic.

### 2. Insert into a BST

Maintaining BST constraints.

### 3. Recover Binary Search Tree

Fix swapped BST nodes.

### 4. Kth Smallest Element in BST

Uses inorder sorted property.

### 5. Lowest Common Ancestor of BST

Uses BST ordering to navigate efficiently.
