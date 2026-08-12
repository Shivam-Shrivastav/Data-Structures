# Construct Binary Tree from Preorder and Inorder Traversal

## 1. Problem Statement with Example

Given two integer arrays:

* `preorder` → preorder traversal of a binary tree
* `inorder` → inorder traversal of the same binary tree

Construct and return the binary tree.

LeetCode: Construct Binary Tree from Preorder and Inorder Traversal

---

## Important Traversal Rules

### Preorder

```text id="m15y7s"
Root → Left → Right
```

### Inorder

```text id="w2wx3w"
Left → Root → Right
```

---

## Example

Input:

```python id="1yp0bn"
preorder = [3,9,20,15,7]
inorder  = [9,3,15,20,7]
```

Output tree:

```text id="slljq0"
        3
       / \
      9   20
         /  \
        15   7
```

---

## Constraints

* `1 <= preorder.length <= 3000`
* inorder.length == preorder.length
* Values are unique
* Both traversals are valid

---

# 2. Diagram

## Key observation

### Preorder gives root first

```text id="vwrr0k"
preorder = [3,9,20,15,7]
             ↑
            root
```

Root = `3`

---

## Inorder splits left and right subtree

```text id="k5cuhg"
inorder = [9,3,15,20,7]
             ↑
            root
```

Everything:

* left of `3` → left subtree
* right of `3` → right subtree

So:

```text id="8eqnqy"
Left subtree  = [9]
Right subtree = [15,20,7]
```

---

## Recursive decomposition

```text id="e0o4rx"
                3
              /   \
             9     20
                  /  \
                 15   7
```

Built recursively from slices/subranges.

---

# 3. Example I/O

## Example 1 (Typical)

Input:

```python id="4e62qe"
preorder = [3,9,20,15,7]
inorder  = [9,3,15,20,7]
```

Output:

```text id="y56xiu"
[3,9,20,null,null,15,7]
```

Explanation:

* preorder tells roots
* inorder splits subtrees

---

## Example 2 (Single Node)

Input:

```python id="8sjwh5"
preorder = [-1]
inorder  = [-1]
```

Output:

```text id="rr75rk"
[-1]
```

---

# 4. Intuition & Pattern Recognition

This is one of the most important **tree construction + DFS recursion** problems.

---

## Core insight

### Preorder tells:

```text id="l9wccz"
Who is the root?
```

Because preorder starts with root.

---

### Inorder tells:

```text id="8u0ptx"
What belongs to left subtree and right subtree?
```

Because inorder structure is:

```text id="jlwm9u"
Left → Root → Right
```

---

## Main recursive pattern

At every recursive step:

```text id="ru54gq"
1. Pick root from preorder
2. Find root in inorder
3. Split inorder into:
   left subtree
   right subtree
4. Recursively build both
```

---

## Interview recognition

Whenever you see:

```text id="0f0ydh"
Construct tree from traversals
```

Think:

| Traversal | What it gives    |
| --------- | ---------------- |
| Preorder  | Root first       |
| Inorder   | Left/right split |

---

# 5. Simpler Version

---

## Simplest Version

Suppose:

```python id="jlwmbl"
preorder = [1]
inorder = [1]
```

Tree:

```text id="8l6z1w"
1
```

Easy:

* first preorder value = root
* no children

---

## Slightly harder

```python id="tlq67q"
preorder = [1,2,3]
inorder  = [2,1,3]
```

Root:

* preorder[0] = 1

Find 1 in inorder:

```text id="95ixd6"
[2,1,3]
   ↑
```

Left subtree:

* `[2]`

Right subtree:

* `[3]`

Build recursively.

---

# Related Simpler Problems

### 1. Binary Tree Preorder Traversal

LeetCode: Binary Tree Preorder Traversal

Understand:

* preorder visits root first

---

### 2. Binary Tree Inorder Traversal

LeetCode: Binary Tree Inorder Traversal

Understand:

* inorder splits left/right subtree

---

### 3. Construct Binary Tree from Inorder and Postorder Traversal

LeetCode: Construct Binary Tree from Inorder and Postorder Traversal

Same idea:

* postorder gives root at end instead of beginning

---

