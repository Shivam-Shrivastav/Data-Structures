# Count Good Nodes in Binary Tree

LeetCode: Count Good Nodes in Binary Tree

---

# 1. Problem Statement with Example

Given a binary tree root, a node `X` is called **Good** if:

```text id="nn5o56"
No node on the path from root to X
has a value greater than X
```

In other words:

```text id="ed5z96"
X >= maximum value seen from root to X
```

Return the number of good nodes.

---

## Example

```text id="qjqg7k"
        3
       / \
      1   4
     /   / \
    3   1   5
```

Good nodes are:

```text id="o5ab8s"
3 (root)
3 (left leaf)
4
5
```

Answer = `4`

---

## Constraints

* Nodes up to `10^5`
* Need linear traversal
* Tree DFS is natural
* We need information from ancestors

---

# 2. Diagram

```text id="n3o9rf"
Path tracking:

        3
       / \
      1   4
     /     \
    3       5

For each node:
carry MAX value seen so far

Example:

root -> 3
maxSoFar = 3

3 -> 1
maxSoFar = 3

1 -> 3
3 >= 3  => GOOD
```

Core DFS state:

```text id="ew7bf9"
(node, maxSoFar)
```

---

# 3. Example I/O

## Example 1

### Input

```text id="kk17hf"
root = [3,1,4,3,null,1,5]
```

### Output

```text id="l64uyr"
4
```

### Why?

Good nodes:

```text id="1wqfnp"
3, 3, 4, 5
```

---

## Example 2

### Input

```text id="jlwmg2"
root = [2,2,2]
```

### Output

```text id="whg9k9"
3
```

### Why?

Equal values are allowed.

Every node satisfies:

```text id="d6p02v"
node.val >= maxSoFar
```

---

## Example 3 (Edge Case)

### Input

```text id="0ls4xu"
root = [1]
```

### Output

```text id="7h99dm"
1
```

Root is always good.

---

# 4. Intuition & Pattern Recognition

This is a classic:

```text id="m38lrz"
Tree DFS + Carry Information From Parent
```

---

## Key observation

To decide whether current node is good:

We only need:

```text id="6m7mp4"
maximum value seen from root till parent
```

Then:

```text id="h7nlhj"
if node.val >= maxSoFar
=> good node
```

Update:

```text id="8t3c0k"
newMax = max(maxSoFar, node.val)
```

and continue DFS.

---

## Interview Pattern Recognition

Whenever problem says:

```text id="y3tcfy"
"on path from root"
"ancestor information"
"path condition"
```

Think:

```text id="7k4evr"
DFS carrying state downward
```

Typical DFS state:

```text id="trix8m"
(node, state_from_parent)
```

---

# 5. Simpler Version

---

## Simplest Version

### Question

Count nodes greater than root.

Easy traversal.

---

## Upgrade

Now compare with ALL ancestors.

Naively:

```text id="1ynf3x"
For every node:
walk upward to root
find maximum
```

That becomes inefficient.

---

## Optimization Insight

While already traversing downward:

just carry:

```text id="up56n4"
maximum seen so far
```

So instead of recomputing ancestor max repeatedly:

```text id="iq3pyc"
reuse parent computation
```

---

# Simpler Related Problems

### 1. Maximum Depth of Binary Tree

Basic DFS traversal.

---

### 2. Path Sum

Carry state from parent (`remainingSum`).

---

### 3. Binary Tree Paths

Carry path information during DFS.

---

### Transition to this problem

```text id="gvbyi5"
Path Sum:
carry remaining target

Good Nodes:
carry maximum seen so far
```

Same DFS pattern.

---

# 6. Brute Force

## Idea

For every node:

* walk upward to root
* find maximum ancestor value
* compare

---

## Complexity

If tree is skewed:

```text id="3td4l5"
For each node:
O(N) upward traversal

Total = O(N²)
```

Space:

```text id="0f9yza"
O(H)
```

---

# 7. Optimal Solution

## Core Idea

During DFS:

Maintain:

```text id="s3jlwm"
maxSoFar
```

At each node:

```text id="ddgv6j"
if node.val >= maxSoFar
=> count++
```

Then update max and continue.

---

# Clean Interview Code (Java)

```java id="4xv7r3"
class Solution {

    int count = 0;

    public int goodNodes(TreeNode root) {

        dfs(root, root.val);

        return count;
    }

    private void dfs(TreeNode node, int maxSoFar) {

        if (node == null) {
            return;
        }

        // current node is good
        if (node.val >= maxSoFar) {
            count++;
        }

        // update maximum for children
        int newMax = Math.max(maxSoFar, node.val);

        dfs(node.left, newMax);
        dfs(node.right, newMax);
    }
}
```

---

# Complexity

```text id="a9ssnq"
Time:  O(N)
Space: O(H)
```

* Every node visited once
* H = tree height

---

# 8. Step-by-Step Trace

Tree:

```text id="s70zj7"
        3
       / \
      1   4
     /   / \
    3   1   5
```

---

## DFS Trace

| Node | maxSoFar Before | Good? | newMax | Count |
| ---- | --------------- | ----- | ------ | ----- |
| 3    | 3               | YES   | 3      | 1     |
| 1    | 3               | NO    | 3      | 1     |
| 3    | 3               | YES   | 3      | 2     |
| 4    | 3               | YES   | 4      | 3     |
| 1    | 4               | NO    | 4      | 3     |
| 5    | 4               | YES   | 5      | 4     |

Final Answer:

```text id="12dl3l"
4
```

---

# 9. Related Problems

### 1. Path Sum

Carry cumulative information downward.

---

### 2. Binary Tree Paths

DFS with path state.

---

### 3. Binary Tree Longest Consecutive Sequence

Parent-child condition tracking.

---

### 4. Longest ZigZag Path in a Binary Tree

DFS carrying traversal state.

---

### 5. Diameter of Binary Tree

Classic recursive tree DP/DFS thinking.
