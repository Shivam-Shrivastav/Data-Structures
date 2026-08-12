# 783. Minimum Distance Between BST Nodes

## 1. Problem Statement with Example

Given the `root` of a Binary Search Tree (BST), return the minimum difference between values of any two different nodes.

---

# BST Property

```text id="e3k8v2"
Left subtree values  < root
Right subtree values > root
```

---

# Important Insight

Inorder traversal of BST gives:

```text id="q7m1x5"
sorted ascending values
```

The minimum difference in a sorted array is always between adjacent elements.

---

## Constraints

* `2 <= number of nodes <= 100`
* `0 <= Node.val <= 10^5`

---

## Example

### Input

```text id="w2n6p8"
root = [4,2,6,1,3]
```

---

## Tree

```text id="r5x1m4"
        4
       / \
      2   6
     / \
    1   3
```

---

## Inorder Traversal

```text id="n8p3v6"
1 -> 2 -> 3 -> 4 -> 6
```

Differences:

```text id="k4m7x9"
2-1 = 1
3-2 = 1
4-3 = 1
6-4 = 2
```

Minimum:

```text id="f1x5n2"
1
```

Output:

```text id="p7m3v8"
1
```

---

# 2. Diagram

# Core Idea

Convert BST into sorted order using inorder traversal.

---

# Example

```text id="u2x6m9"
        5
       / \
      3   8
     / \
    2   4
```

---

# Inorder Traversal

```text id="v4n8p1"
2 -> 3 -> 4 -> 5 -> 8
```

Minimum difference must exist between neighbors:

```text id="y7m2x4"
3-2 = 1
4-3 = 1
5-4 = 1
8-5 = 3
```

Answer:

```text id="t5n1p7"
1
```

---

# 3. Example I/O

## Example 1

### Input

```text id="m8x4n2"
root = [4,2,6,1,3]
```

### Output

```text id="q1p7m5"
1
```

---

## Example 2

### Input

```text id="x6n2p9"
root = [1,0,48,null,null,12,49]
```

---

## Inorder

```text id="r3m8x1"
0 -> 1 -> 12 -> 48 -> 49
```

Minimum difference:

```text id="n5p2v7"
1
```

### Output

```text id="k9x4m2"
1
```

---

# 4. Intuition & Pattern Recognition

This problem becomes easy after recognizing one BST property.

---

# Key Observation

BST inorder traversal gives:

```text id="c7n1p4"
sorted sequence
```

For any sorted sequence:

* minimum difference always occurs between adjacent elements.

Example:

```text id="m2x8p5"
[1, 4, 10, 11]
```

Need only check:

```text id="p6n3x9"
4-1
10-4
11-10
```

No need to compare every pair.

---

# Interview Recognition Signal

Whenever you see:

```text id="v1m7p3"
BST
+
minimum/closest difference
```

Think:

> Inorder traversal → sorted order.

---

# Why Adjacent Elements Are Enough

Suppose sorted array:

```text id="z4n8x2"
a < b < c
```

Then:

```text id="t7m2p6"
c - a > b - a
```

So farther elements can never give smaller difference.

---

# 5. Simpler Version

# Simplest Question

## Binary Tree Inorder Traversal

Learn inorder DFS first.

---

# Next Simpler Idea

## Minimum Difference in Sorted Array

Array:

```text id="w5n1x8"
[1,2,4,7]
```

Minimum difference found by adjacent comparisons.

---

# Combine Both Ideas

BST:

* inorder → sorted
* adjacent comparison → answer

---

# Related Simpler Problems

### 1. Binary Tree Inorder Traversal

Core DFS traversal.

### 2. Validate BST

Uses inorder sorted property.

### 3. Kth Smallest Element in BST

Also relies on inorder order.

### 4. Search in BST

Basic BST understanding.

### 5. Two Sum IV - Input is a BST

Uses BST ordering concepts.

---

# 6. Brute Force

# Naive Idea

### Step 1

Collect all node values.

### Step 2

Compare every pair.

---

# Brute Force Code

```python id="x2m7p4"
class Solution:
    def minDiffInBST(self, root):

        arr = []

        def dfs(node):

            if not node:
                return

            arr.append(node.val)

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        arr.sort()

        ans = float('inf')

        for i in range(1, len(arr)):
            ans = min(ans, arr[i] - arr[i - 1])

        return ans
```

---

# Complexity

### Time

```text id="m5n2x7"
O(N log N)
```

Sorting dominates.

---

### Space

```text id="p8x4n1"
O(N)
```

---

# 7. Optimal Solution

# Core Idea

Perform inorder traversal.
Track:

* previous node value
* minimum difference

---

# Python Code

```python id="v7n3x5"
class Solution:
    def minDiffInBST(self, root):

        self.prev = None
        self.ans = float('inf')

        def inorder(node):

            if not node:
                return

            # Left subtree
            inorder(node.left)

            # Current node
            if self.prev is not None:
                self.ans = min(self.ans, node.val - self.prev)

            self.prev = node.val

            # Right subtree
            inorder(node.right)

        inorder(root)

        return self.ans
```

---

# Complexity

### Time

```text id="n1x6p9"
O(N)
```

Each node visited once.

---

### Space

```text id="q4m8n2"
O(H)
```

Recursive stack depth.

Balanced tree:

```text id="t3p7x1"
O(log N)
```

Worst skewed:

```text id="m9n5x4"
O(N)
```

---

# 8. Step-by-Step Trace

Example:

```text id="r2x7m8"
        4
       / \
      2   6
     / \
    1   3
```

---

# Inorder Traversal

Sequence:

```text id="x5n1p4"
1 -> 2 -> 3 -> 4 -> 6
```

---

# Step 1

Visit `1`

```text id="m8x2p7"
prev = 1
ans = inf
```

---

# Step 2

Visit `2`

```text id="t4n9x1"
2 - 1 = 1
```

Update:

```text id="q7p3m5"
ans = 1
prev = 2
```

---

# Step 3

Visit `3`

```text id="w1x6n8"
3 - 2 = 1
```

No change.

---

# Step 4

Visit `4`

```text id="k5m2p9"
4 - 3 = 1
```

---

# Step 5

Visit `6`

```text id="v8n4x2"
6 - 4 = 2
```

Final:

```text id="y3p7m1"
ans = 1
```

---

# 9. Related Problems

### 1. Kth Smallest Element in BST

Uses inorder sorted ordering.

### 2. Validate BST

Uses inorder monotonic property.

### 3. Binary Tree Inorder Traversal

Core traversal pattern.

### 4. Two Sum IV - Input is a BST

Uses sorted BST traversal concepts.

### 5. Minimum Absolute Difference in BST

Almost identical problem.
