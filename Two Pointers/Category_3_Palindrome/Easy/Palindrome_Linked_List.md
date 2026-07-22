# Palindrome Linked List (LeetCode 234)

## 1. Problem Statement

Given the head of a singly linked list, return `true` if it is a palindrome, otherwise return `false`.

A linked list is a palindrome if it reads the same forwards and backwards.

### Constraints

* Number of nodes: `1 <= n <= 10^5`
* `0 <= Node.val <= 9`
* **Follow-up:** Can you solve it in **O(n)** time and **O(1)** extra space?

---

# 2. Diagram

Example:

```text
Input:

1 → 2 → 3 → 2 → 1
↑                 ↑
Start            End

Step 1: Find Middle

1 → 2 → 3 → 2 → 1
        ↑
      Slow

Step 2: Reverse Second Half

1 → 2 → 3 ← 2 ← 1
        ↑
      Reverse

Becomes

First Half:
1 → 2 → 3

Second Half:
1 → 2

Step 3: Compare

1 == 1 ✓
2 == 2 ✓

Palindrome
```

---

# 3. Example I/O

### Example 1

**Input**

```text
head = [1,2,2,1]
```

**Output**

```text
true
```

Explanation

```text
Forward : 1 2 2 1
Backward: 1 2 2 1
```

---

### Example 2

**Input**

```text
head = [1,2]
```

**Output**

```text
false
```

Explanation

```text
1 != 2
```

---

### Example 3 (Odd Length)

**Input**

```text
head = [1,2,3,2,1]
```

**Output**

```text
true
```

Middle node doesn't affect palindrome property.

---

# 4. Intuition & Pattern Recognition

### Signals

Whenever you see

* Linked List
* Compare first half with second half
* O(1) extra space

Think:

> **Fast & Slow Pointer + Reverse Linked List**

### Why?

Unlike arrays, linked lists don't allow random access.

So we:

1. Find the middle.
2. Reverse the second half.
3. Compare both halves.

### Interview Thinking

Tell yourself:

```text
I cannot move backward.

So I'll reverse the second half.

Now both halves move forward.

Compare node by node.

If every value matches,
it's a palindrome.
```

---

# 5. Simpler Version

## Simpler Question 1

### Valid Palindrome (String)

Use two pointers from both ends.

```text
racecar

L       R

Compare inward.
```

Easy because strings support random access.

---

## Simpler Question 2

### Reverse Linked List

Learn how to reverse a linked list in O(N).

```text
1 → 2 → 3

↓

3 → 2 → 1
```

---

## Simpler Question 3

### Middle of the Linked List

Use fast and slow pointers.

```text
Fast → 2 steps

Slow → 1 step

Slow reaches middle.
```

---

## Current Question

Combine both ideas:

```text
Find Middle

↓

Reverse Second Half

↓

Compare

↓

(Optional) Restore List
```

---

### Thinking Progression

```text
String Palindrome

↓

Middle of Linked List

↓

Reverse Linked List

↓

Compare Both Halves

↓

Palindrome Linked List
```

---

# 6. Brute Force

Copy linked list values into an array.

Then use two pointers.

### Python

```python
class Solution:
    def isPalindrome(self, head):

        arr = []

        while head:
            arr.append(head.val)
            head = head.next

        left = 0
        right = len(arr) - 1

        while left < right:
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1

        return True
```

### Complexity

```text
Time : O(N)

Space: O(N)
```

---

# 7. Optimal Solution (Fast & Slow + Reverse)

### Idea

1. Find middle using slow/fast pointers.
2. Reverse second half.
3. Compare first and second halves.
4. (Optional) Restore original list.

### Python

```python
class Solution:
    def isPalindrome(self, head):

        # Find middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Compare halves
        first = head
        second = prev

        while second:
            if first.val != second.val:
                return False

            first = first.next
            second = second.next

        return True
```

### Complexity

```text
Time  : O(N)

Space : O(1)
```

---

# 8. Step-by-Step Trace

Example

```text
head = [1,2,3,2,1]
```

### Step 1: Find Middle

| Slow | Fast    |
| ---- | ------- |
| 1    | 1       |
| 2    | 3       |
| 3    | 1 (end) |

Middle = **3**

---

### Step 2: Reverse Second Half

Original

```text
3 → 2 → 1
```

Reverse

```text
1 → 2 → 3
```

---

### Step 3: Compare

| First Half | Second Half | Match |
| ---------- | ----------- | ----- |
| 1          | 1           | ✓     |
| 2          | 2           | ✓     |
| 3          | 3           | ✓     |

All matched.

Return

```text
True
```

---

# 9. Related Problems

| Problem                            | Connection                                      |
| ---------------------------------- | ----------------------------------------------- |
| **206. Reverse Linked List**       | Reverse the second half before comparison.      |
| **876. Middle of the Linked List** | Find the midpoint using fast and slow pointers. |
| **141. Linked List Cycle**         | Uses the same fast & slow pointer technique.    |
| **143. Reorder List**              | Find middle, reverse second half, and merge.    |
| **25. Reverse Nodes in k-Group**   | Advanced linked list reversal problem.          |

---

# Key Interview Takeaways

* **Pattern:** Fast & Slow Pointer + Reverse Linked List.
* **Invariant:** First half remains unchanged while the second half is reversed.
* **Rule:** Find the middle → reverse the second half → compare both halves.
* **Optimization:** Avoid copying values into an array to achieve **O(1)** extra space.
* **Complexity:** **O(N)** time and **O(1)** extra space.
