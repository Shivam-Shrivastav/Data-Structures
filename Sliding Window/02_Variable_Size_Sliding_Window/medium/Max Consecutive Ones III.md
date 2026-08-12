# 1004. Max Consecutive Ones III

**Pattern:** Variable-Size Sliding Window + Count Invalid Elements

The key idea is:

> Find the **longest subarray containing at most `k` zeros**.

Because those `k` zeros can be flipped to `1`.

---

# 1. Problem Statement

Given a binary array `nums` and integer `k`, you may flip at most `k` zeros into ones.

Return the maximum number of consecutive `1`s possible after performing at most `k` flips.

### Example

```text
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

Output = 6
```

We can take:

```text
[0,0,1,1,1,1]
 ↑ ↑
flip these

→ [1,1,1,1,1,1]

length = 6
```

### Constraints

* `1 <= nums.length <= 10^5`
* `nums[i]` is `0` or `1`
* `0 <= k <= nums.length`

An `O(N)` sliding-window solution is ideal.

---

# 2. Diagram

Think of zeros as **bad elements** that consume your flip budget.

```text
nums = [1,1,0,0,1,1,1]
k = 2

        L
        ↓
        1 1 0 0 1 1 1
                    ↑
                    R

zeros = 2

Window is valid ✓

We can imagine:

1 1 0 0 1 1 1
    ↓ ↓
1 1 1 1 1 1 1

Length = 7
```

But suppose another zero enters:

```text
k = 2

[1, 0, 1, 0, 1, 0]
 L                 R

zeros = 3 ❌

3 > k

Shrink from left until:

zeros <= 2
```

### Window invariant

```text
number of zeros <= k
```

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

A longest valid window contains four `1`s and two `0`s.

After flipping those two zeros, we get six consecutive ones.

### Example 2

```text
Input:
nums = [0,0,1,1,1,0,0]
k = 0

Output:
3
```

No zeros can be flipped, so we're simply looking for the longest existing sequence of ones:

```text
[1,1,1]
length = 3
```

---

# 4. Intuition & Pattern Recognition

The wording can make this look like a "flip elements" problem.

Don't focus on actually flipping anything.

Translate:

> "Flip at most `k` zeros"

into:

> "Find the longest subarray containing at most `k` zeros."

Now the pattern becomes obvious:

```text
Longest contiguous subarray
        +
At most K bad elements
        ↓
Variable Sliding Window
```

### Interview thinking

Tell yourself:

```text
Zero = bad element

I can tolerate at most k bad elements.

Expand right while zeros <= k.

If zeros > k,
shrink left until zeros <= k again.

Track the longest valid window.
```

This is a very reusable sliding-window pattern.

---

# 5. Simpler Version

## Step 1 — Max Consecutive Ones — LeetCode 485

No flips allowed.

```text
nums = [1,1,0,1,1,1]

Longest = [1,1,1]

Answer = 3
```

Essentially:

```text
k = 0
```

You learn:

> Find the longest continuous region satisfying a condition.

---

## Step 2 — Max Consecutive Ones II — LeetCode 487

You can flip **at most one zero**.

```text
nums = [1,1,0,1,1]

          ↓ flip

       [1,1,1,1,1]

Answer = 5
```

This is:

```text
zeros <= 1
```

---

## Step 3 — Max Consecutive Ones III

Now instead of one flip:

```text
zeros <= k
```

So the progression is:

```text
LeetCode 485

No zeros allowed
zeros <= 0

       ↓

LeetCode 487

One zero allowed
zeros <= 1

       ↓

LeetCode 1004

K zeros allowed
zeros <= K
```

---

## Connection to At Most K Distinct

You just revised:

```text
Longest Substring with At Most K Distinct

invalid condition:
distinct > k
```

Here:

```text
Max Consecutive Ones III

invalid condition:
zeros > k
```

The sliding-window skeleton is identical.

```text
Expand
   ↓
Check validity
   ↓
Invalid?
   ↓
Shrink until valid
   ↓
Update maximum
```

Only the **validity condition** changed.

