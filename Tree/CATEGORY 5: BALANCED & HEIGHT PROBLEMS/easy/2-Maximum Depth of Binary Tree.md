# 104. Maximum Depth of Binary Tree

## 1. Problem Statement with Example

Given the `root` of a binary tree, return its **maximum depth**.

The maximum depth is:

> The number of nodes along the longest path from the root node down to the farthest leaf node.

A leaf node is a node with no children.

---

## Constraints

* Number of nodes: `0 <= n <= 10^4`
* `-100 <= Node.val <= 100`
* Need efficient traversal of all nodes.

---

## Example

```text id="h15b1v"
Input:
        3
       / \
      9  20
         / \
        15  7

Output: 3
```

Longest path:

```text id="1m8xdr"
3 -> 20 -> 15
```

Depth = `3`

---

# 2. Diagram

```text id="klq90g"
                3
              /   \
             9     20
                  /  \
                15    7
```

Depth calculation:

```text id="e1vpsf"
depth(9)  = 1
depth(15) = 1
depth(7)  = 1

depth(20) = 1 + max(1,1) = 2

depth(3)  = 1 + max(1,2) = 3
```

---

# 3. Example I/O

## Example 1

### Input

```text id="df70s7"
root = [3,9,20,null,null,15,7]
```

### Output

```text id="odtnhh"
3
```

### Explanation

Longest root-to-leaf path contains 3 nodes.

---

## Example 2

### Input

```text id="d2rqq8"
root = [1,null,2]
```

### Output

```text id="xj8otx"
2
```

### Explanation

Only path:

```text id="odqf7n"
1 -> 2
```

---

## Edge Case

### Input

```text id="8ezx4z"
root = []
```

### Output

```text id="w8nltx"
0
```

Empty tree has depth `0`.

---

# 4. Intuition & Pattern Recognition

This is one of the most fundamental tree DFS problems.

---

## Pattern

### Tree DFS + Recursion

Key observation:

The depth of a node depends on:

* depth of left subtree
* depth of right subtree

So naturally:

```text id="kmmuwm"
depth(node) = 1 + max(leftDepth, rightDepth)
```

---

## Interview Recognition Signal

Whenever you hear:

```text id="g76jgc"
"longest path"
"height"
"depth"
"levels"
```

Think:

> Recursive DFS returning information upward.

---

## Why Recursion Fits Perfectly

Trees are recursive structures.

Each subtree is itself a smaller binary tree.

So solve:

* left subtree
* right subtree
* combine results

---

# 5. Simpler Version

## Simplest Form

### Depth of Single Node

If node has no children:

```text id="yk5vw1"
depth = 1
```

---

## Then Extend

If node has children:

```text id="03wl18"
Take deeper subtree
+
add current node
```

---

## Thinking Evolution

### Step 1

Understand leaf node:

```text id="wcf38e"
Leaf depth = 1
```

---

### Step 2

Parent depends on children:

```text id="8xrfpm"
1 + max(left, right)
```

---

### Step 3

Apply recursively to entire tree.

---

## Related Simpler Problems

### 1. Same Tree

Basic recursion traversal.

### 2. Invert Binary Tree

Recursive subtree processing.

### 3. Minimum Depth of Binary Tree

Similar recursion with different condition.

### 4. Balanced Binary Tree

Uses subtree heights too.

### 5. Diameter of Binary Tree

Builds directly on depth calculation.

---

# 6. Brute Force

There isn't really a separate brute-force version here because DFS itself is already optimal.

But you can think of:

* traversing every root-to-leaf path
* manually tracking lengths

Still essentially O(N).

---

## Naive DFS

```python id="w0f5r1"
class Solution:
    def maxDepth(self, root):

        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)
```

---

## Complexity

### Time

```text id="l3dzt5"
O(N)
```

Every node visited once.

---

### Space

```text id="h0nk89"
O(H)
```

Recursion stack.

Worst case skewed tree:

```text id="j7f5e6"
O(N)
```

Balanced tree:

```text id="rmwnkg"
O(log N)
```

---

# 7. Optimal Solution

The recursive DFS above is already optimal.

---

## Interview-Friendly Python Solution

```python id="qz9g22"
class Solution:
    def maxDepth(self, root):

        # Empty tree
        if not root:
            return 0

        # Depth of left subtree
        left_depth = self.maxDepth(root.left)

        # Depth of right subtree
        right_depth = self.maxDepth(root.right)

        # Current depth
        return 1 + max(left_depth, right_depth)
```

---

## Iterative BFS Solution (Alternative)

Level-order traversal.

```python id="d7x2f8"
from collections import deque

class Solution:
    def maxDepth(self, root):

        if not root:
            return 0

        q = deque([root])
        depth = 0

        while q:

            # One full level
            for _ in range(len(q)):

                node = q.popleft()

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            depth += 1

        return depth
```

---

## Complexity

### DFS

Time:

```text id="r0egpq"
O(N)
```

Space:

```text id="rffw3l"
O(H)
```

---

### BFS

Time:

```text id="42nbtq"
O(N)
```

Space:

```text id="4xldol"
O(W)
```

`W = maximum width of tree`

---

# 8. Step-by-Step Trace

Example:

```text id="z79u92"
        3
       / \
      9  20
         / \
        15  7
```

---

## Recursive Calls

---

### Node 9

```text id="8e8y7n"
left = 0
right = 0

depth = 1
```

Returns `1`

---

### Node 15

Returns `1`

---

### Node 7

Returns `1`

---

### Node 20

```text id="p43a9z"
left = 1
right = 1

depth = 1 + max(1,1)
      = 2
```

Returns `2`

---

### Node 3

```text id="4d8t3x"
left = 1
right = 2

depth = 1 + max(1,2)
      = 3
```

Returns `3`

---

Final Answer:

```text id="n2rqhy"
3
```

---

# 9. Related Problems

### 1. Minimum Depth of Binary Tree

Find shortest root-to-leaf path instead.

### 2. Balanced Binary Tree

Uses subtree heights at every node.

### 3. Diameter of Binary Tree

Combines left/right depths for longest path.

### 4. Binary Tree Right Side View

Level-order traversal by depth.

### 5. Path Sum

DFS traversal carrying path information.
