# Lowest Common Ancestor of a Binary Tree II (Premium)

LeetCode Premium: Lowest Common Ancestor of a Binary Tree II

---

# 1. Problem Statement with Example

Given:

* root of a binary tree
* two nodes `p` and `q`

Return their:

```text id="d7e1t4"
Lowest Common Ancestor (LCA)
```

BUT:

```text id="sj8l2m"
p and/or q may NOT exist in the tree
```

If either node does not exist:

```text id="7n0k1q"
return null
```

---

# Difference From Standard LCA

Standard LCA problem guarantees:

```text id="9h2m4w"
both nodes always exist
```

This version does NOT.

That changes everything.

---

# Example

Tree:

```text id="g3r5u2"
            3
          /   \
         5     1
```

---

## Case 1

```text id="f2w9x7"
p = 5
q = 1
```

Both exist.

Answer:

```text id="c4y1z8"
3
```

---

## Case 2

```text id="q8l7k1"
p = 5
q = 10
```

Node `10` does not exist.

Answer:

```text id="b1x0n5"
null
```

---

# 2. Diagram

Normal LCA logic:

```text id="z9m1s3"
left subtree finds p
right subtree finds q
=> current node is LCA
```

But now:

```text id="j6d5u0"
What if q doesn't exist?
```

Example:

```text id="d0x2v9"
        3
       /
      5
```

If:

```text id="m7n4r1"
p = 5
q = 100
```

Standard LCA code incorrectly returns:

```text id="v4j8k2"
5
```

because it found only one node.

But correct answer is:

```text id="p5s7w0"
null
```

---

# 3. Example I/O

## Example 1

### Input

```text id="u2k8m6"
root = [3,5,1,6,2,0,8,null,null,7,4]
p = 5
q = 1
```

### Output

```text id="r9f3c1"
3
```

---

## Example 2

### Input

```text id="h0t6v4"
root = [3,5,1]
p = 5
q = 10
```

### Output

```text id="x1b5m8"
null
```

---

## Example 3

### Input

```text id="n6y2q9"
root = [1]
p = 1
q = 1
```

### Output

```text id="c3w7r5"
1
```

---

# 4. Intuition & Pattern Recognition

This is:

```text id="t8u3p4"
Standard LCA + existence validation
```

---

# Key Observation

Normal LCA assumes:

```text id="w2m9k7"
both nodes definitely exist
```

Without that guarantee:

```text id="k1r5n0"
finding only one node is NOT enough
```

We must additionally verify:

```text id="f4v8s2"
Did we actually find BOTH p and q?
```

---

# Core Insight

We need TWO things:

```text id="g7x1u6"
1. LCA logic
2. existence tracking
```

---

# Interview Recognition Signal

Whenever problem says:

```text id="b9q6w3"
"node may not exist"
```

Think:

```text id="n4m2p8"
Need extra validation
```

This is extremely common interview twist.

---

# 5. Simpler Version

---

## Simplest Version

### Standard LCA

Assume both nodes exist.

Simple recursive DFS.

---

## Upgrade

Now one node may be missing.

Example:

```text id="m1x9r7"
find LCA(5, 100)
```

Normal DFS returns:

```text id="d3w5k8"
5
```

Wrong.

---

# Fix

Track whether:

```text id="j0n4u6"
pFound
qFound
```

Only return LCA if both are true.

---

# Simpler Related Problems

### 1. Lowest Common Ancestor of a Binary Tree

Base problem.

---

### 2. Find if Path Exists in Graph

Existence validation thinking.

---

### 3. Subtree of Another Tree

Recursive tree existence checking.

---

## Transition to this problem

```text id="y7u5x0"
Standard LCA:
assume nodes exist

LCA II:
must PROVE nodes exist
```

---

# 6. Brute Force

## Idea

1. Check if p exists
2. Check if q exists
3. If both exist:
   run standard LCA

---

# Complexity

Each traversal:

```text id="c8m4w1"
O(N)
```

Total:

```text id="v6q9t2"
O(N)
```

Still acceptable.

But can be combined into cleaner single DFS solution.

---

# 7. Optimal Solution

## Core Idea

Perform standard LCA recursion.

Meanwhile track:

```text id="x3f7u1"
foundP
foundQ
```

At end:

```text id="j9w2m5"
if both found:
    return LCA
else:
    return null
```

---

# Clean Interview Code (Java)

```java id="r5k8u2"
class Solution {

    boolean foundP = false;
    boolean foundQ = false;

    public TreeNode lowestCommonAncestor(TreeNode root,
                                         TreeNode p,
                                         TreeNode q) {

        TreeNode lca = dfs(root, p, q);

        // both nodes must exist
        if (foundP && foundQ) {
            return lca;
        }

        return null;
    }

    private TreeNode dfs(TreeNode root,
                         TreeNode p,
                         TreeNode q) {

        if (root == null) {
            return null;
        }

        TreeNode left = dfs(root.left, p, q);

        TreeNode right = dfs(root.right, p, q);

        // current node matches p
        if (root == p) {
            foundP = true;
            return root;
        }

        // current node matches q
        if (root == q) {
            foundQ = true;
            return root;
        }

        // nodes split across subtrees
        if (left != null && right != null) {
            return root;
        }

        return left != null ? left : right;
    }
}
```

---

# Complexity

```text id="z1m4u8"
Time:  O(N)
Space: O(H)
```

Where:

* `N` = nodes
* `H` = tree height

---

# 8. Step-by-Step Trace

Tree:

```text id="k7u1m3"
        3
       / \
      5   1
```

Find:

```text id="s4n9w2"
p = 5
q = 10
```

---

# DFS

### Visit 5

```text id="f8x3v6"
foundP = true
```

Return node `5`.

---

### Traverse rest of tree

Never find `10`.

So:

```text id="j2r5m9"
foundQ = false
```

---

# Final Check

```text id="w6p1x4"
foundP && foundQ
```

becomes:

```text id="d0k7u3"
true && false = false
```

Return:

```text id="h5m8n1"
null
```

Correct.

---

# 9. Related Problems

### 1. Lowest Common Ancestor of a Binary Tree

Base LCA problem.

---

### 2. Lowest Common Ancestor of a Binary Search Tree

BST-optimized LCA.

---

### 3. Smallest Subtree with all the Deepest Nodes

Advanced LCA-style recursion.

---

### 4. Subtree of Another Tree

Tree existence verification.

---

### 5. Binary Tree Paths

Recursive subtree exploration patterns.
