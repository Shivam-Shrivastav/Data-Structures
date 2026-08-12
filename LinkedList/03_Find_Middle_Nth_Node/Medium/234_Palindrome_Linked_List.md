
# 234 Palindrome Linked List

## 1. Problem Statement with Example
Check if linked list is palindrome.

Typical constraint signals:
- List size can be up to 10^5
- O(n^2) is usually too slow
- Pointer manipulation is the main focus

---a# Palindrome Linked List

LeetCode 234 — Determine whether a singly linked list is a palindrome.

---

# 1. Problem Statement with Example

Given the head of a singly linked list, return `true` if the linked list is a palindrome, otherwise return `false`.

A palindrome reads the same forward and backward.

### Example

```text
Input: 1 -> 2 -> 2 -> 1
Output: true
```

Because reading from left-to-right and right-to-left gives the same sequence.

### Constraints

* Number of nodes: `1 <= n <= 10^5`
* Node values usually in range `0-9` or integer values
* Must ideally solve in:

  * `O(n)` time
  * `O(1)` extra space

---

# 2. Diagram

## Main Idea

Find middle → reverse second half → compare both halves.

```text
Original:
1 -> 2 -> 3 -> 2 -> 1

Step 1: Find middle
slow stops at 3

1 -> 2 -> 3 -> 2 -> 1
          ^
        slow

Step 2: Reverse second half

First Half:
1 -> 2 -> 3

Second Half Reversed:
1 -> 2

Step 3: Compare

1 == 1
2 == 2

Palindrome ✓
```

---

# 3. Example I/O

## Example 1 (Typical)

```text
Input:
1 -> 2 -> 2 -> 1

Output:
true
```

Explanation:

Forward = `[1,2,2,1]`
Backward = `[1,2,2,1]`

Same sequence.

---

## Example 2 (Not Palindrome)

```text
Input:
1 -> 2

Output:
false
```

Explanation:

Forward = `[1,2]`
Backward = `[2,1]`

Different.

---

## Example 3 (Edge Case)

```text
Input:
1

Output:
true
```

Single node is always palindrome.

---

# 4. Intuition & Pattern Recognition

## Signals for This Pattern

When problem asks:

* Compare front and back of linked list
* Check symmetry
* Need `O(1)` extra space
* Cannot access backward directly

Think:

> "Use slow-fast pointer to split + reverse linked list."

---

## Interview Thought Process

### Arrays are easy

In array:

```python
arr[left] == arr[right]
```

But linked list cannot move backward.

So:

1. Find middle
2. Reverse second half
3. Compare node-by-node

This simulates two pointers.

---

## Why It Works

After reversing second half:

```text
1 -> 2 -> 3 -> 2 -> 1

becomes

First:
1 -> 2 -> 3

Second reversed:
1 -> 2
```

Now both halves move forward together.

---

# 5. Simpler Version

## Simplest Version

### Question

"Check if an array is palindrome."

```python
left = 0
right = n-1

while left < right:
    if arr[left] != arr[right]:
        return False
```

---

## Linked List Difficulty

Problem:

* No random access
* No backward movement

So we convert linked list into a structure where comparison becomes possible.

---

# Simpler Problems That Build This

---

## 1. Reverse Linked List

### Learn:

How to reverse pointers.

Core idea used directly here.

---

## 2. Middle of the Linked List

### Learn:

Slow-fast pointer technique.

Needed to split list.

---

## 3. Linked List Cycle

### Learn:

Fast and slow movement pattern.

Builds pointer intuition.

---

## Thinking Progression

```text
Array palindrome
    ↓
Need backward traversal
    ↓
Reverse part of linked list
    ↓
Need midpoint first
    ↓
Use slow-fast pointers
    ↓
Compare both halves
```

---

# 6. Brute Force

## Idea

Copy linked list values into array.

Then use two pointers.

---

## Code

```python
class Solution:
    def isPalindrome(self, head):
        arr = []

        curr = head

        while curr:
            arr.append(curr.val)
            curr = curr.next

        left = 0
        right = len(arr) - 1

        while left < right:
            if arr[left] != arr[right]:
                return False

            left += 1
            right -= 1

        return True
```

---

## Complexity

### Time

O(n)

### Space

O(n)

(extra array)

---

# 7. Optimal Solution

## Idea

1. Find middle
2. Reverse second half
3. Compare both halves

---

## Code (Interview-Friendly)

```python
class Solution:
    def isPalindrome(self, head):

        # Step 1: Find middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # prev becomes head of reversed half
        second = prev
        first = head

        # Step 3: Compare both halves
        while second:
            if first.val != second.val:
                return False

            first = first.next
            second = second.next

        return True
```

---

# Complexity

### Time

O(n)

### Space

O(1)

---

# 8. Step-by-Step Trace

## Input

```text
1 -> 2 -> 2 -> 1
```

---

## Step 1: Find Middle

| Iteration | slow | fast |
| --------- | ---- | ---- |
| Start     | 1    | 1    |
| 1         | 2    | 2    |
| 2         | 2    | null |

Middle = second `2`

---

## Step 2: Reverse Second Half

Starting from:

```text
2 -> 1
```

### Iteration 1

```text
prev = 2
curr = 1
```

Reversed:

```text
2
```

---

### Iteration 2

```text
prev = 1 -> 2
curr = null
```

Final reversed half:

```text
1 -> 2
```

---

## Step 3: Compare

| First Half | Second Half |
| ---------- | ----------- |
| 1          | 1           |
| 2          | 2           |

All matched.

Return `true`.

---

# 9. Related Problems

## Easy → Medium Progression

### 1. Reverse Linked List

Pure reversal problem. Fundamental building block.

---

### 2. Middle of the Linked List

Learn slow-fast pointer midpoint detection.

---

### 3. Reorder List

Also uses:

* midpoint
* reverse second half
* merge

Very closely related.

---

### 4. Reverse Linked List II

Practice reversing only a portion of list.

---

### 5. Twin Sum of a Linked List

Uses exact same pattern:

* find middle
* reverse half
* compare/combine values

Very important follow-up problem.


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

