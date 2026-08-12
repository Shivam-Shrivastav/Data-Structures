# 2024. Maximize the Confusion of an Exam

**Pattern:** Variable-Size Sliding Window + At Most `k` Replacements

This is a direct progression from **Max Consecutive Ones III**:

```text
Max Consecutive Ones III:
0 → 1 at most k times

Maximize the Confusion:
T ↔ F at most k times
```

The core question is:

> What is the longest substring that can be made **all `T` or all `F`** using at most `k` changes?

---

# 1. Problem Statement

You are given a string `answerKey` consisting only of:

```text
'T' and 'F'
```

and an integer `k`.

You may change at most `k` answers:

```text
T → F
or
F → T
```

Return the **maximum number of consecutive identical answers** obtainable.

### Example

```text
answerKey = "TTFF"
k = 2

Change both F → T

TTFF
  ^^
TTTT

Answer = 4
```

### Constraints

* `1 <= answerKey.length <= 5 * 10^4`
* `answerKey[i]` is `'T'` or `'F'`
* `1 <= k <= answerKey.length`

---

# 2. Diagram

Consider:

```text
answerKey = "TFFT"
k = 1
```

Could we make the whole string all `T`?

```text
T F F T
  ↑ ↑

Need 2 F → T changes

But k = 1 ❌
```

Could we take:

```text
T F F
```

and make it all `F`?

```text
T F F
↑

Change T → F

F F F ✓
```

So length `3` is possible.

The sliding-window question becomes:

```text
Can this window become
all T or all F
using <= k changes?
```

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

Change both `F`s:

```text
TTFF
→
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

For example:

```text
"TFF"

T → F

"FFF"

length = 3
```

---

### Edge Case

```text
Input:
answerKey = "TTTT"
k = 1

Output:
4
```

No replacement is required.

"At most `k`" includes making **zero changes**.

---

# 4. Intuition & Pattern Recognition

The phrase:

> "Change at most `k` answers to maximize consecutive identical answers"

should trigger:

```text
Longest contiguous segment
        +
at most K changes
        ↓
Variable Sliding Window
```

But what makes a window valid?

Suppose:

```text
Window = "TTFFT"
```

Counts:

```text
T = 3
F = 2
```

To make everything `T`:

```text
change 2 F's
```

To make everything `F`:

```text
change 3 T's
```

Obviously, we should keep the majority character and change the minority.

So:

```text
replacements needed = min(countT, countF)
```

Therefore the window is valid when:

```text
min(countT, countF) <= k
```

That's the entire problem.

---

# 5. Simpler Version

## Step 1 — Max Consecutive Ones

LeetCode **485**

```text
[1,1,0,1,1,1]

No changes allowed.

Longest 1s = 3
```

---

## Step 2 — Max Consecutive Ones III

LeetCode **1004**

Now:

```text
0 → 1 at most k times
```

Validity:

```text
zeros <= k
```

For example:

```text
[1,1,0,0,1]
k = 2

zeros = 2

Valid ✓
```

---

## Step 3 — Current Problem

Now either character can become the target.

For target `T`:

```text
F = bad element
countF <= k
```

For target `F`:

```text
T = bad element
countT <= k
```

Combining them:

```text
min(countT, countF) <= k
```

### Progression

```text
Max Consecutive Ones
       ↓
No bad elements

Max Consecutive Ones III
       ↓
At most K zeros

Maximize Confusion
       ↓
At most K minority characters
```

That's the key conceptual jump.

---

# 6. Brute Force

Try every substring and count `T` and `F`.

```python
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans = 0

        for i in range(len(answerKey)):
            countT = 0
            countF = 0

            for j in range(i, len(answerKey)):
                if answerKey[j] == "T":
                    countT += 1
                else:
                    countF += 1

                # Minority chars are the ones we'd replace.
                if min(countT, countF) <= k:
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

Maintain counts of `T` and `F` inside the current window.

```python
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = 0
        countT = 0
        countF = 0
        ans = 0

        for right in range(len(answerKey)):

            # Add current answer to the window.
            if answerKey[right] == "T":
                countT += 1
            else:
                countF += 1

            # Minority answers are the ones we'd need to replace.
            while min(countT, countF) > k:

                # Remove leftmost answer.
                if answerKey[left] == "T":
                    countT -= 1
                else:
                    countF -= 1

                left += 1

            # Window can now be made all T or all F.
            ans = max(ans, right - left + 1)

        return ans
```

### Complexity

```text
Time  : O(N)
Space : O(1)
```

No HashMap is necessary because there are only two possible characters.

---

# 8. Step-by-Step Trace

Take:

```text
answerKey = "TTFTTFT"
k = 1
```

|  R | Char |  T |  F | `min(T,F)` |  L | Window    |   Max |
| -: | :--: | -: | -: | ---------: | -: | --------- | ----: |
|  0 |   T  |  1 |  0 |          0 |  0 | `"T"`     |     1 |
|  1 |   T  |  2 |  0 |          0 |  0 | `"TT"`    |     2 |
|  2 |   F  |  2 |  1 |          1 |  0 | `"TTF"`   |     3 |
|  3 |   T  |  3 |  1 |          1 |  0 | `"TTFT"`  |     4 |
|  4 |   T  |  4 |  1 |          1 |  0 | `"TTFTT"` | **5** |
|  5 |   F  |  4 |  2 |        2 ❌ |  0 | Invalid   |     — |

At `right = 5`:

```text
T T F T T F
L         R

T = 4
F = 2
k = 1

min(4,2) = 2 > 1 ❌
```

We need to shrink.

Remove leftmost `T`:

```text
T F T T F
L       R

T = 3
F = 2

min = 2 ❌
```

Again:

```text
F T T F
L     R

T = 2
F = 2

min = 2 ❌
```

Again, now removing an `F`:

```text
T T F
L   R

T = 2
F = 1

min = 1 <= k ✓
```

Continue with the final `T`:

```text
T T F T

T = 3
F = 1

Valid ✓

length = 4
```

Maximum remains:

```text
"TTFTT"

T = 4
F = 1

Change F → T

"TTTTT"

Answer = 5
```

---

# 9. Related Problems

| Problem                                                       | Connection                                                                                  |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **485. Max Consecutive Ones**                                 | Base problem with no replacements allowed.                                                  |
| **1004. Max Consecutive Ones III**                            | Almost identical: zeros are the bad elements and you can replace at most `k`.               |
| **424. Longest Repeating Character Replacement**              | Generalizes this idea from `{T,F}` to arbitrary characters.                                 |
| **340. Longest Substring with At Most K Distinct Characters** | Same variable-window skeleton, but validity depends on distinct characters.                 |
| **904. Fruit Into Baskets**                                   | Another longest-window problem where the validity condition is at most two distinct values. |

# The Important Connection: LeetCode 1004 → 2024 → 424

This progression is worth remembering.

### Max Consecutive Ones III

Only one possible target:

```text
make everything 1

bad elements = zeros

zeros <= k
```

### Maximize the Confusion

Two possible targets:

```text
make everything T
OR
make everything F

bad elements = minority

min(T, F) <= k
```

### Longest Repeating Character Replacement

Many possible target characters:

```text
"AABABBA"

Make everything equal to
the most frequent character.

bad elements =
windowSize - maxFrequency

windowSize - maxFrequency <= k
```

So the general concept is:

```text
Window size - elements we KEEP <= k
```

For this problem:

```text
elements we keep = max(countT, countF)

replacements =
windowSize - max(countT, countF)

             =
min(countT, countF)
```

That is the pattern to remember for interviews:

> **Longest window + at most K replacements → count how many elements in the window don't match the best target.**
