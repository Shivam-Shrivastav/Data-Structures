# Average of Levels in Binary Tree

LeetCode: Average of Levels in Binary Tree

---

# 1. Problem Statement with Example

Given the `root` of a binary tree, return the **average value of the nodes on each level**.

Answers within `10^-5` of the actual answer are accepted.

---

# Example

Input:

```text id="avg1"
            3
          /   \
         9     20
              /  \
             15   7
```

Output:

```python id="avg2"
[3.00000,14.50000,11.00000]
```

Explanation:

```text id="avg3"
Level 0:
[3]
Average = 3

Level 1:
[9,20]
Average = (9 + 20) / 2 = 14.5

Level 2:
[15,7]
Average = (15 + 7) / 2 = 11
```

---

# Constraints

* Number of nodes: `1 <= n <= 10^4`
* `-2^31 <= Node.val <= 2^31 - 1`

---

# 2. Diagram

# Tree

```text id="avg4"
            3
          /   \
         9     20
              /  \
             15   7
```

---

# Level-by-Level Processing

```text id="avg5"
Level 0:
[3]

Level 1:
[9,20]

Level 2:
[15,7]
```

---

# Average Calculation

```text id="avg6"
Level 0:
3 / 1 = 3

Level 1:
(9 + 20) / 2 = 14.5

Level 2:
(15 + 7) / 2 = 11
```

---

# Core Pattern

```text id="avg7"
Process tree level-by-level using BFS
```

This is the major interview clue.

---

# 3. Example I/O

## Example 1 (Typical)

Input:

```text id="avg8"
root = [3,9,20,null,null,15,7]
```

Output:

```python id="avg9"
[3.00000,14.50000,11.00000]
```

---

## Example 2 (Single Node)

Input:

```text id="avg10"
root = [5]
```

Output:

```python id="avg11"
[5.00000]
```

---

# 4. Intuition & Pattern Recognition

This is a direct BFS level-order traversal problem.

Very similar to:

Binary Tree Level Order Traversal

---

# Key Observation

We need:

```text id="avg12"
Information grouped by levels
```

That immediately suggests:

```text id="avg13"
BFS + Queue
```

---

# Main Idea

For every level:

1. Process all nodes in queue
2. Compute sum
3. Divide by number of nodes

---

# Important Interview Recognition

Whenever problem says:

* level averages
* level sums
* per-level computation
* layer-wise processing

Think:

```text id="avg14"
BFS level traversal
```

---

# Core BFS Insight

At loop start:

```text id="avg15"
Queue contains exactly one level
```

So:

```python id="avg16"
level_size = len(queue)
```

lets us isolate that level.

---

# 5. Simpler Version

---

# Simplest Version

```text id="avg17"
    5
```

Output:

```python id="avg18"
[5]
```

Only one level.

---

# Slightly Harder

```text id="avg19"
      1
     / \
    2   3
```

Level averages:

```text id="avg20"
Level 0:
1

Level 1:
(2 + 3) / 2 = 2.5
```

Output:

```python id="avg21"
[1,2.5]
```

---

# Related Simpler Problems

### 1. Binary Tree Level Order Traversal

LeetCode: Binary Tree Level Order Traversal

Exact same BFS traversal structure.

---

### 2. Binary Tree Level Order Traversal II

LeetCode: Binary Tree Level Order Traversal II

Another BFS level variation.

---

### 3. Maximum Depth of Binary Tree

LeetCode: Maximum Depth of Binary Tree

Can also be solved level-by-level.

---

# Thinking Progression

```text id="avg22"
Need level-wise information
        ↓
Use BFS queue
        ↓
Process one level at a time
        ↓
Compute sum/count
```

---

# 6. Brute Force

## DFS-Based Brute Force

We could:

1. Compute tree height
2. Collect each level separately
3. Compute averages

This causes repeated traversals.

---

# Brute Force Complexity

## Time

```text id="avg23"
O(n^2)
```

Worst case.

---

## Space

```text id="avg24"
O(h)
```

Recursion stack.

---

# 7. Optimal Solution

# BFS Level Traversal

```python id="avg25"
from collections import deque

class Solution:

    def averageOfLevels(self, root):

        if not root:
            return []

        result = []

        queue = deque([root])

        while queue:

            level_size = len(queue)

            level_sum = 0

            # Process current level
            for _ in range(level_size):

                node = queue.popleft()

                level_sum += node.val

                # Add children
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            # Compute average
            result.append(level_sum / level_size)

        return result
```

---

# Why This Works

At each BFS iteration:

```text id="avg26"
Queue = all nodes of current level
```

We:

* sum their values
* divide by count

Then move to next level.

---

# Important Interview Insight

This line:

```python id="avg27"
level_size = len(queue)
```

freezes current level boundary.

Without it:

* levels mix together.

---

# Complexity

## Time

```text id="avg28"
O(n)
```

Each node processed once.

---

## Space

```text id="avg29"
O(n)
```

Queue may contain entire level.

Worst case:

* last level ≈ `n/2`

---

# 8. Step-by-Step Trace

Input:

```text id="avg30"
            3
          /   \
         9     20
              /  \
             15   7
```

---

# Step 1

Queue:

```text id="avg31"
[3]
```

Process:

* sum = 3
* size = 1

Average:

```python id="avg32"
3 / 1 = 3
```

Result:

```python id="avg33"
[3]
```

---

# Step 2

Queue:

```text id="avg34"
[9,20]
```

Process:

* sum = 29
* size = 2

Average:

```python id="avg35"
29 / 2 = 14.5
```

Result:

```python id="avg36"
[3,14.5]
```

---

# Step 3

Queue:

```text id="avg37"
[15,7]
```

Process:

* sum = 22
* size = 2

Average:

```python id="avg38"
22 / 2 = 11
```

Final result:

```python id="avg39"
[3,14.5,11]
```

---

# 9. Related Problems

### 1. Binary Tree Level Order Traversal

Core BFS-by-level traversal.

---

### 2. Binary Tree Level Order Traversal II

Bottom-up BFS traversal.

---

### 3. Binary Tree Right Side View

Uses BFS levels while selecting one node per level.

---

### 4. Find Largest Value in Each Tree Row

Another level-based BFS aggregation problem.

---

### 5. N-ary Tree Level Order Traversal

Generalized BFS traversal pattern.
