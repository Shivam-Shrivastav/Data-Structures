# Binary Tree Preorder Traversal

## 1. Problem Statement with Example

Given the `root` of a binary tree, return the **preorder traversal** of its nodes' values.

In **preorder traversal**, we visit nodes in this order:

1. Root
2. Left subtree
3. Right subtree

LeetCode: Binary Tree Preorder Traversal

### Example

Input:

```text
    1
     \
      2
     /
    3
```

Preorder traversal:

```text
1 → 2 → 3
```

Output:

```python
[1,2,3]
```

### Constraints

* Number of nodes: `0 <= n <= 100`
* `-100 <= Node.val <= 100`

These constraints allow:

* Recursive DFS
* Iterative stack solution

---

# 2. Diagram

```text
        1
       / \
      2   3
     / \
    4   5
```

Preorder order:

```text
Visit Root first:
1

Then Left subtree:
2 → 4 → 5

Then Right subtree:
3
```

Final traversal:

```text
[1,2,4,5,3]
```

Traversal flow:

```text
          1
        ↙   ↘
       2     3
     ↙  ↘
    4    5

Order:
1 → 2 → 4 → 5 → 3
```

---

# 3. Example I/O

## Example 1 (Typical)

Input:

```text
root = [1,null,2,3]
```

Tree:

```text
    1
     \
      2
     /
    3
```

Output:

```python
[1,2,3]
```

Explanation:

* Visit 1
* Go right to 2
* Visit left child 3

---

## Example 2 (Edge Case)

Input:

```text
root = []
```

Output:

```python
[]
```

Explanation:

* Empty tree → nothing to traverse.

---

# 4. Intuition & Pattern Recognition

This is a classic **Tree DFS Traversal** problem.

Key signal:

> “Traverse binary tree in preorder”

Immediately think:

```text
Root → Left → Right
```

In interview:

```text
Preorder = process current node BEFORE children.
```

### Mental model

Whenever you reach a node:

1. Add current node value
2. Explore left
3. Explore right

DFS naturally fits because:

* We fully explore one branch before another.
* Recursion mirrors tree structure.

---

# 5. Simpler Version

## Simplest Version

### Just print nodes in preorder

```text
1
/ \
2 3
```

Print:

```text
1 2 3
```

Instead of storing values in array.

---

## Related simpler problems

### 1. Binary Tree Inorder Traversal

LeetCode: Binary Tree Inorder Traversal

Pattern:

```text
Left → Root → Right
```

Difference:

* Root is processed in middle.

---

### 2. Binary Tree Postorder Traversal

LeetCode: Binary Tree Postorder Traversal

Pattern:

```text
Left → Right → Root
```

Difference:

* Root processed last.

---

### Thinking progression

```text
Learn recursion on tree
    ↓
Understand DFS
    ↓
Learn inorder
    ↓
Change order slightly
    ↓
Get preorder
```

Core idea remains same:

* Recursive traversal
* Only visiting order changes.

---

# 6. Brute Force

There is no real “worse” approach here beyond traversal itself.

Recursive DFS itself is already optimal.

### Recursive Brute Force

```python
class Solution:
    def preorderTraversal(self, root):
        result = []

        def dfs(node):
            if not node:
                return

            result.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return result
```

### Complexity

* Time: `O(n)`
* Space: `O(h)`

  * `h` = tree height
  * recursion stack

Worst case:

* skewed tree → `O(n)`

---

# 7. Optimal Solution

## Recursive DFS (Most Interview Friendly)

```python
class Solution:
    def preorderTraversal(self, root):
        result = []

        def dfs(node):
            # Base case
            if not node:
                return

            # 1. Visit current node
            result.append(node.val)

            # 2. Traverse left subtree
            dfs(node.left)

            # 3. Traverse right subtree
            dfs(node.right)

        dfs(root)

        return result
```

---

## Iterative Stack Solution

Useful when interviewer asks:

> “Can you do it iteratively?”

```python
class Solution:
    def preorderTraversal(self, root):

        if not root:
            return []

        stack = [root]
        result = []

        while stack:

            node = stack.pop()

            # Visit node
            result.append(node.val)

            # Push right first
            if node.right:
                stack.append(node.right)

            # Push left second
            if node.left:
                stack.append(node.left)

        return result
```

### Why push right first?

Stack is LIFO.

We want:

```text
Root → Left → Right
```

So:

* push right first
* left stays on top
* left processed first

---

## Complexity

### Recursive

* Time: `O(n)`
* Space: `O(h)`

### Iterative

* Time: `O(n)`
* Space: `O(h)`

---

# 8. Step-by-Step Trace

Tree:

```text
        1
       / \
      2   3
     / \
    4   5
```

Using recursive DFS.

---

| Step | Current Node | Result      |
| ---- | ------------ | ----------- |
| 1    | 1            | [1]         |
| 2    | 2            | [1,2]       |
| 3    | 4            | [1,2,4]     |
| 4    | NULL         | backtrack   |
| 5    | NULL         | backtrack   |
| 6    | 5            | [1,2,4,5]   |
| 7    | NULL         | backtrack   |
| 8    | NULL         | backtrack   |
| 9    | 3            | [1,2,4,5,3] |

Final answer:

```python
[1,2,4,5,3]
```

---

# 9. Related Problems

### 1. Binary Tree Inorder Traversal

Same DFS traversal idea, only visiting order changes.

---

### 2. Binary Tree Postorder Traversal

Another traversal variation where root is processed last.

---

### 3. Binary Tree Level Order Traversal

Switch from DFS to BFS using queue.

---

### 4. Maximum Depth of Binary Tree

Uses DFS recursion similarly, but computes height instead of traversal.

---

### 5. Construct Binary Tree from Preorder and Inorder Traversal

Advanced use of preorder traversal properties to rebuild trees.