---

# 6. Brute Force

Start from every index and extend right while counting zeros.

```python
class Solution:
    def longestOnes(self, nums, k):
        ans = 0

        for i in range(len(nums)):
            zeros = 0

            for j in range(i, len(nums)):
                if nums[j] == 0:
                    zeros += 1

                if zeros > k:
                    break

                ans = max(ans, j - i + 1)

        return ans
```

### Complexity

```text
Time  : O(N²)
Space : O(1)
```

---

# 7. Optimal Solution

We don't need a `HashMap` here.

Why?

We only care about one thing:

```text
How many zeros are inside my window?
```

So a single counter is enough.

```python
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        zeros = 0
        ans = 0

        for right in range(len(nums)):

            # A zero consumes one flip.
            if nums[right] == 0:
                zeros += 1

            # Too many zeros: shrink until valid.
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1

                left += 1

            # Window now contains at most k zeros.
            ans = max(ans, right - left + 1)

        return ans
```

### Complexity

```text
Time  : O(N)
Space : O(1)
```

Although there's a `while` inside the `for`, this is still `O(N)`.

`right` moves forward `N` times, and `left` can also move forward at most `N` times.

---

# 8. Step-by-Step Trace

Take:

```text
nums = [1,1,0,0,1,1,1]
k = 1
```

We may tolerate **one zero**.

|  R | `nums[R]` | zeros | Action           |  L | Valid Window |   Max |
| -: | --------: | ----: | ---------------- | -: | ------------ | ----: |
|  0 |         1 |     0 | Keep             |  0 | `[1]`        |     1 |
|  1 |         1 |     0 | Keep             |  0 | `[1,1]`      |     2 |
|  2 |         0 |     1 | Keep             |  0 | `[1,1,0]`    | **3** |
|  3 |         0 |     2 | Invalid → shrink |  0 | —            |     3 |

At `right = 3`:

```text
[1,1,0,0]
 L     R

zeros = 2
k = 1

2 > 1 ❌
```

Move `left`:

```text
[1,0,0]
 L   R

Removed 1
zeros = 2

Still invalid
```

Again:

```text
[0,0]
 L R

Removed 1
zeros = 2

Still invalid
```

Again:

```text
[0]
 L/R

Removed first 0

zeros = 1 ✓
```

Continue:

```text
right = 4

[0,1]

zeros = 1
length = 2
```

Then:

```text
right = 5

[0,1,1]

zeros = 1
length = 3
```

Then:

```text
right = 6

[0,1,1,1]

zeros = 1
length = 4
```

Final:

```text
Answer = 4
```

Flip the zero:

```text
[0,1,1,1]
 ↓

[1,1,1,1]
```

---

# 9. Related Problems

| Problem                                                       | Connection                                                                                                 |
| ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **485. Max Consecutive Ones**                                 | Simplest version: no zeros allowed, effectively `k = 0`.                                                   |
| **487. Max Consecutive Ones II**                              | Same idea with exactly one available flip.                                                                 |
| **904. Fruit Into Baskets**                                   | Longest window with at most 2 distinct values instead of at most K zeros.                                  |
| **340. Longest Substring with At Most K Distinct Characters** | Same expand/shrink template, with distinct characters as the constraint.                                   |
| **424. Longest Repeating Character Replacement**              | Similar "change at most K elements" idea, but requires tracking the most frequent character in the window. |

# Key Interview Takeaway

The important part isn't the `1`s.

The key transformation is:

```text
"Flip at most K zeros"

            ↓

"Longest subarray with
 at most K zeros"

            ↓

Variable Sliding Window
```

Then the generic pattern becomes:

```python
for right in range(len(nums)):

    # Add new element
    if nums[right] == 0:
        zeros += 1

    # Shrink while invalid
    while zeros > k:
        if nums[left] == 0:
            zeros -= 1
        left += 1

    # Current window is valid
    ans = max(ans, right - left + 1)
```

For quick recognition, remember:

**Longest + contiguous + at most K bad elements → variable sliding window.**
