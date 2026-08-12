# Binary Tree Zigzag Level Order Traversal

LeetCode: Binary Tree Zigzag Level Order Traversal

---

# 1. Problem Statement with Example

Given the `root` of a binary tree, return the **zigzag level order traversal** of its nodes' values.

This means:

* Level 0 → left to right
* Level 1 → right to left
* Level 2 → left to right
* and so on...

---

# Example

Input:

```text id="zig1"
            3
          /   \
         9     20
              /  \
             15   7
```

Normal level order:

```python id="zig2"
[[3],[9,20],[15,7]]
```

Zigzag level order:

```python id="zig3"
[[3],[20,9],[15,7]]
```

---

# Constraints

* `0 <= number of nodes <= 2000`
* `-100 <= Node.val <= 100`

---

# 2. Diagram

# Tree

```text id="zig4"
            3
          /   \
         9     20
              /  \
             15   7
```

---

# Zigzag Traversal

```text id="zig5"
Level 0:
Left → Right
[3]

Level 1:
Right → Left
[20,9]

Level 2:
Left → Right
[15,7]
```

---

# Visual Direction Change

```text id="zig6"
→ Level 0
← Level 1
→ Level 2
← Level 3
```

---

# Core Pattern

```text id="zig7"
Normal BFS level traversal
+ alternate direction per level
```

That is the main interview insight.

---

# 3. Example I/O

## Example 1 (Typical)

Input:

```text id="zig8"
root = [3,9,20,null,null,15,7]
```

Output:

```python id="zig9"
[[3],[20,9],[15,7]]
```

---

## Example 2 (Single Node)

Input:

```text id="zig10"
root = [1]
```

Output:

```python id="zig11"
[[1]]
```

---

## Example 3 (Empty Tree)

Input:

```text id="zig12"
root = []
```

Output:

```python id="zig13"
[]
```

---

# 4. Intuition & Pattern Recognition

This is an extension of:

Binary Tree Level Order Traversal

---

# Key Observation

We still need:

```text id="zig14"
Level-by-level traversal
```

So:

```text id="zig15"
BFS + Queue
```

remains the best approach.

---

# Only New Requirement

Alternate traversal direction every level.

---

# Important Insight

We DO NOT need:

* reverse actual tree
* change queue ordering

We only change:

```text id="zig16"
How current level is stored
```

---

# Interview Recognition

Whenever problem says:

* zigzag
* spiral traversal
* alternating direction

Think:

```text id="zig17"
BFS levels + parity check
```

(level index even/odd)

---

# Key Trick

After collecting current level:

```python id="zig18"
if reverse_needed:
    current.reverse()
```

---

# 5. Simpler Version

---

# Simplest Version

```text id="zig19"
    1
```

Output:

```python id="zig20"
[[1]]
```

Only one level.

---

# Slightly Harder

```text id="zig21"
      1
     / \
    2   3
```

Normal BFS:

```python id="zig22"
[[1],[2,3]]
```

Zigzag:

```python id="zig23"
[[1],[3,2]]
```

---

# Related Simpler Problems

### 1. Binary Tree Level Order Traversal

LeetCode: Binary Tree Level Order Traversal

Base BFS level traversal.

---

### 2. Binary Tree Level Order Traversal II

LeetCode: Binary Tree Level Order Traversal II

Another output-format variation.

---

### 3. Average of Levels in Binary Tree

LeetCode: Average of Levels in Binary Tree

Same BFS level processing.

---

# Thinking Progression

```text id="zig24"
Need level traversal
        ↓
Use BFS
        ↓
Track level direction
        ↓
Reverse alternate levels
```

---

# 6. Brute Force

## Idea

1. Do normal BFS
2. Reverse odd-indexed levels afterward

---

# Brute Force Complexity

## Time

```text id="zig25"
O(n)
```

---

## Space

```text id="zig26"
O(n)
```

Actually already optimal enough.

---

# 7. Optimal Solution

# BFS + Direction Flag

```python id="zig27"
from collections import deque

class Solution:

    def zigzagLevelOrder(self, root):

        if not root:
            return []

        result = []

        queue = deque([root])

        left_to_right = True

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

            # Reverse alternate levels
            if not left_to_right:
                current_level.reverse()

            result.append(current_level)

            # Flip direction
            left_to_right = not left_to_right

        return result
```

---

# Why This Works

BFS naturally gives:

```text id="zig28"
Left → Right
```

for every level.

For zigzag:

* even levels stay same
* odd levels reversed

So we simply reverse alternate levels.

---

# Important Interview Insight

We are NOT changing traversal order.

Only output representation changes.

Queue behavior remains normal BFS.

---

# Alternative Optimization

Instead of reversing:

Use deque:

```python id="zig29"
appendleft()
```

for reverse levels.

But interview-wise:

* reversing is cleaner
* easier to explain

---

# Complexity

## Time

```text id="zig30"
O(n)
```

Each node processed once.

---

## Space

```text id="zig31"
O(n)
```

Queue + output storage.

---

# 8. Step-by-Step Trace

Input:

```text id="zig32"
            3
          /   \
         9     20
              /  \
             15   7
```

---

# Step 1

Queue:

```text id="zig33"
[3]
```

Direction:

```text id="zig34"
Left → Right
```

Level:

```python id="zig35"
[3]
```

Result:

```python id="zig36"
[[3]]
```

---

# Step 2

Queue:

```text id="zig37"
[9,20]
```

Direction:

```text id="zig38"
Right → Left
```

Collected:

```python id="zig39"
[9,20]
```

Reverse:

```python id="zig40"
[20,9]
```

Result:

```python id="zig41"
[[3],[20,9]]
```

---

# Step 3

Queue:

```text id="zig42"
[15,7]
```

Direction:

```text id="zig43"
Left → Right
```

Level:

```python id="zig44"
[15,7]
```

Final:

```python id="zig45"
[[3],[20,9],[15,7]]
```

---

# 9. Related Problems

### 1. Binary Tree Level Order Traversal

Core BFS-by-level traversal.

---

### 2. Binary Tree Level Order Traversal II

Bottom-up BFS traversal.

---

### 3. Average of Levels in Binary Tree

Per-level aggregation using BFS.

---

### 4. Binary Tree Right Side View

Uses BFS levels to select visible nodes.

---

### 5. N-ary Tree Level Order Traversal

Generalized BFS traversal pattern.
