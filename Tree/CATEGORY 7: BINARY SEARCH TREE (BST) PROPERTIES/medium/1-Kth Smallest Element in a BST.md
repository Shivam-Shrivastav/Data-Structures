# 230. Kth Smallest Element in a BST

## 1. Problem Statement with Example

Given the `root` of a Binary Search Tree (BST) and an integer `k`, return the `kth` smallest value in the BST.

---

# BST Property

```text id="zq3v8n"
Left subtree values  < root
Right subtree values > root
```

---

# Important Property

## Inorder Traversal of BST

```text id="3nn0zj"
Left -> Root -> Right
```

produces values in:

```text id="5yvhq6"
sorted ascending order
```

This is the key insight.

---

## Constraints

* `1 <= k <= number of nodes <= 10^4`

---

## Example

### Input

```text id="0h2p5x"
root = [3,1,4,null,2]
k = 1
```

---

## Tree

```text id="mjlwm8"
       3
      / \
     1   4
      \
       2
```

---

## Inorder Traversal

```text id="jlwm5q"
1 -> 2 -> 3 -> 4
```

1st smallest:

```text id="jlwm1b"
1
```

Output:

```text id="jlwm4x"
1
```

---

# 2. Diagram

# Core Insight

BST inorder traversal gives sorted order.

---

## Example

```text id="4jlwmm"
        5
       / \
      3   6
     / \
    2   4
   /
  1
```

---

## Inorder Traversal

```text id="0jlwmm"
1 -> 2 -> 3 -> 4 -> 5 -> 6
```

If:

```text id="jlwm9p"
k = 3
```

Answer:

```text id="jlwm5t"
3
```

---

# 3. Example I/O

## Example 1

### Input

```text id="0jlwmk"
root = [3,1,4,null,2]
k = 1
```

### Output

```text id="7jlwmv"
1
```

---

## Example 2

### Input

```text id="7jlwmf"
root = [5,3,6,2,4,null,null,1]
k = 3
```

### Output

```text id="0jlwm3"
3
```

---

## Edge Case

### Input

```text id="jlwm8s"
root = [1]
k = 1
```

### Output

```text id="jlwm4k"
1
```

---

# 4. Intuition & Pattern Recognition

This is a classic BST inorder problem.

---

# Key Observation

BST inorder traversal naturally produces:

```text id="0jlwmx"
sorted sequence
```

So:

* smallest = first node in inorder
* kth smallest = kth node visited in inorder

---

# Interview Recognition Signal

Whenever you see:

```text id="4jlwm9"
BST
+
kth smallest/largest
```

Immediately think:

> Inorder traversal.

---

# Why Inorder Works

BST guarantees:

```text id="0jlwmm9"
all left < root < all right
```

So inorder traversal visits:

* smaller elements first
* larger later

Exactly sorted order.

---

# 5. Simpler Version

# Simplest Question

## Binary Tree Inorder Traversal

There:

* just collect inorder sequence.

Here:

* stop at kth visited node.

---

# Thinking Evolution

## Step 1

Know inorder traversal order.

---

## Step 2

Realize BST inorder is sorted.

---

## Step 3

Count visited nodes.

---

## Step 4

Return kth node.

---

# Related Simpler Problems

### 1. Binary Tree Inorder Traversal

Foundation traversal.

### 2. Search in BST

Understanding BST ordering.

### 3. Validate BST

Uses inorder sorted property.

### 4. Kth Largest Element

Reverse inorder traversal.

### 5. BST Iterator

Inorder traversal simulation.

---

# 6. Brute Force

## Naive Idea

### Step 1

Perform inorder traversal.

### Step 2

Store all values in array.

### Step 3

Return:

```text id="jlwmz0"
arr[k-1]
```

---

# Brute Force Code

```python id="0jlwmr"
class Solution:
    def kthSmallest(self, root, k):

        arr = []

        def inorder(node):

            if not node:
                return

            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)

        inorder(root)

        return arr[k - 1]
```

---

# Complexity

### Time

```text id="0jlwmm5"
O(N)
```

---

### Space

```text id="2jlwmm"
O(N)
```

Extra inorder array.

---

# 7. Optimal Solution

# Core Idea

Do inorder traversal.
Stop once kth node is reached.

No extra array needed.

---

# Recursive Solution

```python id="0jlwmmv"
class Solution:
    def kthSmallest(self, root, k):

        self.k = k
        self.answer = None

        def inorder(node):

            if not node or self.answer is not None:
                return

            # Visit left subtree
            inorder(node.left)

            # Process current node
            self.k -= 1

            # kth smallest found
            if self.k == 0:
                self.answer = node.val
                return

            # Visit right subtree
            inorder(node.right)

        inorder(root)

        return self.answer
```

---

# Iterative Solution (Interview Preferred)

Uses explicit stack.

---

```python id="0jlwmm0"
class Solution:
    def kthSmallest(self, root, k):

        stack = []
        current = root

        while True:

            # Go to leftmost node
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()

            # Visit node
            k -= 1

            # kth smallest found
            if k == 0:
                return current.val

            # Explore right subtree
            current = current.right
```

---

# Complexity

### Time

```text id="0jlwmm2"
O(H + k)
```

Worst case:

```text id="0jlwmmf"
O(N)
```

---

### Space

```text id="0jlwmm7"
O(H)
```

Stack/recursion depth.

---

# 8. Step-by-Step Trace

Example:

```text id="0jlwmmc"
        5
       / \
      3   6
     / \
    2   4
   /
  1
```

Find:

```text id="0jlwmmk"
k = 3
```

---

# Inorder Traversal Order

---

## Visit 1

```text id="0jlwmmr"
k = 2
```

---

## Visit 2

```text id="0jlwmmz"
k = 1
```

---

## Visit 3

```text id="0jlwmm1"
k = 0
```

Found answer:

```text id="0jlwmm3"
3
```

Stop traversal.

---

# 9. Related Problems

### 1. Binary Tree Inorder Traversal

Core inorder DFS pattern.

### 2. BST Iterator

Iterative inorder traversal with stack.

### 3. Validate BST

Uses inorder sorted ordering.

### 4. Kth Largest Element in BST

Reverse inorder traversal.

### 5. Two Sum IV - Input is a BST

Uses BST inorder sorted property.
