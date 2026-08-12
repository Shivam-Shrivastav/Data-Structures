# 340. Longest Substring with At Most K Distinct Characters

**Pattern:** Variable-Size Sliding Window + Frequency HashMap

This is the **generalized version of Fruit Into Baskets**:

```text
Fruit Into Baskets       → at most 2 distinct
This problem             → at most K distinct
```

It also builds naturally on **Longest Substring Without Repeating Characters**, where the window is constrained by uniqueness. 

---

# 1. Problem Statement

Given a string `s` and an integer `k`, return the **length of the longest substring containing at most `k` distinct characters**.

A substring must be **contiguous**.

### Example

```text
s = "eceba"
k = 2

Answer = 3

Longest valid substring = "ece"
Distinct = {e, c}
```

### Key Constraint

The window may contain duplicate characters:

```text
"eeeeecc"

Distinct characters = 2
Window length        = 7
```

We care about the **number of distinct characters**, not their frequencies individually.

---

# 2. Diagram

```text
s = "eceba"
k = 2

Expand →

e c e
L   R

freq = {e:2, c:1}
distinct = 2       ✓

Window = "ece"
Length = 3


Next:

e c e b
L     R

freq = {e:2, c:1, b:1}
distinct = 3       ✗

Need at most 2.

Shrink →

  c e b
  L   R

freq = {e:1, c:1, b:1}
Still 3             ✗

Shrink →

    e b
    L R

freq = {e:1, b:1}
Now 2               ✓
```

The window invariant is:

> **`len(freq) <= k`**

---

# 3. Example I/O

### Example 1 — Typical

```text
Input:
s = "eceba"
k = 2

Output:
3
```

Because:

```text
"ece"

length = 3
distinct = {e, c}
```

---

### Example 2

```text
Input:
s = "aa"
k = 1

Output:
2
```

`"aa"` contains only one distinct character.

---

### Edge Case

```text
Input:
s = "abc"
k = 0

Output:
0
```

No non-empty substring can contain at most `0` distinct characters.

---

# 4. Intuition & Pattern Recognition

Look for these signals:

```text
Longest substring
      +
contiguous
      +
at most K distinct
      ↓
Variable Sliding Window
```

Why variable-size?

Because we don't know the optimal window size.

We want to:

```text
Expand as much as possible
        ↓
Too many distinct?
        ↓
Shrink until valid
        ↓
Continue expanding
```

### Interview thought process

When you read:

> "Longest substring with at most K distinct..."

Immediately think:

> "Maintain a sliding window and a frequency map. Expand right. If distinct count exceeds K, shrink left until valid again. Track the maximum valid window."

That's essentially the whole problem.

---

# 5. Simpler Version

There are several problems that naturally lead to this one.

### Step 1 — Longest Substring Without Repeating Characters

LeetCode **3**

```text
s = "abcabcbb"
```

Constraint:

```text
Every character must occur at most once.
```

You learn:

```text
right expands
left shrinks
maintain valid window
```

A `HashSet` is enough because we're primarily detecting duplicates.

---

### Step 2 — Longest Substring with At Most Two Distinct Characters

LeetCode **159**

Now duplicates are allowed:

```text
"eceeeeee"
```

We only care that:

```text
distinct <= 2
```

So we need frequencies:

```text
e → 7
c → 1
```

This introduces:

> **Frequency HashMap + variable window**

---

### Step 3 — Fruit Into Baskets

LeetCode **904**

Exactly the same algorithm:

```text
fruits = [1,2,1,2,3]

At most 2 fruit types
```

Think of:

```text
fruit type     = character
2 baskets      = k = 2
```

So Fruit Into Baskets is basically:

> **Longest Subarray with At Most 2 Distinct Values**

---

### Step 4 — Current Problem

Generalize:

```text
At most 2
    ↓
At most K
```

That's it.

```text
Longest Substring Without Repeating
            ↓
Variable Sliding Window
            ↓
At Most 2 Distinct
            ↓
Fruit Into Baskets
            ↓
At Most K Distinct
```

---

# 6. Brute Force

Generate every substring and count its distinct characters.

