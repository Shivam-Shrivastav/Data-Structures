# 389. Find the Difference

**Pattern:** Frequency Counting / HashMap
**Difficulty:** Easy

---

## 1. Problem Statement

You are given two strings `s` and `t`.

`t` is created by:

1. Taking all characters from `s`.
2. Rearranging them in any order.
3. Adding **exactly one extra character**.

Return that extra character.

### Example

```text
s = "abcd"
t = "abcde"

Output: "e"
```

### Constraints

```text
0 <= s.length <= 1000
t.length == s.length + 1

s and t contain lowercase English letters.
```

The important detail is that characters **can repeat**, so simply comparing sets is not sufficient.

---

# 2. Diagram

```text
s = "abcd"
t = "abcde"

Frequency:

        a  b  c  d  e
s       1  1  1  1  0
t       1  1  1  1  1
                        ↑
                     extra
```

Another example with duplicates:

```text
s = "aabb"
t = "ababc"

        a  b  c
s       2  2  0
t       2  2  1
              ↑
            extra
```

So conceptually:

```text
frequency(t) - frequency(s)
              ↓
        one character left
```

---

# 3. Example I/O

### Example 1 — Typical

```text
Input:
s = "abcd"
t = "abcde"

Output:
"e"
```

`t` contains everything from `s`, plus `e`.

### Example 2 — Edge Case

```text
Input:
s = ""
t = "y"

Output:
"y"
```

There were no original characters, so `y` must be the added one.

### Example 3 — Duplicate characters

```text
Input:
s = "aabb"
t = "ababc"

Output:
"c"
```

The frequencies of `a` and `b` cancel, leaving `c`.

---

# 4. Intuition & Pattern Recognition

The strongest signal is:

> `t` contains all characters from `s` + exactly one extra character.

This is a **difference between two collections** problem.

Your first thought can be:

```text
Count characters in s
        ↓
Remove/match characters from t
        ↓
Whatever remains is extra
```

So the natural pattern is:

> **Frequency Counting**

### Interview thinking

```text
Same elements
+ arbitrary ordering
+ duplicates possible
+ one extra element

→ Don't compare positions.
→ Compare frequencies.
```

But there is an even cleaner observation:

> Every character appears the same number of times in both strings except one.

That allows an **XOR** solution with `O(1)` extra space.

---

# 5. Simpler Version

## Simpler 1: Contains Duplicate — 217

Given an array, determine whether any value appears more than once.

```text
[1,2,3,1]

count / set
      ↓
1 appears again
```

This introduces using hashing to track occurrences.

---

## Simpler 2: Valid Anagram — 242

Given `s` and `t`, determine whether they contain exactly the same characters with exactly the same frequencies.

```text
s = "anagram"
t = "nagaram"

freq(s) == freq(t)
```

This is the **closest simpler problem**.

Find the Difference is basically:

```text
Valid Anagram:

freq(s) == freq(t)


Find the Difference:

freq(s) + ONE CHARACTER == freq(t)
```

### Thinking progression

```text
Contains Duplicate
        ↓
Can I track occurrences?

Valid Anagram
        ↓
Can I compare frequencies
between two strings?

Find the Difference
        ↓
Frequencies are identical
except for one extra occurrence.
```

---

# 6. Brute Force

For every character in `t`, search for a matching character in `s` and remove it.

```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        chars = list(s)

        for ch in t:
            if ch in chars:
                chars.remove(ch)
            else:
                return ch
```

For example:

```text
s = "abcd"
t = "abcde"

chars = [a,b,c,d]

a → remove → [b,c,d]
b → remove → [c,d]
c → remove → [d]
d → remove → []
e → not found → return e
```

### Complexity

```text
Time:  O(N²)
Space: O(N)
```

Both membership lookup and removal from a list can cost `O(N)`.

---

# 7. Optimal Solution

## Approach 1 — Frequency Counting

This is the most direct solution for the **frequency counting pattern**.

```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = {}

        # Count characters from s.
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        # Match characters from t.
        for ch in t:
            if count.get(ch, 0) == 0:
                return ch

            count[ch] -= 1
```

### Why does this work?

Consider:

```text
s = "aabb"
t = "ababc"
```

Build:

```text
count = {
    a: 2,
    b: 2
}
```

Then consume `t`:

```text
a → a:1
b → b:1
a → a:0
b → b:0

c → count[c] = 0
    ↑
    extra character
```

### Complexity

```text
Time:  O(N)
Space: O(N)
```

Since only lowercase English letters are allowed, technically the number of possible keys is bounded by 26, so auxiliary space can also be considered `O(1)` with respect to input size.

---

## Approach 2 — XOR

This is the cleanest space-optimal solution.

XOR has three useful properties:

```text
x ^ x = 0

x ^ 0 = x

order doesn't matter
```

So XOR every character from both strings:

```text
s = "abcd"
t = "abcde"

a ^ b ^ c ^ d
^
a ^ b ^ c ^ d ^ e

Pairs cancel:

(a^a) ^ (b^b) ^ (c^c) ^ (d^d) ^ e

= 0 ^ 0 ^ 0 ^ 0 ^ e

= e
```

### Python

```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0

        for ch in s:
            result ^= ord(ch)

        for ch in t:
            result ^= ord(ch)

        return chr(result)
```

### Complexity

```text
Time:  O(N)
Space: O(1)
```

### Which approach in an interview?

For this exact problem, **XOR is excellent** because every character has a matching copy except exactly one.

For the broader pattern, remember frequency counting because it generalizes much better.

---

# 8. Step-by-Step Trace

Take:

```text
s = "abcd"
t = "abcde"
```

Using frequency counting:

### Build frequencies from `s`

| Character | Count |
| --------- | ----: |
| `a`       |     1 |
| `b`       |     1 |
| `c`       |     1 |
| `d`       |     1 |

Now process `t`:

| `ch` | Count before | Action             | Count after |
| ---- | -----------: | ------------------ | ----------: |
| `a`  |            1 | Match              |           0 |
| `b`  |            1 | Match              |           0 |
| `c`  |            1 | Match              |           0 |
| `d`  |            1 | Match              |           0 |
| `e`  |            0 | **Extra → return** |           — |

Answer:

```text
"e"
```

---

# 9. Related Problems

| Problem                      | Connection                                                         |
| ---------------------------- | ------------------------------------------------------------------ |
| **217. Contains Duplicate**  | Basic HashSet/frequency tracking.                                  |
| **242. Valid Anagram**       | Compare complete character frequencies between two strings.        |
| **389. Find the Difference** | Same frequencies except exactly one extra occurrence.              |
| **136. Single Number**       | Same XOR cancellation idea: pairs cancel and one value remains.    |
| **49. Group Anagrams**       | Uses character frequency/signature to identify equivalent strings. |

## Quick Revision

```text
Signal:

t = shuffled s + one extra character

Think:

Same characters
+ duplicates possible
+ order irrelevant
        ↓
Frequency Counting

Frequency solution:
count s
consume using t
first unmatched char = answer

Special optimization:
Everything occurs equally except one
        ↓
XOR all characters
        ↓
matching characters cancel
        ↓
extra character remains

Time:  O(N)
Space:
HashMap → O(N) / bounded alphabet
XOR     → O(1)
```

**Key connection:** `Find the Difference` is essentially **Valid Anagram with exactly one extra character**, while its XOR solution is the string equivalent of **Single Number**.
