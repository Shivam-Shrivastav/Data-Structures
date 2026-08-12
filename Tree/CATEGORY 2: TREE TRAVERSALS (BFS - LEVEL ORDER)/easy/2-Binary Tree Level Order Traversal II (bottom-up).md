# Binary Tree Level Order Traversal II (Bottom-Up)

LeetCode: Binary Tree Level Order Traversal II

---

# 1. Problem Statement with Example

Given the `root` of a binary tree, return the **bottom-up level order traversal** of its nodes' values.

This means:

```text id="bt1"
Traverse level by level,
but return levels from bottom to top.
```

---

# Example

Input:

```text id="bt2"
            3
          /   \
         9     20
              /  \
             15   7
```

Normal level order:

```python id="bt3"
[[3],[9,20],[15,7]]
```

Bottom-up level order:

```python id="bt4"
[[15,7],[9,20],[3]]
```

---

# Constraints

* `0 <= number of nodes <= 2000`
* `-1000 <= Node.val <= 1000`

---

# 2. Diagram

# Tree

```text id="bt5"
            3
          /   \
         9     20
              /  \
             15   7
```

---

# BFS Traversal

```text id="bt6"
Top-down traversal:
Level 0 → [3]
Level 1 → [9,20]
Level 2 → [15,7]
```

---

# Final Reversal

```text id="bt7"
Before reverse:
[[3],[9,20],[15,7]]

After reverse:
[[15,7],[9,20],[3]]
```

---

# Key Observation

This is:

```text id="bt8"
Normal BFS level order
+ reverse at end
```

That’s the main interview insight.

---

# 3. Example I/O

## Example 1 (Typical)

Input:

```text id="bt9"
root = [3,9,20,null,null,15,7]
```

Output:

```python id="bt10"
[[15,7],[9,20],[3]]
```

---

## Example 2 (Single Node)

Input:

```text id="bt11"
root = [1]
```

Output:

```python id="bt12"
[[1]]
```

---

## Example 3 (Empty Tree)

Input:

```text id="bt13"
root = []
```

Output:

```python id="bt14"
[]
```

---

# 4. Intuition & Pattern Recognition

This is a direct extension of:

Binary Tree Level Order Traversal

---

# Core Insight

We still need:

```text id="bt15"
Level-by-level traversal
```

So:

```text id="bt16"
BFS + Queue
```

remains the best approach.

---

# Only Difference

Instead of:

```python id="bt17"
[[top],[middle],[bottom]]
```

we want:

```python id="bt18"
[[bottom],[middle],[top]]
```

So after BFS:

```python id="bt19"
reverse result
```

---

# Interview Recognition

Whenever you see:

* bottom-up levels
* reverse level order
* reverse BFS output

Think:

```text id="bt20"
Normal BFS first
Then reverse
```

---

# Key BFS Pattern

At every iteration:

```text id="bt21"
Queue contains exactly one level
```

Process that level fully before moving to next.

---

# 5. Simpler Version

---

# Simplest Version

```text id="bt22"
    1
```

Output:

```python id="bt23"
[[1]]
```

Reverse doesn’t matter.

---

# Slightly Harder

```text id="bt24"
      1
     / \
    2   3
```

Normal BFS:

```python id="bt25"
[[1],[2,3]]
```

Bottom-up:

```python id="bt26"
[[2,3],[1]]
```

---

# Related Simpler Problems

### 1. Binary Tree Level Order Traversal

LeetCode: Binary Tree Level Order Traversal

Exact same BFS logic.

---

### 2. Binary Tree Zigzag Level Order Traversal

LeetCode: Binary Tree Zigzag Level Order Traversal

Another level-order BFS variation.

---

### 3. Maximum Depth of Binary Tree

LeetCode: Maximum Depth of Binary Tree

Can also be solved using BFS levels.

---

# Thinking Progression

```text id="bt27"
Need level-order traversal
        ↓
Use BFS queue
        ↓
Collect levels normally
        ↓
Reverse answer
```

---

# 6. Brute Force

## DFS-Based Brute Force

We can:

1. Compute height
2. Collect each level recursively
3. Append levels bottom-up

---

# Brute Force Complexity

## Time

```text id="bt28"
O(n^2)
```

Repeated traversals.

---

## Space

```text id="bt29"
O(h)
```

Recursion stack.

---

# 7. Optimal Solution

# BFS + Reverse

```python id="bt30"
from collections import deque

class Solution:

    def levelOrderBottom(self, root):

        if not root:
            return []

        result = []

        queue = deque([root])

        while queue:

            level_size = len(queue)

            current_level = []

            # Process one level
            for _ in range(level_size):

                node = queue.popleft()

                current_level.append(node.val)

                # Add children
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(current_level)

        # Reverse levels
        return result[::-1]
```

---

# Why This Works

BFS naturally gives:

```text id="bt31"
Top → Bottom
```

But problem wants:

```text id="bt32"
Bottom → Top
```

So reversing final result solves it cleanly.

---

# Important Interview Insight

This problem is NOT fundamentally different from normal level order traversal.

Only output formatting changes.

---

# Alternative Optimization

Instead of reversing later:

```python id="bt33"
result.insert(0, current_level)
```

But this is slower because:

```text id="bt34"
insert(0, x) = O(n)
```

So reversing at end is cleaner and faster.

---

# Complexity

## Time

```text id="bt35"
O(n)
```

Each node processed once.

---

## Space

```text id="bt36"
O(n)
```

Queue + output storage.

---

# 8. Step-by-Step Trace

Input:

```text id="bt37"
            3
          /   \
         9     20
              /  \
             15   7
```

---

# Step 1

Queue:

```text id="bt38"
[3]
```

Process:

```python id="bt39"
[3]
```

Add children:

```text id="bt40"
[9,20]
```

Result:

```python id="bt41"
[[3]]
```

---

# Step 2

Process:

```python id="bt42"
[9,20]
```

Add children:

```text id="bt43"
[15,7]
```

Result:

```python id="bt44"
[[3],[9,20]]
```

---

# Step 3

Process:

```python id="bt45"
[15,7]
```

Result:

```python id="bt46"
[[3],[9,20],[15,7]]
```

---

# Step 4 — Reverse

```python id="bt47"
[[15,7],[9,20],[3]]
```

---

# 9. Related Problems

### 1. Binary Tree Level Order Traversal

Core BFS level traversal.

---

### 2. Binary Tree Zigzag Level Order Traversal

BFS with alternating directions.

---

### 3. Average of Levels in Binary Tree

Uses same BFS-by-level pattern.

---

### 4. Binary Tree Right Side View

Uses BFS levels while tracking last node.

---

### 5. N-ary Tree Level Order Traversal

General BFS traversal on N-ary trees.
