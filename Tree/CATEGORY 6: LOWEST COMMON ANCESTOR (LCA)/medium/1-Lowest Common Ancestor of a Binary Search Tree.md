# Lowest Common Ancestor of a Binary Search Tree

LeetCode: Lowest Common Ancestor of a Binary Search Tree

---

# 1. Problem Statement with Example

Given a Binary Search Tree (BST) and two nodes `p` and `q`, return their:

```text id="bq7x11"
Lowest Common Ancestor (LCA)
```

---

# Definition of LCA

The LCA of two nodes is:

```text id="m1ow6z"
the lowest node in the tree
that has both p and q
in its subtree
```

A node can be ancestor of itself.

---

## Example

```text id="cq4y0w"
          6
        /   \
       2     8
      / \   / \
     0   4 7   9
        / \
       3   5
```

Find LCA of:

```text id="vfdu0m"
p = 2
q = 8
```

Answer:

```text id="wo1lm0"
6
```

because:

* 2 is in left subtree
* 8 is in right subtree

---

## Constraints

* Tree is guaranteed to be BST
* All node values are unique
* Both nodes exist in tree

---

# 2. Diagram

BST property:

```text id="jlwm34"
left subtree  < root
right subtree > root
```

Suppose:

```text id="jlwm35"
p = 2
q = 8
root = 6
```

Visualization:

```text id="jlwm36"
          6
        /   \
       2     8
```

Since:

```text id="jlwm37"
2 < 6 < 8
```

they split here.

So:

```text id="jlwm38"
6 is LCA
```

---

## Another Case

Find LCA of:

```text id="jlwm39"
p = 2
q = 4
```

Tree:

```text id="jlwm40"
          6
         /
        2
         \
          4
```

Both nodes are on left side of 6.

Move left.

Eventually:

```text id="jlwm41"
2 becomes LCA
```

because a node can be ancestor of itself.

---

# 3. Example I/O

## Example 1

### Input

```text id="jlwm42"
root = [6,2,8,0,4,7,9,null,null,3,5]
p = 2
q = 8
```

### Output

```text id="jlwm43"
6
```

---

## Example 2

### Input

```text id="jlwm44"
root = [6,2,8,0,4,7,9,null,null,3,5]
p = 2
q = 4
```

### Output

```text id="jlwm45"
2
```

---

## Example 3

### Input

```text id="jlwm46"
root = [2,1]
p = 2
q = 1
```

### Output

```text id="jlwm47"
2
```

---

# 4. Intuition & Pattern Recognition

This is a classic:

```text id="jlwm48"
BST directional traversal problem
```

---

# Key Observation

BST gives ordering information.

At current node:

### Case 1

If:

```text id="jlwm49"
p.val < root.val
q.val < root.val
```

then BOTH nodes are in left subtree.

Move left.

---

### Case 2

If:

```text id="jlwm50"
p.val > root.val
q.val > root.val
```

then BOTH nodes are in right subtree.

Move right.

---

### Case 3

Otherwise:

```text id="jlwm51"
nodes split across current root
```

This current node is LCA.

---

# Why does split mean LCA?

Because:

```text id="jlwm52"
this is the FIRST node
where paths diverge
```

Exactly the definition of lowest common ancestor.

---

# Interview Recognition Signal

Whenever problem says:

```text id="jlwm53"
BST
ancestor
LCA
```

Think:

```text id="jlwm54"
Use BST ordering to eliminate subtrees
```

No need for full DFS.

---

# 5. Simpler Version

---

## Simplest Version

### Question

Search for a value in BST.

Logic:

```text id="jlwm55"
smaller -> go left
larger  -> go right
```

---

## Upgrade

Now instead of ONE node:

track TWO nodes.

If both go same direction:

continue there.

If they split:

current node is answer.

---

# Simpler Related Problems

### 1. Search in a Binary Search Tree

Learn BST directional traversal.

---

### 2. Lowest Common Ancestor of a Binary Tree

General tree version without BST optimization.

---

### 3. Validate Binary Search Tree

BST ordering fundamentals.

---

## Transition to this problem

```text id="jlwm56"
BST search:
one target decides direction

LCA in BST:
two targets decide direction
```

---

# 6. Brute Force

## General Binary Tree LCA

Without BST property:

* DFS both subtrees
* propagate answers upward

Complexity:

```text id="jlwm57"
Time:  O(N)
Space: O(H)
```

---

# BST Optimization

BST ordering allows:

```text id="jlwm58"
single path traversal
```

Much cleaner.

---

# 7. Optimal Solution

## Core Idea

At every node:

* both smaller → left
* both larger → right
* split → current node is LCA

---

# Clean Interview Code (Java)

```java id="jlwm59"
class Solution {

    public TreeNode lowestCommonAncestor(TreeNode root,
                                         TreeNode p,
                                         TreeNode q) {

        while (root != null) {

            // both nodes in left subtree
            if (p.val < root.val && q.val < root.val) {

                root = root.left;
            }

            // both nodes in right subtree
            else if (p.val > root.val && q.val > root.val) {

                root = root.right;
            }

            // split occurs here
            else {
                return root;
            }
        }

        return null;
    }
}
```

---

# Complexity

```text id="jlwm60"
Time:  O(H)
Space: O(1)
```

Where:

* `H` = tree height

Balanced BST:

```text id="jlwm61"
O(log N)
```

Worst skewed tree:

```text id="jlwm62"
O(N)
```

---

# 8. Step-by-Step Trace

Tree:

```text id="jlwm63"
          6
        /   \
       2     8
      / \
     0   4
```

Find:

```text id="jlwm64"
p = 2
q = 4
```

---

## Step 1

Current root:

```text id="jlwm65"
6
```

Check:

```text id="jlwm66"
2 < 6
4 < 6
```

Both left.

Move left.

---

## Step 2

Current root:

```text id="jlwm67"
2
```

Check:

```text id="jlwm68"
p == root
```

Split condition automatically satisfied.

Answer:

```text id="jlwm69"
2
```

---

# 9. Related Problems

### 1. Lowest Common Ancestor of a Binary Tree

General tree version without BST optimization.

---

### 2. Search in a Binary Search Tree

Core BST directional movement.

---

### 3. Insert into a Binary Search Tree

Another BST traversal problem.

---

### 4. Validate Binary Search Tree

BST ordering fundamentals.

---

### 5. Kth Smallest Element in a BST

Uses BST traversal properties.
