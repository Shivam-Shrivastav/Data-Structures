# Lowest Common Ancestor of a Binary Tree

LeetCode: Lowest Common Ancestor of a Binary Tree

---

# 1. Problem Statement with Example

Given a binary tree and two nodes `p` and `q`, return their:

```text id="2j2m5h"
Lowest Common Ancestor (LCA)
```

---

# Definition

The LCA is:

```text id="6u4d6m"
the lowest node in the tree
that has both p and q
in its subtree
```

A node can be ancestor of itself.

---

## Example

```text id="6kz0b9"
             3
           /   \
          5     1
         / \   / \
        6   2 0   8
           / \
          7   4
```

Find:

```text id="bq3h1e"
p = 5
q = 1
```

Answer:

```text id="mp5l3o"
3
```

because:

* 5 is in left subtree
* 1 is in right subtree

---

## Another Example

Find:

```text id="6gw6k2"
p = 5
q = 4
```

Answer:

```text id="6nyhvn"
5
```

because a node can be ancestor of itself.

---

## Constraints

* Tree is NOT necessarily BST
* Node values unique
* Both nodes exist in tree

---

# 2. Diagram

Case where nodes split:

```text id="1rgr3j"
             3
           /   \
          5     1
```

At node `3`:

```text id="6bc3nl"
p found in left subtree
q found in right subtree
```

So:

```text id="s0jv2h"
3 is LCA
```

---

## Case where one node is ancestor

```text id="v0r1p4"
          5
         / \
        6   2
           / \
          7   4
```

Find:

```text id="s0r9jo"
p = 5
q = 4
```

Since `5` already contains `4` in its subtree:

```text id="iqg6e6"
5 is LCA
```

---

# 3. Example I/O

## Example 1

### Input

```text id="91u8gm"
root = [3,5,1,6,2,0,8,null,null,7,4]
p = 5
q = 1
```

### Output

```text id="6m1bje"
3
```

---

## Example 2

### Input

```text id="5vfwgh"
root = [3,5,1,6,2,0,8,null,null,7,4]
p = 5
q = 4
```

### Output

```text id="6p5dzk"
5
```

---

## Example 3

### Input

```text id="3t6m7z"
root = [1,2]
p = 1
q = 2
```

### Output

```text id="4k4s2i"
1
```

---

# 4. Intuition & Pattern Recognition

This is a classic:

```text id="76dz5h"
Postorder DFS + Information Propagation
```

---

# Key Observation

At every node:

We ask:

```text id="u8df7x"
Does left subtree contain p or q?
Does right subtree contain p or q?
```

---

# Important Cases

### Case 1 — Current node is p or q

Return current node upward.

---

### Case 2 — p and q split across subtrees

```text id="1i0y1n"
left != null
right != null
```

Then:

```text id="km8b0u"
current node is LCA
```

---

### Case 3 — Both nodes on same side

Return whichever side is non-null.

---

# Why Postorder DFS?

Because current node decision depends on:

```text id="5c7r4l"
results from children
```

Classic bottom-up recursion.

---

# Interview Recognition Signal

Whenever problem says:

```text id="2k6x4t"
ancestor
path
common node
```

Think:

```text id="j4u8wr"
DFS returning information upward
```

---

# 5. Simpler Version

---

## Simplest Version

### Question

Find whether a value exists in tree.

Simple DFS.

---

## Upgrade

Now find TWO values.

If:

```text id="c6m0bp"
one found left
one found right
```

current node becomes merge point.

That merge point is LCA.

---

# Simpler Related Problems

### 1. Search in a Binary Tree

Basic recursive traversal.

---

### 2. Lowest Common Ancestor of a Binary Search Tree

Easier BST-optimized version.

---

### 3. Path Sum

DFS returning information upward.

---

## Transition to this problem

```text id="pmg6b2"
Normal DFS:
returns true/false

LCA DFS:
returns node references upward
```

---

# 6. Brute Force

## Idea

For each node:

1. Store path from root to p
2. Store path from root to q
3. Compare paths

Last common node = LCA.

---

# Complexity

```text id="qf7v1v"
Time:  O(N)
Space: O(N)
```

Works, but extra storage needed.

---

# 7. Optimal Solution

## Core Idea

Recursive DFS returns:

```text id="j3t5ko"
- p
- q
- LCA
- null
```

---

# Recursive Logic

At node:

```text id="f3e4j8"
1. recurse left
2. recurse right
```

Then:

### If current node is p/q

return current node.

### If both sides return non-null

current node is LCA.

### Otherwise

return non-null child.

---

# Clean Interview Code (Java)

```java id="4y0s5l"
class Solution {

    public TreeNode lowestCommonAncestor(TreeNode root,
                                         TreeNode p,
                                         TreeNode q) {

        // base cases
        if (root == null || root == p || root == q) {
            return root;
        }

        TreeNode left = lowestCommonAncestor(root.left, p, q);

        TreeNode right = lowestCommonAncestor(root.right, p, q);

        // nodes found on both sides
        if (left != null && right != null) {
            return root;
        }

        // return whichever side found something
        return left != null ? left : right;
    }
}
```

---

# Complexity

```text id="tb0r1n"
Time:  O(N)
Space: O(H)
```

Where:

* `N` = number of nodes
* `H` = tree height

---

# 8. Step-by-Step Trace

Tree:

```text id="l4f0jm"
             3
           /   \
          5     1
         / \
        6   2
           / \
          7   4
```

Find:

```text id="m4x4p0"
p = 5
q = 4
```

---

# DFS Flow

---

## Node 5

Matches `p`.

Return:

```text id="2l5u9k"
5
```

---

## Node 4

Matches `q`.

Return:

```text id="mj8h2g"
4
```

---

## Node 2

Receives:

```text id="3x1y9m"
left = null
right = 4
```

Returns:

```text id="1r6d5u"
4
```

---

## Node 5

Already matched `p`.

So subtree rooted at 5 contains both nodes.

Answer:

```text id="mw9r8w"
5
```

---

# 9. Related Problems

### 1. Lowest Common Ancestor of a Binary Search Tree

BST-optimized version.

---

### 2. Binary Tree Paths

Tree path DFS.

---

### 3. Path Sum

Recursive subtree information propagation.

---

### 4. Diameter of Binary Tree

Classic bottom-up DFS.

---

### 5. Smallest Subtree with all the Deepest Nodes

Advanced LCA-style recursion.
