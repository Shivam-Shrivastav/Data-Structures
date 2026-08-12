# 109. Convert Sorted List to Binary Search Tree

## 1. Problem Statement with Example

Given the head of a singly linked list where elements are sorted in ascending order, convert it into a **height-balanced Binary Search Tree (BST)**.

A height-balanced BST means:

> For every node, the height difference between left and right subtree is at most 1.

---

## BST Property

```text id="3cfh0n"
Left subtree values  < root
Right subtree values > root
```

---

## Constraints

* `0 <= number of nodes <= 2 * 10^4`
* `-10^5 <= Node.val <= 10^5`
* List is sorted in ascending order.

---

## Example

### Input

```text id="vyr3r0"
head = [-10,-3,0,5,9]
```

### One Valid Output

```text id="lj4tna"
        0
       / \
     -10   5
       \    \
       -3    9
```

Many valid balanced BSTs are acceptable.

---

# 2. Diagram

## Main Difficulty

Unlike arrays:

```text id="d4ep44"
Array -> O(1) random access
Linked List -> O(N) traversal
```

So we cannot directly access the middle efficiently.

---

# Approach Visualization

## Linked List

```text id="vjlwm6"
-10 -> -3 -> 0 -> 5 -> 9
```

---

## Find Middle Using Slow/Fast Pointer

```text id="t5r7vf"
slow moves 1 step
fast moves 2 steps
```

When fast reaches end:

```text id="e63ye6"
slow = middle node
```

---

## Middle Becomes Root

```text id="18phlj"
          0
```

Left list:

```text id="t9xwh2"
-10 -> -3
```

Right list:

```text id="mho6u5"
5 -> 9
```

Recurse on both halves.

---

# 3. Example I/O

## Example 1

### Input

```text id="4p6g5y"
head = [-10,-3,0,5,9]
```

### Output

```text id="e2k7f8"
[0,-3,9,-10,null,5]
```

or any valid balanced BST.

---

## Example 2

### Input

```text id="jlwmz0"
head = []
```

### Output

```text id="2o8gpr"
[]
```

---

## Edge Case

### Input

```text id="a7b08u"
head = [1]
```

### Output

```text id="qarfze"
[1]
```

---

# 4. Intuition & Pattern Recognition

This problem is almost identical to:

## Simpler Problem

### Convert Sorted Array to BST

But arrays allow:

* direct middle access

Linked lists do not.

---

## Key Observation

For balanced BST:

* middle element must become root.

So problem becomes:

```text id="4tzw40"
How do we find middle efficiently?
```

Answer:

* slow-fast pointers.

---

## Interview Recognition Signal

Whenever you see:

```text id="x4thh1"
sorted linked list
+
balanced BST
```

Think:

> Find middle node recursively.

---

## Why Slow/Fast Pointer Works

```text id="g4omqr"
slow -> 1 step
fast -> 2 steps
```

When fast ends:

* slow reaches midpoint.

Classic linked list middle finding technique.

---

# 5. Simpler Version

# Simpler Question

## 108. Convert Sorted Array to BST

There:

* midpoint access is easy.

Here:

* midpoint access itself is the challenge.

---

# Thinking Evolution

## Step 1 — Sorted Array Version

```text id="j81dui"
mid element = root
```

Easy because indexing exists.

---

## Step 2 — Replace Array with Linked List

Now:

* no indexing
* must traverse to middle.

---

## Step 3 — Use Slow/Fast Pointer

Efficient midpoint discovery.

---

## Step 4 — Split List

Middle:

* becomes root
* left half -> left subtree
* right half -> right subtree

---

# Related Simpler Problems

### 1. Middle of the Linked List

Exact slow-fast midpoint logic.

### 2. Convert Sorted Array to BST

Same recursion structure.

### 3. Maximum Depth of Binary Tree

Basic recursive tree building.

### 4. Linked List Cycle

Introduces slow-fast pointers.

### 5. Balanced Binary Tree

Understanding balanced height property.

---

# 6. Brute Force

## Naive Idea

### Step 1

Convert linked list into array.

### Step 2

Use sorted-array-to-BST solution.

---

## Complexity

### Time

```text id="g8bkvp"
O(N)
```

---

### Space

```text id="ij5k4m"
O(N)
```

Extra array storage.

---

# Brute Force Code

```python id="0qv62y"
class Solution:
    def sortedListToBST(self, head):

        arr = []

        while head:
            arr.append(head.val)
            head = head.next

        def build(left, right):

            if left > right:
                return None

            mid = (left + right) // 2

            root = TreeNode(arr[mid])

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(arr) - 1)
```

---

# 7. Optimal Solution

## Core Idea

Use:

* slow-fast pointer to find middle
* recursively build left and right BSTs

No extra array needed.

---

# Python Code

```python id="7w0vqn"
class Solution:
    def sortedListToBST(self, head):

        # Base case
        if not head:
            return None

        # Single node becomes leaf
        if not head.next:
            return TreeNode(head.val)

        prev = None
        slow = head
        fast = head

        # Find middle node
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Disconnect left half
        prev.next = None

        # Middle becomes root
        root = TreeNode(slow.val)

        # Left subtree
        root.left = self.sortedListToBST(head)

        # Right subtree
        root.right = self.sortedListToBST(slow.next)

        return root
```

---

# Complexity

### Time

```text id="z6srmh"
O(N log N)
```

Why?

* Each recursive call scans for middle again.

---

### Space

```text id="vud1r9"
O(log N)
```

Recursive stack for balanced tree.

---

# 8. Step-by-Step Trace

Example:

```text id="c56wv6"
-10 -> -3 -> 0 -> 5 -> 9
```

---

# Step 1 — Find Middle

```text id="p3d3fd"
slow = 0
```

Root:

```text id="n9o4v1"
      0
```

Split into:

Left:

```text id="zj0v74"
-10 -> -3
```

Right:

```text id="r0t1tx"
5 -> 9
```

---

# Step 2 — Left Subtree

List:

```text id="mjz9nk"
-10 -> -3
```

Middle:

```text id="d1r7po"
-3
```

Tree:

```text id="1snuhk"
      0
     /
   -3
  /
-10
```

---

# Step 3 — Right Subtree

List:

```text id="7hrpyw"
5 -> 9
```

Middle:

```text id="j9gjgv"
9
```

Tree:

```text id="frphrz"
      0
     / \
   -3   9
  /    /
-10   5
```

Balanced BST complete.

---

# 9. Related Problems

### 1. Convert Sorted Array to BST

Directly related easier version.

### 2. Middle of the Linked List

Core slow-fast pointer technique.

### 3. Balance a Binary Search Tree

Rebuilding BST into balanced structure.

### 4. Validate Binary Search Tree

BST property verification.

### 5. Construct Binary Tree from Traversals

Recursive tree construction using segments/subproblems.
