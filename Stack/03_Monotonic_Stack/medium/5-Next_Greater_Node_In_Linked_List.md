# **1019. Next Greater Node In Linked List**

## 1. Problem Statement

You are given the head of a singly linked list.

For every node, find the **value of the first node to its right** whose value is **strictly greater** than the current node's value.

* If no such node exists, return `0`.

Return an integer array where `answer[i]` is the next greater value for the `i`-th node (0-indexed).

### Constraints

* Number of nodes: `1 <= n <= 10⁴`
* `1 <= Node.val <= 10⁹`

The important phrase is:

> **Next Greater Element on the Right (Linked List Version)**

---

# 2. Diagram

Example

```text
Linked List

2 → 1 → 5

Index:   0   1   2
Value:   2   1   5

2 ─────────► 5
1 ───► 5
5 ───► None

Answer

[5,5,0]
```

Since linked lists don't support random access, we first convert them into an array.

---

# 3. Example I/O

### Example 1

**Input**

```text
head = [2,1,5]
```

**Output**

```text
[5,5,0]
```

---

### Example 2

**Input**

```text
head = [2,7,4,3,5]
```

**Output**

```text
[7,0,5,5,0]
```

Explanation

```text
2 → 7
7 → None
4 → 5
3 → 5
5 → None
```

---

### Edge Case

```text
head = [10]

Output

[0]
```

---

# 4. Intuition & Pattern Recognition

## Interview Signals

Whenever you see

* Next greater node
* First greater node to the right
* Linked list version of Next Greater Element

Think

> **Convert to Array + Monotonic Stack**

---

### Why convert to an array?

A linked list cannot move backward or access arbitrary indices efficiently.

Monotonic stack algorithms often need:

* right-to-left traversal **or**
* index-based updates.

Converting to an array makes both easy.

---

### Key Observation

After conversion,

```text
2 → 7 → 4 → 3 → 5

becomes

[2,7,4,3,5]
```

Now it is exactly the same as

> **496. Next Greater Element I**

---

# 5. Simpler Version

## Simplest Problem

Next Greater Element

```text
[2,1,5]

2 → 5
1 → 5
5 → None
```

---

## Difference Here

Instead of receiving an array,

we receive

```text
Linked List
```

So thinking becomes

```text
Linked List
      ↓
Convert to Array
      ↓
Next Greater Element
      ↓
Return answers
```

---

## Simpler Problems Leading Here

1. Next Greater Element I
2. Next Greater Element II
3. Daily Temperatures
4. Next Greater Node In Linked List

Thinking progression

```text
Need Next Greater
        ↓
Monotonic Stack
        ↓
Input is Linked List
        ↓
Convert to Array
        ↓
Apply Same Algorithm
```

---

# 6. Brute Force

Convert to an array.

For every element,

search to the right until a larger value is found.

### Python

```python
class Solution:
    def nextLargerNodes(self, head):
        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        n = len(nums)
        ans = [0] * n

        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    ans[i] = nums[j]
                    break

        return ans
```

### Complexity

Time

```text
O(n²)
```

Space

```text
O(n)
```

---

# 7. Optimal Solution

## Method 1 (Right → Left)

### Idea

1. Convert linked list to an array.
2. Traverse from right to left.
3. Maintain a **monotonic decreasing stack**.
4. Remove all smaller or equal elements.
5. Stack top becomes the next greater value.

### Python

```python
class Solution:
    def nextLargerNodes(self, head):
        nums = []

        # Convert linked list to array
        while head:
            nums.append(head.val)
            head = head.next

        n = len(nums)
        ans = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):

            # Remove smaller/equal values
            while stack and stack[-1] <= nums[i]:
                stack.pop()

            if stack:
                ans[i] = stack[-1]

            stack.append(nums[i])

        return ans
```

### Complexity

Time

```text
O(n)
```

Space

```text
O(n)
```

---

## Method 2 (Left → Right) ⭐ (Most Interview Friendly)

