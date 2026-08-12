# Populating Next Right Pointers in Each Node (Perfect Binary Tree)

LeetCode: Populating Next Right Pointers in Each Node

---

# 1. Problem Statement with Example

You are given a **perfect binary tree** where:

* every parent has exactly 2 children
* all leaves are at the same level

Each node has an additional pointer:

```python id="pop1"
next
```

which should point to its immediate right neighbor on the same level.

If no neighbor exists:

```python id="pop2"
next = None
```

Return the root after connecting all `next` pointers.

---

# Example

Input:

```text id="pop3"
            1
          /   \
         2     3
        / \   / \
       4  5  6  7
```

Output connections:

```text id="pop4"
1  -> NULL

2  -> 3 -> NULL

4  -> 5 -> 6 -> 7 -> NULL
```

---

# Constraints

* Number of nodes: `0 <= n <= 2^12 - 1`
* Tree is perfect

---

# 2. Diagram

# Original Tree

```text id="pop5"
            1
          /   \
         2     3
        / \   / \
       4  5  6  7
```

---

# After Connecting

```text id="pop6"
            1 → NULL
          /   \
         2  →  3 → NULL
        / \   / \
       4→ 5→ 6→ 7 → NULL
```

---

# Important Cross Connection

Inside same parent:

```text id="pop7"
2.left.next = 2.right
```

Cross-parent connection:

```text id="pop8"
5.next = 6
```

This is THE key interview insight.

---

# 3. Example I/O

## Example 1 (Typical)

Input:

```text id="pop9"
root = [1,2,3,4,5,6,7]
```

Output:

```text id="pop10"
[1,#,2,3,#,4,5,6,7,#]
```

(`#` denotes end of level)

---

## Example 2 (Empty Tree)

Input:

```text id="pop11"
root = []
```

Output:

```text id="pop12"
[]
```

---

# 4. Intuition & Pattern Recognition

This is a **tree pointer connection** problem.

Because tree is:

```text id="pop13"
Perfect binary tree
```

we get very powerful guarantees.

---

# Core Observation

For every node:

```text id="pop14"
left child should connect to right child
```

Easy:

```python id="pop15"
node.left.next = node.right
```

---

# Harder Part

How do we connect:

```text id="pop16"
node.right → neighboring subtree
```

Example:

```text id="pop17"
5 → 6
```

---

# Critical Insight

If:

```text id="pop18"
node.next exists
```

then:

```python id="pop19"
node.right.next = node.next.left
```

This is the entire problem.

---

# Interview Recognition

Whenever problem says:

* connect sibling pointers
* next neighbor
* level linking

Think:

* BFS level traversal
  OR
* exploit tree structure

---

# Why Perfect Tree Matters

Without perfect tree:

* neighbors may not exist predictably.

Here:

* every internal node has both children.

This allows elegant `O(1)` solution.

---

# 5. Simpler Version

---

# Simplest Version

```text id="pop20"
    1
   / \
  2   3
```

Connection:

```text id="pop21"
2 → 3
```

Easy:

```python id="pop22"
root.left.next = root.right
```

---

# Slightly Harder

```text id="pop23"
        1
      /   \
     2     3
    / \   / \
   4  5  6  7
```

Need:

```text id="pop24"
5 → 6
```

Cross-parent connection.

---

# Related Simpler Problems

### 1. Binary Tree Level Order Traversal

LeetCode: Binary Tree Level Order Traversal

Basic BFS level processing.

---

### 2. Populating Next Right Pointers in Each Node II

LeetCode: Populating Next Right Pointers in Each Node II

Harder because tree is NOT perfect.

---

### 3. Binary Tree Right Side View

LeetCode: Binary Tree Right Side View

Another level-based tree problem.

---

# Thinking Progression

```text id="pop25"
Connect siblings under same parent
        ↓
Connect across parents
        ↓
Use next pointers recursively
```

---

# 6. Brute Force

# BFS Level Traversal

Use queue:

1. Traverse level-by-level
2. Connect consecutive nodes

---

# BFS Code

```python id="pop26"
from collections import deque

class Solution:

    def connect(self, root):

        if not root:
            return root

        queue = deque([root])

        while queue:

            size = len(queue)

            prev = None

            for _ in range(size):

                node = queue.popleft()

                if prev:
                    prev.next = node

                prev = node

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return root
```

---

# Complexity

## Time

```text id="pop27"
O(n)
```

---

## Space

```text id="pop28"
O(n)
```

Queue storage.

---

# 7. Optimal Solution

# Recursive O(1) Space Solution

---

# Core Connections

For every node:

## Same parent

```python id="pop29"
node.left.next = node.right
```

---

## Cross parent

```python id="pop30"
if node.next:
    node.right.next = node.next.left
```

---

# Optimal Code

```python id="pop31"
class Solution:

    def connect(self, root):

        if not root:
            return root

        # Connect children of current node
        if root.left:
            root.left.next = root.right

        # Connect across subtrees
        if root.right and root.next:
            root.right.next = root.next.left

        # Recurse
        self.connect(root.left)
        self.connect(root.right)

        return root
```

---

# Why This Works

Suppose:

```text id="pop32"
        1
      /   \
     2     3
    / \   / \
   4  5  6  7
```

At node `2`:

```python id="pop33"
2.left.next = 2.right
```

means:

```text id="pop34"
4 → 5
```

---

Then:

```python id="pop35"
2.right.next = 2.next.left
```

Since:

```text id="pop36"
2.next = 3
```

we get:

```text id="pop37"
5 → 6
```

---

# Important Interview Insight

The recursion works because:

```text id="pop38"
parent next pointers already exist
```

when processing children.

---

# Alternative Iterative O(1) Solution

Very interview-popular.

---

# Idea

Use already-created next pointers to traverse levels.

```python id="pop39"
class Solution:

    def connect(self, root):

        if not root:
            return root

        leftmost = root

        while leftmost.left:

            current = leftmost

            while current:

                # Same parent
                current.left.next = current.right

                # Cross parent
                if current.next:
                    current.right.next = current.next.left

                current = current.next

            leftmost = leftmost.left

        return root
```

---

# Why Iterative Works

Once one level is connected:

```text id="pop40"
We can traverse entire level using next pointers.
```

No queue needed.

---

# Complexity

## Time

```text id="pop41"
O(n)
```

Each node processed once.

---

## Space

### Recursive

```text id="pop42"
O(h)
```

### Iterative

```text id="pop43"
O(1)
```

This is the optimal interview answer.

---

# 8. Step-by-Step Trace

Input:

```text id="pop44"
            1
          /   \
         2     3
        / \   / \
       4  5  6  7
```

---

# Step 1 — Node 1

Connect:

```text id="pop45"
2 → 3
```

---

# Step 2 — Node 2

Connect:

```text id="pop46"
4 → 5
```

Cross connection:

```text id="pop47"
5 → 6
```

(using `2.next = 3`)

---

# Step 3 — Node 3

Connect:

```text id="pop48"
6 → 7
```

---

# Final Connections

```text id="pop49"
1 → NULL

2 → 3 → NULL

4 → 5 → 6 → 7 → NULL
```

---

# 9. Related Problems

### 1. Populating Next Right Pointers in Each Node II

Harder version with non-perfect trees.

---

### 2. Binary Tree Level Order Traversal

Classic BFS-by-level traversal.

---

### 3. Binary Tree Right Side View

Another level-based tree problem.

---

### 4. Invert Binary Tree

Tree pointer manipulation.

---

### 5. Flatten Binary Tree to Linked List

Advanced tree pointer rewiring problem.
