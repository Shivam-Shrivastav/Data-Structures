# 700. Search in a Binary Search Tree

## 1. Problem Statement with Example

Given the `root` of a Binary Search Tree (BST) and an integer `val`, find the node in the BST whose value equals `val`.

Return:

* the subtree rooted at that node if found
* `None` if not found

---

## BST Property

```text id="gx36ul"
Left subtree values  < root
Right subtree values > root
```

This property allows efficient searching.

---

## Constraints

* `1 <= number of nodes <= 5000`
* `1 <= Node.val <= 10^7`
* BST contains unique values.

---

## Example

### Input

```text id="r8cz5v"
root = [4,2,7,1,3]
val = 2
```

### Tree

```text id="2jlwmm"
        4
       / \
      2   7
     / \
    1   3
```

### Output

```text id="ctjlwm"
[2,1,3]
```

Returned subtree:

```text id="9myhdb"
      2
     / \
    1   3
```

---

# 2. Diagram

## Core Idea

Use BST ordering to eliminate half the tree.

---

### Example

Search for `2`

```text id="b8e5kl"
        4
       / \
      2   7
     / \
    1   3
```

---

## Step 1

```text id="cjlwm6"
2 < 4
```

Move LEFT.

---

## Step 2

```text id="8yjlwm"
current = 2
```

Found target ✅

---

# 3. Example I/O

## Example 1

### Input

```text id="gmmjlwm"
root = [4,2,7,1,3]
val = 2
```

### Output

```text id="1jlwmr"
[2,1,3]
```

---

## Example 2

### Input

```text id="7xqf5u"
root = [4,2,7,1,3]
val = 5
```

### Output

```text id="6cljlwm"
[]
```

`5` does not exist.

---

## Edge Case

### Input

```text id="jlwm6n"
root = [1]
val = 1
```

### Output

```text id="s5k2q7"
[1]
```

---

# 4. Intuition & Pattern Recognition

This is the most fundamental BST problem.

---

# Key Observation

In a normal binary tree:

* may need to search everywhere.

In BST:

* one comparison tells direction.

---

# Decision Rule

At node:

```text id="cxwjlwm"
if val < node.val:
    go left

if val > node.val:
    go right
```

Because BST guarantees ordering.

---

# Interview Recognition Signal

Whenever you see:

```text id="0jlwmm"
Binary Search Tree
+
find/search/value
```

Think:

> Binary Search on a tree.

---

# Why It Works

BST removes half the search space at every step.

Exactly like binary search in arrays.

---

# 5. Simpler Version

# Simplest Problem

## Binary Search in Sorted Array

Array:

```text id="jlwm8r"
[1,2,3,4,5]
```

Binary search:

* compare middle
* go left/right

---

# This Problem

BST is basically:

* hierarchical binary search structure.

---

# Thinking Evolution

## Step 1

Understand binary search in array.

---

## Step 2

BST stores sorted structure implicitly.

---

## Step 3

Use comparisons to move downward.

---

# Related Simpler Problems

### 1. Binary Search

Exact same elimination logic.

### 2. Insert into BST

Uses same traversal direction.

### 3. Validate BST

Checks BST ordering property.

### 4. Minimum Depth of Binary Tree

Basic tree traversal.

### 5. Lowest Common Ancestor of BST

Navigates tree using BST ordering.

---

# 6. Brute Force

## Naive Idea

Ignore BST property.

Traverse entire tree using DFS.

---

# Brute Force Code

```python id="jlwmv7"
class Solution:
    def searchBST(self, root, val):

        if not root:
            return None

        if root.val == val:
            return root

        left = self.searchBST(root.left, val)

        if left:
            return left

        return self.searchBST(root.right, val)
```

---

# Complexity

### Time

```text id="jlwm54"
O(N)
```

May visit all nodes.

---

### Space

```text id="jlwmx9"
O(H)
```

Recursion stack.

---

# 7. Optimal Solution

# Core Idea

Use BST ordering:

* smaller → left
* larger → right

---

# Recursive Solution

```python id="jlwmk5"
class Solution:
    def searchBST(self, root, val):

        # Not found
        if not root:
            return None

        # Found target
        if root.val == val:
            return root

        # Search left subtree
        if val < root.val:
            return self.searchBST(root.left, val)

        # Search right subtree
        return self.searchBST(root.right, val)
```

---

# Iterative Solution (Interview Preferred)

Avoids recursion stack.

```python id="jlwm6z"
class Solution:
    def searchBST(self, root, val):

        current = root

        while current:

            # Found target
            if current.val == val:
                return current

            # Move left
            if val < current.val:
                current = current.left

            # Move right
            else:
                current = current.right

        return None
```

---

# Complexity

### Time

Balanced BST:

```text id="jlwmmh"
O(log N)
```

Worst skewed BST:

```text id="jlwm8f"
O(N)
```

---

### Space

Recursive:

```text id="jlwmxy"
O(H)
```

Iterative:

```text id="jlwm7q"
O(1)
```

---

# 8. Step-by-Step Trace

Example:

```text id="7jlwm9"
        4
       / \
      2   7
     / \
    1   3
```

Search:

```text id="2y8s4f"
val = 3
```

---

# Step 1

Current:

```text id="3jlwm3"
4
```

Compare:

```text id="jlwm6b"
3 < 4
```

Move LEFT.

---

# Step 2

Current:

```text id="jlwm0v"
2
```

Compare:

```text id="jlwmr4"
3 > 2
```

Move RIGHT.

---

# Step 3

Current:

```text id="jlwm9s"
3
```

Found target ✅

Return subtree:

```text id="jlwmz1"
    3
```

---

# 9. Related Problems

### 1. Insert into a BST

Same traversal direction logic.

### 2. Delete Node in BST

BST navigation plus restructuring.

### 3. Validate Binary Search Tree

Checks ordering constraints.

### 4. Lowest Common Ancestor of BST

Uses BST comparisons to find split point.

### 5. Kth Smallest Element in BST

Uses BST inorder sorted property.
