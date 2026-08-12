# 2024. Maximize the Confusion of an Exam

## 1. Problem Statement

A teacher writes the answers to an exam as a string `answerKey` consisting of only:

* `'T'` (True)
* `'F'` (False)

You may **change at most `k` characters**.

Return the **maximum number of consecutive identical answers** (all `'T'` or all `'F'`) that can be obtained after performing at most `k` changes.

### Constraints

* `1 <= answerKey.length <= 5 × 10^4`
* `answerKey[i]` is `'T'` or `'F'`
* `1 <= k <= answerKey.length`

Since `n` can be large, an **O(n²)** solution will timeout.

---

# 2. Diagram

We need the longest window that can become

* all **T**, or
* all **F**

### Case 1: Make everything `T`

```text
answerKey = T T F T F
k = 1

Window

T T F T
↑      ↑

Need to flip

F -> T

Changes = 1 ✅
```

Expand

```text
T T F T F

Need to flip

F
F

Changes = 2 ❌
```

Shrink.

---

### Case 2: Make everything `F`

```text
T T F T

Need to flip

T
T
T

Changes = 3 ❌
```

Not a good window.

Take the maximum of both cases.

---

# 3. Example I/O

### Example 1

```text
Input:
answerKey = "TTFF"
k = 2

Output:
4
```

Explanation

```text
Flip both F's.

TTTT
```

---

### Example 2

```text
Input:
answerKey = "TFFT"
k = 1

Output:
3
```

Explanation

```text
Flip one T

TFFF

or

Flip one F

TTFT

Longest = 3
```

---

### Edge Case

```text
Input:
answerKey = "TTTT"
k = 2

Output:
4
```

Already consecutive.

---

# 4. Intuition & Pattern Recognition

## Signal 1

Question asks

> Maximum consecutive characters

Think

> **Sliding Window**

---

## Signal 2

Window is valid if it can be converted into

all **T**

OR

all **F**

using at most `k` changes.

---

### Key Observation

To make a window all **T**

we only need to count

```text
Number of F's
```

because only F's need changing.

Similarly,

to make everything **F**

count

```text
Number of T's
```

---

### Interview Thought Process

> "This is almost identical to Max Consecutive Ones III."

Instead of

```text
Zeros <= K
```

we now have

```text
F's <= K
```

or

```text
T's <= K
```

Run the sliding window twice.

---

# 5. Simpler Version

## Simpler Problem

### 1004. Max Consecutive Ones III

There,

```text
Flip at most K zeros.
```

Here,

```text
Flip at most K T's

OR

Flip at most K F's
```

It is exactly the same algorithm.

---

### Thinking Progression

```text
Max Consecutive Ones III

↓

Binary values

↓

Characters T/F

↓

Run twice

Make everything T

Make everything F

↓

Take maximum
```

---

### Related Simpler Questions

* 485. Max Consecutive Ones
* 487. Max Consecutive Ones II
* 1004. Max Consecutive Ones III

---

# 6. Brute Force

Generate every substring.

Count T's and F's.

```python
class Solution:
    def maxConsecutiveAnswers(self, answerKey, k):
        n = len(answerKey)
        ans = 0

        for i in range(n):

            t = 0
            f = 0

            for j in range(i, n):

                if answerKey[j] == 'T':
                    t += 1
                else:
                    f += 1

                if min(t, f) <= k:
                    ans = max(ans, j - i + 1)

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

## Approach 1 (Most Interview Friendly)

Create a helper function.

* Convert everything to **T**
* Convert everything to **F**

Return the maximum.

```python
class Solution:
    def maxConsecutiveAnswers(self, answerKey, k):

        def longest(target):
            left = 0
            changes = 0
            ans = 0

            for right in range(len(answerKey)):

                # This character must be changed to become 'target'.
                if answerKey[right] != target:
                    changes += 1

                # Too many changes needed? Shrink window.
                while changes > k:
                    if answerKey[left] != target:
                        changes -= 1
                    left += 1

                ans = max(ans, right - left + 1)

            return ans

        return max(longest('T'), longest('F'))
```

---

### Why does this work?

For

```text
Target = T
```

we count

```text
F's
```

For

```text
Target = F
```

we count

```text
T's
```

Both are identical sliding-window problems.

---

### Complexity

Time

```text
O(2n)

≈ O(n)
```

Space

```text
O(1)
```

---

# Alternative Optimal (Single Pass)

A neat optimization is to maintain counts of both `'T'` and `'F'` in one window.

The window is valid if:

```text
min(countT, countF) <= k
```

because we only need to flip the **minority** character.

```python
class Solution:
    def maxConsecutiveAnswers(self, answerKey, k):
        left = 0
        countT = countF = 0
        ans = 0

        for right in range(len(answerKey)):
            if answerKey[right] == 'T':
                countT += 1
            else:
                countF += 1

            while min(countT, countF) > k:
                if answerKey[left] == 'T':
                    countT -= 1
                else:
                    countF -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
```

This is also **O(n)**.

---

# 8. Step-by-Step Trace

Example

```text
answerKey = "TFFT"
k = 1
```

Making everything **T**

| Right | Char | Changes Needed (F's) | Window | Action | Answer |
| ----: | :--: | :------------------: | ------ | ------ | :----: |
|     0 |   T  |           0          | T      | Valid  |    1   |
|     1 |   F  |           1          | TF     | Valid  |    2   |
|     2 |   F  |           2          | TFF    | Shrink |    2   |
|       |      |           1          | FF     | Valid  |    2   |
|     3 |   T  |           1          | FFT    | Valid  |    3   |

Making everything **F**

Best window length = **3**

Final Answer

```text
3
```

---

# 9. Related Problems (Increasing Difficulty)

| Problem                                                       | Connection                                                                                                                                          |
| ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **485. Max Consecutive Ones**                                 | Longest consecutive ones with no flips.                                                                                                             |
| **487. Max Consecutive Ones II**                              | Same idea with exactly one flip (`k = 1`).                                                                                                          |
| **1004. Max Consecutive Ones III**                            | Direct binary-array equivalent where zeros are flipped to ones.                                                                                     |
| **424. Longest Repeating Character Replacement**              | Similar "change at most `k` characters" problem, but with 26 possible characters instead of just two.                                               |
| **340. Longest Substring with At Most K Distinct Characters** | Uses the same variable-size sliding window framework, but the validity condition is based on distinct character count rather than required changes. |

---

## Pattern Summary

This problem belongs to the **"Variable Size Sliding Window with Constraint"** family.

```text
Longest window

↓

Window must satisfy a condition

↓

If condition breaks

↓

Shrink from left

↓

Update maximum answer
```

The only thing that changes across these problems is **what makes the window valid**:

| Problem                                                   | Window Valid If                                                    |
| --------------------------------------------------------- | ------------------------------------------------------------------ |
| 1004. Max Consecutive Ones III                            | `zeros <= k`                                                       |
| 904. Fruit Into Baskets                                   | `distinct <= 2`                                                    |
| 340. Longest Substring with At Most K Distinct Characters | `distinct <= k`                                                    |
| 2024. Maximize the Confusion of an Exam                   | `changes needed <= k` (or equivalently `min(countT, countF) <= k`) |
| 424. Longest Repeating Character Replacement              | `window_size - max_frequency <= k`                                 |
