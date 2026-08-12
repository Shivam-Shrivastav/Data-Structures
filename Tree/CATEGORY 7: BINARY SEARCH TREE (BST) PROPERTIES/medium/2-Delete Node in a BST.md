# 450. Delete Node in a BST

## 1. Problem Statement with Example

Given the `root` of a Binary Search Tree (BST) and an integer `key`, delete the node with value `key` from the BST.

Return the root of the updated BST.

The BST property must remain valid after deletion.

---

# BST Property

```text id="axjz3f"
Left subtree values  < root
Right subtree values > root
```

---

## Constraints

* Number of nodes: `0 <= n <= 10^4`
* `-10^5 <= Node.val <= 10^5`

---

## Example

### Input

```text id="t5d84g"
root = [5,3,6,2,4,null,7]
key = 3
```

---

## Original Tree

```text id="n5l6q7"
        5
       / \
      3   6
     / \   \
    2   4   7
```

---

## After Deletion

```text id="clp8u0"
        5
       / \
      4   6
     /     \
    2       7
```

Output:

```text id="l3f8n9"
[5,4,6,2,null,null,7]
```

---

# 2. Diagram

Deletion in BST has **3 cases**.

---

# Case 1 — Leaf Node

Delete directly.

```text id="mgq2y8"
    5
   /
  3
```

Delete `3`

```text id="s8f6w2"
    5
```

---

# Case 2 — One Child

Replace node with child.

```text id="f2v8k4"
    5
   /
  3
 /
2
```

Delete `3`

```text id="c7x9u1"
    5
   /
  2
```

---

# Case 3 — Two Children (Important)

Use:

* inorder successor (smallest in right subtree)

OR

* inorder predecessor (largest in left subtree)

---

## Example

```text id="w6k1r0"
        5
       / \
      3   6
     / \   
    2   4
```

Delete `3`

Successor:

```text id="k4m9z2"
4
```

Replace:

```text id="u7c3n1"
        5
       / \
      4   6
     /
    2
```

---

# 3. Example I/O

## Example 1

### Input

```text id="q3n8v6"
root = [5,3,6,2,4,null,7]
key = 3
```

### Output

```text id="h8y2m5"
[5,4,6,2,null,null,7]
```

---

## Example 2

### Input

```text id="p1t6s9"
root = [5,3,6,2,4,null,7]
key = 0
```

### Output

```text id="j4d7k8"
[5,3,6,2,4,null,7]
```

Key not found.

---

## Edge Case

### Input

```text id="r2w5q1"
root = [1]
key = 1
```

### Output

```text id="x9n4c3"
[]
```

---

# 4. Intuition & Pattern Recognition

This is the hardest basic BST operation.

---

# Key Observation

Searching is easy because BST gives direction.

Deletion is harder because:

* removing node can break tree structure.

---

# Critical Part

When node has:

* 0 children → easy
* 1 child → easy
* 2 children → tricky

Need replacement value that preserves BST ordering.

---

# Why Inorder Successor Works

Successor is:

```text id="f8q2z4"
smallest node in right subtree
```

So it is:

* greater than everything on left
* smaller than remaining right subtree

Perfect replacement.

---

# Interview Recognition Signal

Whenever you see:

```text id="k9p3t7"
BST deletion
```

Think immediately:

> 3 deletion cases.

---

# 5. Simpler Version

# Simplest Questions

## 1. Search in BST

Find target node.

---

## 2. Insert into BST

Understand tree restructuring.

---

# Thinking Evolution

## Step 1

Search for node.

---

## Step 2

Handle simple cases:

* no child
* one child

---

## Step 3

Learn inorder successor replacement.

---

# Related Simpler Problems

### 1. Search in BST

Finding target node.

### 2. Insert into BST

Basic BST modification.

### 3. Validate BST

Understanding BST ordering.

### 4. Inorder Traversal

Needed for successor intuition.

### 5. Kth Smallest Element in BST

Uses inorder sorted ordering.

---

# 6. Brute Force

## Naive Idea

### Step 1

Perform inorder traversal.

### Step 2

Store all values except target.

### Step 3

Rebuild BST from scratch.

---

# Complexity

### Time

```text id="y3m8v1"
O(N)
```

---

### Space

```text id="t5c9k4"
O(N)
```

Extra array + rebuild.

---

# 7. Optimal Solution

# Core Idea

Recursive BST deletion using 3 cases.

---

# Python Code

```python id="z8p4n6"
class Solution:
    def deleteNode(self, root, key):

        if not root:
            return None

        # Search left subtree
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        # Search right subtree
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        # Node found
        else:

            # Case 1: no left child
            if not root.left:
                return root.right

            # Case 2: no right child
            if not root.right:
                return root.left

            # Case 3: two children
            # Find inorder successor
            successor = root.right

            while successor.left:
                successor = successor.left

            # Replace value
            root.val = successor.val

            # Delete successor node
            root.right = self.deleteNode(root.right, successor.val)

        return root
```

---

# Complexity

### Time

Balanced BST:

```text id="m1n5q8"
O(log N)
```

Worst skewed BST:

```text id="d6r2v9"
O(N)
```

---

### Space

Recursive stack:

```text id="p4x7c1"
O(H)
```

---

# 8. Step-by-Step Trace

Example:

```text id="u8y4m2"
        5
       / \
      3   6
     / \   \
    2   4   7
```

Delete:

```text id="c3n9k7"
3
```

---

# Step 1 — Find Node

```text id="v5q1m8"
3 < 5
```

Move LEFT.

---

# Step 2 — Node Found

```text id="z7p2x4"
root = 3
```

Node has:

* left child = 2
* right child = 4

So:

```text id="j8r5n1"
Case 3
```

---

# Step 3 — Find Successor

Right subtree:

```text id="f4m8v2"
4
```

Successor:

```text id="w9k3p6"
4
```

---

# Step 4 — Replace Value

```text id="y2c7n5"
root.val = 4
```

Tree becomes:

```text id="g5x1r8"
        5
       / \
      4   6
     / \   \
    2   4   7
```

---

# Step 5 — Delete Duplicate Successor

Delete right-side `4`.

Final:

```text id="n6v2p9"
        5
       / \
      4   6
     /     \
    2       7
```

---

# 9. Related Problems

### 1. Insert into BST

Basic BST modification.

### 2. Search in BST

Core BST traversal.

### 3. Validate BST

Ensuring ordering correctness.

### 4. Recover Binary Search Tree

BST correction problem.

### 5. Kth Smallest Element in BST

Uses inorder ordering property.
