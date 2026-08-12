# 237. Delete Node in a Linked List

## 1. Problem Statement with Example

You are given **only a node** in a singly linked list, and you must delete it.

You are **not given the head** of the linked list.

The node:

* is guaranteed **not to be the last node**
* exists inside the list
* all node values are unique

You must modify the linked list so that:

* the given node’s value disappears
* list size decreases by 1
* relative order of remaining nodes stays same

### Example

Input list:

```text
4 → 5 → 1 → 9
```

Given node:

```text
5
```

After deletion:

```text
4 → 1 → 9
```

---

## 2. Diagram

We cannot access the previous node.

Normal deletion:

```text
prev.next = node.next
```

But here:

```text
❌ No access to prev
```

So instead:

```text
Before:
4 → [5] → [1] → 9

Step 1:
Copy next node value into current node

4 → [1] → [1] → 9

Step 2:
Skip next node

4 → [1] ─────→ 9
```

Effectively, original `5` disappears.

---

## 3. Example I/O

### Example 1

Input:

```text
head = [4,5,1,9]
node = 5
```

Output:

```text
[4,1,9]
```

Explanation:

* Copy `1` into node `5`
* Remove original `1`

---

### Example 2 (Edge Case)

Input:

```text
head = [1,2]
node = 1
```

Output:

```text
[2]
```

Explanation:

* Replace `1` with `2`
* Remove original `2`

---

## 4. Intuition & Pattern Recognition

### Key observation

Normally in linked list deletion, we need:

* access to previous node

Because:

```python
prev.next = curr.next
```

But this problem intentionally removes access to:

* `head`
* `prev`

So ask yourself:

> “Can I make this node look like the next node?”

YES.

### Trick

Instead of deleting current node:

* copy next node’s value into current node
* bypass next node

This works because:

* values are unique
* node is not the last node

### Interview Recognition Signal

If a linked list question:

* gives only node reference
* no head
* asks deletion

Immediately think:

> “Overwrite current node using next node.”

This is a classic linked list trick problem.

---

## 5. Simpler Version

### Simplest Version

Delete node when head is available.

Example:

```python
prev.next = curr.next
```

Easy because we can access previous node.

---

### Related Simpler Problems

#### 1. Reverse Linked List

Cracking the Coding Interview style linked list basics.

Teaches:

* pointer manipulation
* changing next references

---

#### 2. Remove Linked List Elements

Delete nodes using:

```python
prev.next = curr.next
```

Difference:

* there we have head access
* here we don’t

---

### Thinking Progression

Normal deletion:

```text
Need previous node
```

This problem:

```text
No previous node available
```

So:

```text
Transform current node into next node
```

That is the core insight.

---

## 6. Brute Force

### Idea

Impossible in true brute force form because:

* singly linked list
* no head access
* cannot move backward to find previous node

Without modifying constraints:

```text
No valid traditional deletion possible
```

So this problem is actually testing whether you know the trick.

---

## 7. Optimal Solution

### Approach

1. Copy next node value into current node
2. Skip next node

---

### Python Code

```python
class Solution:
    def deleteNode(self, node):
        # Copy next node's value
        node.val = node.next.val

        # Skip next node
        node.next = node.next.next
```

---

### Why it works

Suppose:

```text
5 → 1 → 9
```

After copying:

```text
1 → 1 → 9
```

After skipping:

```text
1 → 9
```

Original `5` effectively removed.

---

### Complexity

| Complexity | Value |
| ---------- | ----- |
| Time       | O(1)  |
| Space      | O(1)  |

---

## 8. Step-by-Step Trace

Input:

```text
4 → 5 → 1 → 9
```

Given:

```text
node = 5
```

---

### Initial State

| Current Node | Next Node |
| ------------ | --------- |
| 5            | 1         |

List:

```text
4 → 5 → 1 → 9
```

---

### Step 1: Copy next value

```python
node.val = node.next.val
```

Now:

| Current Node | Next Node |
| ------------ | --------- |
| 1            | 1         |

List becomes:

```text
4 → 1 → 1 → 9
```

---

### Step 2: Skip next node

```python
node.next = node.next.next
```

List:

```text
4 → 1 → 9
```

Done.

---

## 9. Related Problems

### 1. Reverse Linked List

Core linked list pointer manipulation.

---

### 2. Remove Linked List Elements

Classic deletion using previous pointer.

---

### 3. Remove Duplicates from Sorted List

Deletion while traversing linked list.

---

### 4. Copy List with Random Pointer

Advanced node-copy manipulation problem.

---

### 5. Reverse Linked List II

More complex pointer rewiring within sublists.
