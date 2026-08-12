# 173. Binary Search Tree Iterator

## 1. Problem Statement with Example

Implement a BST iterator class that represents the **inorder traversal** of a Binary Search Tree (BST).

You need to implement:

### `BSTIterator(root)`

Initializes iterator.

### `next()`

Returns next smallest number.

### `hasNext()`

Returns `True` if traversal still has elements.

---

# Important Requirement

Both operations should be:

```text id="o4wz3c"
Average O(1) time
```

and use:

```text id="v7p2m8"
O(H) memory
```

where:

* `H = tree height`

---

# BST Property

```text id="d5k8n1"
Inorder traversal of BST gives sorted order.
```

---

## Example

### BST

```text id="f9x2r4"
        7
       / \
      3   15
         /  \
        9    20
```

---

## Operations

```text id="w3m7v2"
BSTIterator(root)
next()    -> 3
next()    -> 7
hasNext() -> True
next()    -> 9
next()    -> 15
next()    -> 20
hasNext() -> False
```

---

# 2. Diagram

# Core Idea

Simulate inorder traversal using stack.

---

# Inorder Traversal

```text id="p6n4x9"
Left -> Root -> Right
```

---

# Initialization

Push all left nodes.

```text id="x1m8q3"
        7
       /
      3
```

Stack:

```text id="k5v2r7"
[7, 3]
```

Top = next smallest.

---

# next()

Pop top:

```text id="t8p4n6"
3
```

Then process its right subtree.

---

# After next()

Stack:

```text id="u2m7x1"
[7]
```

---

# 3. Example I/O

## Example 1

### Input

```text id="r9k3m5"
["BSTIterator", "next", "next", "hasNext", "next"]
[[[7,3,15,null,null,9,20]], [], [], [], []]
```

---

### Output

```text id="z4p8n2"
[null, 3, 7, true, 9]
```

---

## Edge Case

### Input

```text id="j7m1v4"
root = [1]
```

Operations:

```text id="y5x9k3"
next() -> 1
hasNext() -> False
```

---

# 4. Intuition & Pattern Recognition

This is an inorder traversal simulation problem.

---

# Key Observation

BST inorder traversal produces:

```text id="q2n6p8"
sorted ascending order
```

Iterator should:

* lazily generate next value
* not store all values beforehand

---

# Why Stack Works

Recursive inorder traversal uses call stack.

We simulate it manually using explicit stack.

---

# Interview Recognition Signal

Whenever you see:

```text id="m8v3x1"
iterator
+
tree traversal
```

Think:

> Controlled DFS using stack.

---

# 5. Simpler Version

# Simplest Problem

## Binary Tree Inorder Traversal

Normal recursion:

```python id="p5r2n7"
inorder(left)
visit(root)
inorder(right)
```

---

# This Problem

Instead of full traversal:

* pause traversal state
* continue later

So we need persistent stack.

---

# Thinking Evolution

## Step 1

Understand inorder traversal.

---

## Step 2

Convert recursion to stack.

---

## Step 3

Pause traversal between operations.

---

# Related Simpler Problems

### 1. Binary Tree Inorder Traversal

Core traversal pattern.

### 2. Kth Smallest Element in BST

Uses inorder ordering.

### 3. Validate BST

Uses inorder sorted property.

### 4. Flatten Binary Tree to Linked List

Controlled DFS traversal.

### 5. Implement Queue using Stacks

State simulation using data structure.

---

# 6. Brute Force

# Naive Idea

### Step 1

Perform complete inorder traversal.

### Step 2

Store all values in array.

### Step 3

Use pointer index for iterator.

---

# Brute Force Code

```python id="n4x7p2"
class BSTIterator:

    def __init__(self, root):

        self.arr = []
        self.index = 0

        def inorder(node):

            if not node:
                return

            inorder(node.left)
            self.arr.append(node.val)
            inorder(node.right)

        inorder(root)

    def next(self):
        val = self.arr[self.index]
        self.index += 1
        return val

    def hasNext(self):
        return self.index < len(self.arr)
```

---

# Complexity

### Initialization

```text id="w6m2k8"
O(N)
```

---

### Space

```text id="t1x5n9"
O(N)
```

Stores entire traversal.

---

# 7. Optimal Solution

# Core Idea

Maintain stack of:

* current path toward smallest unvisited node.

---

# Python Code

```python id="v3p8m1"
class BSTIterator:

    def __init__(self, root):

        self.stack = []

        # Push all left nodes
        self.pushLeft(root)

    def pushLeft(self, node):

        while node:
            self.stack.append(node)
            node = node.left

    def next(self):

        # Smallest available node
        node = self.stack.pop()

        # Process right subtree
        self.pushLeft(node.right)

        return node.val

    def hasNext(self):

        return len(self.stack) > 0
```

---

# Complexity

## next()

Average:

```text id="f8n4p2"
O(1)
```

Amortized because each node:

* pushed once
* popped once

---

## Space

```text id="u5m1x7"
O(H)
```

Only current traversal path stored.

---

# 8. Step-by-Step Trace

Example:

```text id="c2p7n4"
        7
       / \
      3   15
         /  \
        9    20
```

---

# Initialization

Push left chain:

```text id="r4m8x1"
7 -> 3
```

Stack:

```text id="n9p2v5"
[7, 3]
```

Top = `3`

---

# next()

Pop:

```text id="t6x1m8"
3
```

Stack:

```text id="q3n7p4"
[7]
```

Return:

```text id="m1v5x9"
3
```

---

# next()

Pop:

```text id="w8p2n6"
7
```

Process right subtree:

* push `15`
* push `9`

Stack:

```text id="k4m7x2"
[15, 9]
```

Return:

```text id="j2n8p5"
7
```

---

# next()

Pop:

```text id="f1x6m3"
9
```

Stack:

```text id="r5p9n2"
[15]
```

Return:

```text id="z7m4x1"
9
```

Traversal continues similarly.

---

# 9. Related Problems

### 1. Binary Tree Inorder Traversal

Foundation traversal pattern.

### 2. Kth Smallest Element in BST

Inorder traversal on BST.

### 3. Validate BST

Uses inorder sorted ordering.

### 4. Flatten Binary Tree to Linked List

Controlled DFS state handling.

### 5. Serialize and Deserialize BST

BST traversal + reconstruction concepts.
