# Binary Tree Postorder Traversal

## 1. Problem Statement with Example

Given the `root` of a binary tree, return the **postorder traversal** of its nodes' values.

In **postorder traversal**, nodes are visited in this order:

```text id="d83j0r"
Left → Right → Root
```

LeetCode: Binary Tree Postorder Traversal

---

### Example

Input tree:

```text id="fphl9y"
    1
     \
      2
     /
    3
```

Traversal order:

```text id="twj6ik"
Left of 1 → none

Go right to 2:
Left of 2 → 3
Visit 3
Visit 2

Visit 1
```

Output:

```python id="zrm8jr"
[3,2,1]
```

---

### Constraints

* `0 <= number of nodes <= 100`
* `-100 <= Node.val <= 100`

---

# 2. Diagram

Tree:

```text id="7r7h1u"
        1
       / \
      2   3
     / \
    4   5
```

Postorder traversal:

```text id="3lud4r"
Left subtree:
4 → 5 → 2

Right subtree:
3

Finally root:
1
```

Final order:

```text id="ddvhp0"
[4,5,2,3,1]
```

Traversal flow:

```text id="9w4w8j"
          1
        ↙   ↘
       2     3
     ↙  ↘
    4    5

Order:
4 → 5 → 2 → 3 → 1
```

---

# 3. Example I/O

## Example 1 (Typical)

Input:

```text id="n1kr8r"
root = [1,null,2,3]
```

Tree:

```text id="cmkq09"
    1
     \
      2
     /
    3
```

Output:

```python id="jlwm7r"
[3,2,1]
```

Explanation:

* Visit left subtree of 2 → 3
* Visit 2
* Visit 1 last

---

## Example 2 (Edge Case)

Input:

```text id="e94j36"
root = []
```

Output:

```python id="yx4m14"
[]
```

Explanation:

* Empty tree → no traversal.

---

# 4. Intuition & Pattern Recognition

This is another classic **DFS traversal** problem.

Signal:

> “Postorder traversal”

Immediately think:

```text id="o8e2m3"
Left → Right → Root
```

---

## Key intuition

Postorder means:

```text id="j5pb7h"
Process children BEFORE parent.
```

This is useful when:

* deleting tree
* calculating subtree info
* bottom-up processing

---

## Interview recognition

If problem says:

* compute something from children
* process subtree first
* bottom-up tree logic

Postorder DFS is usually involved.

---

## Mental model

At every node:

```text id="bmttjt"
1. Finish left subtree
2. Finish right subtree
3. Process current node
```

---

# 5. Simpler Version

## Simplest Version

Just print nodes in postorder.

Example:

```text id="9gdz2x"
    1
   / \
  2   3
```

Print:

```text id="nrm9wf"
2 3 1
```

---

## Related simpler problems

### 1. Preorder Traversal

LeetCode: Binary Tree Preorder Traversal

Pattern:

```text id="v4mbkc"
Root → Left → Right
```

Difference:

* Root processed first.

---

### 2. Inorder Traversal

LeetCode: Binary Tree Inorder Traversal

Pattern:

```text id="o4ed73"
Left → Root → Right
```

Difference:

* Root processed in middle.

---

## Thinking progression

```text id="a8e2y0"
Learn DFS recursion
    ↓
Understand subtree traversal
    ↓
Delay processing current node
    ↓
Get postorder traversal
```

---

# 6. Brute Force

Recursive DFS itself is already optimal.

## Recursive Solution

```python id="66c0r7"
class Solution:
    def postorderTraversal(self, root):

        result = []

        def dfs(node):

            if not node:
                return

            # Traverse left subtree
            dfs(node.left)

            # Traverse right subtree
            dfs(node.right)

            # Visit current node
            result.append(node.val)

        dfs(root)

        return result
```

---

## Complexity

* Time: `O(n)`
* Space: `O(h)`

Where:

* `n` = number of nodes
* `h` = tree height

Worst case skewed tree:

* recursion stack = `O(n)`

---

# 7. Optimal Solution

## Recursive DFS (Most Interview Friendly)

```python id="p0wmz7"
class Solution:
    def postorderTraversal(self, root):

        result = []

        def dfs(node):

            # Base case
            if not node:
                return

            # 1. Traverse left subtree
            dfs(node.left)

            # 2. Traverse right subtree
            dfs(node.right)

            # 3. Visit current node
            result.append(node.val)

        dfs(root)

        return result
```

---

## Iterative Stack Solution

Postorder iterative is trickier.

### Easy interview version:

* Use modified preorder
* Reverse result at end

---

### Idea

Normal preorder:

```text id="4al9e9"
Root → Left → Right
```

Modified preorder:

```text id="e0v9gk"
Root → Right → Left
```

Reverse it:

```text id="iowu89"
Left → Right → Root
```

Which becomes postorder.

---

## Iterative Code

```python id="o9nrb8"
class Solution:
    def postorderTraversal(self, root):

        if not root:
            return []

        stack = [root]
        result = []

        while stack:

            node = stack.pop()

            # Add current node
            result.append(node.val)

            # Push left first
            if node.left:
                stack.append(node.left)

            # Push right second
            if node.right:
                stack.append(node.right)

        # Reverse final order
        return result[::-1]
```

---

## Why this works

Generated order:

```text id="g9v1se"
Root → Right → Left
```

Reverse:

```text id="jx1m4k"
Left → Right → Root
```

Exactly postorder.

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

```text id="b8r7lp"
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
| 4    | Visit 5        | [4,5]       |
| 5    | Visit 2        | [4,5,2]     |
| 6    | Visit 3        | [4,5,2,3]   |
| 7    | Visit 1        | [4,5,2,3,1] |

Final answer:

```python id="gfd7p7"
[4,5,2,3,1]
```

---

# 9. Related Problems

### 1. Binary Tree Preorder Traversal

Same DFS structure with root processed first.

---

### 2. Binary Tree Inorder Traversal

DFS traversal where root processed in middle.

---

### 3. Balanced Binary Tree

Uses postorder traversal to compute subtree heights bottom-up.

---

### 4. Diameter of Binary Tree

Classic postorder DFS because child heights are needed before parent.

---

### 5. Binary Tree Maximum Path Sum

Advanced postorder DFS where subtree results are propagated upward.
