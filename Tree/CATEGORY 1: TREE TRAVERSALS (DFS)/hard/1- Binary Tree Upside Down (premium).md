# Binary Tree Upside Down

LeetCode Premium: Binary Tree Upside Down

---

# 1. Problem Statement with Example

Given the root of a binary tree where:

* every right child is either:

  * a leaf node with a sibling
  * or `null`

Flip the tree upside down.

After flipping:

```text id="jlwm1a"
Original left child → becomes new parent
Original parent     → becomes right child
Original right child→ becomes left child
```

Return the new root.

---

# Example

Input:

```text id="jlwm2a"
        1
       / \
      2   3
     / \
    4   5
```

Output:

```text id="jlwm3a"
        4
       / \
      5   2
         / \
        3   1
```

---

# Constraints

* Number of nodes: `1 <= n <= 10`
* Tree structure follows problem condition.

---

# 2. Diagram

# Original Tree

```text id="jlwm4a"
        1
       / \
      2   3
     / \
    4   5
```

---

# Observe transformation

For node `2`:

```text id="jlwm5a"
    2
   / \
  4   5
```

After flipping:

```text id="jlwm6a"
    4
   / \
  5   2
```

---

# Entire Transformation

```text id="jlwm7a"
Before:                    After:

        1                         4
       / \                       / \
      2   3                     5   2
     / \                           / \
    4   5                         3   1
```

---

# Key Pattern

```text id="jlwm8a"
left child becomes parent
```

This is the core interview insight.

---

# 3. Example I/O

## Example 1 (Typical)

Input:

```text id="jlwm9a"
root = [1,2,3,4,5]
```

Output:

```text id="jlwm0b"
[4,5,2,null,null,3,1]
```

---

## Example 2 (Single Node)

Input:

```text id="jlwm1b"
root = [1]
```

Output:

```text id="jlwm2b"
[1]
```

Nothing changes.

---

# 4. Intuition & Pattern Recognition

This is a **pointer rewiring DFS** problem.

---

# Core Observation

We keep moving LEFT until:

```text id="jlwm3b"
leftmost node
```

That node becomes:

```text id="jlwm4b"
new root
```

Then while backtracking:

* old right child becomes new left child
* old parent becomes new right child

---

# Important Visualization

Original:

```text id="jlwm5b"
    parent
    /    \
 child   right
```

After flip:

```text id="jlwm6b"
     child
     /   \
 right  parent
```

---

# Interview Recognition

Whenever problem says:

* rotate tree structure
* flip tree
* upside down
* rewire children/parents

Think:

* DFS + pointer manipulation

---

# Key Recursive Insight

We must process:

```text id="jlwm7b"
deepest left node first
```

because that becomes new root.

This naturally suggests:

```text id="jlwm8b"
postorder-style DFS
```

(bottom-up processing)

---

# 5. Simpler Version

---

# Simplest Version

```text id="jlwm9b"
    1
   /
  2
```

Flip:

```text id="jlwm0c"
    2
     \
      1
```

---

# Slightly Harder

```text id="jlwm1c"
    1
   / \
  2   3
```

Flip:

```text id="jlwm2c"
    2
   / \
  3   1
```

Now extend recursively downward.

---

# Related Simpler Problems

### 1. Invert Binary Tree

LeetCode: Invert Binary Tree

Simple child swapping.

Difference:

* no parent-child restructuring.

---

### 2. Flatten Binary Tree to Linked List

LeetCode: Flatten Binary Tree to Linked List

Another pointer rewiring problem.

---

### 3. Binary Tree Postorder Traversal

LeetCode: Binary Tree Postorder Traversal

Important because transformation happens bottom-up.

---

# Thinking Progression

```text id="jlwm3c"
Go to deepest left node
        ↓
That becomes new root
        ↓
While backtracking:
rewire pointers
```

---

# 6. Brute Force

## Idea

1. Store parent-child relationships
2. Rebuild flipped tree manually

This is cumbersome and unnecessary.

---

## Brute Force Complexity

* Time: `O(n)`
* Space: `O(n)`

Extra storage needed.

---

# 7. Optimal Solution

# Recursive DFS (Interview-Friendly)

```python id="jlwm4c"
class Solution:

    def upsideDownBinaryTree(self, root):

        # Base case:
        # leftmost node becomes new root
        if not root or not root.left:
            return root

        # Recursively go left
        new_root = self.upsideDownBinaryTree(root.left)

        # Pointer rewiring
        root.left.left = root.right
        root.left.right = root

        # Disconnect old pointers
        root.left = None
        root.right = None

        return new_root
```

---

# Why This Works

Suppose:

```text id="jlwm5c"
    1
   / \
  2   3
```

After recursive call:

* subtree rooted at `2` already flipped

Now rewire:

```text id="jlwm6c"
2.left  = 3
2.right = 1
```

Result:

```text id="jlwm7c"
    2
   / \
  3   1
```

---

# Important Interview Insight

This line:

```python id="jlwm8c"
root.left.left = root.right
```

means:

```text id="jlwm9c"
old right child becomes new left child
```

---

And:

```python id="jlwm0d"
root.left.right = root
```

means:

```text id="jlwm1d"
old parent becomes new right child
```

---

# Complexity

## Time

```text id="jlwm2d"
O(n)
```

Each node visited once.

---

## Space

```text id="jlwm3d"
O(h)
```

Recursion stack.

Worst case skewed tree:

* `O(n)`

---

# 8. Step-by-Step Trace

Input:

```text id="jlwm4d"
        1
       / \
      2   3
     / \
    4   5
```

---

# Step 1 — Go left recursively

Traversal:

```text id="jlwm5d"
1 → 2 → 4
```

`4` becomes new root.

---

# Step 2 — Rewire at node 2

Original:

```text id="jlwm6d"
    2
   / \
  4   5
```

Rewire:

```text id="jlwm7d"
4.left  = 5
4.right = 2
```

Tree becomes:

```text id="jlwm8d"
    4
   / \
  5   2
```

---

# Step 3 — Rewire at node 1

Original:

```text id="jlwm9d"
    1
   / \
  2   3
```

Rewire:

```text id="jlwm0e"
2.left  = 3
2.right = 1
```

Final tree:

```text id="jlwm1e"
        4
       / \
      5   2
         / \
        3   1
```

---

# 9. Related Problems

### 1. Invert Binary Tree

Basic tree pointer manipulation.

---

### 2. Flatten Binary Tree to Linked List

Advanced pointer rewiring in trees.

---

### 3. Binary Tree Postorder Traversal

Bottom-up DFS processing pattern.

---

### 4. Populating Next Right Pointers in Each Node

Tree pointer manipulation problem.

---

### 5. Recover Binary Search Tree

Another tree structure correction/manipulation problem.
