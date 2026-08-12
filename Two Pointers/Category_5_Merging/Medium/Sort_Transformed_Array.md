# Sort Transformed Array (LeetCode 360)

**Pattern:** Two Pointers + Sorted Array + Quadratic Function

---

# 1. Problem Statement

You are given:

* A sorted integer array `nums`
* Three integers `a`, `b`, and `c`

Define the quadratic function:

[
f(x)=ax^2+bx+c
]

Return a **sorted array** after applying `f(x)` to every element.

### Constraints

* `1 <= nums.length <= 2 * 10^4`
* `nums` is already sorted.
* `-100 <= nums[i], a, b, c <= 100`
* Aim for **O(N)**.

---

# 2. Diagram

### Example

```
nums = [-4,-2,2,4]
a = 1
b = 3
c = 5

Quadratic:

          ^
         / \
        /   \
-------/-----\------------>

Both ends become larger.

Transform:

-4 -> 9
-2 -> 3
 2 ->15
 4 ->33

Need:

[3,9,15,33]
```

Since the array is sorted, the **largest transformed values are at one of the ends**.

---

### If a < 0

```
          \   /
           \ /
            V

Middle becomes largest.

Ends become smallest.
```

The direction of filling changes.

---

# 3. Example I/O

### Example 1

```
Input

nums = [-4,-2,2,4]
a = 1
b = 3
c = 5

Output

[3,9,15,33]
```

Explanation

```
f(-4)=9
f(-2)=3
f(2)=15
f(4)=33

Sorted:
[3,9,15,33]
```

---

### Example 2

```
Input

nums = [-4,-2,2,4]
a = -1
b = 3
c = 5

Output

[-23,-5,1,7]
```

Explanation

```
f(-4)=-23
f(-2)=-5
f(2)=7
f(4)=1

Sorted:
[-23,-5,1,7]
```

---

### Edge Case

```
nums=[0]

a=5
b=2
c=1

Output

[1]
```

---

# 4. Intuition & Pattern Recognition

## Signals

Whenever you see

* Sorted input
* Need sorted output
* Function applied independently to every element
* O(N) expected

Think:

> **Can I avoid sorting again?**

Sorting transformed values would be

```
Transform -> O(N)

Sort -> O(N log N)
```

Can we exploit the original ordering?

Yes.

---

### Important Observation

Quadratic functions are **parabolas**.

For

```
a > 0
```

```
      ^
     / \
```

The largest values occur far from the vertex.

Since the input array is sorted,

the largest transformed value must come from

```
Left end
or
Right end
```

Exactly the same idea as

```
Squares of a Sorted Array
```

---

### Interview Thinking

Tell yourself:

```
Input is sorted.

Quadratic preserves symmetry.

Largest transformed value
must be at one end.

Compare both ends.

Place the larger one.

Move inward.
```

---

# 5. Simpler Version

## Simpler Question 1

### Squares of a Sorted Array (LeetCode 977)

```
nums = [-4,-2,0,3]

Square each.

Need sorted answer.
```

Solution:

Two pointers.

---

## Why?

Because

```
(-4)^2 > 3^2
```

Largest square is at an end.

---

## Current Question

Instead of

```
x²
```

we have

```
ax²+bx+c
```

Still a parabola.

Same property.

---

### Thinking Progression

```
Sorted Array

↓

Transform

↓

Need sorted output

↓

Avoid sorting

↓

Observe extremes

↓

Two pointers
```

---

# 6. Brute Force

Compute every transformed value.

```
ans=[]

for x in nums:
    ans.append(a*x*x+b*x+c)

sort(ans)
```

### Complexity

```
Time

Transform : O(N)

Sort      : O(N log N)

Overall   : O(N log N)

Space

O(N)
```

---

# 7. Optimal Solution

## Idea

Maintain

```
left
right
```

Evaluate

```
f(nums[left])

f(nums[right])
```

---

### Case 1

```
a >= 0
```

Largest values belong at the ends.

Fill answer from **right to left**.

---

### Case 2

```
a < 0
```

Smallest values belong at the ends.

Fill answer from **left to right**.

---

### Python

```python
class Solution:
    def sortTransformedArray(self, nums, a, b, c):

        def f(x):
            return a * x * x + b * x + c

        n = len(nums)
        ans = [0] * n

        left = 0
        right = n - 1

        # Fill from the end if parabola opens upward
        idx = n - 1 if a >= 0 else 0

        while left <= right:

            left_val = f(nums[left])
            right_val = f(nums[right])

            if a >= 0:
                # Larger value goes to the end
                if left_val > right_val:
                    ans[idx] = left_val
                    left += 1
                else:
                    ans[idx] = right_val
                    right -= 1
                idx -= 1

            else:
                # Smaller value goes to the beginning
                if left_val < right_val:
                    ans[idx] = left_val
                    left += 1
                else:
                    ans[idx] = right_val
                    right -= 1
                idx += 1

        return ans
```

---

### Complexity

```
Time : O(N)

Space: O(N)
```

---

# 8. Step-by-Step Trace

Example

```
nums = [-4,-2,2,4]

a = 1
b = 3
c = 5
```

Compute:

```
f(-4)=9

f(-2)=3

f(2)=15

f(4)=33
```

Fill from the end.

| Left | Right | Left Value | Right Value | Choose | Answer      |
| ---- | ----- | ---------- | ----------- | ------ | ----------- |
| 0    | 3     | 9          | 33          | 33     | [*,*,_,33]  |
| 0    | 2     | 9          | 15          | 15     | [*,*,15,33] |
| 0    | 1     | 9          | 3           | 9      | [_,9,15,33] |
| 1    | 1     | 3          | 3           | 3      | [3,9,15,33] |

Final answer

```
[3,9,15,33]
```

---

# 9. Related Problems

| Problem                              | Connection                                                            |
| ------------------------------------ | --------------------------------------------------------------------- |
| **977. Squares of a Sorted Array**   | Direct simpler version. Replace `x²` with a quadratic function.       |
| **167. Two Sum II**                  | Uses two pointers on a sorted array by exploiting order.              |
| **11. Container With Most Water**    | Another classic "compare ends and move inward" two-pointer problem.   |
| **16. 3Sum Closest**                 | Two pointers after sorting; relies on ordered data.                   |
| **986. Interval List Intersections** | Two pointers over sorted structures, advancing one pointer at a time. |

---

# Key Interview Takeaways

* **Pattern:** Two Pointers on a Sorted Array.
* **Key Observation:** A quadratic function forms a parabola, so the extreme transformed values come from the ends of the sorted input.
* **Rule:** Compare the transformed values at both ends.

  * If `a >= 0`, place the larger value at the end of the result.
  * If `a < 0`, place the smaller value at the beginning.
* **Complexity:** **O(N)** time and **O(N)** extra space—better than transforming then sorting (`O(N log N)`). 
