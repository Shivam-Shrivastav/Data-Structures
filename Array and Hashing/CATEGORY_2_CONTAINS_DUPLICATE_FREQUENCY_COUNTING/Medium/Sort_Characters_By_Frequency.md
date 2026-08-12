# 451. Sort Characters By Frequency

**Pattern:** Frequency Counting + Sorting / Bucket Sort
**Difficulty:** Medium

---

## 1. Problem Statement

Given a string `s`, rearrange its characters so that characters with **higher frequency appear before characters with lower frequency**.

Characters with the same frequency can appear in **any order**.

### Example

```text
s = "tree"

Frequency:
t → 1
r → 1
e → 2

Output:
"eert"
```

`"eetr"` is also valid because `t` and `r` have equal frequency.

### Constraints

```text
1 <= s.length <= 5 * 10^5
s contains uppercase/lowercase letters and digits.
```

The large input size makes repeatedly counting characters inefficient.

---

# 2. Diagram

```text
s = "tree"

          Frequency Count
                ↓

        ┌───────┬───────┐
        │ char  │ freq  │
        ├───────┼───────┤
        │   t   │   1   │
        │   r   │   1   │
        │   e   │   2   │
        └───────┴───────┘

                ↓
       Sort by frequency ↓

            e → 2
            t → 1
            r → 1

                ↓
        Reconstruct string

          "ee" + "t" + "r"

                ↓

              "eetr"
```

The key transformation is:

```text
String
  ↓
Frequency Map
  ↓
Order characters by frequency
  ↓
Repeat each character frequency times
```

---

# 3. Example I/O

### Example 1 — Typical

```text
Input:
s = "tree"

Output:
"eert"
```

Because:

```text
e → 2
t → 1
r → 1
```

`e` must appear before `t` and `r`.

---

### Example 2

```text
Input:
s = "cccaaa"

Output:
"cccaaa"
```

But:

```text
"aaaccc"
```

is also valid because:

```text
c → 3
a → 3
```

Equal frequencies can appear in any order.

---

### Edge Case

```text
Input:
s = "Aabb"

Output:
"bbAa"
```

Frequency:

```text
b → 2
A → 1
a → 1
```

Uppercase and lowercase characters are different.

---

# 4. Intuition & Pattern Recognition

The strongest signal is:

> **Rearrange elements according to frequency.**

Think:

```text
Count frequency
      ↓
Rank/group by frequency
      ↓
Reconstruct answer
```

Unlike **1636. Sort Array by Increasing Frequency**, here the requirement is:

```text
451:
frequency ↓

1636:
frequency ↑
value ↓ on ties
```

Another important observation:

We don't actually care about sorting **every character occurrence**.

For:

```text
"aaaaaaaaaabbbcc"
```

instead of sorting all 15 characters, think:

```text
a → 10
b → 3
c → 2
```

Sort these **unique character-frequency pairs**, then rebuild.

### Interview thinking

> "The output order depends only on character frequency. I'll count each character once, sort the unique characters by decreasing frequency, then append each character `freq` times."

That immediately gives a clean solution.

---

# 5. Simpler Version

## Step 1 — Frequency Counting

A simpler problem is **242. Valid Anagram**.

Given:

```text
s = "anagram"
```

build:

```text
a → 3
n → 1
g → 1
r → 1
m → 1
```

This teaches:

> Use a HashMap when the problem depends on occurrence counts.

---

## Step 2 — Sort Array by Increasing Frequency

**1636. Sort Array by Increasing Frequency** is almost the numeric version of this problem.

There:

```text
nums = [1,1,2,2,2,3]

1 → 2
2 → 3
3 → 1
```

Then sort according to frequency.

The difference:

```text
1636 → frequency ascending + value tie-break
451  → frequency descending
```

---

## Step 3 — Current Problem

Instead of directly sorting occurrences:

```text
t r e e
```

compress first:

```text
t → 1
r → 1
e → 2
```

Order:

```text
e → 2
t → 1
r → 1
```

Expand:

```text
ee + t + r
```

Result:

```text
eetr
```

### Thinking progression

```text
Valid Anagram
    ↓
Learn frequency map

Sort Array by Increasing Frequency
    ↓
Learn frequency-based ordering

Current problem
    ↓
Count → order unique chars → reconstruct

Sort Characters By Frequency
```

---

# 6. Brute Force

For every character, calculate its frequency by scanning the entire string.

Then sort characters according to that frequency.

```python
class Solution:
    def frequencySort(self, s: str) -> str:

        def frequency(ch):
            count = 0

            for c in s:
                if c == ch:
                    count += 1

            return count

        return ''.join(sorted(s, key=lambda ch: -frequency(ch)))
```

For every character we potentially scan the string again.

```text
Frequency calculations → O(N²)
Sorting               → O(N log N)

Time  → O(N²)
Space → O(N)
```

