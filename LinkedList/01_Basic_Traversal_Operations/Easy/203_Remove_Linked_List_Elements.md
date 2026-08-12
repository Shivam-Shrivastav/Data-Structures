
# 203 Remove Linked List Elements

## 1. Problem Statement with Example
Remove all nodes with a target value.

Typical constraint signals:
- List size can be up to 10^5
- O(n^2) is usually too slow
- Pointer manipulation is the main focus

---
# Remove Linked List Elements

LeetCode #203 — Easy
Pattern: Linked List Traversal, Node Deletion

---

# 1. Problem Statement with Example

Given the head of a linked list and an integer `val`, remove **all nodes** from the linked list that have `Node.val == val`.

Return the new head of the modified linked list.

---

### Constraints

* Number of nodes: `0 <= n <= 10^4`
* `1 <= Node.val <= 50`
* `0 <= val <= 50`

---

### Example

Input:

```text id="6z46r7"
head = 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
val = 6
```

Output:

```text id="2c3n9m"
1 -> 2 -> 3 -> 4 -> 5
```

---

# 2. Diagram

Problem with deleting nodes in linked list:

```text id="1w0x4k"
1 -> 2 -> 6 -> 3
          ^
       remove this
```

To delete:

```python id="c5d4dv"
prev.next = curr.next
```

After deletion:

```text id="5wx1c6"
1 -> 2 ------> 3
```

---

## Why Dummy Node Helps

Edge case:

```text id="7jjqg8"
6 -> 6 -> 1 -> 2
```

Head itself must be removed.

Using dummy:

```text id="x4rjaf"
dummy -> 6 -> 6 -> 1 -> 2
```

Now deletion becomes uniform.

---

# 3. Example I/O

## Example 1 (Typical)

### Input

```text id="pj7b4t"
head = [1,2,6,3,4,5,6]
val = 6
```

### Output

```text id="xvlr26"
[1,2,3,4,5]
```

### Why?

Remove both nodes containing `6`.

---

## Example 2 (Edge Case)

### Input

```text id="p2p4ww"
head = [7,7,7,7]
val = 7
```

### Output

```text id="6p0i1d"
[]
```

### Why?

All nodes are deleted.

---

# 4. Intuition & Pattern Recognition

### Core Observation

To remove a node from linked list:

```python id="wt5g88"
prev.next = curr.next
```

But deleting head is tricky.

---

### Key Pattern

Whenever linked list deletion may involve:

* Head node
* Multiple consecutive deletions

Think:

> “Use a dummy node”

---

### Interview Recognition

Signals:

* “Remove nodes”
* “Return modified head”
* “Head itself may change”

Immediate thought:

```text id="vb6z3m"
dummy node
```

---

# 5. Simpler Version

## Simplest Version

Delete a single node from middle:

```text id="o8rv1v"
1 -> 2 -> 6 -> 3
```

Remove `6`.

Easy because head does not change.

---

## Full Problem Difference

Now:

* Multiple nodes may match
* Head may need deletion
* Consecutive deletions possible

Example:

```text id="71oypo"
6 -> 6 -> 6 -> 2
```

This is why dummy node becomes important.

---

## Simpler related problems

### 1. Delete Node in Linked List

Basic deletion operation.

### 2. Remove Duplicates from Sorted List

Also removes nodes using pointer rewiring.

### 3. Reverse Linked List

Builds pointer confidence.

### 4. Merge Two Sorted Lists

Traversal + pointer manipulation.

---

# 6. Brute Force

## Idea

* Store nodes not equal to `val`
* Create new linked list

---

## Brute Force Code

```python id="jlwm4p"
class Solution:
    def removeElements(self, head, val):

        values = []

        curr = head

        while curr:

            if curr.val != val:
                values.append(curr.val)

            curr = curr.next

        dummy = ListNode(0)
        tail = dummy

        for v in values:
            tail.next = ListNode(v)
            tail = tail.next

        return dummy.next
```

---

## Complexity

### Time

```text id="l6v29r"
O(n)
```

### Space

```text id="p10x7x"
O(n)
```

---

# 7. Optimal Solution

## Key Insight

Use:

* `dummy` before head
* `prev` pointer
* `curr` pointer

