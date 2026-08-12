# Construct Binary Tree from Inorder and Postorder Traversal

## 1. Problem Statement with Example

Given two integer arrays:

* `inorder` → inorder traversal of a binary tree
* `postorder` → postorder traversal of the same binary tree

Construct and return the binary tree.

LeetCode: Construct Binary Tree from Inorder and Postorder Traversal

---

# Important Traversal Rules

## Inorder

```text id="w0b4c8"
Left → Root → Right
```

## Postorder

```text id="jlwmc8"
Left → Right → Root
```

---

## Example

Input:

```python id="jlwm8c"
inorder   = [9,3,15,20,7]
postorder = [9,15,7,20,3]
```

Output tree:

```text id="jlwm9w"
        3
       / \
      9   20
         /  \
        15   7
```

---

## Constraints

* `1 <= inorder.length <= 3000`
* postorder.length == inorder.length
* Values are unique
* Both traversals are valid

---

# 2. Diagram

# Core Observation

## Postorder gives root LAST

```text id="8w7e3x"
postorder = [9,15,7,20,3]
                        ↑
                      root
```

Root = `3`

---

## Inorder splits left/right subtree

```text id="n0vjlwm"
inorder = [9,3,15,20,7]
             ↑
            root
```

So:

```text id="jlwm9v"
Left subtree  = [9]
Right subtree = [15,20,7]
```

---

# Important Subtlety

Because postorder is:

```text id="jlwmf2"
Left → Right → Root
```

When traversing backward:

```text id="jlwmz9"
Root → Right → Left
```

This is VERY important.

---

## Recursive Construction

```text id="jlwm7n"
                3
              /   \
             9     20
                  /  \
                 15   7
```

---

# 3. Example I/O

## Example 1 (Typical)

Input:

```python id="jlwm5t"
inorder   = [9,3,15,20,7]
postorder = [9,15,7,20,3]
```

Output:

```text id="jlwm0y"
[3,9,20,null,null,15,7]
```

---

## Example 2 (Single Node)

Input:

```python id="jlwm6z"
inorder   = [-1]
postorder = [-1]
```

Output:

```text id="jlwm9t"
[-1]
```

---

# 4. Intuition & Pattern Recognition

This problem is almost identical to:

Construct Binary Tree from Preorder and Inorder Traversal

BUT:

| Problem             | Traversal giving root |
| ------------------- | --------------------- |
| Preorder + Inorder  | Root at beginning     |
| Postorder + Inorder | Root at end           |

---

# Core Insight

## Postorder tells:

```text id="jlwmj5"
Who is the root?
```

Because root is always last.

---

## Inorder tells:

```text id="jlwmv4"
How to split left/right subtree?
```

---

# The Important Trick

When consuming postorder backward:

```text id="4fjlwm"
Root → Right → Left
```

So recursion must build:

```text id="rjlwm9"
1. Right subtree first
2. Left subtree second
```

Otherwise indices break.

---

# Interview Recognition

Whenever you see:

```text id="hjlwm7"
Construct tree using inorder + another traversal
```

Think:

| Traversal          | Gives              |
| ------------------ | ------------------ |
| inorder            | subtree boundaries |
| preorder/postorder | root positions     |

---

# 5. Simpler Version

---

## Simplest Version

```python id="qjlwm7"
inorder   = [1]
postorder = [1]
```

Tree:

```text id="jlwmx4"
1
```

Easy:

* last postorder element = root

---

## Slightly Harder

```python id="6qjlwm"
inorder   = [2,1,3]
postorder = [2,3,1]
```

Root:

```text id="jjlwm4"
1
```

Find in inorder:

```text id="djlwm7"
[2,1,3]
   ↑
```

Split:

* left = `[2]`
* right = `[3]`

Build recursively.

---

# Related Simpler Problems

### 1. Binary Tree Postorder Traversal

LeetCode: Binary Tree Postorder Traversal

Need strong understanding that:

* root appears last

---

### 2. Binary Tree Inorder Traversal

LeetCode: Binary Tree Inorder Traversal

Need understanding of subtree splitting.

---

### 3. Construct Binary Tree from Preorder and Inorder Traversal

LeetCode: Construct Binary Tree from Preorder and Inorder Traversal

