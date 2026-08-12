# 108. Convert Sorted Array to Binary Search Tree

## 1. Problem Statement with Example

Given an integer array `nums` sorted in **ascending order**, convert it into a **height-balanced Binary Search Tree (BST)**.

A height-balanced BST means:

> For every node, the height difference between left and right subtree is at most 1.

---

## BST Property

```text id="rw3cv0"
Left subtree values  < root
Right subtree values > root
```

---

## Constraints

* `1 <= nums.length <= 10^4`
* `-10^4 <= nums[i] <= 10^4`
* `nums` is strictly increasing.

---

## Example

### Input

```text id="7k04kh"
nums = [-10,-3,0,5,9]
```

### One Valid Output

```text id="lmrb7w"
        0
       / \
     -10   5
       \    \
       -3    9
```

Another valid balanced BST is also acceptable.

---

# 2. Diagram

## Key Idea

Always choose the **middle element** as root.

Why?

Because:

* left side elements become left subtree
* right side elements become right subtree
* tree stays balanced

---

## Example

```text id="e7klg3"
nums = [-10,-3,0,5,9]
```

---

### Step 1 — Pick Middle

```text id="zly59o"
          0
```

Left:

```text id="o6kjr2"
[-10,-3]
```

Right:

```text id="dhvif4"
[5,9]
```

---

### Step 2 — Recurse

```text id="5uwlgu"
          0
        /   \
      -10     5
         \      \
         -3      9
```

Balanced BST formed.

---

# 3. Example I/O

## Example 1

### Input

```text id="k04e2w"
nums = [-10,-3,0,5,9]
```

### Output

```text id="87l14e"
[0,-3,9,-10,null,5]
```

or any other balanced BST.

---

## Example 2

### Input

```text id="xrr8f9"
nums = [1,3]
```

### Output

```text id="a4m4mf"
[3,1]
```

or

```text id="7wd7mx"
[1,null,3]
```

Both are balanced.

---

## Edge Case

### Input

```text id="s2x5nv"
nums = [1]
```

### Output

```text id="dk3cnh"
[1]
```

---

# 4. Intuition & Pattern Recognition

This problem combines:

* Sorted Array
* BST
* Balanced Tree

---

## Critical Observation

### Inorder Traversal of BST = Sorted Order

If array is already sorted:

```text id="c09s4d"
left elements < middle < right elements
```

This perfectly matches BST rules.

---

## Main Trick

To keep tree balanced:

> Always choose the middle element as root.

Because middle divides array nearly equally.

---

## Interview Recognition Signal

Whenever you see:

```text id="49tytc"
sorted array
+
balanced BST
```

Immediately think:

> Binary Search style recursion using middle element.

---

## Why This Works

Middle element:

* becomes current root
* left half naturally smaller
* right half naturally larger

So:

* BST property maintained
* balanced height maintained

---

# 5. Simpler Version

## Simplest Problem

### Binary Search

In binary search:

```text id="3kq25s"
mid = (left + right) // 2
```

You divide array into halves repeatedly.

---

## This Problem = Binary Search + Tree Construction

Instead of searching:

* create node at midpoint
* recurse left
* recurse right

---

## Thinking Evolution

### Step 1

Pick middle as root.

---

### Step 2

Left half becomes left subtree.

---

### Step 3

Right half becomes right subtree.

---

### Step 4

Repeat recursively.

---

## Related Simpler Problems

### 1. Binary Search

Same midpoint splitting idea.

### 2. Maximum Depth of Binary Tree

Basic tree recursion.

### 3. Convert Sorted List to BST

Harder because linked list lacks random access.

### 4. Validate BST

Understanding BST properties.

### 5. Balanced Binary Tree

Understanding balanced structures.

---

# 6. Brute Force

## Naive Idea

You could:

1. Insert elements one-by-one into BST.
2. Since array is sorted, BST becomes skewed.

Example:

```text id="d9ldlc"
1
 \
  2
   \
    3
```

---

## Complexity

### Time

```text id="5u50eo"
O(N^2)
```

Worst case skewed insertions.

### Space

```text id="wtm26k"
O(N)
```

---

# 7. Optimal Solution

## Core Idea

Use divide-and-conquer recursion:

* midpoint → root
* left half → left subtree
* right half → right subtree

---

## Python Code

```python id="8s4sg4"
class Solution:
    def sortedArrayToBST(self, nums):

        def build(left, right):

            # No elements left
            if left > right:
                return None

            # Middle element
            mid = (left + right) // 2

            # Create root node
            root = TreeNode(nums[mid])

            # Build left subtree
            root.left = build(left, mid - 1)

            # Build right subtree
            root.right = build(mid + 1, right)

            return root

        return build(0, len(nums) - 1)
```

---

## Complexity

### Time

```text id="g2i4jw"
O(N)
```

Each element used once.

---

### Space

```text id="mrj7z4"
O(log N)
```

Balanced recursion stack.

---

# 8. Step-by-Step Trace

Example:

```text id="onr6xj"
nums = [-10,-3,0,5,9]
```

---

## Step 1

```text id="i52czd"
left = 0
right = 4

mid = 2
nums[mid] = 0
```

Tree:

```text id="m7x3x2"
      0
```

---

## Step 2 — Left Subtree

```text id="h8j53n"
left = 0
right = 1

mid = 0
nums[mid] = -10
```

Tree:

```text id="mh3t4o"
       0
      /
    -10
```

---

## Step 3

Right child of `-10`

```text id="suljlwm"
mid = 1
nums[mid] = -3
```

Tree:

```text id="9e0eyg"
        0
       /
    -10
       \
       -3
```

---

## Step 4 — Right Subtree

```text id="xj75b7"
left = 3
right = 4

mid = 3
nums[mid] = 5
```

Tree:

```text id="t75dbd"
        0
       / \
    -10   5
       \
       -3
```

---

## Step 5

```text id="0qtm9q"
mid = 4
nums[mid] = 9
```

Final Tree:

```text id="c7ql5d"
        0
       / \
    -10    5
       \     \
       -3     9
```

---

# 9. Related Problems

### 1. Convert Sorted List to Binary Search Tree

Same idea but linked list access makes it harder.

### 2. Validate Binary Search Tree

Check BST ordering rules.

### 3. Balance a Binary Search Tree

Rebuild BST into balanced form.

### 4. Binary Search

Core midpoint recursion pattern.

### 5. Construct Binary Tree from Preorder and Inorder Traversal

Recursive tree construction from array segments.