Instead of finding the answer for the current node,

the **current node becomes the answer** for previous smaller nodes.

Maintain a **monotonic decreasing stack of indices**.

Whenever a larger value arrives,

resolve everyone waiting on the stack.

### Python

```python
class Solution:
    def nextLargerNodes(self, head):
        nums = []

        # Convert linked list to array
        while head:
            nums.append(head.val)
            head = head.next

        ans = [0] * len(nums)
        stack = []          # stores indices

        for i, val in enumerate(nums):

            # Current value is next greater
            while stack and nums[stack[-1]] < val:
                idx = stack.pop()
                ans[idx] = val

            stack.append(i)

        return ans
```

### Why store indices?

Because we need to fill the answer for **previous nodes** once their next greater value is found.

---

# 8. Step-by-Step Trace (Left → Right)

Example

```text
Linked List

2 → 7 → 4 → 3 → 5

Converted Array

[2,7,4,3,5]
```

| Index | Value | Stack (Indices) | Action                           | Answer      |
| ----- | ----- | --------------- | -------------------------------- | ----------- |
| 0     | 2     | []              | Push 0                           | [0,0,0,0,0] |
| 1     | 7     | [0]             | 7>2 → ans[0]=7                   | [7,0,0,0,0] |
|       |       |                 | Push 1                           |             |
| 2     | 4     | [1]             | Push 2                           |             |
| 3     | 3     | [1,2]           | Push 3                           |             |
| 4     | 5     | [1,2,3]         | 5>3 → ans[3]=5<br>5>4 → ans[2]=5 | [7,0,5,5,0] |

Final Answer

```text
[7,0,5,5,0]
```

---

# 9. Related Problems

1. **496. Next Greater Element I**
   The classic next greater element problem on arrays.

2. **503. Next Greater Element II**
   Extends the next greater element problem to a circular array.

3. **739. Daily Temperatures**
   Finds the next warmer day and returns the distance instead of the value.

4. **901. Online Stock Span**
   Uses a monotonic stack to find spans based on previous greater elements.

5. **1944. Number of Visible People in a Queue**
   Another monotonic stack problem involving visibility to the right.

---

# Pattern Summary (Interview Revision)

| Problem Clue                   | Pattern                      |
| ------------------------------ | ---------------------------- |
| Next greater node              | Monotonic Decreasing Stack   |
| Linked list input              | Convert to array first       |
| First greater on the right     | Next Greater Element         |
| Need answer for previous nodes | Store indices (left → right) |

## Recognition Shortcut

> **"Find the next greater node in a linked list."**
>
> Think:
>
> 1. Convert the linked list into an **array**.
> 2. This becomes a standard **Next Greater Element** problem.
> 3. Use a **Monotonic Decreasing Stack**.
> 4. The **left-to-right approach with indices** is often the most intuitive: whenever a larger value arrives, it resolves all previous smaller nodes waiting on the stack.

---

# Comparison with Other Monotonic Stack Problems

| Problem                                    | Looking For             | Direction        | Stack Stores                         | Output             |
| ------------------------------------------ | ----------------------- | ---------------- | ------------------------------------ | ------------------ |
| **496. Next Greater Element I**            | Next Greater            | Right            | Values                               | Next greater value |
| **503. Next Greater Element II**           | Next Greater (Circular) | Right (2 passes) | Indices                              | Next greater value |
| **739. Daily Temperatures**                | Next Warmer             | Right            | Indices                              | Distance           |
| **1475. Final Prices**                     | Next Smaller or Equal   | Right            | Values/Indices                       | Discounted price   |
| **901. Online Stock Span**                 | Previous Greater        | Left             | (Price, Span)                        | Span               |
| **1019. Next Greater Node in Linked List** | Next Greater            | Right            | **Indices (after array conversion)** | Next greater value |

### Memory Trick

* **Array problems** → Apply the monotonic stack directly.
* **Linked list + Next Greater** → **Convert to an array first**, then use the exact same Next Greater Element algorithm.