Same exact pattern.
Only recursive direction changes.

---

# Thinking Progression

```text id="zjlwm6"
Understand traversals
        ↓
Root identification
        ↓
Subtree splitting
        ↓
Recursive construction
        ↓
Reverse recursion direction for postorder
```

---

# 6. Brute Force

## Idea

At every recursive call:

1. Take last postorder value as root
2. Search root in inorder
3. Recursively construct left/right

---

## Brute Force Code

```python id="jlwmc5"
class Solution:

    def buildTree(self, inorder, postorder):

        if not inorder or not postorder:
            return None

        # Last postorder value is root
        root_val = postorder[-1]

        root = TreeNode(root_val)

        # Find root in inorder
        mid = inorder.index(root_val)

        # Build left subtree
        root.left = self.buildTree(
            inorder[:mid],
            postorder[:mid]
        )

        # Build right subtree
        root.right = self.buildTree(
            inorder[mid+1:],
            postorder[mid:-1]
        )

        return root
```

---

# Complexity

## Time

```text id="jlwmm2"
O(n^2)
```

Because:

* linear search at every recursive step

---

## Space

```text id="6jlwm1"
O(n)
```

Due to:

* recursion
* array slicing

---

# 7. Optimal Solution

# Key Optimization

Use hashmap:

```python id="3jlwmf"
value -> inorder index
```

Now root lookup becomes:

```text id="8jlwm0"
O(1)
```

---

# Optimal Recursive DFS

```python id="jjlwm1"
class Solution:

    def buildTree(self, inorder, postorder):

        # Map value -> inorder index
        inorder_map = {
            value: idx
            for idx, value in enumerate(inorder)
        }

        postorder_index = len(postorder) - 1

        def dfs(left, right):

            nonlocal postorder_index

            # No subtree exists
            if left > right:
                return None

            # Current root
            root_val = postorder[postorder_index]
            postorder_index -= 1

            root = TreeNode(root_val)

            # Find split point
            mid = inorder_map[root_val]

            # IMPORTANT:
            # Build right subtree FIRST
            root.right = dfs(mid + 1, right)

            # Then build left subtree
            root.left = dfs(left, mid - 1)

            return root

        return dfs(0, len(inorder) - 1)
```

---

# Why Right Subtree First?

Postorder:

```text id="1jlwm3"
Left → Right → Root
```

Backward traversal:

```text id="4jlwm4"
Root → Right → Left
```

So after root:

* next nodes belong to right subtree first.

This is the most important interview point.

---

# Complexity

## Time

```text id="9jlwm5"
O(n)
```

Each node processed once.

---

## Space

```text id="3jlwm6"
O(n)
```

For:

* hashmap
* recursion stack

---

# 8. Step-by-Step Trace

Input:

```python id="7jlwm7"
inorder   = [9,3,15,20,7]
postorder = [9,15,7,20,3]
```

---

# Step 1

Root from postorder end:

```text id="2jlwm8"
3
```

Find in inorder:

```text id="0jlwm9"
[9,3,15,20,7]
   ↑
```

Build:

```text id="8jlwm0"
        3
```

---

# Step 2 — Right subtree FIRST

Next postorder value:

```text id="9jlwm1"
20
```

Build:

```text id="6jlwm2"
        3
          \
           20
```

---

# Step 3

Right of 20:

```text id="5jlwm3"
7
```

Left of 20:

```text id="2jlwm4"
15
```

Build:

```text id="7jlwm5"
        3
          \
           20
          /  \
         15   7
```

---

# Step 4 — Left subtree of 3

Remaining value:

```text id="1jlwm6"
9
```

Final tree:

```text id="9jlwm7"
        3
       / \
      9   20
         /  \
        15   7
```

---

# 9. Related Problems

### 1. Construct Binary Tree from Preorder and Inorder Traversal

Same recursion pattern with preorder instead of postorder.

---

### 2. Binary Tree Postorder Traversal

Critical for understanding root-last property.

---

### 3. Binary Tree Inorder Traversal

Critical for subtree splitting logic.

---

### 4. Serialize and Deserialize Binary Tree

Advanced reconstruction/encoding problem.

---

### 5. Construct String from Binary Tree

Another recursive tree construction problem.
