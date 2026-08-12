# Recover Binary Search Tree

Cracking the Coding Interview style interview classic: detect two swapped nodes in a BST and restore the tree **without changing structure**.

---

# 1. Problem Statement with Example

You are given the `root` of a Binary Search Tree (BST), where **exactly two nodes were swapped by mistake**.

Recover the tree without changing its structure.

A BST property:

* Left subtree values `< root`
* Right subtree values `> root`

If two nodes are swapped, the inorder traversal is no longer sorted.

### Example

Input:

```text
    3
   / \
  1   4
     /
    2
```

Correct BST should be:

```text
    2
   / \
  1   4
     /
    3
```

Output:

```text
    2
   / \
  1   4
     /
    3
```

### Constraints

* Number of nodes: `[2, 1000]`
* `-2^31 <= Node.val <= 2^31 - 1`

Follow-up:

* Can you solve it in `O(1)` extra space?

---

# 2. Diagram

## Key Observation

### Inorder traversal of BST should be sorted

Correct BST inorder:

```text
1 2 3 4 5
```

Swapped BST:

```text
1 4 3 2 5
```

Violations happen where:

```text
prev > current
```

Visual:

```text
prev current
 4  >  3   ← violation #1

prev current
 3  >  2   ← violation #2
```

Swapped nodes:

* first = 4
* second = 2

Swap them back.

---

# 3. Example I/O

## Example 1

Input:

```text
root = [1,3,null,null,2]

    1
   /
  3
   \
    2
```

Inorder:

```text
3 2 1
```

Output:

```text
    3
   /
  1
   \
    2
```

Why?

Sorted inorder should be:

```text
1 2 3
```

Swapped nodes are `1` and `3`.

---

## Example 2 (Adjacent Swap)

Input:

```text
    2
   / \
  3   1
```

Inorder:

```text
3 2 1
```

Output:

```text
    2
   / \
  1   3
```

---

# 4. Intuition & Pattern Recognition

This is a **BST inorder traversal** problem.

### Signal to identify pattern quickly

Whenever you hear:

* "BST corrupted"
* "Recover BST"
* "Two nodes swapped"
* "Validate BST"

Immediately think:

```text
BST inorder traversal = sorted order
```

---

## Core Insight

If two nodes are swapped:

### Case 1: Non-adjacent swap

Correct:

```text
1 2 3 4 5
```

Swapped:

```text
1 4 3 2 5
```

You get TWO violations.

---

### Case 2: Adjacent swap

Correct:

```text
1 2 3 4
```

Swapped:

```text
1 3 2 4
```

Only ONE violation.

---

## Interview Thinking

Say this:

> “Since inorder traversal of a BST must be sorted, I’ll detect where ordering breaks. The misplaced larger value is the first node, and the final misplaced smaller value is the second node.”

---

# 5. Simpler Version

## Simplest Problem

### “Check if BST inorder traversal is sorted”

LeetCode:

* Introduction to Algorithms style BST validation
* Related LC: Validate Binary Search Tree

You simply detect:

```text
prev >= current
```

---

## Next Level

### “Find two swapped numbers in sorted array”

Example:

```text
1 5 3 4 2 6
```

Violations:

```text
5 > 3
4 > 2
```

Swapped numbers:

* 5
* 2

BST version is identical — except inorder traversal produces the array dynamically.

---

## Thinking Progression

```text
Validate BST
    ↓
Observe inorder sorted
    ↓
Detect violations
    ↓
Store wrong nodes
    ↓
Swap values back
```

---

# 6. Brute Force

## Idea

1. Store inorder traversal into array
2. Find two misplaced values
3. Traverse tree again and swap them

---

## Complexity

* Time: `O(N)`
* Space: `O(N)`

---

## Brute Force Code

```python
class Solution:
    def recoverTree(self, root):
        inorder = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            inorder.append(node)
            dfs(node.right)

        dfs(root)

        x = y = None

        for i in range(len(inorder) - 1):
            if inorder[i].val > inorder[i + 1].val:
                y = inorder[i + 1]

                if not x:
                    x = inorder[i]
                else:
                    break

        x.val, y.val = y.val, x.val
```

---

# 7. Optimal Solution

## Optimal Idea

Do inorder traversal while tracking:

* `prev` → previous inorder node
* `first` → first wrong node
* `second` → second wrong node

Whenever:

```text
prev.val > current.val
```

we found a violation.

---

## Why This Works

### First violation

```text
prev = wrong larger node
```

### Second violation (or same)

```text
current = wrong smaller node
```

At the end:

* swap `first` and `second`

---

# Optimal Code (Recursive Inorder)

```python
class Solution:
    def recoverTree(self, root):
        self.first = None
        self.second = None
        self.prev = TreeNode(float('-inf'))

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            # violation found
            if self.prev.val > node.val:

                # first wrong node
                if not self.first:
                    self.first = self.prev

                # keep updating second
                self.second = node

            self.prev = node

            inorder(node.right)

        inorder(root)

        # swap values back
        self.first.val, self.second.val = (
            self.second.val,
            self.first.val
        )
```

---

## Complexity

### Recursive Version

* Time: `O(N)`
* Space: `O(H)`

  * recursion stack

---

# Morris Traversal Follow-up (O(1) Space)

This problem is famous because interviewers ask:

> “Can you do it with constant extra space?”

Use:

* Morris Inorder Traversal

Same logic:

* detect violations
* no recursion stack

---

# 8. Step-by-Step Trace

Example:

```text
    3
   / \
  1   4
     /
    2
```

Inorder:

```text
1 3 2 4
```

---

| Current | Prev | Violation? | First | Second |
| ------- | ---- | ---------- | ----- | ------ |
| 1       | -inf | No         | None  | None   |
| 3       | 1    | No         | None  | None   |
| 2       | 3    | YES        | 3     | 2      |
| 4       | 2    | No         | 3     | 2      |

Swap:

```text
3 ↔ 2
```

Recovered BST:

```text
1 2 3 4
```

---

# 9. Related Problems

## 1. Validate Binary Search Tree

Detect whether inorder traversal remains sorted.

---

## 2. Kth Smallest Element in a BST

Uses inorder traversal because BST inorder is sorted.

---

## 3. Binary Search Tree Iterator

Simulates controlled inorder traversal.

---

## 4. Convert Sorted Array to BST

Reverse direction:

* sorted array → BST

---

## 5. Balance a Binary Search Tree

Uses inorder traversal to extract sorted nodes, then rebuild balanced BST.
