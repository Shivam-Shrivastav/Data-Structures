# 1004. Max Consecutive Ones III

## 1. Problem Statement

Given a binary array `nums` and an integer `k`, return the **maximum number of consecutive `1`s** in the array if you can flip **at most `k` zeros** to `1`s.

### Constraints

* `1 <= nums.length <= 10^5`
* `nums[i]` is either `0` or `1`
* `0 <= k <= nums.length`

Since `n` can be `10^5`, an **O(n²)** solution will timeout.

---

# 2. Diagram

The window is valid as long as it contains **at most `k` zeros**.

Example:

```text
nums = [1,1,1,0,0,1,1]
k = 1
```

```text
Window

1 1 1 0
↑       ↑
L       R

Zeros = 1 ✅
Length = 4
```

Expand:

```text
1 1 1 0 0
        ↑

Zeros = 2 ❌
```

Shrink until only one zero remains.

```text
Remove left

1 1 0 0

Still 2 zeros

Remove again

1 0 0

Still 2

Remove again

0 0

Still 2

Remove first zero

0

Zeros = 1 ✅
```

Continue expanding...

---

# 3. Example I/O

### Example 1

```text
Input:
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

Output:
6
```

Explanation

```text
Flip two zeros.

Longest consecutive ones

[1,1,1,0,0,1]

Length = 6
```

---

### Example 2

```text
Input:
nums = [0,0,1,1,1,0,0]
k = 0

Output:
3
```

Explanation

```text
No flips allowed.

Longest consecutive ones = 3
```

---

### Edge Case

```text
Input:
nums = [0,0,0]
k = 3

Output:
3
```

All zeros can be flipped.

---

# 4. Intuition & Pattern Recognition

## Signal 1

Question asks

> Maximum consecutive subarray

Think

> **Sliding Window**

---

## Signal 2

Validity depends on

> Number of zeros

Instead of counting distinct elements,

we simply count

```text
zeros
```

---

## Pattern

Expand window.

Whenever

```text
zeros <= k
```

window is valid.

If

```text
zeros > k
```

Shrink from the left until valid again.

---

### Interview Thought Process

> "Longest valid subarray."

> "Validity = at most K zeros."

> "Maintain zero count."

> "Shrink whenever too many zeros."

---

# 5. Simpler Version

## Simpler Problem

### 485. Max Consecutive Ones

No zero flips allowed.

Simply count consecutive ones.

---

### Current Problem

Instead of

```text
Zero count = 0
```

Allow

```text
Zero count <= K
```

Everything else remains identical.

---

### Thinking Progression

```text
Max Consecutive Ones

↓

Allow one flip

↓

Allow K flips

↓

Window validity

↓

Zeros <= K

↓

Sliding Window
```

---

### Related Simpler Questions

* 485. Max Consecutive Ones
* 487. Max Consecutive Ones II (flip one zero)
* 904. Fruit Into Baskets (at most 2 distinct)
* 340. Longest Substring with At Most K Distinct Characters

---

# 6. Brute Force

Start from every index.

Count zeros while extending.

```python
class Solution:
    def longestOnes(self, nums, k):
        n = len(nums)
        ans = 0

        for i in range(n):
            zeros = 0

            for j in range(i, n):

                if nums[j] == 0:
                    zeros += 1

                if zeros <= k:
                    ans = max(ans, j - i + 1)
                else:
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

# 7. Optimal Solution (Sliding Window)

```python
class Solution:
    def longestOnes(self, nums, k):
        left = 0
        zeros = 0
        ans = 0

        for right in range(len(nums)):

            # Count zeros in the current window.
            if nums[right] == 0:
                zeros += 1

            # Too many zeros? Shrink window.
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            # Current window is valid.
            ans = max(ans, right - left + 1)

        return ans
```

---

### Why only count zeros?

The only restriction is

```text
Number of zeros <= K
```

We don't care how many ones exist.

So a single integer (`zeros`) is enough.

No HashMap or HashSet is required.

---

### Complexity

Time

```text
O(n)
```

Each element enters and leaves the window once.

Space

```text
O(1)
```

---

# 8. Step-by-Step Trace

Example

```text
nums = [1,1,1,0,0,1,1]
k = 1
```

| Right | Value | Window      | Zeros | Action | Answer |
| ----: | :---: | ----------- | :---: | ------ | :----: |
|     0 |   1   | [1]         |   0   | Valid  |    1   |
|     1 |   1   | [1,1]       |   0   | Valid  |    2   |
|     2 |   1   | [1,1,1]     |   0   | Valid  |    3   |
|     3 |   0   | [1,1,1,0]   |   1   | Valid  |    4   |
|     4 |   0   | [1,1,1,0,0] |   2   | Shrink |    4   |
|       |       | [1,1,0,0]   |   2   | Shrink |    4   |
|       |       | [1,0,0]     |   2   | Shrink |    4   |
|       |       | [0,0]       |   2   | Shrink |    4   |
|       |       | [0]         |   1   | Valid  |    4   |
|     5 |   1   | [0,1]       |   1   | Valid  |    4   |
|     6 |   1   | [0,1,1]     |   1   | Valid  |    4   |

Final Answer

```text
4
```

---

# 9. Related Problems (Increasing Difficulty)

| Problem                                                       | Connection                                                                                                               |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **485. Max Consecutive Ones**                                 | Simplest version with no flips allowed.                                                                                  |
| **487. Max Consecutive Ones II**                              | Same problem but you can flip **only one** zero (`k = 1`).                                                               |
| **904. Fruit Into Baskets**                                   | Variable-size sliding window where validity is based on **at most two distinct values** instead of zero count.           |
| **340. Longest Substring with At Most K Distinct Characters** | General sliding-window pattern using a frequency map to maintain at most `k` distinct characters.                        |
| **424. Longest Repeating Character Replacement**              | Another variable-size sliding window where validity depends on the number of replacements needed rather than zero count. |
