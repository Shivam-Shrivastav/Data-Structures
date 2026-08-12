# Construct Binary Tree from Preorder and Postorder Traversal

## 1. Problem Statement with Example

Given two integer arrays:

* `preorder` → preorder traversal of a binary tree
* `postorder` → postorder traversal of the same tree

Construct and return the binary tree.

If multiple answers exist, return any of them.

LeetCode: Construct Binary Tree from Preorder and Postorder Traversal

---

# Important Traversal Rules

## Preorder

```text id="4clscf"
Root → Left → Right
```

## Postorder

```text id="0b4e2n"
Left → Right → Root
```

---

## Example

Input:

```python id="gr1lcl"
preorder  = [1,2,4,5,3,6,7]
postorder = [4,5,2,6,7,3,1]
```

Output:

```text id="spxbg4"
        1
      /   \
     2     3
    / \   / \
   4  5  6   7
```

---

# Important Note

Unlike inorder problems:

```text id="4ib0jt"
Tree is NOT always uniquely determined.
```

Multiple valid trees may exist.

Problem allows returning any valid one.

---

## Constraints

* `1 <= preorder.length <= 30`
* Values are unique

---

# 2. Diagram

# Key Observations

## Preorder gives current root FIRST

```text id="jlwmm7"
preorder = [1,2,4,5,3,6,7]
             ↑
            root
```

Root = `1`

---

## Next preorder element = left subtree root

```text id="7jlwm8"
preorder = [1,2,4,5,3,6,7]
               ↑
         left subtree root
```

Left root = `2`

---

## Find left subtree boundary in postorder

```text id="3jlwm9"
postorder = [4,5,2,6,7,3,1]
                 ↑
               left root
```

Everything until `2` belongs to left subtree.

---

# Recursive Split

```text id="6jlwm0"
                1
              /   \
             2     3
            / \   / \
           4  5  6   7
```

---

# 3. Example I/O

## Example 1 (Typical)

Input:

```python id="2jlwm1"
preorder  = [1,2,4,5,3,6,7]
postorder = [4,5,2,6,7,3,1]
```

Output:

```text id="9jlwm2"
[1,2,3,4,5,6,7]
```

---

## Example 2 (Single Node)

Input:

```python id="5jlwm3"
preorder  = [1]
postorder = [1]
```

Output:

```text id="1jlwm4"
[1]
```

---

# 4. Intuition & Pattern Recognition

This is harder than:

* preorder + inorder
* inorder + postorder

Because:

```text id="7jlwm5"
No inorder traversal available
```

So subtree boundaries are harder to determine.

---

# Core Insight

## Preorder tells:

```text id="4jlwm6"
Current root immediately
```

---

## Postorder tells:

```text id="8jlwm7"
Where subtree ends
```

---

# The Critical Trick

After root in preorder:

```text id="9jlwm8"
Next element = left subtree root
```

Find that value in postorder:

```text id="3jlwm9"
Everything before it belongs to left subtree
```

This gives subtree size.

---

# Interview Recognition

Whenever you see:

```text id="6jlwm0"
preorder + postorder
```

Think:

```text id="0jlwm1"
Use next preorder node
to determine left subtree size
```

---

# 5. Simpler Version

---

# Simplest Version

```python id="4jlwm2"
preorder  = [1]
postorder = [1]
```

Tree:

```text id="8jlwm3"
1
```

Easy:

* single node root

---

# Slightly Harder

```python id="2jlwm4"
preorder  = [1,2,3]
postorder = [3,2,1]
```

Root:

```text id="5jlwm5"
1
```

Next preorder element:

```text id="9jlwm6"
2
```

Find `2` in postorder:

```text id="1jlwm7"
[3,2,1]
   ↑
```

Left subtree size:

```text id="7jlwm8"
2 nodes
```

Build recursively.

---

# Related Simpler Problems

### 1. Construct Binary Tree from Preorder and Inorder Traversal

LeetCode: Construct Binary Tree from Preorder and Inorder Traversal

Easier because inorder directly splits subtrees.

---

### 2. Construct Binary Tree from Inorder and Postorder Traversal

LeetCode: Construct Binary Tree from Inorder and Postorder Traversal

Same recursive construction pattern.

---

### 3. Binary Tree Preorder Traversal

LeetCode: Binary Tree Preorder Traversal

Need strong understanding of preorder ordering.

---

### 4. Binary Tree Postorder Traversal

