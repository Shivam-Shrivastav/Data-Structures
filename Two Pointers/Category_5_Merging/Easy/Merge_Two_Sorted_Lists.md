# Merge Two Sorted Lists (LeetCode 21)

**Pattern:** Two Pointers + Linked List Manipulation

---

# 1. Problem Statement

You are given the heads of two **sorted linked lists** `list1` and `list2`.

Merge the two lists into **one sorted linked list** by **splicing together the existing nodes** (do not create new values).

Return the head of the merged linked list.

### Constraints

* Number of nodes in both lists: `0 <= n <= 100`
* `-100 <= Node.val <= 100`
* Both linked lists are sorted in non-decreasing order.

---

# 2. Diagram

Example:

```text
list1: 1 → 2 → 4
        ↑

list2: 1 → 3 → 4
        ↑

Dummy

D

Compare 1 and 1

Take list2 (or list1, either works)

D → 1

Compare

1 → 2 → 4
↑

3 → 4
↑

Take 1

D → 1 → 1

Continue...
```

Final

```text
Dummy
  |
  v

1 → 1 → 2 → 3 → 4 → 4
```

---

# 3. Example I/O

### Example 1

**Input**

```text
list1 = [1,2,4]

list2 = [1,3,4]
```

**Output**

```text
[1,1,2,3,4,4]
```

---

### Example 2

**Input**

```text
list1 = []

list2 = []
```

**Output**

```text
[]
```

---

### Example 3 (Edge Case)

**Input**

```text
list1 = []

list2 = [0]
```

**Output**

```text
[0]
```

---

# 4. Intuition & Pattern Recognition

### Signals

Whenever you see

* Two sorted sequences
* Merge while maintaining sorted order
* Linked Lists

Think

> **Two Pointers**

Unlike arrays, linked lists don't require shifting.

Just reconnect pointers.

### Why use a Dummy Node?

Without a dummy node:

```text
First node is special.

Need extra if statements.
```

With a dummy node:

```text
Every node is handled exactly the same.

No special cases.
```

### Interview Thinking

```text
Both lists are sorted.

Compare current nodes.

Attach the smaller node.

Move that pointer.

Continue until one list finishes.

Attach the remaining list.
```

---

# 5. Simpler Version

## Simpler Question 1

### Merge Sorted Array (LeetCode 88)

```text
Merge two sorted arrays.
```

Difference:

Arrays require backward merging because overwriting is an issue.

---

## Simpler Question 2

### Reverse Linked List (LeetCode 206)

Introduces pointer manipulation.

```text
Current

Next

Reconnect pointers
```

---

## Current Question

Need both ideas

```text
Two pointers

+

Pointer manipulation

=

Merge Two Sorted Lists
```

---

### Thinking Progression

```text
Merge arrays

↓

Learn linked list pointers

↓

Compare two nodes

↓

Reconnect pointers

↓

Merge Two Sorted Lists
```

---

# 6. Brute Force

Store all values.

Sort them.

Create a brand-new linked list.

```python
values = []

Traverse list1
Traverse list2

Sort(values)

Create new list
```

### Complexity

```text
Time : O((m+n) log(m+n))

Space : O(m+n)
```

---

# 7. Optimal Solution (Dummy Node + Two Pointers)

### Idea

Maintain

```text
dummy

tail

list1

list2
```

Always attach the smaller node to `tail`.

Move `tail` and the corresponding list pointer.

Finally attach the remaining nodes.

### Python

```python
class Solution:
    def mergeTwoLists(self, list1, list2):

        dummy = ListNode(-1)
        tail = dummy

        # Compare nodes from both lists
        while list1 and list2:

            if list1.val <= list2.val:
                tail.next = list1      # Attach node from list1
                list1 = list1.next
            else:
                tail.next = list2      # Attach node from list2
                list2 = list2.next

            tail = tail.next           # Move tail forward

        # Attach remaining nodes
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next
```

### Complexity

```text
Time  : O(m+n)

Space : O(1)
```

---

## Recursive Solution

```python
class Solution:
    def mergeTwoLists(self, list1, list2):

        if not list1:
            return list2

        if not list2:
            return list1

        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
```

### Complexity

```text
Time  : O(m+n)

Space : O(m+n)    # recursion stack
```

---

# 8. Step-by-Step Trace

Example

```text
list1 = 1 → 2 → 4

list2 = 1 → 3 → 4
```

| list1 | list2 | Smaller          | Result      |
| ----- | ----- | ---------------- | ----------- |
| 1     | 1     | 1 (list1)        | 1           |
| 2     | 1     | 1 (list2)        | 1→1         |
| 2     | 3     | 2                | 1→1→2       |
| 4     | 3     | 3                | 1→1→2→3     |
| 4     | 4     | 4 (list1)        | 1→1→2→3→4   |
| None  | 4     | Append remaining | 1→1→2→3→4→4 |

Final

```text
1 → 1 → 2 → 3 → 4 → 4
```

---

# 9. Related Problems

| Problem                                    | Connection                                                                                               |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| **206. Reverse Linked List**               | Fundamental pointer manipulation in linked lists.                                                        |
| **83. Remove Duplicates from Sorted List** | Traversing and modifying a sorted linked list.                                                           |
| **86. Partition List**                     | Uses dummy nodes to split and reconnect lists.                                                           |
| **148. Sort List**                         | Uses Merge Sort, where merging two sorted linked lists is the core operation.                            |
| **23. Merge k Sorted Lists**               | Generalizes this problem by merging multiple sorted linked lists using a min-heap or divide-and-conquer. |

---

# Key Interview Takeaways

* **Pattern:** Two Pointers + Linked List Manipulation.
* **Key Trick:** Use a **dummy node** to eliminate special cases for the head node.
* **Pointers:** `list1`, `list2`, and `tail`.
* **Rule:** Compare the current nodes, attach the smaller one to `tail`, and move both `tail` and the corresponding list pointer.
* **After the loop:** Attach the remaining nodes directly, since they are already sorted.
* **Complexity:** **O(m+n)** time and **O(1)** extra space (iterative solution).
