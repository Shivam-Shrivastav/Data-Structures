 # Binary Tree Level Order Traversal

## 1. Problem Statement with Example

Given the `root` of a binary tree, return the **level order traversal** of its nodes' values.

Level order traversal means:

```text id="jlwm1k"
Traverse level by level from top to bottom,
left to right.
```

LeetCode: Binary Tree Level Order Traversal

---

# Example

Input:

```text id="jlwm2k"
        3
       / \
      9   20
         /  \
        15   7
```

Output:

```python id="jlwm3k"
[[3],[9,20],[15,7]]
```

Explanation:

```text id="jlwm4k"
Level 0 → [3]
Level 1 → [9,20]
Level 2 → [15,7]
```

---

# Constraints

* Number of nodes: `0 <= n <= 2000`
* `-1000 <= Node.val <= 1000`

---

# 2. Diagram

# Tree

```text id="jlwm5k"
            3
          /   \
         9     20
              /  \
             15   7
```

---

# BFS Traversal Flow

```text id="jlwm6k"
Level 0:
3

Level 1:
9 → 20

Level 2:
15 → 7
```

---

# Queue Visualization

```text id="jlwm7k"
Start:
[3]

After processing 3:
[9,20]

After processing 9:
[20]

After processing 20:
[15,7]
```

---

# Core Pattern

```text id="jlwm8k"
Use queue for level-by-level traversal
```

This is the biggest interview clue.

---

# 3. Example I/O

## Example 1 (Typical)

Input:

```text id="jlwm9k"
root = [3,9,20,null,null,15,7]
```

Output:

```python id="jlwm0l"
[[3],[9,20],[15,7]]
```

---

## Example 2 (Single Node)

Input:

```text id="jlwm1l"
root = [1]
```

Output:

```python id="jlwm2l"
[[1]]
```

---

## Example 3 (Empty Tree)

Input:

```text id="jlwm3l"
root = []
```

Output:

```python id="jlwm4l"
[]
```

---

# 4. Intuition & Pattern Recognition

This is the most classic **BFS (Breadth First Search)** tree problem.

---

# Key Observation

We need:

```text id="jlwm5l"
Level-by-level traversal
```

DFS goes deep first, so not natural.

BFS is perfect because:

```text id="jlwm6l"
Queue processes nodes in level order.
```

---

# Core BFS Pattern

```text id="jlwm7l"
1. Put root into queue
2. Process all nodes currently in queue
3. Add their children
4. Repeat
```

---

# Important Interview Signal

Whenever problem says:

* level order
* nearest level
* minimum steps
* shortest path
* layer by layer

Think:

```text id="jlwm8l"
BFS + Queue
```

---

# Key Insight

At any moment:

```text id="jlwm9l"
Queue contains exactly one level.
```

This is why we use:

```python id="jlwm0m"
level_size = len(queue)
```

---

# 5. Simpler Version

---

# Simplest Version

```text id="jlwm1m"
    1
```

Output:

```python id="jlwm2m"
[[1]]
```

Only one level.

---

# Slightly Harder

```text id="jlwm3m"
      1
     / \
    2   3
```

Output:

```python id="jlwm4m"
[[1],[2,3]]
```

Process:

* root first
* then children

---

# Related Simpler Problems

### 1. Binary Tree Preorder Traversal

LeetCode: Binary Tree Preorder Traversal

DFS traversal.

Difference:

* goes depth-first instead of level-by-level.

---

### 2. Maximum Depth of Binary Tree

LeetCode: Maximum Depth of Binary Tree

Can also be solved using BFS levels.

---

### 3. Binary Tree Zigzag Level Order Traversal

LeetCode: Binary Tree Zigzag Level Order Traversal

Same BFS pattern with alternating direction.

---

# Thinking Progression

```text id="jlwm5m"
Need level-wise traversal
        ↓
Use BFS
        ↓
Queue stores current frontier
        ↓
Process one level at a time
```

---

# 6. Brute Force

## DFS-Based Brute Force

We can:

1. Compute tree height
2. Print nodes level by level recursively

---

# Brute Force Code

```python id="jlwm6m"
class Solution:

    def levelOrder(self, root):

        result = []

        def height(node):

            if not node:
                return 0

            return 1 + max(
                height(node.left),
                height(node.right)
            )

        def collect(node, level):

            if not node:
                return

            if level == 0:
                current.append(node.val)
                return

            collect(node.left, level - 1)
            collect(node.right, level - 1)

        h = height(root)

        for lvl in range(h):

            current = []

            collect(root, lvl)

            result.append(current)

        return result
```

---

# Complexity

## Time

Worst case:

```text id="jlwm7m"
O(n^2)
```

Repeated traversals for each level.

---

## Space

```text id="jlwm8m"
O(h)
```

Recursion stack.

---

# 7. Optimal Solution

# BFS Using Queue

```python id="’wini9m"
from collections import deque

class Solution:

    def levelOrder(self, root):

        if not root:
            return []

        result = []

        queue = deque([root])

        while queue:

            level_size = len(queue)

            current_level = []

            # Process exactly one level
            for _ in range(level_size):

                node = queue.popleft()

                current_level.append(node.val)

                # Add children for next level
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(current_level)

        return result
```

---

# Why This Works

At loop start:

```text id="’wini0n"
queue contains all nodes of current level
```

We process exactly:

```python id="’wini1n"
level_size
```

nodes.

Children added become:

```text id="’wini2n"
next level
```

---

# Important Interview Insight

This line:

```python id="’wini3n"
level_size = len(queue)
```

freezes current level size.

Without it:

* levels get mixed together.

---

# Complexity

## Time

```text id="’wini4n"
O(n)
```

Each node processed once.

---

## Space

```text id="’wini5n"
O(n)
```

Queue may store entire level.

Worst case:

* complete tree last level ≈ `n/2`

---

# 8. Step-by-Step Trace

Input:

```text id="’wini6n"
            3
          /   \
         9     20
              /  \
             15   7
```

---

# Step 1

Queue:

```text id="’wini7n"
[3]
```

Process level:

```python id="’wini8n"
[3]
```

Add children:

```text id="’wini9n"
[9,20]
```

---

# Step 2

Process:

```python id="m0o0o0"
[9,20]
```

Add children of 20:

```text id="m1o1o1"
[15,7]
```

---

# Step 3

Process:

```python id="m2o2o2"
[15,7]
```

No more children.

---

# Final Result

```python id="m3o3o3"
[[3],[9,20],[15,7]]
```

---

# 9. Related Problems

### 1. Binary Tree Zigzag Level Order Traversal

Same BFS traversal with alternating directions.

---

### 2. Binary Tree Right Side View

BFS level traversal while tracking rightmost node.

---

### 3. Average of Levels in Binary Tree

Same level-order traversal pattern.

---

### 4. Maximum Depth of Binary Tree

Can be solved using BFS levels.

---

### 5. N-ary Tree Level Order Traversal

Generalization of BFS traversal to N-ary trees.
