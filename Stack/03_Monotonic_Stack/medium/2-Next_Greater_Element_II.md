# **503. Next Greater Element II**

## 1. Problem Statement

You are given a **circular integer array** `nums`.

For every element, find the **first greater element to its right**.

* Since the array is **circular**, after reaching the last element, continue searching from the beginning.
* If no greater element exists, return `-1`.

Return an array containing the next greater element for every index.

### Constraints

* `1 <= nums.length <= 10⁴`
* `-10⁹ <= nums[i] <= 10⁹`

The important part is:

> **Next Greater Element + Circular Array**

---

# 2. Diagram

Example

```text
nums = [1,2,1]

Circular Array

        ┌──────────────┐
        │              │
1 ───► 2 ───► 1 ───────┘
```

Finding answers

```text
Index:   0   1   2
Value:   1   2   1

1 → 2
2 → None
1 → (wrap around) → 2

Answer

[2,-1,2]
```

---

# 3. Example I/O

### Example 1

**Input**

```text
nums = [1,2,1]
```

**Output**

```text
[2,-1,2]
```

Explanation

* First 1 → 2
* 2 → none
* Last 1 wraps around → 2

---

### Example 2

**Input**

```text
nums = [1,2,3,4,3]
```

**Output**

```text
[2,3,4,-1,4]
```

---

### Edge Case

```text
nums = [5]

Output

[-1]
```

---

# 4. Intuition & Pattern Recognition

## Interview Signals

Whenever the problem says

* Next greater element
* Circular array
* Wrap around
* Search continues from beginning

Think

> **Monotonic Stack + Traverse Twice**

---

### Why Twice?

Normally

```text
1 2 1
```

For the last **1**, there's nothing on its right.

But because the array is circular,

we must continue searching

```text
1 2 1 1 2 1
```

Notice:

We don't actually duplicate the array.

We simply iterate **2 × n** times using modulo.

---

# 5. Simpler Version

## Simplest Problem

**Next Greater Element I**

```text
[2,1,5,3]

2 → 5
1 → 5
5 → None
3 → None
```

---

## Difference Here

Now the array wraps around.

Instead of

```text
2 1 5 3
```

Think

```text
2 1 5 3 2 1 5 3
```

But we only need one extra traversal.

---

### Progression

```text
Next Greater Element
          ↓
Monotonic Stack
          ↓
Array becomes circular
          ↓
Traverse twice
```

---

# 6. Brute Force

For every element,

search the next `n-1` elements using modulo.

### Python

```python
class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        ans = [-1] * n

        for i in range(n):
            for j in range(1, n):
                nxt = (i + j) % n

                if nums[nxt] > nums[i]:
                    ans[i] = nums[nxt]
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
O(1)
```

---

# 7. Optimal Solution

## Method 1 (Right → Left) ⭐ Recommended

### Idea

Pretend the array has length `2n`.

Traverse from

```text
2n-1 → 0
```

using modulo.

Maintain a **monotonic decreasing stack**.

For each index:

* Remove all smaller or equal elements.
* During the **first pass (i < n)**, the top is the answer.
* Push the current number.

### Python

```python
class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        ans = [-1] * n
        stack = []

        # Traverse twice from right to left
        for i in range(2 * n - 1, -1, -1):
            curr = nums[i % n]

            # Remove smaller or equal elements
            while stack and stack[-1] <= curr:
                stack.pop()

            # Fill answers only during first pass
            if i < n:
                if stack:
                    ans[i] = stack[-1]

            stack.append(curr)

        return ans
```

---

### Complexity

Time

```text
O(n)
```

Each element is pushed and popped at most twice.

Space

```text
O(n)
```

---

# Method 2 (Left → Right)

Maintain a stack of **indices**.

Traverse the array twice.

Whenever the current value is larger than the index on top of the stack,

resolve that index.

Push indices only during the **first pass**.

### Python

```python
class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        ans = [-1] * n
        stack = []

        for i in range(2 * n):
            curr = nums[i % n]

            while stack and nums[stack[-1]] < curr:
                idx = stack.pop()
                ans[idx] = curr

            # Push only during the first traversal
            if i < n:
                stack.append(i)

        return ans
```

### Why only push in first pass?

Because every index should appear only once.

The second traversal is only used to resolve unanswered indices.

---

# 8. Step-by-Step Trace

Example

```text
nums = [1,2,1]
```

Using the left-to-right method:

| i | Current | Stack (Indices) | Action         | Answer     |
| - | ------- | --------------- | -------------- | ---------- |
| 0 | 1       | []              | Push 0         | [-1,-1,-1] |
| 1 | 2       | [0]             | 2>1 → ans[0]=2 | [2,-1,-1]  |
|   |         |                 | Push 1         |            |
| 2 | 1       | [1]             | Push 2         | [2,-1,-1]  |
| 3 | 1       | [1,2]           | No pop         | [2,-1,-1]  |
| 4 | 2       | [1,2]           | 2>1 → ans[2]=2 | [2,-1,2]   |
| 5 | 1       | [1]             | End            | [2,-1,2]   |

Final Answer

```text
[2,-1,2]
```

---

# 9. Related Problems

1. **496. Next Greater Element I**
   Basic next greater element using a monotonic stack.

2. **739. Daily Temperatures**
   Same pattern but returns the number of days until a greater temperature.

3. **1475. Final Prices With a Special Discount in a Shop**
   Finds the next **smaller or equal** element instead of the next greater one.

4. **84. Largest Rectangle in Histogram**
   Uses previous and next smaller elements to compute rectangle widths.

5. **907. Sum of Subarray Minimums**
   Advanced monotonic stack problem based on previous and next smaller elements.

---

# Pattern Summary (Interview Revision)

| Problem Clue         | Pattern                                                                                             |
| -------------------- | --------------------------------------------------------------------------------------------------- |
| Next greater element | Monotonic Decreasing Stack                                                                          |
| Circular array       | Traverse **2 × n** times                                                                            |
| Wrap around          | Use **`i % n`**                                                                                     |
| Fill answers once    | Push indices only in the first pass (left → right) or fill answers only when `i < n` (right → left) |

## Recognition Shortcut

> **"Find the next greater element in a circular array."**
>
> Think:
>
> 1. **Monotonic Decreasing Stack**
> 2. **Simulate circularity by traversing `2 × n` times**
> 3. **Use `i % n` to wrap around**
>
> **Memory Trick:**
>
> * **Normal Next Greater** → traverse once.
> * **Circular Next Greater** → traverse **twice**, but **store each index only once**.