LeetCode: Binary Tree Postorder Traversal

Need strong understanding of subtree endings.

---

# Thinking Progression

```text id="3jlwm9"
Understand traversals
        ↓
Root identification
        ↓
Infer subtree sizes
        ↓
Recursive reconstruction
```

---

# 6. Brute Force

## Idea

Recursively:

1. Take preorder root
2. Find next preorder value in postorder
3. Compute left subtree size
4. Split arrays recursively

Naively use slicing.

---

# Brute Force Code

```python id="6jlwm0"
class Solution:

    def constructFromPrePost(self, preorder, postorder):

        if not preorder:
            return None

        root = TreeNode(preorder[0])

        if len(preorder) == 1:
            return root

        # Left subtree root
        left_root = preorder[1]

        # Find boundary in postorder
        idx = postorder.index(left_root)

        left_size = idx + 1

        root.left = self.constructFromPrePost(
            preorder[1:left_size+1],
            postorder[:left_size]
        )

        root.right = self.constructFromPrePost(
            preorder[left_size+1:],
            postorder[left_size:-1]
        )

        return root
```

---

# Complexity

## Time

```text id="9jlwm1"
O(n^2)
```

Because:

* repeated linear searches
* array slicing

---

## Space

```text id="2jlwm2"
O(n)
```

---

# 7. Optimal Solution

# Optimization

Use hashmap:

```python id="5jlwm3"
value -> postorder index
```

Now subtree boundary lookup becomes:

```text id="8jlwm4"
O(1)
```

---

# Optimal Recursive DFS

```python id="1jlwm5"
class Solution:

    def constructFromPrePost(self, preorder, postorder):

        post_map = {
            value: idx
            for idx, value in enumerate(postorder)
        }

        preorder_index = 0

        def dfs(left, right):

            nonlocal preorder_index

            # No subtree
            if left > right:
                return None

            # Current root
            root_val = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(root_val)

            # Leaf node
            if left == right:
                return root

            # Next preorder value = left subtree root
            left_root = preorder[preorder_index]

            # Find left subtree boundary
            mid = post_map[left_root]

            # Build left subtree
            root.left = dfs(left, mid)

            # Build right subtree
            root.right = dfs(mid + 1, right - 1)

            return root

        return dfs(0, len(postorder) - 1)
```

---

# Why this works

---

## Preorder gives

```text id="7jlwm6"
Current subtree root first
```

---

## Next preorder value gives

```text id="4jlwm7"
Left subtree root
```

---

## Postorder gives

```text id="9jlwm8"
Where left subtree ends
```

Which determines subtree size.

---

# Important Interview Insight

This reconstruction is possible because:

```text id="2jlwm9"
Values are unique
```

Otherwise subtree boundaries become ambiguous.

---

# Complexity

## Time

```text id="6jlwm0"
O(n)
```

Each node processed once.

---

## Space

```text id="0jlwm1"
O(n)
```

For:

* hashmap
* recursion stack

---

# 8. Step-by-Step Trace

Input:

```python id="3jlwm2"
preorder  = [1,2,4,5,3,6,7]
postorder = [4,5,2,6,7,3,1]
```

---

# Step 1

Root:

```text id="7jlwm3"
1
```

Next preorder value:

```text id="1jlwm4"
2
```

Find in postorder:

```text id="5jlwm5"
[4,5,2,6,7,3,1]
       ↑
```

Left subtree size:

```text id="8jlwm6"
3 nodes
```

---

# Step 2 — Left subtree

Build from:

```text id="2jlwm7"
preorder  = [2,4,5]
postorder = [4,5,2]
```

Root = `2`

---

# Step 3 — Right subtree

Build from:

```text id="6jlwm8"
preorder  = [3,6,7]
postorder = [6,7,3]
```

Root = `3`

---

# Final Tree

```text id="9jlwm9"
        1
      /   \
     2     3
    / \   / \
   4  5  6   7
```

---

# 9. Related Problems

### 1. Construct Binary Tree from Preorder and Inorder Traversal

Easier tree reconstruction using inorder splitting.

---

### 2. Construct Binary Tree from Inorder and Postorder Traversal

Similar recursive reconstruction pattern.

---

### 3. Serialize and Deserialize Binary Tree

Advanced tree reconstruction and encoding.

---

### 4. Binary Tree Preorder Traversal

Needed for understanding root-first traversal.

---

### 5. Binary Tree Postorder Traversal

Needed for understanding subtree-end traversal.