## Thinking progression

```text id="sgzibw"
Traversal order understanding
        ↓
Root identification
        ↓
Subtree splitting
        ↓
Recursive tree construction
```

---

# 6. Brute Force

## Idea

At every recursive call:

1. Take root from preorder
2. Search root in inorder using linear scan
3. Recursively build left/right

---

## Brute Force Code

```python id="jlwm3m"
class Solution:

    def buildTree(self, preorder, inorder):

        if not preorder or not inorder:
            return None

        # First preorder value is root
        root_val = preorder[0]

        root = TreeNode(root_val)

        # Find root in inorder
        mid = inorder.index(root_val)

        # Build left subtree
        root.left = self.buildTree(
            preorder[1:mid+1],
            inorder[:mid]
        )

        # Build right subtree
        root.right = self.buildTree(
            preorder[mid+1:],
            inorder[mid+1:]
        )

        return root
```

---

## Complexity

### Time

Worst case:

```text id="riuwz2"
O(n^2)
```

Because:

* every recursive call does linear search

### Space

```text id="jlwm85"
O(n)
```

Due to recursion + array slicing.

---

# 7. Optimal Solution

## Key optimization

Use hashmap:

```python id="z0efna"
value -> inorder index
```

Now root lookup becomes:

```text id="jlwm0m"
O(1)
```

---

# Optimal Recursive DFS

```python id="jlwmxw"
class Solution:

    def buildTree(self, preorder, inorder):

        # Map value -> inorder index
        inorder_map = {
            value: idx
            for idx, value in enumerate(inorder)
        }

        preorder_index = 0

        def dfs(left, right):

            nonlocal preorder_index

            # No subtree exists
            if left > right:
                return None

            # Pick current root from preorder
            root_val = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(root_val)

            # Split inorder
            mid = inorder_map[root_val]

            # Build left subtree
            root.left = dfs(left, mid - 1)

            # Build right subtree
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(inorder) - 1)
```

---

# Why this works

## Preorder guarantees

```text id="2a59za"
Current preorder element = current subtree root
```

---

## Inorder guarantees

```text id="r4zjlwm"
Everything left of root index → left subtree
Everything right → right subtree
```

---

## Recursive magic

Each recursive call gets:

```text id="7xtrrl"
Current inorder boundaries
```

Which fully defines subtree.

---

# Complexity

## Time

```text id="jlwm0w"
O(n)
```

Each node processed once.

---

## Space

```text id="jlwmtr"
O(n)
```

For:

* hashmap
* recursion stack

---

# 8. Step-by-Step Trace

Input:

```python id="5uwbn0"
preorder = [3,9,20,15,7]
inorder  = [9,3,15,20,7]
```

---

## Step 1

Root from preorder:

```text id="jlwm1p"
3
```

Find in inorder:

```text id="jlwmv0"
[9,3,15,20,7]
   ↑
```

Build:

```text id="jlwmx1"
        3
```

---

## Step 2 — Left subtree

Inorder left part:

```text id="9a8g52"
[9]
```

Next preorder value:

```text id="p8nn74"
9
```

Build:

```text id="jlwmz5"
        3
       /
      9
```

---

## Step 3 — Right subtree

Inorder right part:

```text id="jlwmx9"
[15,20,7]
```

Next preorder value:

```text id="jlwmq8"
20
```

Build:

```text id="4gwsu6"
        3
       / \
      9   20
```

---

## Step 4

Left of 20:

```text id="3m8s4d"
15
```

Right of 20:

```text id="jlwm8m"
7
```

Final tree:

```text id="jlwmv7"
        3
       / \
      9   20
         /  \
        15   7
```

---

# 9. Related Problems

### 1. Construct Binary Tree from Inorder and Postorder Traversal

Same construction logic, but postorder gives root at end.

---

### 2. Binary Tree Preorder Traversal

Helps understand why preorder identifies roots.

---

### 3. Binary Tree Inorder Traversal

Critical for understanding subtree splitting.

---

### 4. Serialize and Deserialize Binary Tree

Advanced tree reconstruction problem.

---

### 5. Validate Binary Search Tree

Another recursion-heavy tree structure problem.