The obvious optimization is:

> Calculate each frequency **once**.

---

# 7. Optimal Solution — HashMap + Sorting

```python
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:

        # Count frequency of each character
        freq = Counter(s)

        # Sort unique characters by decreasing frequency
        chars = sorted(freq, key=lambda ch: freq[ch], reverse=True)

        # Repeat each character according to its frequency
        return ''.join(ch * freq[ch] for ch in chars)
```

For:

```text
s = "tree"

freq =
{
    't': 1,
    'r': 1,
    'e': 2
}
```

Then:

```text
chars = ['e', 't', 'r']
```

Finally:

```text
'e' * 2 → "ee"
't' * 1 → "t"
'r' * 1 → "r"

"ee" + "t" + "r"
      ↓
    "eetr"
```

### Complexity

Let:

```text
N = length of string
K = number of unique characters
```

Counting:

```text
O(N)
```

Sorting unique characters:

```text
O(K log K)
```

Building answer:

```text
O(N)
```

Therefore:

```text
Time  → O(N + K log K)
Space → O(N + K)
```

Since `K <= N`, this is at most **O(N log N)** time.

---

# 8. Step-by-Step Trace

Take:

```text
s = "tree"
```

### Step 1: Count

| Character read | Frequency map     |
| -------------- | ----------------- |
| `t`            | `{t:1}`           |
| `r`            | `{t:1, r:1}`      |
| `e`            | `{t:1, r:1, e:1}` |
| `e`            | `{t:1, r:1, e:2}` |

Final:

```text
t → 1
r → 1
e → 2
```

### Step 2: Sort unique characters

Before:

```text
[t, r, e]
```

Compare by frequency descending:

```text
e → 2
t → 1
r → 1
```

So:

```text
chars = [e, t, r]
```

`r,t` would also be valid for the final two positions.

### Step 3: Reconstruct

| `ch` | `freq[ch]` | Add    | Answer   |
| ---- | ---------: | ------ | -------- |
| `e`  |          2 | `"ee"` | `"ee"`   |
| `t`  |          1 | `"t"`  | `"eet"`  |
| `r`  |          1 | `"r"`  | `"eetr"` |

Answer:

```text
"eetr"
```

---

# 9. Bucket Sort — Important Alternative

There is an even stronger observation:

For a string of length `N`, character frequency can only be:

```text
1, 2, 3, ... N
```

So frequency itself can act as a **bucket index**.

For:

```text
s = "tree"
```

we have:

```text
t → 1
r → 1
e → 2
```

Buckets:

```text
frequency

3 → []
2 → [e]
1 → [t, r]
```

Traverse from high frequency to low:

```text
2 → "ee"
1 → "t", "r"

→ "eetr"
```

### Code

```python
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:

        freq = Counter(s)

        # Index represents frequency
        buckets = [[] for _ in range(len(s) + 1)]

        for ch, count in freq.items():
            buckets[count].append(ch)

        result = []

        # Higher frequency first
        for count in range(len(s), 0, -1):
            for ch in buckets[count]:
                result.append(ch * count)

        return ''.join(result)
```

### Complexity

```text
Count       → O(N)
Build bucket→ O(K)
Traverse    → O(N)
Output      → O(N)

Time  → O(N)
Space → O(N)
```

For interviews, **Counter + sorting** is usually the cleanest initial solution. Mention bucket sort when the interviewer asks whether sorting can be eliminated.

---

# 10. Related Problems

| Problem                                      | Connection                                                                                                     |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **242. Valid Anagram**                       | Fundamental frequency-map problem.                                                                             |
| **1636. Sort Array by Increasing Frequency** | Same frequency-counting + sorting idea, but ascending frequency with a tie-breaker.                            |
| **347. Top K Frequent Elements**             | Count frequencies, then retrieve elements with highest frequencies using heap/buckets.                         |
| **692. Top K Frequent Words**                | Frequency ranking with an additional lexicographical tie-breaker.                                              |
| **767. Reorganize String**                   | Frequency counting becomes harder: high-frequency characters must be rearranged so adjacent characters differ. |

## Quick Revision

```text
451. Sort Characters By Frequency

Signal:
"Arrange based on occurrence count"

Pattern:
Frequency Counting + Sorting

Counter:
freq = Counter(s)

Sort unique characters:
sorted(freq, key=lambda ch: freq[ch], reverse=True)

Reconstruct:
''.join(ch * freq[ch] for ch in chars)

Sorting:
Time  → O(N + K log K)

Bucket Sort:
Time  → O(N)

Core idea:

COUNT → ORDER BY FREQUENCY ↓ → RECONSTRUCT
```

The main progression to remember is:

**Valid Anagram → Sort Array by Increasing Frequency → Sort Characters By Frequency → Top K Frequent Elements → Reorganize String.**