```python
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        ans = 0

        for i in range(len(s)):
            seen = set()

            for j in range(i, len(s)):
                seen.add(s[j])

                if len(seen) > k:
                    break

                ans = max(ans, j - i + 1)

        return ans
```

### Complexity

```text
Time  : O(N²)
Space : O(K) approximately
```

We try every starting position and expand until the substring becomes invalid.

---

# 7. Optimal Solution

Maintain:

```text
left
right
freq
ans
```

The invariant is:

```text
len(freq) <= k
```

### Python

```python
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        if k == 0:
            return 0

        freq = defaultdict(int)
        left = 0
        ans = 0

        for right in range(len(s)):

            # Add current character to the window
            freq[s[right]] += 1

            # Too many distinct characters
            while len(freq) > k:

                # Remove one occurrence of the left character
                freq[s[left]] -= 1

                # Character no longer exists in window
                if freq[s[left]] == 0:
                    del freq[s[left]]

                left += 1

            # Current window is valid
            ans = max(ans, right - left + 1)

        return ans
```

### Complexity

```text
Time  : O(N)
Space : O(K)
```

Each character enters the window once and leaves at most once.

---

# 8. Step-by-Step Trace

Take:

```text
s = "eceba"
k = 2
```

| `right` | Char | `freq` after add | Shrink? | `left` | Valid Window | `ans` |
| ------: | :--: | :--------------- | :-----: | -----: | :----------- | ----: |
|       0 |   e  | `{e:1}`          |    No   |      0 | `"e"`        |     1 |
|       1 |   c  | `{e:1,c:1}`      |    No   |      0 | `"ec"`       |     2 |
|       2 |   e  | `{e:2,c:1}`      |    No   |      0 | `"ece"`      | **3** |
|       3 |   b  | `{e:2,c:1,b:1}`  |   Yes   |      0 | Invalid      |     3 |

At `right = 3`:

```text
e c e b
L     R

{e:2, c:1, b:1}

3 distinct > 2
```

Shrink once:

```text
Remove e

freq = {e:1, c:1, b:1}

  c e b
  L   R

Still 3 distinct
```

Shrink again:

```text
Remove c

freq[c] = 0
delete c

freq = {e:1, b:1}

    e b
    L R

2 distinct ✓
```

Then `right = 4`, character `a`:

```text
e b a
L   R

{e:1, b:1, a:1}

3 > 2
```

Remove `e`:

```text
b a
L R

{b:1, a:1}

Valid ✓
```

Maximum encountered:

```text
"ece"

length = 3
```

So:

```text
Answer = 3
```

---

# 9. Related Problems

| Problem                                                         | Connection                                                                              |
| --------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **3. Longest Substring Without Repeating Characters**           | Variable sliding window where duplicates make the window invalid.                       |
| **159. Longest Substring with At Most Two Distinct Characters** | Same problem with `K = 2`.                                                              |
| **904. Fruit Into Baskets**                                     | Same algorithm on an integer array with `K = 2`.                                        |
| **992. Subarrays with K Different Integers**                    | Takes this pattern further to count subarrays with **exactly K** distinct values.       |
| **76. Minimum Window Substring**                                | Frequency-map sliding window, but asks for the smallest window satisfying requirements. |

---

# Key Interview Takeaway

Memorize the generic **At Most K** template:

```python
for right in range(len(s)):

    # expand
    freq[s[right]] += 1

    # shrink until valid
    while len(freq) > k:
        freq[s[left]] -= 1

        if freq[s[left]] == 0:
            del freq[s[left]]

        left += 1

    # process valid window
    ans = max(ans, right - left + 1)
```

The mental model is:

```text
Longest + At Most K
        ↓
Expand greedily
        ↓
distinct > K?
        ↓
Shrink until distinct <= K
        ↓
Record maximum
```

And the key distinction:

```text
Longest Substring Without Repeating
→ duplicates matter
→ each char allowed once

At Most K Distinct
→ duplicates DON'T matter
→ number of TYPES matters

Fruit Into Baskets
→ At Most K Distinct with K = 2
```

Once **At Most K Distinct** becomes automatic, **Subarrays with Exactly K Distinct Integers** is the natural next step: `exactly(K) = atMost(K) - atMost(K - 1)`.
