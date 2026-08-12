# 110. Balanced Binary Tree

## 1. Problem Statement with Example

Given the root of a binary tree, determine whether the tree is **height-balanced**.

A binary tree is height-balanced if:

> For every node, the difference between the heights of the left and right subtree is at most `1`.

Return `True` if balanced, otherwise `False`.

### Constraints

* Number of nodes: `0 <= n <= 5000`
* Node values can be anything (not important here)
* Need efficient traversal because checking height repeatedly can become costly.

---

## 2. Diagram

### Balanced Tree

```text
        3
       / \
      9  20
         / \
        15  7
```

Heights:

```text
Node 9  -> 1
Node 15 -> 1
Node 7  -> 1
Node 20 -> 2
Node 3  -> 3
```

At every node:

```text
|leftHeight - rightHeight| <= 1
```

Balanced ✅

---

### Unbalanced Tree

```text
        1
       /
      2
     /
    3
```

At node `1`:

```text
leftHeight = 2
rightHeight = 0

difference = 2
```

Unbalanced ❌

---

## 3. Example I/O

### Example 1

### Input

```text
root = [3,9,20,null,null,15,7]
```

### Output

```text
True
```

### Why?

All nodes have subtree height difference ≤ 1.

---

### Example 2

### Input

```text
root = [1,2,2,3,3,null,null,4,4]
```

### Output

```text
False
```

### Why?

Left subtree becomes too deep compared to right subtree.

---

### Edge Case

### Input

```text
root = []
```

### Output

```text
True
```

Empty tree is balanced.

---

# 4. Intuition & Pattern Recognition

This problem screams:

## Pattern → Tree DFS + Bottom-Up Height Calculation

Key observation:

To check balance at a node, we need:

```text
height(left subtree)
height(right subtree)
```

Naively:

* Compute left height
* Compute right height
* Repeat for every node

This causes repeated height calculations.

---

## Interview Recognition Signal

Whenever you see:

```text
"for every node"
+
"height/depth"
```

Think:

> "Can I compute height while returning information upward?"

This usually means:

* Postorder DFS
* Bottom-up recursion

---

## Why Bottom-Up Works

Each node only needs:

* left subtree height
* right subtree height

Children can compute their heights first and return upward.

So one DFS traversal is enough.

---

# 5. Simpler Version

## Simplest Problem

### Maximum Depth of Binary Tree

LeetCode: `104. Maximum Depth of Binary Tree`

There:

* You only compute height.

Here:

* You compute height
* PLUS validate balance condition.

---

## Simpler Thinking → Current Problem

### Step 1

Learn height calculation:

```python
height = 1 + max(left, right)
```

---

### Step 2

Add condition:

```python
abs(left - right) <= 1
```

---

### Step 3

If any subtree becomes unbalanced:

* propagate failure upward immediately.

---

## Related Simpler Problems

### 1. Maximum Depth of Binary Tree

Only compute height.

### 2. Minimum Depth of Binary Tree

Variation of depth recursion.

### 3. Diameter of Binary Tree

Uses subtree heights similarly.

### 4. Same Tree

Basic recursive tree traversal.

### 5. Symmetric Tree

Recursive comparison pattern.

---

# 6. Brute Force

## Idea

For every node:

1. Compute left height
2. Compute right height
3. Check difference
4. Recurse again on children

This recomputes heights many times.

---

## Python Code

```python
class Solution:
    def isBalanced(self, root):

        def height(node):
            if not node:
                return 0

            return 1 + max(height(node.left), height(node.right))

        if not root:
            return True

        left = height(root.left)
        right = height(root.right)

        if abs(left - right) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
```

---

## Complexity

### Time

```text
O(N^2)
```

Worst case:

* skewed tree
* repeated height calculations

### Space

```text
O(H)
```

Recursion stack.

---

# 7. Optimal Solution

## Core Idea

Return:

* subtree height if balanced
* `-1` if unbalanced

This avoids extra traversals.

---

## Python Code

```python
class Solution:
    def isBalanced(self, root):

        def dfs(node):

            # Empty tree height = 0
            if not node:
                return 0

            # Get left subtree height
            left = dfs(node.left)

            # Left subtree already unbalanced
            if left == -1:
                return -1

            # Get right subtree height
            right = dfs(node.right)

            # Right subtree already unbalanced
            if right == -1:
                return -1

            # Current node unbalanced
            if abs(left - right) > 1:
                return -1

            # Return current height
            return 1 + max(left, right)

        return dfs(root) != -1
```

---

## Complexity

### Time

```text
O(N)
```

Each node visited once.

### Space

```text
O(H)
```

`H = tree height`

Worst case:

```text
O(N)
```

Balanced tree:

```text
O(log N)
```

---

# 8. Step-by-Step Trace

Example:

```text
        3
       / \
      9  20
         / \
        15  7
```

---

## DFS Traversal

### Node 9

```text
left = 0
right = 0

height = 1
```

Returns `1`

---

### Node 15

Returns `1`

---

### Node 7

Returns `1`

---

### Node 20

```text
left = 1
right = 1

abs(1 - 1) = 0
height = 2
```

Returns `2`

---

### Node 3

```text
left = 1
right = 2

abs(1 - 2) = 1
height = 3
```

Returns `3`

---

Final:

```text
dfs(root) != -1
```

Result:

```text
True
```

---

# 9. Related Problems

### 1. Maximum Depth of Binary Tree

Foundation problem for height recursion.

### 2. Diameter of Binary Tree

Uses left/right subtree heights similarly.

### 3. Binary Tree Maximum Path Sum

Bottom-up DFS returning subtree information.

### 4. Validate Binary Search Tree

Tree DFS with constraint propagation.

### 5. Subtree of Another Tree

Recursive tree structure checking with DFS.
