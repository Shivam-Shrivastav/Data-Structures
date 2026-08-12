    # Minimum Absolute Difference in BST

LeetCode: Minimum Absolute Difference in BST

---

# 1. Problem Statement with Example

Given the root of a Binary Search Tree (BST), return:

```text id="q8u2m5"
minimum absolute difference
between values of any two different nodes
```

---

# BST Property

```text id="m4u7x1"
left subtree values  < node.val
right subtree values > node.val
```

Most important BST property:

```text id="r9u5m2"
Inorder traversal of BST
gives sorted order
```

---

# Example

Tree:

```text id="v1u8m4"
        4
       / \
      2   6
     / \
    1   3
```

Inorder traversal:

```text id="j6u2m7"
[1, 2, 3, 4, 6]
```

Differences:

```text id="d3u9m1"
2 - 1 = 1
3 - 2 = 1
4 - 3 = 1
6 - 4 = 2
```

Minimum absolute difference:

```text id="k5u1m8"
1
```

---

# Important Note

This problem is essentially identical to:

Minimum Distance Between BST Nodes

Same logic.
Same solution.

---

# 2. Diagram

BST:

```text id="n7u4m2"
         5
        / \
       3   8
      / \
     2   4
```

Inorder traversal:

```text id="p2u8m5"
2 -> 3 -> 4 -> 5 -> 8
```

---

# Key Insight

In sorted order:

```text id="f9u1m7"
minimum difference
always occurs between adjacent elements
```

No need to compare every pair.

---

# Why?

Suppose:

```text id="x4u7m3"
a < b < c
```

Then:

```text id="w8u2m6"
(c - a) >= (b - a)
```

So farther elements cannot create smaller difference than neighbors.

---

# 3. Example I/O

## Example 1

### Input

```text id="m1u5x9"
root = [4,2,6,1,3]
```

### Output

```text id="g3u8m2"
1
```

---

## Example 2

### Input

```text id="r7u4m1"
root = [1,0,48,null,null,12,49]
```

Inorder:

```text id="y2u9m5"
[0,1,12,48,49]
```

Minimum difference:

```text id="c6u1m8"
49 - 48 = 1
```

### Output

```text id="v5u3m4"
1
```

---

## Example 3

### Input

```text id="t8u2m7"
root = [1,null,3]
```

### Output

```text id="d4u9m1"
2
```

---

# 4. Intuition & Pattern Recognition

This is a classic:

```text id="k9u5m2"
BST inorder sorted-order problem
```

---

# Core Insight

BST inorder traversal gives:

```text id="x1u7m4"
sorted sequence
```

For sorted numbers:

```text id="q5u2m8"
minimum absolute difference
comes from adjacent values
```

---

# Important Optimization

We do NOT need entire inorder array.

During traversal:

maintain:

```text id="m8u4x1"
previous visited value
```

Compute:

```text id="f2u7m5"
current - previous
```

Update minimum.

---

# Interview Recognition Signal

Whenever you see:

```text id="w6u1m3"
BST + closest/minimum difference
```

Think:

```text id="p4u8m2"
inorder traversal
```

because inorder automatically sorts BST values.

---

# 5. Simpler Version

---

## Simplest Version

### Question

Find minimum difference in sorted array.

Easy:

```text id="j7u5m1"
compare adjacent elements
```

---

## Upgrade

Now numbers are stored in BST.

Use inorder traversal to generate sorted order.

---

# Simpler Related Problems

### 1. Binary Tree Inorder Traversal

Core inorder traversal.

---

### 2. Kth Smallest Element in a BST

Uses inorder sorted ordering.

---

### 3. Validate Binary Search Tree

BST ordering fundamentals.

---

## Transition to this problem

```text id="n3u7m8"
Sorted array:
adjacent difference check

BST:
inorder traversal creates sorted order
```

---

# 6. Brute Force

## Idea

1. Store all node values
2. Compare every pair

---

# Complexity

```text id="y8u1m4"
Time:  O(N²)
Space: O(N)
```

Very inefficient.

---

# Better Brute Force

1. Inorder traversal
2. Store sorted array
3. Check adjacent differences

Complexity:

```text id="r2u9m5"
Time:  O(N)
Space: O(N)
```

---

# 7. Optimal Solution

## Core Idea

Perform inorder traversal.

Maintain:

```text id="v6u3m1"
prev value
minimum difference
```

At each node:

```text id="d9u5m2"
diff = current - prev
```

Update answer.

---

# Clean Interview Code (Java)

```java id="t4u8m1"
class Solution {

    Integer prev = null;

    int minDiff = Integer.MAX_VALUE;

    public int getMinimumDifference(TreeNode root) {

        inorder(root);

        return minDiff;
    }

    private void inorder(TreeNode node) {

        if (node == null) {
            return;
        }

        inorder(node.left);

        // compare with previous inorder node
        if (prev != null) {

            minDiff =
                Math.min(minDiff, node.val - prev);
        }

        prev = node.val;

        inorder(node.right);
    }
}
```

---

# Complexity

```text id="m7u2x5"
Time:  O(N)
Space: O(H)
```

Where:

* `N` = nodes
* `H` = tree height

---

# 8. Step-by-Step Trace

Tree:

```text id="q1u8m4"
        4
       / \
      2   6
     / \
    1   3
```

---

# Inorder Traversal

Visit order:

```text id="x5u4m2"
1 -> 2 -> 3 -> 4 -> 6
```

---

# Processing

| Current | Prev | Difference | Min |
| ------- | ---- | ---------- | --- |
| 1       | null | -          | INF |
| 2       | 1    | 1          | 1   |
| 3       | 2    | 1          | 1   |
| 4       | 3    | 1          | 1   |
| 6       | 4    | 2          | 1   |

Final answer:

```text id="g8u1m7"
1
```

---

# 9. Related Problems

### 1. Minimum Distance Between BST Nodes

Essentially identical problem.

---

### 2. Kth Smallest Element in a BST

BST inorder sorted traversal.

---

### 3. Validate Binary Search Tree

BST ordering rules.

---

### 4. Two Sum IV - Input is a BST

Uses BST sorted ordering.

---

### 5. Closest Binary Search Tree Value

Nearest-value BST problem.
