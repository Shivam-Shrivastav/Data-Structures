# 92. Reverse Linked List II

**Pattern:** Linked List Pointer Manipulation

---

# 1. Problem Statement with Example

Given the head of a singly linked list and two integers `left` and `right` where `1 <= left <= right <= n`, reverse the nodes of the list from position `left` to position `right`, and return the modified list.

You must reverse **only that portion** while keeping the rest of the list unchanged.

### Example

Input:
`1 -> 2 -> 3 -> 4 -> 5`
`left = 2, right = 4`

Output:
`1 -> 4 -> 3 -> 2 -> 5`

Because only nodes from positions 2 to 4 are reversed.

### Constraints

* Number of nodes: `[1, 500]`
* `-500 <= Node.val <= 500`
* `1 <= left <= right <= n`

---

# 2. Diagram

### Before

```text
dummy -> 1 -> 2 -> 3 -> 4 -> 5
           ↑         ↑
         left=2    right=4
```

### Reverse only middle part

```text
dummy -> 1 -> 4 -> 3 -> 2 -> 5
```

---

# 3. Example I/O

## Example 1 (Typical)

Input:

```text
head = [1,2,3,4,5]
left = 2
right = 4
```

Output:

```text
[1,4,3,2,5]
```

Explanation:

Reverse sublist:

```text
2 -> 3 -> 4
```

Becomes:

```text
4 -> 3 -> 2
```

---

## Example 2 (Edge Case)

Input:

```text
head = [5]
left = 1
right = 1
```

Output:

```text
[5]
```

Explanation:
Only one node, nothing changes.

---

# 4. Intuition & Pattern Recognition

### Signals for Linked List Reversal Pattern

* Problem says:

  * “reverse linked list”
  * “between positions”
  * “in-place”
* This usually means:

  * pointer rewiring
  * local reversal
  * reconnecting edges carefully

### Key Observation

Normal reverse linked list reverses the whole list.

Here:

* reverse only a section
* keep:

  * left part intact
  * right part intact

So we need:

1. Reach node before `left`
2. Reverse sublist
3. Reconnect both ends

---

# 5. Simpler Version

## Simpler Question

### Reverse Linked List

Reverse the **entire** linked list.

### Core Idea There

```text
curr.next = prev
```

Repeatedly reverse pointers.

---

# How It Evolves Into This Problem

In this problem:

* same reversal logic
* but only inside a window `[left, right]`

So think:

```text
Reverse Linked List
+
Keep track of boundaries
+
Reconnect edges
```

---

# Simpler Thinking → Full Problem Thinking

## Step 1

Reverse whole list:

```text
1 -> 2 -> 3
```

becomes:

```text
3 -> 2 -> 1
```

---

## Step 2

What if we reverse only:

```text
2 -> 3 -> 4
```

inside:

```text
1 -> 2 -> 3 -> 4 -> 5
```

Need to preserve:

```text
1
and
5
```

---

## Step 3

Store:

* node before sublist
* first node of sublist
* node after sublist

Reconnect after reversal.

---

# Related Easier Problems

1. Reverse Linked List
   Learn basic reversal.

2. Reverse Nodes in k-Group
   Reverse chunks repeatedly.

3. Swap Nodes in Pairs
   Local pointer rewiring.

---

# 6. Brute Force

## Idea

* Copy linked list values into array
* Reverse subarray
* Rebuild values into linked list

---

## Brute Force Code (Python)

```python
class Solution:
    def reverseBetween(self, head, left, right):
        arr = []

        curr = head

        while curr:
            arr.append(curr.val)
            curr = curr.next

        arr[left - 1:right] = reversed(arr[left - 1:right])

        curr = head
        i = 0

        while curr:
            curr.val = arr[i]
            i += 1
            curr = curr.next

        return head
```

---

## Complexity

* Time: `O(n)`
* Space: `O(n)`

---

# 7. Optimal Solution

## Core Idea

Use in-place reversal.

### Steps

1. Create dummy node
2. Reach node before `left`
3. Reverse nodes until `right`
4. Reconnect

---

## Optimal Code (Python)

```python
class Solution:
    def reverseBetween(self, head, left, right):

        # Edge case
        if not head or left == right:
            return head

        # Dummy helps when left = 1
        dummy = ListNode(0)
        dummy.next = head

        # Move prev to node before left
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        # Start reversing
        curr = prev.next

        # Reverse nodes one by one
        for _ in range(right - left):

            temp = curr.next              # Node to move

            curr.next = temp.next         # Remove temp

            temp.next = prev.next         # Insert temp at front

            prev.next = temp              # Connect front

        return dummy.next
```

---

# Why This Works

We repeatedly take next node and insert it at the front of sublist.

### Visualization

Start:

```text
1 -> 2 -> 3 -> 4 -> 5
```

After moving 3:

```text
1 -> 3 -> 2 -> 4 -> 5
```

After moving 4:

```text
1 -> 4 -> 3 -> 2 -> 5
```

---

## Complexity

* Time: `O(n)`
* Space: `O(1)`

---

# 8. Step-by-Step Trace

Input:

```text
1 -> 2 -> 3 -> 4 -> 5
left = 2
right = 4
```

---

## Initial

```text
dummy -> 1 -> 2 -> 3 -> 4 -> 5
prev = 1
curr = 2
```

---

## Iteration 1

### temp = 3

Remove 3:

```text
1 -> 2 -> 4 -> 5
```

Insert 3 after prev:

```text
1 -> 3 -> 2 -> 4 -> 5
```

---

## Iteration 2

### temp = 4

Remove 4:

```text
1 -> 3 -> 2 -> 5
```

Insert 4 after prev:

```text
1 -> 4 -> 3 -> 2 -> 5
```

---

## Final Answer

```text
1 -> 4 -> 3 -> 2 -> 5
```

---

# 9. Related Problems

1. Reverse Linked List
   Basic full linked list reversal.

2. Reverse Nodes in k-Group
   Reverse list in fixed-size groups.

3. Swap Nodes in Pairs
   Pairwise local reversals.

4. Rotate List
   Another pointer-rewiring linked list problem.

5. Palindrome Linked List
   Uses linked list reversal as subroutine.
