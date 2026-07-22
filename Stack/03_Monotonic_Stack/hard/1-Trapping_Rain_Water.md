# **84. Largest Rectangle in Histogram**

## 1. Problem Statement

You are given an array `heights` where `heights[i]` represents the height of the `iᵗʰ` bar in a histogram. Each bar has a width of **1**.

Find the **area of the largest rectangle** that can be formed inside the histogram.

### Example

```text
Input:
heights = [2,1,5,6,2,3]

Output:
10

Explanation:
The largest rectangle is formed using bars with heights 5 and 6.

      █
      █ █
      █ █
█     █ █
█ █   █ █   █
█ █ █ █ █ █
---------------
2 1 5 6 2 3

Rectangle:
      █ █
      █ █

Height = 5
Width  = 2
Area = 5 × 2 = 10
```

### Constraints

* `1 <= heights.length <= 10^5`
* `0 <= heights[i] <= 10^4`

---

# 2. Diagram

### Key Idea

Every bar acts as the **minimum height** of some rectangle.

We need to find:

* First smaller element on the left
* First smaller element on the right

```
Index:
0 1 2 3 4 5

Height:
2 1 5 6 2 3


          6
        ███
      █████
█     █████
█ █   █████ █
█ █ █ █████ █
--------------
2 1 5 6 2 3

Consider height = 5

Left smaller = index 1
Right smaller = index 4

Rectangle extends:

        █ █
        █ █

Width = 4 - 1 - 1 = 2
Area = 5 × 2
```

Instead of explicitly computing left/right smaller arrays, the **monotonic increasing stack** discovers them while traversing.

---

# 3. Example I/O

### Example 1

```text
Input:
[2,1,5,6,2,3]

Output:
10
```

Explanation

```
Rectangle:
5 6

Minimum height = 5
Width = 2

Area = 10
```

---

### Example 2 (Edge Case)

```text
Input:
[2,4]

Output:
4
```

Explanation

Possible rectangles:

```
2 -> area = 2
4 -> area = 4
2 4 -> min =2 width=2 area=4
```

Maximum = **4**

---

# 4. Intuition & Pattern Recognition

### Interview Signal

Whenever you hear:

* largest rectangle
* nearest smaller
* previous smaller
* next smaller
* expand until smaller
* histogram

Think:

> **Monotonic Increasing Stack**

---

### Why does it work?

Suppose current bar has height = **h**.

As long as the next bars are **taller**, rectangle can continue.

The moment we find a **smaller** bar:

```
Current bar cannot extend anymore.
```

So we immediately calculate its maximum rectangle.

Stack always stores indices with

```
Increasing Heights

1
2
4
5
```

When a smaller height appears

```
Current = 2

Stack:
1
2
4
5

5 >2 → pop
4 >2 → pop
2 <=2 stop
```

Every popped bar now knows:

* Right boundary = current index
* Left boundary = new stack top

---

### Interview Thinking

> Every bar wants to know how far it can stretch left and right before hitting a smaller bar.

Instead of checking both directions separately, the stack tells us exactly when a bar's expansion ends.

---

# 5. Simpler Version

## Simplest Problem

### Find Next Smaller Element

Example

```
5 6 2

For 6

Next smaller =2
```

Stack solves this.

---

### Slightly Harder

Find Previous Smaller Element.

Again stack.

---

### LeetCode progression

1. Next Greater Element I
2. Daily Temperatures
3. Previous Smaller Element
4. Largest Rectangle in Histogram ← Current
5. Maximal Rectangle

---

### Thinking Progression

```
Find next greater
      ↓

Find next smaller
      ↓

Find previous smaller
      ↓

Know left/right boundaries
      ↓

Rectangle width
      ↓

Largest Rectangle
```

---

# 6. Brute Force

For every bar

Expand left

Expand right

until smaller element found.

```
for each bar:
    move left
    move right
```

### Complexity

Time

```
O(n²)
```

Space

```
O(1)
```

---

# 7. Optimal Solution (Monotonic Increasing Stack)

### Idea

Maintain an **increasing stack of indices**.

Whenever current height becomes smaller than stack top:

* Pop
* Compute rectangle
* Continue

Append a `0` height at the end (sentinel) so every remaining bar is processed.

### Python

```python
class Solution:
    def largestRectangleArea(self, heights):
        stack = []          # stores indices of increasing heights
        max_area = 0

        # Sentinel bar to flush remaining stack
        heights.append(0)

        for i in range(len(heights)):

            # Current bar is smaller -> rectangles end here
            while stack and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]

                # Left boundary after popping
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area
```

### Time Complexity

```
O(n)
```

Each index is pushed once and popped once.

### Space Complexity

```
O(n)
```

---

# 8. Step-by-Step Trace

Example

```
[2,1,5,6,2,3]
```

After appending sentinel:

```
[2,1,5,6,2,3,0]
```

| i | Height | Stack (indices) | Action          | Area   |
| - | ------ | --------------- | --------------- | ------ |
| 0 | 2      | []              | Push 0          | -      |
| 1 | 1      | [0]             | Pop 2 → width=1 | 2      |
|   |        | []              | Push 1          | -      |
| 2 | 5      | [1]             | Push 2          | -      |
| 3 | 6      | [1,2]           | Push 3          | -      |
| 4 | 2      | [1,2,3]         | Pop 6 width=1   | 6      |
|   |        | [1,2]           | Pop 5 width=2   | **10** |
|   |        | [1]             | Push 4          | -      |
| 5 | 3      | [1,4]           | Push 5          | -      |
| 6 | 0      | [1,4,5]         | Pop 3 width=1   | 3      |
|   |        | [1,4]           | Pop 2 width=4   | 8      |
|   |        | [1]             | Pop 1 width=6   | 6      |

Maximum area

```
10
```

---

# 9. Related Problems

1. **496. Next Greater Element I**
   Learn the basic monotonic stack pattern for finding the next greater element.

2. **739. Daily Temperatures**
   Uses a monotonic decreasing stack to determine how far ahead a warmer day occurs.

3. **907. Sum of Subarray Minimums**
   Uses previous and next smaller elements to determine each element's contribution to the total sum.

4. **85. Maximal Rectangle** ⭐
   Converts each matrix row into a histogram and repeatedly applies **Largest Rectangle in Histogram**.

5. **42. Trapping Rain Water**
   Another classic monotonic stack problem where boundaries determine trapped water instead of rectangle area.

---

# Interview Cheat Sheet

* **Pattern:** Monotonic Increasing Stack
* **Stack stores:** Indices
* **Pop when:** Current height `<` stack top height
* **On Pop:**

  * `height = popped bar`
  * `right = current index`
  * `left = new stack top`
  * `width = right - left - 1`
  * `area = height × width`
* **Sentinel:** Append `0` at the end to process all remaining bars.
* **Complexity:** `O(n)` time, `O(n)` space.
