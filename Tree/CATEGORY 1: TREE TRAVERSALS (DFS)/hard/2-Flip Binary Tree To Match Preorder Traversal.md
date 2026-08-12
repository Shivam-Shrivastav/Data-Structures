# Flip Binary Tree To Match Preorder Traversal

LeetCode: Flip Binary Tree To Match Preorder Traversal

---

# 1. Problem Statement with Example

You are given:

* the `root` of a binary tree
* an array `voyage`

You may flip any node in the tree.

A **flip** means:

```text id="jlwm1f"
swap left and right child
```

Return a list of nodes where flips happened so that the tree’s preorder traversal matches `voyage`.

If impossible:

```python id="jlwm2f"
return [-1]
```

---

# Important

Preorder traversal means:

```text id="jlwm3f"
Root → Left → Right
```

---

# Example

Input:

```text id="jlwm4f"
Tree:
      1
     / \
    2   3

voyage = [1,3,2]
```

---

Without flip:

```text id="jlwm5f"
1 → 2 → 3
```

Does NOT match.

---

Flip node `1`:

```text id="jlwm6f"
      1
     / \
    3   2
```

Now preorder:

```text id="jlwm7f"
1 → 3 → 2
```

Matches voyage.

Output:

```python id="jlwm8f"
[1]
```

---

# Constraints

* `1 <= n <= 100`
* Values are unique

---

# 2. Diagram

# Original Tree

```text id="jlwm9f"
        1
       / \
      2   3
```

Desired preorder:

```text id="jlwm0g"
[1,3,2]
```

---

# Problem

Normal preorder gives:

```text id="jlwm1g"
1 → 2 → 3
```

Mismatch at second value.

---

# Flip at Node 1

```text id="jlwm2g"
        1
       / \
      3   2
```

Now preorder:

```text id="jlwm3g"
1 → 3 → 2
```

Correct.

---

# Key Observation

At every node:

```text id="jlwm4g"
If left child doesn't match next preorder value,
we must flip.
```

This is THE interview insight.

---

# 3. Example I/O

## Example 1 (Needs Flip)

Input:

```text id="jlwm5g"
root = [1,2,3]
voyage = [1,3,2]
```

Output:

```python id="jlwm6g"
[1]
```

---

## Example 2 (Impossible)

Input:

```text id="jlwm7g"
root = [1,2]
voyage = [2,1]
```

Output:

```python id="jlwm8g"
[-1]
```

Why?

```text id="jlwm9g"
Root must always come first in preorder.
```

Impossible to change that.

---

## Example 3 (No Flip Needed)

Input:

```text id="jlwm0h"
root = [1,2,3]
voyage = [1,2,3]
```

Output:

```python id="jlwm1h"
[]
```

---

# 4. Intuition & Pattern Recognition

This is a **DFS simulation + greedy flipping** problem.

---

# Core Observation

Preorder traversal order is fixed:

```text id="jlwm2h"
Root → Left → Right
```

We simulate traversal while matching voyage.

---

# Important Greedy Insight

Suppose current node is:

```text id="jlwm3h"
    1
   / \
  2   3
```

Next expected voyage value is:

```text id="jlwm4h"
3
```

But preorder naturally goes left first (`2`).

So only way to fix:

```text id="jlwm5h"
Flip current node.
```

---

# Key Interview Recognition

Whenever problem says:

* modify traversal order
* reorder children
* match DFS sequence

Think:

* DFS simulation
* greedy local decisions

---

# Important Pattern

At node:

```text id="jlwm6h"
If left child != next expected value
→ flip immediately
```

Because preorder MUST visit next child now.

No future correction possible.

---

# 5. Simpler Version

---

# Simplest Version

```text id="jlwm7h"
    1
   / \
  2   3
```

Desired preorder:

```text id="jlwm8h"
[1,2,3]
```

No flip needed.

---

# Slightly Harder

Desired preorder:

```text id="jlwm9h"
[1,3,2]
```

Now:

* next expected = `3`
* left child = `2`

Mismatch → flip.

---

# Related Simpler Problems

### 1. Binary Tree Preorder Traversal

LeetCode: Binary Tree Preorder Traversal

Critical because whole problem is preorder simulation.

---

### 2. Same Tree

LeetCode: Same Tree

Recursive tree matching pattern.

---

### 3. Recover Binary Search Tree

LeetCode: Recover Binary Search Tree

Another tree correction problem.

---

# Thinking Progression

```text id="jlwm0i"
Simulate preorder traversal
        ↓
Compare with voyage
        ↓
Mismatch?
        ↓
Try flipping
```

---

# 6. Brute Force

## Idea

At every node:

* try without flipping
* try with flipping

Backtracking all possibilities.

---

# Why bad?

Each node has:

* flip
* no flip

Total possibilities:

```text id="jlwm1i"
O(2^n)
```

Too expensive.

---

# 7. Optimal Solution

# Greedy DFS

Key idea:

```text id="jlwm2i"
Flip ONLY when necessary.
```

---

# Optimal Code

```python id="jlwm3i"
class Solution:

    def flipMatchVoyage(self, root, voyage):

        self.index = 0
        result = []

        def dfs(node):

            if not node:
                return True

            # Current node must match voyage
            if node.val != voyage[self.index]:
                return False

            self.index += 1

            # Need flip?
            if (
                node.left and
                self.index < len(voyage) and
                node.left.val != voyage[self.index]
            ):

                # Record flip
                result.append(node.val)

                # Traverse flipped order
                return (
                    dfs(node.right)
                    and
                    dfs(node.left)
                )

            # Normal preorder
            return (
                dfs(node.left)
                and
                dfs(node.right)
            )

        if dfs(root):
            return result

        return [-1]
```

---

# Why This Works

---

# Core Greedy Logic

Suppose:

```text id="jlwm4i"
current node = 1
next expected = 3
left child = 2
```

Preorder must immediately visit next child.

Only way to visit `3` first:

```text id="jlwm5i"
flip current node
```

So greedy choice is forced.

---

# Important Interview Insight

This condition:

```python id="jlwm6i"
node.left.val != voyage[index]
```

means:

```text id="jlwm7i"
natural preorder order won't work
```

Thus flip is mandatory.

---

# Complexity

## Time

```text id="jlwm8i"
O(n)
```

Each node visited once.

---

## Space

```text id="jlwm9i"
O(h)
```

Recursion stack.

Worst case skewed tree:

* `O(n)`

---

# 8. Step-by-Step Trace

Input:

```text id="jlwm0j"
Tree:
      1
     / \
    2   3

voyage = [1,3,2]
```

---

# Step 1

Current node:

```text id="jlwm1j"
1
```

Matches voyage[0].

Next expected:

```text id="jlwm2j"
3
```

---

# Step 2

Left child:

```text id="jlwm3j"
2
```

Mismatch.

So flip node `1`.

Result:

```python id="jlwm4j"
[1]
```

Traversal order becomes:

* right subtree first
* left subtree second

---

# Step 3

Visit:

```text id="jlwm5j"
3
```

Matches.

Then:

```text id="jlwm6j"
2
```

Matches.

---

# Final Answer

```python id="jlwm7j"
[1]
```

---

# 9. Related Problems

### 1. Binary Tree Preorder Traversal

Core preorder DFS understanding.

---

### 2. Recover Binary Search Tree

Tree correction/modification problem.

---

### 3. Same Tree

Recursive tree matching pattern.

---

### 4. Invert Binary Tree

Tree child swapping manipulation.

---

### 5. Construct Binary Tree from Preorder and Inorder Traversal

Advanced preorder traversal reasoning.
