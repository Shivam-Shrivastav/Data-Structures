# Binary Tree Inorder Traversal

## 1. Problem Statement with Example

Given the `root` of a binary tree, return the **inorder traversal** of its nodes' values.

In **inorder traversal**, nodes are visited in this order:

```text id="u5x5pn"
Left → Root → Right
```

LeetCode: Binary Tree Inorder Traversal

---

### Example

Input tree:

```text id="k5tyau"
    1
     \
      2
     /
    3
```

Traversal order:

```text id="7k4m4x"
Left of 1 → none
Visit 1

Go to 2:
Left of 2 → 3
Visit 3
Visit 2
```

Output:

```python id="3hvhjx"
[1,3,2]
```

---

### Constraints

* `0 <= number of nodes <= 100`
* `-100 <= Node.val <= 100`

---

# 2. Diagram

Tree:

```text id="k6kvh6"
        1
       / \
      2   3
     / \
    4   5
```

Inorder traversal:

```text id="j2tv3x"
Left subtree first:
4 → 2 → 5

Then root:
1

Then right subtree:
3
```

Final order:

```text id="6eik2w"
[4,2,5,1,3]
```

Traversal flow:

```text id="dbr0n8"
          1
        ↙   ↘
       2     3
     ↙  ↘
    4    5

Order:
4 → 2 → 5 → 1 → 3
```

---

# 3. Example I/O

## Example 1 (Typical)

Input:

```text id="s8hzx3"
root = [1,null,2,3]
```

Tree:

```text id="wejvv4"
    1
     \
      2
     /
    3
```

Output:

```python id="r8f9vw"
[1,3,2]
```

Explanation:

* Visit left of 1 → none
* Visit 1
* Visit left of 2 → 3
* Visit 2

---

## Example 2 (Edge Case)

Input:

```text id="6mn8n7"
root = []
```

Output:

```python id="5j5x9k"
[]
```

Explanation:

* Empty tree.

---

# 4. Intuition & Pattern Recognition

This is a classic **DFS tree traversal** problem.

Signal:

> “Inorder traversal”

Immediately think:

```text id="zw0pns"
Left → Root → Right
```

---

### Important property

For a **Binary Search Tree (BST)**:

```text id="n2jlwm"
Inorder traversal gives sorted order.
```

This is one of the biggest reasons inorder traversal is important.

---

### Interview recognition

Whenever problem says:

* traverse tree
* recursive visiting
* process left before root

Think:

* DFS recursion
* inorder template

---

### Mental model

At every node:

```text id="3z5npr"
1. Explore left subtree completely
2. Process current node
3. Explore right subtree
```

---

# 5. Simpler Version

## Simplest Version

Just print nodes in inorder.

Example:

```text id="4hmo4v"
    2
   / \
  1   3
```

Print:

```text id="2f33ua"
1 2 3
```

---

## Related simpler problems

### 1. Preorder Traversal

LeetCode: Binary Tree Preorder Traversal

Pattern:

```text id="7wb8de"
Root → Left → Right
```

Difference:

* Root visited first.

---

### 2. Postorder Traversal

LeetCode: Binary Tree Postorder Traversal

Pattern:

```text id="gzk25z"
Left → Right → Root
```

Difference:

* Root visited last.

---

### Thinking progression

```text id="1iv5mx"
Learn DFS recursion
    ↓
Understand subtree traversal
    ↓
Change visiting order
    ↓
Get inorder traversal
```

Only traversal order changes.

---

# 6. Brute Force

Recursive DFS itself is already optimal.

## Recursive Solution

```python id="2pjy42"
class Solution:
    def inorderTraversal(self, root):

        result = []

        def dfs(node):

            if not node:
                return

            # Traverse left subtree
            dfs(node.left)

            # Visit current node
            result.append(node.val)

            # Traverse right subtree
            dfs(node.right)

        dfs(root)

        return result
```

---

## Complexity

* Time: `O(n)`
* Space: `O(h)`

Where:

* `n` = number of nodes
* `h` = height of tree

Worst case skewed tree:

* `O(n)` recursion stack

---

# 7. Optimal Solution

## Recursive DFS (Most Interview Friendly)

```python id="33aj1x"
class Solution:
    def inorderTraversal(self, root):

        result = []

        def dfs(node):

            # Base case
            if not node:
                return

            # 1. Go left
            dfs(node.left)

            # 2. Visit current node
            result.append(node.val)

            # 3. Go right
            dfs(node.right)

        dfs(root)

        return result
```

---

## Iterative Stack Solution

This is commonly asked in interviews.

```python id="g6slzy"
class Solution:
    def inorderTraversal(self, root):

        stack = []
        result = []

        curr = root

        while curr or stack:

            # Go as left as possible
            while curr:
                stack.append(curr)
                curr = curr.left

            # Process node
            curr = stack.pop()
            result.append(curr.val)

            # Move to right subtree
            curr = curr.right

        return result
```

---

## Why iterative works

Stack simulates recursion.

Recursive call stack behavior:

```text id="63p7sm"
Keep going left
    ↓
Process node
    ↓
Move right
```

Iterative solution mimics exactly this.

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

```text id="18v02s"
        1
       / \
      2   3
     / \
    4   5
```

---

## Recursive Trace

| Step | Current Node   | Result      |
| ---- | -------------- | ----------- |
| 1    | Go left from 1 | []          |
| 2    | Go left from 2 | []          |
| 3    | Visit 4        | [4]         |
| 4    | Back to 2      | [4,2]       |
| 5    | Visit 5        | [4,2,5]     |
| 6    | Back to 1      | [4,2,5,1]   |
| 7    | Visit 3        | [4,2,5,1,3] |

Final answer:

```python id="lk5f8z"
[4,2,5,1,3]
```

---

# 9. Related Problems

### 1. Binary Tree Preorder Traversal

Same DFS traversal with different visiting order.

---

### 2. Binary Tree Postorder Traversal

Another traversal variant where root processed last.

---

### 3. Validate Binary Search Tree

Uses inorder traversal property of BST being sorted.

---

### 4. Kth Smallest Element in a BST

Inorder traversal naturally visits BST nodes in sorted order.

---

### 5. Binary Tree Level Order Traversal

Switches from DFS recursion to BFS queue traversal.
