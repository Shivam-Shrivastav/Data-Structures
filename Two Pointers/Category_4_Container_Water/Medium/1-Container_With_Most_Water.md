# Container With Most Water (LeetCode 11)

**Pattern:** Two Pointers (Greedy)

---

# 1. Problem Statement

You are given an integer array `height`, where `height[i]` represents the height of a vertical line drawn at position `i`.

Choose **two lines** that, together with the x-axis, form a container capable of holding the **maximum amount of water**.

Return the **maximum amount of water** the container can store.

The amount of water between two lines is:

[
\text{Area} = \min(\text{height[left]}, \text{height[right]}) \times (\text{right} - \text{left})
]

### Constraints

* `2 <= height.length <= 10^5`
* `0 <= height[i] <= 10^4`
* Need an **O(N)** solution.

---

# 2. Diagram

```
height = [1,8,6,2,5,4,8,3,7]

Index:
0 1 2 3 4 5 6 7 8
| | | | | | | | |
1 8 6 2 5 4 8 3 7

L-----------------------R
1                       7

Width = 8
Height = min(1,7)=1

Area = 1 × 8 = 8

-----------------------------------

Move Left →

    L-------------------R
    8                   7

Width = 7
Height = min(8,7)=7

Area = 7 × 7 = 49  ← Maximum
```

The width decreases every move, so we must hope to find a taller line to compensate.

---

# 3. Example I/O

### Example 1

```
Input:
height = [1,8,6,2,5,4,8,3,7]

Output:
49
```

Explanation

Container formed by heights **8** and **7**.

```
Width = 7
Height = 7

Area = 49
```

---

### Example 2

```
Input:
height = [1,1]

Output:
1
```

Explanation

```
Width = 1
Height = 1

Area = 1
```

---

### Example 3 (Edge Case)

```
Input:
height = [5,5]

Output:
5
```

---

# 4. Intuition & Pattern Recognition

### Signals

Whenever you see:

* Two ends of an array
* Need maximum/minimum value
* Answer depends on both ends
* No sorting allowed
* Brute force is O(N²)

Think:

> **Two Pointers**

---

### Key Observation

Area depends on:

```
Area = min(leftHeight, rightHeight)
       ×
       width
```

Every move reduces the width.

So the **only way to increase area** is to increase the limiting height.

Which height limits the area?

```
min(leftHeight, rightHeight)
```

Therefore,

Move the **shorter pointer**.

---

### Why not move the taller one?

Suppose

```
3 -------- 10

Area = 3 × width
```

Moving the taller line:

```
3 ----- ?

Width decreases

Minimum height is still at most 3.

Area cannot improve.
```

Only replacing the shorter height might increase the minimum height.

---

### Interview Thinking

Tell yourself:

```
Width always decreases.

So I need a taller minimum height.

The shorter wall limits the area.

Move only the shorter pointer.
```

---

# 5. Simpler Version

## Simpler Question 1

### Largest Distance Between Two Indices

```
Max width

No heights involved.

Simply first and last.
```

Introduces width.

---

## Simpler Question 2

### Find Maximum Pair Sum

Need to evaluate pairs.

Brute force checks every pair.

---

## Current Question

Now each pair contributes

```
Area

=

minimum height

×

width
```

Need to intelligently skip impossible pairs.

That's where the Two Pointer greedy proof comes in.

---

### Thinking Progression

```
Check every pair

↓

Need faster

↓

Observe width only decreases

↓

Smaller height limits area

↓

Move smaller pointer

↓

O(N)
```

---

# 6. Brute Force

Check every pair.

```
maxArea = 0

for i:

    for j > i:

        area = min(height[i], height[j]) * (j-i)

        update answer
```

### Complexity

```
Time : O(N²)

Space : O(1)
```

---

# 7. Optimal Solution (Two Pointers)

### Idea

Start from the widest container.

Compute area.

Move only the shorter line.

Repeat until pointers meet.

### Python

```python
class Solution:
    def maxArea(self, height: List[int]):

        left = 0
        right = len(height) - 1

        ans = 0

        while left < right:

            # Width between pointers
            width = right - left

            # Current container area
            area = min(height[left], height[right]) * width

            ans = max(ans, area)

            # Move the limiting wall
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return ans
```

### Complexity

```
Time  : O(N)

Space : O(1)
```

Each pointer moves at most `N` times.

---

# 8. Step-by-Step Trace

Example

```
height = [1,8,6,2,5,4,8,3,7]
```

| Left | Right | Heights | Width | Area | Max | Move    |
| ---- | ----- | ------- | ----- | ---- | --- | ------- |
| 0    | 8     | 1,7     | 8     | 8    | 8   | Left++  |
| 1    | 8     | 8,7     | 7     | 49   | 49  | Right-- |
| 1    | 7     | 8,3     | 6     | 18   | 49  | Right-- |
| 1    | 6     | 8,8     | 5     | 40   | 49  | Right-- |
| 1    | 5     | 8,4     | 4     | 16   | 49  | Right-- |
| 1    | 4     | 8,5     | 3     | 15   | 49  | Right-- |
| 1    | 3     | 8,2     | 2     | 4    | 49  | Right-- |
| 1    | 2     | 8,6     | 1     | 6    | 49  | Right-- |

Final Answer

```
49
```

---

### Why move the smaller pointer?

Current state

```
8 ---------------- 7

Area = 7 × width
```

Move taller one

```
8 -------- ?

Width ↓

Minimum height ≤ 7

Area cannot become larger.
```

Move smaller one

```
?

---------------- 7
```

Maybe

```
10 ---------------- 7

Area = 7 × new width
```

Still has a chance to improve.

---

# 9. Related Problems

| Problem                                     | Connection                                            |
| ------------------------------------------- | ----------------------------------------------------- |
| **167. Two Sum II – Input Array Is Sorted** | Classic two-pointer movement based on a condition.    |
| **125. Valid Palindrome**                   | Move pointers inward while maintaining an invariant.  |
| **42. Trapping Rain Water**                 | Advanced two-pointer problem using left/right maxima. |
| **15. 3Sum**                                | Uses sorting + two pointers to search efficiently.    |
| **881. Boats to Save People**               | Greedy pairing using two pointers after sorting.      |

---

# Key Interview Takeaways

* **Pattern:** Two Pointers (Greedy).
* **Invariant:** Start with the **maximum width** and shrink inward.
* **Observation:** The **shorter wall** limits the current area.
* **Rule:** Always move the **shorter pointer**, since moving the taller one cannot increase the area.
* **Complexity:** **O(N)** time and **O(1)** space.

---

### Common Interview Proof (Why moving the shorter pointer is correct)

Suppose:

```
leftHeight = 4
rightHeight = 9
width = 8

Area = 4 × 8 = 32
```

If we move the **right (taller)** pointer:

* Width becomes `7`.
* The limiting height is still at most `4` (because the left wall is unchanged).
* So the new area is at most `4 × 7 = 28`, which cannot beat the current area.

If instead we move the **left (shorter)** pointer:

* Width decreases to `7`.
* But the new left height might be greater than `4` (say `10`).
* Then the limiting height becomes `min(10, 9) = 9`, giving an area of `9 × 7 = 63`.

Only moving the shorter wall gives a possibility of increasing the limiting height enough to offset the reduced width.

This greedy observation is what makes the **O(N)** two-pointer solution correct.
