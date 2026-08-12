# **496. Next Greater Element I**

## 1. Problem Statement

You are given two integer arrays `nums1` and `nums2`.

* `nums1` is a subset of `nums2`.
* Every element in both arrays is **unique**.

For each element in `nums1`, find the **first greater element to its right** in `nums2`.

* If such an element exists, return it.
* Otherwise, return `-1`.

Return an array where each answer corresponds to the elements in `nums1`.

### Constraints

* `1 <= nums1.length <= nums2.length <= 1000`
* `0 <= nums1[i], nums2[i] <= 10⁴`
* All elements are **unique**.

---

# 2. Diagram

```text
nums1 = [2,4]
nums2 = [1,2,3,4]

nums2

Index:   0   1   2   3
Value:   1   2   3   4

1 ─────► 2
2 ─────► 3
3 ─────► 4
4 ─────► None

Map:
1 → 2
2 → 3
3 → 4
4 → -1

nums1

2 → 3
4 → -1

Answer = [3,-1]
```

This is a **Next Greater Element** problem.

---

# 3. Example I/O

### Example 1

**Input**

```text
nums1 = [4,1,2]
nums2 = [1,3,4,2]
```

**Output**

```text
[-1,3,-1]
```

Explanation

* 4 → no greater element
* 1 → 3
* 2 → none

---

### Example 2

**Input**

```text
nums1 = [2,4]
nums2 = [1,2,3,4]
```

**Output**

```text
[3,-1]
```

---

### Edge Case

```text
nums1 = [1]
nums2 = [1]

Output:
[-1]
```

---

# 4. Intuition & Pattern Recognition

## Interview Signals

Whenever you see:

* First greater element
* Nearest greater element
* Next greater element
* First larger element on the right

Think immediately:

> **Monotonic Stack**

---

### Why?

If we search to the right for every element,

```text
O(n²)
```

Instead,

we process the array once and maintain useful candidates inside a stack.

---

### Key Observation

Since `nums1` is only a **subset**,

we first compute the next greater element for **every number in `nums2`**.

Store it in a hashmap:

```text
number → nextGreater
```

Then answering each query from `nums1` is just a dictionary lookup.

---

# 5. Simpler Version

## Simplest Problem

Given one array,

find the next greater element for every position.

Example

```text
[2,1,5,3]

Answer

2 → 5
1 → 5
5 → None
3 → None
```

---

## Difference Here

Instead of returning answers for every element,

we only return answers for numbers present in `nums1`.

Thinking becomes

```text
Find Next Greater for nums2
          ↓
Store in HashMap
          ↓
Answer nums1 queries
```

---

## Simpler Problems Leading Here

1. Next Greater Element
2. Daily Temperatures
3. Stock Span
4. Next Greater Element I

Thinking progression

```text
Nearest Greater
       ↓
Monotonic Stack
       ↓
Need answer for entire array
       ↓
Store in HashMap
       ↓
Answer subset queries
```

---

# 6. Brute Force

For every element in `nums1`

* Find its position in `nums2`
* Search to the right until a greater element is found.

### Python

```python
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        ans = []

        for num in nums1:
            idx = nums2.index(num)

            greater = -1
            for j in range(idx + 1, len(nums2)):
                if nums2[j] > num:
                    greater = nums2[j]
                    break

            ans.append(greater)

        return ans
```

### Complexity

Time

```
O(m × n)
```

Space

```
O(1)
```

where

* `m = len(nums1)`
* `n = len(nums2)`

---

# 7. Optimal Solution

## Method 1 (Right → Left)

### Idea

Traverse `nums2` from right to left.

Maintain a **monotonic decreasing stack**.

For every number

* Remove all smaller numbers.
* Stack top becomes the next greater element.
* Store it in a hashmap.
* Push current number.

Finally,

construct answer for `nums1`.

### Python

```python
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        nextGreater = {}

        # Process nums2 from right to left
        for num in reversed(nums2):

            # Remove smaller elements
            while stack and stack[-1] < num:
                stack.pop()

            # Top is the next greater element
            if stack:
                nextGreater[num] = stack[-1]
            else:
                nextGreater[num] = -1

            stack.append(num)

        return [nextGreater[num] for num in nums1]
```

### Complexity

Time

```
O(n + m)
```

Space

```
O(n)
```

---

# Method 2 (Left → Right) ⭐ (Very Intuitive)

Instead of finding the answer for the current element,

the **current element becomes the answer** for previous smaller elements.

Maintain a **monotonic decreasing stack**.

When a larger element arrives,

everyone smaller on the stack gets resolved.

### Python

```python
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        nextGreater = {}

        for num in nums2:

            # Current number is next greater
            while stack and stack[-1] < num:
                prev = stack.pop()
                nextGreater[prev] = num

            stack.append(num)

        # Remaining elements have no next greater
        while stack:
            nextGreater[stack.pop()] = -1

        return [nextGreater[num] for num in nums1]
```

### Why this works

Suppose

```text
nums2 = [2,1,5]
```

When **5** arrives,

it immediately becomes the next greater element for

```text
1
2
```

So we pop them and store

```text
1 → 5
2 → 5
```

This approach feels very natural because the current number answers previous unresolved elements.

---

# 8. Step-by-Step Trace (Left → Right)

Example

```text
nums2 = [1,2,3,4]
```

| Current | Stack Before | Action    | Map                | Stack After |
| ------- | ------------ | --------- | ------------------ | ----------- |
| 1       | []           | Push      | {}                 | [1]         |
| 2       | [1]          | 1<2 → 1→2 | {1:2}              | [2]         |
| 3       | [2]          | 2<3 → 2→3 | {1:2,2:3}          | [3]         |
| 4       | [3]          | 3<4 → 3→4 | {1:2,2:3,3:4}      | [4]         |
| End     | [4]          | 4→-1      | {1:2,2:3,3:4,4:-1} | []          |

Now

```text
nums1 = [2,4]

2 → 3
4 → -1

Answer = [3,-1]
```

---

# 9. Related Problems

1. **739. Daily Temperatures**
   Uses the next greater element pattern but returns the distance instead of the value.

2. **1475. Final Prices With a Special Discount in a Shop**
   Same idea, but searches for the next **smaller or equal** element.

3. **503. Next Greater Element II**
   Extends the problem to a circular array.

4. **84. Largest Rectangle in Histogram**
   Uses previous and next smaller elements to compute rectangle widths.

5. **907. Sum of Subarray Minimums**
   Advanced monotonic stack problem using previous and next smaller elements.

---

# Pattern Summary (Interview Revision)

| Problem Clue                   | Pattern                         |
| ------------------------------ | ------------------------------- |
| First greater element on right | Monotonic Decreasing Stack      |
| First smaller element on right | Monotonic Increasing Stack      |
| Nearest greater/smaller        | Monotonic Stack                 |
| `nums1` is a subset of `nums2` | Precompute on `nums2` + HashMap |

## Recognition Shortcut

> **"Find the first greater element to the right."**
>
> * **Right → Left:** Pop smaller elements; the stack top is the next greater element.
> * **Left → Right:** Keep unresolved elements in a **monotonic decreasing stack**. When a larger element arrives, it becomes the answer for all smaller elements waiting on the stack.
>
> **For interview speed, the left-to-right approach is often the easiest to visualize and explain.**
