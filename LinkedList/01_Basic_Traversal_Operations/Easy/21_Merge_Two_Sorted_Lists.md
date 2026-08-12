# Merge Two Sorted Lists

LeetCode #21 — Easy
Pattern: Linked List, Two Pointers

---

# 1. Problem Statement with Example

You are given the heads of two sorted singly linked lists `list1` and `list2`.

Merge them into **one sorted linked list** by splicing together the nodes of the original lists.

Return the head of the merged linked list.

### Constraints

* Number of nodes in both lists: `0 <= n <= 100`
* `-100 <= Node.val <= 100`
* Both lists are sorted in non-decreasing order.

---

### Example

Input:

```text
list1 = 1 -> 2 -> 4
list2 = 1 -> 3 -> 4
```

Output:

```text
1 -> 1 -> 2 -> 3 -> 4 -> 4
```

---

# 2. Diagram

```text
list1: 1 -> 2 -> 4
         ^
list2: 1 -> 3 -> 4
         ^

Compare current nodes:
1 vs 1

Take smaller/equal one into result.

dummy -> 1
          ^
Move pointer in list1

Now:
list1: 2 -> 4
         ^
list2: 1 -> 3 -> 4
         ^

Again compare...
```

Final merged chain:

```text
dummy -> 1 -> 1 -> 2 -> 3 -> 4 -> 4
```

---

# 3. Example I/O

## Example 1 (Typical)

### Input

```text
list1 = [1,2,4]
list2 = [1,3,4]
```

### Output

```text
[1,1,2,3,4,4]
```

### Why?

At every step, choose the smaller node from the two current heads.

---

## Example 2 (Edge Case)

### Input

```text
list1 = []
list2 = [0]
```

### Output

```text
[0]
```

### Why?

If one list is empty, return the other list directly.

---

# 4. Intuition & Pattern Recognition

This is a classic **two pointers on linked lists** problem.

### Signals that hint this pattern

* Two sorted structures
* Need merged sorted output
* Sequential traversal only
* Linked list (cannot use indexing)

### Core idea

Since both lists are already sorted:

* Compare current nodes
* Smaller node definitely belongs next in merged list
* Move that pointer forward

This is identical to the **merge step of Merge Sort**.

### Interview recognition sentence

> “Whenever I see two sorted lists/arrays and need combined sorted output, I immediately think of two pointers.”

---

# 5. Simpler Version

## Simplest Version

Merge two sorted arrays.

Example:

```text
[1,2,4]
[1,3,4]
```

Use two indices:

* Compare elements
* Push smaller one

---

## How it evolves into linked list version

### Array Version

```python
if arr1[i] < arr2[j]:
    result.append(arr1[i])
```

### Linked List Version

Instead of appending values:

* Connect actual nodes

```python
tail.next = list1
list1 = list1.next
```

---

## Related simpler problems

### 1. Merge Sorted Array

Same exact idea with arrays.

### 2. Remove Duplicates from Sorted List

Uses traversal on sorted linked list.

### 3. Reverse Linked List

Basic pointer manipulation foundation.

### 4. Middle of Linked List

Builds comfort with linked list pointer movement.

---

# 6. Brute Force

## Idea

* Copy all nodes into an array
* Sort the array
* Create a new linked list

---

## Brute Force Code

```python
class Solution:
    def mergeTwoLists(self, list1, list2):
        values = []

        while list1:
            values.append(list1.val)
            list1 = list1.next

        while list2:
            values.append(list2.val)
            list2 = list2.next

        values.sort()

        dummy = ListNode(0)
        curr = dummy

        for val in values:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next
```

---

## Complexity

### Time

```text
O((n+m) log(n+m))
```

### Space

```text
O(n+m)
```

---

# 7. Optimal Solution

## Key Insight

No need to create new nodes or sort again.

Since lists are already sorted:

* Reuse existing nodes
* Build answer while traversing once

---

## Optimal Code (Iterative)

```python
class Solution:
    def mergeTwoLists(self, list1, list2):

        # Dummy node helps simplify edge cases
        dummy = ListNode(0)

        # Tail points to last node of merged list
        tail = dummy

        # Traverse both lists
        while list1 and list2:

            # Pick smaller node
            if list1.val <= list2.val:

                tail.next = list1
                list1 = list1.next

            else:
                tail.next = list2
                list2 = list2.next

            # Move tail forward
            tail = tail.next

        # Attach remaining nodes
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next
```

---

## Complexity

### Time

```text
O(n + m)
```

Each node visited once.

---

### Space

```text
O(1)
```

Only pointers used.

---

# 8. Step-by-Step Trace

Input:

```text
list1 = 1 -> 2 -> 4
list2 = 1 -> 3 -> 4
```

---

| Step | list1 | list2 | Chosen      | Result                     |
| ---- | ----- | ----- | ----------- | -------------------------- |
| 1    | 1     | 1     | 1(list1)    | 1                          |
| 2    | 2     | 1     | 1(list2)    | 1 -> 1                     |
| 3    | 2     | 3     | 2           | 1 -> 1 -> 2                |
| 4    | 4     | 3     | 3           | 1 -> 1 -> 2 -> 3           |
| 5    | 4     | 4     | 4(list1)    | 1 -> 1 -> 2 -> 3 -> 4      |
| End  | None  | 4     | attach rest | 1 -> 1 -> 2 -> 3 -> 4 -> 4 |

---

# 9. Related Problems

### 1. Merge Sorted Array

Array version of same two-pointer merge logic.

### 2. Sort List

Uses merge sort + merge-two-lists internally.

### 3. Merge k Sorted Lists

Extension of this problem to multiple lists.

### 4. Intersection of Two Linked Lists

Another pointer movement linked list problem.

### 5. Reorder List

Advanced pointer manipulation with linked lists.
