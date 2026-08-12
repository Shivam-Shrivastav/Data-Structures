# 19. Remove Nth Node From End of List

## 1. Problem Statement with Example

Given the head of a linked list, remove the `n`th node from the **end** of the list and return the head.

---

## Example

```text
Input:
1 → 2 → 3 → 4 → 5
n = 2
```

Remove the 2nd node from end:

```text
5 (1st from end)
4 (2nd from end)
```

Result:

```text
1 → 2 → 3 → 5
```

---

## Constraints

```text
1 <= sz <= 30
1 <= Node.val <= 100
1 <= n <= sz
```

Important:

* Must handle deleting:

  * head node
  * middle node
  * tail node
* Follow-up expects one-pass solution.

---

# 2. Diagram

## Core Idea — Two Pointer Gap

```text
dummy → 1 → 2 → 3 → 4 → 5
          s
                  f
```

Maintain:

```text
gap between fast and slow = n
```

When fast reaches end:

* slow reaches node BEFORE target.

---

## Final Removal

```text
Before:
3 → 4 → 5

After:
3 ─────→ 5
```

---

# 3. Example I/O

## Example 1

### Input

```text
head = [1,2,3,4,5]
n = 2
```

### Output

```text
[1,2,3,5]
```

---

## Example 2

### Input

```text
head = [1]
n = 1
```

### Output

```text
[]
```

Deleting only node.

---

## Example 3

### Input

```text
head = [1,2]
n = 1
```

### Output

```text
[1]
```

Deleting tail.

---

# 4. Intuition & Pattern Recognition

## Biggest Clue

Whenever problem says:

* nth from end
* kth from end
* single traversal
* linked list distance

→ Think:

# Two Pointers with Fixed Gap

---

## Core Insight

If fast pointer is `n` nodes ahead:

```text
fast ---- n gap ---- slow
```

Then when:

* fast reaches end

slow automatically reaches:

* node before target

---

## Why Dummy Node?

Without dummy:

Deleting head becomes annoying.

Example:

```text
[1]
n = 1
```

Need uniform handling.

Dummy simplifies all edge cases.

---

## Interview Recognition Trick

If question says:

```text
"from end"
```

Immediately think:

```text
Use two pointers with distance gap
```

---

# 5. Simpler Version

## Simplest Problem

### Remove kth node from beginning

Easy:

* traverse directly

---

## Next Harder

### Find kth node from end

Can:

1. compute length
2. go to `(length-k)`th node

---

## Final Optimization

Can we avoid two passes?

Yes:

* maintain pointer gap.

---

## Related Simpler Problems

### 1. Middle of Linked List

Fast/slow traversal intuition.

---

### 2. Linked List Cycle

Two-pointer synchronization.

---

### 3. Find kth Node From End

Direct precursor problem.

---

## Thinking Progression

```text
Need nth from end
       ↓
Can compute length
       ↓
Need one pass
       ↓
Maintain gap of n
```

---

# 6. Brute Force

# Two Pass Solution

---

## Idea

### Pass 1

Find length.

### Pass 2

Go to:

```text
(length - n)
```

position.

Remove node.

---

## Code

```python
class Solution:

    def removeNthFromEnd(self, head, n):

        length = 0
        curr = head

        # calculate length
        while curr:
            length += 1
            curr = curr.next

        dummy = ListNode(0)
        dummy.next = head

        curr = dummy

        # move before target node
        for _ in range(length - n):
            curr = curr.next

        # delete node
        curr.next = curr.next.next

        return dummy.next
```

---

## Complexity

### Time

O(n)

### Space

O(1)

---

# 7. Optimal Solution

# One Pass — Two Pointer Gap

---

## Core Idea

1. Move `fast` ahead by `n`
2. Move both together
3. When fast reaches end:

   * slow is before target

---

## Diagram

```text
dummy → 1 → 2 → 3 → 4 → 5
  s                 f
```

Gap maintained.

---

## Code

```python
class Solution:

    def removeNthFromEnd(self, head, n):

        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # create gap of n+1
        for _ in range(n + 1):
            fast = fast.next

        # move together
        while fast:

            slow = slow.next
            fast = fast.next

        # remove target node
        slow.next = slow.next.next

        return dummy.next
```

---

## Why `n + 1` Gap?

We want:

```text
slow = node BEFORE deletion target
```

Thus extra one-step separation needed.

---

## Complexity

### Time

O(n)

### Space

O(1)

---

# 8. Step-by-Step Trace

## Example

```text
1 → 2 → 3 → 4 → 5
n = 2
```

---

## Initial

```text
dummy → 1 → 2 → 3 → 4 → 5
s
f
```

---

## Move Fast `n+1 = 3` Steps

```text
dummy → 1 → 2 → 3 → 4 → 5
s               f
```

---

## Move Together

### Step 1

```text
s = 1
f = 4
```

### Step 2

```text
s = 2
f = 5
```

### Step 3

```text
s = 3
f = None
```

Stop.

---

## Delete

```text
slow.next = slow.next.next
```

Becomes:

```text
1 → 2 → 3 → 5
```

---

# 9. Related Problems

## 1. Middle of Linked List

Fast/slow pointer fundamentals.

---

## 2. Linked List Cycle

Pointer synchronization pattern.

---

## 3. Delete Node in Linked List

Basic deletion operation.

---

## 4. Rotate List

Uses length and pointer movement.

---

## 5. Partition List

Advanced linked list manipulation.

---

# Interview One-Liner

> “Maintain a gap of `n` nodes between two pointers so when fast reaches the end, slow reaches the node before the target.”
