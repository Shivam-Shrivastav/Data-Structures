# **880. Decoded String at Index (Greedy + Reverse Simulation)**

---

# 1. Problem Statement

Given an encoded string `s` and an integer `k`, imagine decoding the string using these rules:

* Letters are appended directly to the decoded string.
* A digit `d` means **repeat the entire decoded string built so far `d` times**.

Return the **k-th character (1-indexed)** in the decoded string.

> **Important:** You **must not actually build the decoded string**, because it can become astronomically large.

### Constraints

* `2 <= s.length <= 100`
* `s` consists of lowercase English letters and digits `2` to `9`.
* `1 <= k <= 10^9`
* The decoded string is guaranteed to have at least `k` characters.

---

## Example

```text
Input:
s = "leet2code3"
k = 10

Decoded String:

leet
↓

leetleet

↓

leetleetcode

↓

leetleetcodeleetleetcodeleetleetcode

10th character = "o"

Output:
"o"
```

---

# 2. Diagram

```text
s = "ha22"

Read characters

h          size = 1
ha         size = 2
haha       size = 4
hahahaha   size = 8

We never build this string.

Instead we only keep

size = 8

Then work backwards.
```

---

# 3. Example I/O

### Example 1

```text
Input:
s = "leet2code3"
k = 10

Output:
"o"
```

Explanation

```text
Decoded:

leetleetcodeleetleetcodeleetleetcode

10th character = o
```

---

### Example 2

```text
Input:
s = "ha22"
k = 5

Decoded

ha
↓

haha

↓

hahahaha

Output:
"h"
```

---

### Edge Case

```text
Input:
s = "a2345678999999999999999"
k = 1

Output:
"a"
```

Notice the decoded string is impossibly large, but the answer is still easy.

---

# 4. Intuition & Pattern Recognition

## Signals

* Output can be **10⁹+ characters**
* Cannot build the final string
* Need only one character
* Repetitions of the whole prefix

This usually hints:

> **Track lengths, not strings.**

---

### Key Observation

Suppose

```text
abc3

↓

abcabcabc
```

Length becomes

```text
3

↓

9
```

If we want the **8th** character,

it's the same as asking

```text
8 % 3 = 2

↓

2nd character of "abc"
```

So repeated blocks map back into the original prefix.

---

### Interview Thinking

Don't think

```text
Build string
```

Think

```text
Build only LENGTH

Then walk backwards

Undo every operation.
```

---

# 5. Simpler Version

## Simpler Question

```
abc3
```

Decoded

```
abcabcabc
```

Find the 8th character.

Instead of building,

```
8 % 3 = 2

↓

2nd character of abc
```

---

## Slightly Harder

```
ab2c
```

Decoded

```
ababc
```

Again,

track only sizes.

---

## Full Question

```
leet2code3
```

Multiple repetitions happen.

Walk backwards,

undo each multiplication.

---

### Related Simpler Problems

* **38. Count and Say** → encoding/decoding idea.
* **394. Decode String** → actually build decoded string.
* **880. Decoded String at Index** → impossible to build, use reverse simulation.

---

# 6. Brute Force

Idea

Actually decode the string.

Then return

```python
decoded[k-1]
```

### Problem

Decoded string can exceed

```
10^18 characters
```

Impossible.

### Complexity

Time

```
Exponential / Huge
```

Space

```
Huge
```

Not feasible.

---

# 7. Optimal Solution (Greedy + Reverse Simulation)

## Idea

### Phase 1

Compute decoded length only.

Example

```
leet2code3

l ->1
e ->2
e ->3
t ->4
2 ->8
c ->9
o ->10
d ->11
e ->12
3 ->36
```

Now

```
decoded length = 36
```

---

### Phase 2

Walk backwards.

Whenever

### Letter

Reduce size by 1.

If

```
k == size
```

that letter is the answer.

---

### Digit

Suppose

```
size = 36

digit = 3
```

Before multiplication,

```
previous size = 12
```

So

```
k %= 12
```

because every repeated block is identical.

Then continue.

---

## Python Solution

```python
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0

        # Compute decoded length
        for ch in s:
            if ch.isdigit():
                size *= int(ch)
            else:
                size += 1

        # Walk backwards
        for ch in reversed(s):
            # Map k into the current decoded prefix
            k %= size

            # If k == 0 and current character is a letter,
            # this is the answer.
            if ch.isalpha() and k == 0:
                return ch

            if ch.isdigit():
                # Undo the expansion
                size //= int(ch)
            else:
                # Remove this character
                size -= 1
```

---

## Complexity

Time

```
O(n)
```

Two passes.

Space

```
O(1)
```

No decoded string stored.

---

# 8. Step-by-Step Trace

Input

```
s = "ha22"
k = 5
```

---

### Forward Pass

| Character | Decoded Length |
| --------- | -------------- |
| h         | 1              |
| a         | 2              |
| 2         | 4              |
| 2         | 8              |

---

### Reverse Pass

| Character | Size | k before | k %= size | Action        |
| --------- | ---- | -------- | --------- | ------------- |
| 2         | 8    | 5        | 5         | size = 4      |
| 2         | 4    | 5        | 1         | size = 2      |
| a         | 2    | 1        | 1         | size = 1      |
| h         | 1    | 1        | 0         | k==0 → Answer |

Output

```
"h"
```

---

# 9. Related Problems

1. **394. Decode String**
   Decode the entire string using a stack.

2. **443. String Compression**
   Manipulates encoded string representations.

3. **38. Count and Say**
   Generate encoded sequences iteratively.

4. **880. Decoded String at Index**
   Reverse simulation using decoded lengths.

5. **936. Stamping The Sequence**
   Another problem that solves the process by working backwards instead of forwards.

---

# Interview Cheat Sheet

## Recognition Keywords

* Decoded string is **too large**.
* Need only **one character**.
* Repeated prefixes.
* Cannot construct the output.

---

## Core Insight

```
Forward:
Only compute decoded length.

Backward:
Undo every operation.

Digit:
size /= digit
k %= size

Letter:
If k == 0
return letter

Else
size--
```

---

## Pattern

```text
Forward Pass
↓

Compute decoded size

↓

Reverse Pass

↓

Undo multiplication

↓

Undo letters

↓

Return answer
```

---

## Common Mistakes

* ❌ Building the decoded string (causes memory/time issues).
* ❌ Forgetting `k %= size` **before** processing each character in the reverse pass.
* ❌ Forgetting that `k == 0` represents the **last character** of the current decoded prefix after the modulo operation.
* ❌ Dividing `size` after processing a digit in the wrong order.