If node should be removed:

```python id="otn4wk"
prev.next = curr.next
```

Else:

```python id="crb8by"
prev = curr
```

---

## Optimal Code

```python id="kqjlwm"
class Solution:
    def removeElements(self, head, val):

        # Dummy handles head deletions
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:

            # Remove current node
            if curr.val == val:
                prev.next = curr.next

            else:
                # Move prev only if node kept
                prev = curr

            # Always move curr
            curr = curr.next

        return dummy.next
```

---

## Complexity

### Time

```text id="gxjv0g"
O(n)
```

Each node visited once.

---

### Space

```text id="my5r3f"
O(1)
```

Only pointers used.

---

# 8. Step-by-Step Trace

Input:

```text id="rl6t1e"
1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
val = 6
```

---

| Step | prev  | curr | Action | List          |
| ---- | ----- | ---- | ------ | ------------- |
| 1    | dummy | 1    | keep   | 1→2→6→3→4→5→6 |
| 2    | 1     | 2    | keep   | same          |
| 3    | 2     | 6    | remove | 1→2→3→4→5→6   |
| 4    | 2     | 3    | keep   | same          |
| 5    | 3     | 4    | keep   | same          |
| 6    | 4     | 5    | keep   | same          |
| 7    | 5     | 6    | remove | 1→2→3→4→5     |

---

# 9. Related Problems

### 1. Delete Node in a Linked List

Foundation of node deletion.

### 2. Remove Duplicates from Sorted List

Uses similar pointer skipping.

### 3. Remove Nth Node From End of List

Deletion with two pointers.

### 4. Partition List

Advanced linked list restructuring.

### 5. Reverse Linked List

Core pointer manipulation skill.

## 2. Diagram

```text
1 -> 2 -> 3 -> 4

slow ---->
fast ---------->
```

---

## 3. Example I/O

### Example 1
Input:
```text
head = [1,2,3,4]
```

Output:
```text
[4,3,2,1]
```

Explanation:
Pointers are rearranged in-place.

### Example 2 (Edge Case)
Input:
```text
head = [1]
```

Output:
```text
[1]
```

Explanation:
Single node remains unchanged.

---

## 4. Intuition & Pattern Recognition

Interview signals:
- “Linked list” + “one pass” → think fast/slow pointers
- “Reverse” → iterative pointer manipulation
- “Merge” → dummy node pattern
- “Cycle” → Floyd’s algorithm
- “Nth from end” → gap between pointers

What to say in interview:
> “Since random access is unavailable, I should solve this using pointer traversal rather than indexing.”

---

## 5. Simpler Version

### Simpler Thinking
Start with:
- Traverse a linked list
- Reverse a small part
- Use two pointers
- Build result using dummy node

### Related Easier Problems
- Reverse Linked List
- Middle of Linked List
- Merge Two Sorted Lists

### Transition to This Problem
The full problem adds:
- More pointer conditions
- Boundary handling
- Multiple traversals or partial reversal

---

## 6. Brute Force

### Idea
Convert linked list into array/vector.
Perform operation on array.
Rebuild linked list if needed.

### Complexity
- Time: O(n)
- Space: O(n)

---

## 7. Optimal Solution

```python
class Solution:
    def solve(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next      # store next node
            curr.next = prev     # reverse pointer
            prev = curr          # move prev
            curr = nxt           # move current

        return prev
```

### Complexity
- Time: O(n)
- Space: O(1)

Why optimal?
- Single traversal
- In-place pointer manipulation
- Constant extra memory

---

## 8. Step-by-Step Trace

| Step | curr | prev | Remaining |
|---|---|---|---|
| 1 | 1 | None | 2->3->4 |
| 2 | 2 | 1 | 3->4 |
| 3 | 3 | 2->1 | 4 |
| 4 | 4 | 3->2->1 | None |

Final:
```text
4 -> 3 -> 2 -> 1
```

---

## 9. Related Problems

1. Reverse Linked List — base reversal pattern.
2. Reverse Linked List II — reverse subrange.
3. Reverse Nodes in k-Group — grouped reversal.
4. Reorder List — combine middle + reverse.
5. Merge k Sorted Lists — advanced merge pattern.

