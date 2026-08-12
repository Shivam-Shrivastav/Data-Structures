# Recover Binary Search Tree

LeetCode: Recover Binary Search Tree

---

# 1. Problem Statement with Example

You are given the root of a Binary Search Tree (BST), where:

```text id="gjl1r0"
exactly two nodes were swapped by mistake
```

Recover the BST **without changing its structure**.

You must fix the tree by swapping the values back.

---

# BST Property

For every node:

```text id="6o3gpf"
left subtree values  < root
right subtree values > root
```

Most important property:

```text id="13av06"
Inorder traversal of BST is sorted
```

---

## Example

Broken BST:

```text id="q7g3n5"
      3
     / \
    1   4
       /
      2
```

Inorder traversal:

```text id="1h6w1n"
[1, 3, 2, 4]
```

Not sorted.

Correct BST should be:

```text id="hjlwm1"
      2
     / \
    1   4
       /
      3
```

---

## Constraints

* Number of nodes up to `1000`
* Must modify tree in-place
* Follow-up asks for O(1) extra space (Morris Traversal)

---

# 2. Diagram

Correct BST inorder:

```text id="hjlwm2"
[1, 2, 3, 4, 5]
```

Suppose `2` and `4` are swapped:

```text id="hjlwm3"
[1, 4, 3, 2, 5]
```

Notice violations:

```text id="hjlwm4"
4 > 3
3 > 2
```

These "inversions" reveal swapped nodes.

---

## Adjacent Swap

```text id="hjlwm5"
[1, 3, 2, 4]
```

Only one violation.

---

## Non-Adjacent Swap

```text id="hjlwm6"
[1, 5, 3, 4, 2]
```

Two violations.

---

# 3. Example I/O

## Example 1

### Input

```text id="hjlwm7"
root = [1,3,null,null,2]
```

Tree:

```text id="hjlwm8"
    1
   /
  3
   \
    2
```

### Output

```text id="hjlwm9"
[3,1,null,null,2]
```

Recovered BST.

---

## Example 2

### Input

```text id="hjlwm10"
root = [3,1,4,null,null,2]
```

### Output

```text id="hjlwm11"
[2,1,4,null,null,3]
```

---

# 4. Intuition & Pattern Recognition

This is a classic:

```text id="hjlwm12"
BST inorder property problem
```

---

# Key Observation

A valid BST gives:

```text id="hjlwm13"
sorted inorder traversal
```

If two nodes are swapped:

```text id="hjlwm14"
sorted order breaks
```

So problem reduces to:

```text id="hjlwm15"
Find two misplaced elements in almost-sorted array
```

---

# Detecting Violations

During inorder traversal:

If:

```text id="hjlwm16"
prev.val > current.val
```

then BST ordering is broken.

---

# Which nodes to swap?

### First violation

```text id="hjlwm17"
first = prev
second = current
```

### Second violation (if exists)

Update:

```text id="hjlwm18"
second = current
```

Finally swap:

```text id="hjlwm19"
first.val <-> second.val
```

---

# Interview Recognition Signal

Whenever BST problem involves:

```text id="hjlwm20"
"two nodes swapped"
"BST corrupted"
"recover BST"
```

Immediately think:

```text id="hjlwm21"
Inorder traversal should be sorted
```

---

# 5. Simpler Version

---

## Simplest Version

### Question

Check if array is sorted.

Easy linear scan.

---

## Upgrade

Now exactly two elements are swapped.

Find them.

Example:

```text id="hjlwm22"
[1, 5, 3, 4, 2]
```

Violations:

```text id="hjlwm23"
5 > 3
4 > 2
```

Swapped elements:

```text id="hjlwm24"
5 and 2
```

---

## Final Upgrade

Instead of array:

we get BST.

Use inorder traversal to simulate sorted array.

---

# Simpler Related Problems

### 1. Binary Tree Inorder Traversal

Core inorder DFS.

---

### 2. Validate Binary Search Tree

Understanding BST inorder property.

---

### 3. Kth Smallest Element in a BST

Uses inorder sorted ordering.

---

## Transition to this problem

```text id="hjlwm25"
Valid BST:
inorder is sorted

Recover BST:
find where sorted order breaks
```

---

# 6. Brute Force

## Idea

1. Store inorder traversal in array
2. Sort array
3. Compare original vs sorted
4. Find mismatched nodes
5. Traverse tree again and fix

---

# Complexity

```text id="hjlwm26"
Time:  O(N log N)
Space: O(N)
```

Sorting dominates.

---

# 7. Optimal Solution

## Core Idea

Single inorder traversal.

Track:

```text id="hjlwm27"
prev
first
second
```

Detect inversions directly.

---

# Clean Interview Code (Java)

```java id="hjlwm28"
class Solution {

    TreeNode first = null;
    TreeNode second = null;
    TreeNode prev = null;

    public void recoverTree(TreeNode root) {

        inorder(root);

        // swap incorrect values
        int temp = first.val;
        first.val = second.val;
        second.val = temp;
    }

    private void inorder(TreeNode node) {

        if (node == null) {
            return;
        }

        inorder(node.left);

        // BST violation detected
        if (prev != null && prev.val > node.val) {

            // first violation
            if (first == null) {
                first = prev;
            }

            // always update second
            second = node;
        }

        prev = node;

        inorder(node.right);
    }
}
```

---

# Complexity

```text id="hjlwm29"
Time:  O(N)
Space: O(H)
```

Where:

* `H` = tree height
* recursion stack space

---

# 8. Step-by-Step Trace

Tree:

```text id="hjlwm30"
      3
     / \
    1   4
       /
      2
```

---

## Inorder Traversal

```text id="hjlwm31"
[1, 3, 2, 4]
```

---

## Scan

| prev | current | Violation? |
| ---- | ------- | ---------- |
| 1    | 3       | No         |
| 3    | 2       | YES        |
| 2    | 4       | No         |

---

## First Violation

```text id="hjlwm32"
first = 3
second = 2
```

Swap them.

---

## Final Tree

```text id="hjlwm33"
      2
     / \
    1   4
       /
      3
```

BST restored.

---

# 9. Related Problems

### 1. Validate Binary Search Tree

Core inorder BST property.

---

### 2. Binary Tree Inorder Traversal

Foundation traversal.

---

### 3. Kth Smallest Element in a BST

Uses inorder sorted order.

---

### 4. Convert BST to Greater Tree

BST traversal transformation.

---

### 5. Balance a Binary Search Tree

Another BST reconstruction problem.
