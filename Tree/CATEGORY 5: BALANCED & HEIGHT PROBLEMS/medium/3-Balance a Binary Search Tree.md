# Balance a Binary Search Tree

LeetCode: Balance a Binary Search Tree

---

# 1. Problem Statement with Example

Given the root of a Binary Search Tree (BST), return a:

```text id="0w10kg"
balanced BST
```

with the same node values.

A BST is balanced if:

```text id="dkn76x"
For every node:

| leftHeight - rightHeight | <= 1
```

You may return **any** valid balanced BST.

---

## Example

### Input (Unbalanced BST)

```text id="93i6qv"
        1
         \
          2
           \
            3
             \
              4
```

This is skewed like a linked list.

---

## Output (Balanced BST)

```text id="0cvlsr"
        2
       / \
      1   3
           \
            4
```

or

```text id="jlwmu1"
        3
       / \
      2   4
     /
    1
```

Both are balanced.

---

## Constraints

* Number of nodes up to `10^4`
* Existing tree is already a BST
* Need efficient reconstruction

---

# 2. Diagram

## Key Observation

Inorder traversal of BST gives:

```text id="jlwmu2"
sorted order
```

---

## Step 1 — Inorder Traversal

```text id="jlwmu3"
        1
         \
          2
           \
            3
             \
              4
```

Inorder:

```text id="jlwmu4"
[1, 2, 3, 4]
```

---

## Step 2 — Build Balanced BST

Use middle element repeatedly.

```text id="jlwmu5"
        2
       / \
      1   3
           \
            4
```

Exactly same idea as:

```text id="jlwmu6"
Convert Sorted Array to BST
```

---

# 3. Example I/O

## Example 1

### Input

```text id="jlwmu7"
root = [1,null,2,null,3,null,4]
```

### Output

```text id="jlwmu8"
[2,1,3,null,null,null,4]
```

---

## Example 2

### Input

```text id="jlwmu9"
root = [2,1,3]
```

### Output

```text id="jlwmu10"
[2,1,3]
```

Already balanced.

---

## Example 3 (Edge Case)

### Input

```text id="jlwmu11"
root = [1]
```

### Output

```text id="jlwmu12"
[1]
```

---

# 4. Intuition & Pattern Recognition

This is a combination of:

```text id="jlwmu13"
1. BST inorder traversal
2. Divide and conquer
```

---

## Key Insight

BST property guarantees:

```text id="jlwmu14"
inorder traversal = sorted array
```

Once we have sorted values:

problem reduces to:

```text id="jlwmu15"
Convert Sorted Array to Balanced BST
```

---

## Interview Recognition Signal

Whenever you see:

```text id="jlwmu16"
BST + sorted order
```

Think:

```text id="jlwmu17"
inorder traversal
```

Whenever you see:

```text id="jlwmu18"
balanced BST from sorted data
```

Think:

```text id="jlwmu19"
middle element recursion
```

---

# 5. Simpler Version

---

## Simplest Version

### Question

Get sorted values from BST.

Answer:

```text id="jlwmu20"
Inorder traversal
```

---

## Next Upgrade

Now rebuild tree from sorted values.

That becomes:

```text id="jlwmu21"
Convert Sorted Array to BST
```

---

# Simpler Related Problems

### 1. Binary Tree Inorder Traversal

Foundation for BST sorted extraction.

---

### 2. Convert Sorted Array to Binary Search Tree

Core rebuilding logic.

---

### 3. Validate Binary Search Tree

Understanding BST ordering.

---

## Transition to this problem

```text id="jlwmu22"
BST -> sorted array
sorted array -> balanced BST
```

Two standard problems combined.

---

# 6. Brute Force

## Naive Idea

Repeatedly rotate/rebalance manually like AVL tree operations.

Very complicated.

---

## Better Simpler Approach

1. Store inorder traversal
2. Rebuild balanced BST

This already gives optimal complexity.

---

# 7. Optimal Solution

## Core Idea

### Step 1

Perform inorder traversal:

```text id="jlwmu23"
BST -> sorted list
```

### Step 2

Build balanced BST from sorted array:

```text id="jlwmu24"
middle element = root
```

---

# Clean Interview Code (Java)

```java id="jlwmu25"
class Solution {

    List<Integer> inorder = new ArrayList<>();

    public TreeNode balanceBST(TreeNode root) {

        // step 1: get sorted values
        inorderTraversal(root);

        // step 2: build balanced BST
        return build(0, inorder.size() - 1);
    }

    private void inorderTraversal(TreeNode node) {

        if (node == null) {
            return;
        }

        inorderTraversal(node.left);

        inorder.add(node.val);

        inorderTraversal(node.right);
    }

    private TreeNode build(int left, int right) {

        if (left > right) {
            return null;
        }

        int mid = left + (right - left) / 2;

        TreeNode root = new TreeNode(inorder.get(mid));

        root.left = build(left, mid - 1);

        root.right = build(mid + 1, right);

        return root;
    }
}
```

---

# Complexity

## Time

```text id="jlwmu26"
O(N)
```

* Inorder traversal = O(N)
* Tree rebuilding = O(N)

---

## Space

```text id="jlwmu27"
O(N)
```

For storing inorder array.

---

# 8. Step-by-Step Trace

Input BST:

```text id="jlwmu28"
        1
         \
          2
           \
            3
             \
              4
```

---

## Step 1 — Inorder Traversal

```text id="jlwmu29"
[1, 2, 3, 4]
```

---

## Step 2 — Build Tree

Middle:

```text id="jlwmu30"
mid = 1
root = 2
```

Tree:

```text id="jlwmu31"
      2
```

---

## Left Half

```text id="jlwmu32"
[1]
```

Becomes:

```text id="jlwmu33"
      2
     /
    1
```

---

## Right Half

```text id="jlwmu34"
[3,4]
```

Middle:

```text id="jlwmu35"
3
```

Tree:

```text id="jlwmu36"
      2
     / \
    1   3
         \
          4
```

Balanced BST complete.

---

# 9. Related Problems

### 1. Convert Sorted Array to Binary Search Tree

Directly reused rebuilding logic.

---

### 2. Convert Sorted List to Binary Search Tree

Harder sorted-data-to-BST problem.

---

### 3. Binary Tree Inorder Traversal

BST sorted extraction.

---

### 4. Validate Binary Search Tree

BST ordering fundamentals.

---

### 5. Balanced Binary Tree

Understanding balance conditions.
