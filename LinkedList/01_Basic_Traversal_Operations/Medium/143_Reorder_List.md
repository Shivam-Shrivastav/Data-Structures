# 143. Reorder List

**Pattern:** Fast & Slow Pointer + Reverse Linked List

---

# 1. Problem Statement with Example

Given the head of a singly linked list:

```text id="bqj2om"
L0 → L1 → L2 → ... → Ln
```

Reorder it into:

```text id="vt5zw8"
L0 → Ln → L1 → Ln-1 → L2 → Ln-2 ...
```

You must:

* reorder **in-place**
* not modify node values
* only change pointers

---

## Example

Input:

```text id="77q0nh"
1 -> 2 -> 3 -> 4
```

Output:

```text id="lbmxzw"
1 -> 4 -> 2 -> 3
```

---

## Constraints

* Number of nodes: `[1, 5 * 10^4]`
* Node values: `[1, 1000]`

Large input size means:

* avoid extra array if possible
* prefer `O(1)` space

---

# 2. Diagram

## Original

```text id="zgjxw7"
1 -> 2 -> 3 -> 4 -> 5
```

---

## Step 1: Find Middle

```text id="t8q5vx"
1 -> 2 -> 3 -> 4 -> 5
          ↑
        middle
```

---

## Step 2: Reverse Second Half

```text id="1n2j7m"
First half:   1 -> 2 -> 3
Second half:  5 -> 4
```

---

## Step 3: Merge Alternately

```text id="hkj64d"
1 -> 5 -> 2 -> 4 -> 3
```

---

# 3. Example I/O

## Example 1 (Typical)

Input:

```text id="jlwmx9"
[1,2,3,4,5]
```

Output:

```text id="56n7rq"
[1,5,2,4,3]
```

Explanation:

Take:

* first node
* last node
* second node
* second last node

---

## Example 2 (Even Length)

Input:

```text id="h61s3f"
[1,2,3,4]
```

Output:

```text id="jvjjyc"
[1,4,2,3]
```

---

# 4. Intuition & Pattern Recognition

## Key Signal

Whenever you see:

```text id="m4vwur"
front + back + front + back
```

or

```text id="s9mxiy"
L0, Ln, L1, Ln-1
```

Think:

### Split the list into halves.

Then:

1. reverse one half
2. merge alternately

---

# Why Reverse?

We can easily traverse:

```text id="01xmh2"
1 -> 2 -> 3
```

But cannot easily access:

```text id="l6ebcx"
last -> second last
```

in singly linked list.

So:

* reverse second half
* now both halves move forward normally

---

# 5. Simpler Version

---

# Simpler Question 1

### Middle of the Linked List

Find middle using fast & slow pointers.

### Core Idea

```python id="pmu2a4"
slow = slow.next
fast = fast.next.next
```

---

# Simpler Question 2

### Reverse Linked List

Reverse second half.

---

# Simpler Question 3

### Merge Two Sorted Lists

Merge two linked lists alternately.

---

# Simpler Thinking → Full Problem

This problem is basically:

```text id="nuxjlwm"
Find middle
+
Reverse second half
+
Merge alternately
```

---

# Mental Interview Shortcut

If problem says:

```text id="brrfj7"
first node, last node, second node, second last
```

Think immediately:

```text id="p3dt0s"
middle + reverse + merge
```

---

# 6. Brute Force

## Idea

Store nodes in array.

Then use:

* left pointer
* right pointer

Reconnect nodes alternately.

---

## Brute Force Code

```python id="zbmzfj"
class Solution:
    def reorderList(self, head):

        arr = []

        curr = head

        while curr:
            arr.append(curr)
            curr = curr.next

        left = 0
        right = len(arr) - 1

        while left < right:

            arr[left].next = arr[right]
            left += 1

            if left == right:
                break

            arr[right].next = arr[left]
            right -= 1

        arr[left].next = None
```

---

## Complexity

* Time: `O(n)`
* Space: `O(n)`

---

# 7. Optimal Solution

## Core Steps

### 1. Find middle

Use fast & slow pointer.

---

### 2. Reverse second half

Convert:

```text id="3ntr4r"
4 -> 5
```

into:

```text id="3j7ob2"
5 -> 4
```

---

### 3. Merge both halves

Alternate nodes.

---

# Optimal Code (Python)

```python id="e9jth8"
class Solution:
    def reorderList(self, head):

        # Step 1: Find middle
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev = None
        curr = slow.next

        slow.next = None  # Split list

        while curr:

            nxt = curr.next

            curr.next = prev

            prev = curr

            curr = nxt

        # prev = head of reversed second half

        # Step 3: Merge alternately
        first = head
        second = prev

        while second:

            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
```

---

# Why This Works

After reversing:

```text id="x7a1g5"
1 -> 2 -> 3
5 -> 4
```

Both lists move forward naturally.

Now alternate merge becomes easy.

---

# 8. Step-by-Step Trace

Input:

```text id="07b7v8"
1 -> 2 -> 3 -> 4 -> 5
```

---

# Step 1: Find Middle

```text id="0p71y2"
slow = 3
```

Split:

```text id="u6m0of"
First:  1 -> 2 -> 3
Second: 4 -> 5
```

---

# Step 2: Reverse Second Half

```text id="hm4t72"
4 -> 5
```

becomes:

```text id="8cyi1u"
5 -> 4
```

---

# Step 3: Merge

---

## Iteration 1

```text id="p5m45z"
1 -> 5 -> 2 -> 3
```

Remaining:

```text id="7u5b7v"
4
```

---

## Iteration 2

```text id="zzd6lc"
1 -> 5 -> 2 -> 4 -> 3
```

Done.

---

# Final Answer

```text id="j7gwwy"
1 -> 5 -> 2 -> 4 -> 3
```

---

# 9. Related Problems

1. Middle of the Linked List
   Learn fast & slow pointers.

2. Reverse Linked List
   Core reversal logic.

3. Palindrome Linked List
   Same pattern: middle + reverse.

4. Twin Sum of a Linked List
   Uses reversed second half.

5. Reverse Linked List II
   Partial linked list reversal.
