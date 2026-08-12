# 701. Insert into a Binary Search Tree

## 1. Problem Statement with Example

You are given the `root` of a Binary Search Tree (BST) and an integer `val`.

Insert `val` into the BST and return the root of the updated BST.

The BST property must remain valid after insertion.

---

# BST Property

```text id="j2nq5k"
Left subtree values  < root
Right subtree values > root
```

The problem guarantees:

* `val` does not already exist in the BST.

---

## Constraints

* Number of nodes: `0 <= n <= 10^4`
* `-10^8 <= Node.val <= 10^8`

---

## Example

### Input

```text id="mbq7pk"
root = [4,2,7,1,3]
val = 5
```

---

### Original Tree

```text id="nt5h0q"
        4
       / \
      2   7
     / \
    1   3
```

---

### After Insertion

```text id="xwgj6h"
        4
       / \
      2   7
     / \  /
    1  3 5
```

---

# 2. Diagram

## Key Idea

Insertion path is determined entirely by BST ordering.

---

## Example

Insert `5`

---

### Step 1

```text id="c0vlfm"
current = 4

5 > 4
```

Move RIGHT.

---

### Step 2

```text id="bjlwm7"
current = 7

5 < 7
```

Move LEFT.

---

### Step 3

Left child is empty:

```text id="jlwmz6"
7.left = TreeNode(5)
```

Done ✅

---

# 3. Example I/O

## Example 1

### Input

```text id="jlwm1v"
root = [4,2,7,1,3]
val = 5
```

### Output

```text id="jlwm98"
[4,2,7,1,3,5]
```

---

## Example 2

### Input

```text id="jlwmr9"
root = [40,20,60,10,30,50,70]
val = 25
```

### Output

```text id="jlwm5u"
[40,20,60,10,30,50,70,null,null,25]
```

---

## Edge Case

### Input

```text id="jlwm4o"
root = []
val = 1
```

### Output

```text id="jlwm8v"
[1]
```

---

# 4. Intuition & Pattern Recognition

This is the natural extension of:

## Search in BST

Instead of stopping when value not found:

* insert node there.

---

# Key Observation

BST structure tells exactly:

* where new node belongs.

At every node:

```text id="jlwm3g"
val < node.val -> left
val > node.val -> right
```

Eventually:

* reach empty spot (`None`)
* insert there.

---

# Interview Recognition Signal

Whenever you see:

```text id="6jlwmm"
BST
+
insert
```

Think:

> Same traversal as binary search.

---

# Why This Works

BST guarantees:

* every subtree is ordered.

So by moving:

* left for smaller
* right for larger

you preserve BST property automatically.

---

# 5. Simpler Version

# Simplest Question

## Search in BST

There:

* stop when found.

Here:

* stop when NULL found
* place node there.

---

# Thinking Evolution

## Step 1

Traverse like binary search.

---

## Step 2

Find missing child position.

---

## Step 3

Attach new node there.

---

# Related Simpler Problems

### 1. Search in BST

Exact same traversal logic.

### 2. Binary Search

Underlying decision pattern.

### 3. Validate BST

Understanding BST constraints.

### 4. Delete Node in BST

Harder BST modification problem.

### 5. Lowest Common Ancestor in BST

BST-directed traversal.

---

# 6. Brute Force

## Naive Idea

Ignore BST property:

* traverse all nodes
* find valid insertion place manually.

This wastes BST advantage.

---

# Complexity

### Time

```text id="jlwmv4"
O(N)
```

---

### Space

```text id="0jlwmc"
O(H)
```

---

# 7. Optimal Solution

# Core Idea

Traverse using BST ordering until:

* empty child found.

Insert new node there.

---

# Recursive Solution

```python id="jlwm2y"
class Solution:
    def insertIntoBST(self, root, val):

        # Empty spot found
        if not root:
            return TreeNode(val)

        # Insert into left subtree
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)

        # Insert into right subtree
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root
```

---

# Iterative Solution (Interview Friendly)

```python id="jlwm7p"
class Solution:
    def insertIntoBST(self, root, val):

        # Empty tree
        if not root:
            return TreeNode(val)

        current = root

        while True:

            # Go left
            if val < current.val:

                # Empty position found
                if not current.left:
                    current.left = TreeNode(val)
                    break

                current = current.left

            # Go right
            else:

                # Empty position found
                if not current.right:
                    current.right = TreeNode(val)
                    break

                current = current.right

        return root
```

---

# Complexity

### Time

Balanced BST:

```text id="jlwm5j"
O(log N)
```

Worst skewed tree:

```text id="7jlwm6"
O(N)
```

---

### Space

Recursive:

```text id="jlwm0f"
O(H)
```

Iterative:

```text id="jlwmm8"
O(1)
```

---

# 8. Step-by-Step Trace

Example:

```text id="9jlwmn"
        4
       / \
      2   7
     / \
    1   3
```

Insert:

```text id="xjlwm8"
5
```

---

# Step 1

Current:

```text id="3jlwmj"
4
```

Compare:

```text id="qjlwm5"
5 > 4
```

Move RIGHT.

---

# Step 2

Current:

```text id="jlwmx6"
7
```

Compare:

```text id="jlwmf2"
5 < 7
```

Move LEFT.

---

# Step 3

```text id="jlwm2r"
7.left = None
```

Insert:

```text id="jlwm8m"
7.left = TreeNode(5)
```

---

# Final Tree

```text id="2jlwmh"
        4
       / \
      2   7
     / \  /
    1  3 5
```

---

# 9. Related Problems

### 1. Search in BST

Same traversal logic.

### 2. Delete Node in BST

More complex BST modification.

### 3. Validate BST

Checks BST ordering rules.

### 4. Kth Smallest Element in BST

Uses inorder ordering.

### 5. Lowest Common Ancestor of BST

BST-directed navigation.
