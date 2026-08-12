# Check If a String Contains All Binary Codes of Size K (LeetCode 1461)

**Pattern:** Fixed Size Sliding Window + HashSet + Rolling Window

> This is one of the most important **Fixed Size Sliding Window** problems because it teaches how to generate all windows of length `k` efficiently and avoid duplicate work.

(Reference sliding window notes: )

---

# 1. Problem Statement

Given a binary string `s` and an integer `k`, determine whether **every possible binary code of length `k`** appears as a substring of `s`.

Return:

* `true` if all `2^k` binary strings of length `k` exist.
* `false` otherwise.

### Constraints

* `1 <= s.length <= 5 × 10⁵`
* `1 <= k <= 20`
* String contains only `'0'` and `'1'`

Need an efficient solution close to **O(N)**.

---

# 2. Diagram

Example

```text
s = "00110110"
k = 2

Window size = 2

0 0 1 1 0 1 1 0
|_|

00

  |_|
 01

    |_|
    11

      |_|
      10

        |_|
        01

          |_|
          11

            |_|
            10
```

Collected windows

```text
00
01
11
10
```

Possible binary strings of length 2

```text
00
01
10
11
```

Everything exists.

Answer = True

---

# 3. Example I/O

### Example 1

```text
Input:
s = "00110110"
k = 2

Output:
true
```

Explanation

Found

```text
00
01
10
11
```

All four binary codes exist.

---

### Example 2

```text
Input:
s = "0110"
k = 2

Output:
false
```

Only

```text
01
11
10
```

Missing

```text
00
```

---

### Edge Case

```text
Input:
s = "0"
k = 1

Output:
false
```

Need

```text
0
1
```

Only `0` exists.

---

# 4. Intuition & Pattern Recognition

### Signals

Whenever you see

* Check every substring of size K
* Window size never changes
* Need efficient scanning

Think

> **Fixed Size Sliding Window**

Unlike variable windows, this problem never expands or shrinks dynamically.

Window is always exactly `k`.

---

### Interview Thinking

Tell yourself

```text
Every substring of length k is a candidate binary code.

Instead of generating all possible binary strings,

I'll scan every window of length k exactly once.

Store each unique window.

Finally,

if unique windows == 2^k

return True.
```

---

# 5. Simpler Version

## Simpler Question 1

### Maximum Average Subarray I

```text
Move fixed window

Remove left

Add right
```

Learns fixed-size window movement.

---

## Simpler Question 2

### Count Distinct Substrings of Size K

Store every window in a HashSet.

Very similar.

---

## Current Question

Now instead of counting windows,

we must verify whether **every possible binary code** exists.

Thinking progression

```text
Fixed Window

↓

Generate every window

↓

Store unique windows

↓

Compare with total possible codes

↓

Check If String Contains All Binary Codes
```

---

# 6. Brute Force

Generate every binary string of length `k`.

Example

```text
k = 3

000
001
010
011
100
101
110
111
```

For each code,

search entire string.

```text
for every binary code
    if code not found in s
        return False
```

### Complexity

Generate codes

```text
2^k
```

Searching each

```text
O(N)
```

Overall

```text
Time = O(N × 2^k)

Space = O(2^k)
```

Very slow.

---

# 7. Optimal Solution

## Approach 1 (Easy Interview Solution)

Store every substring of size `k`.

### Python

```python
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        # Impossible if there aren't enough windows
        if len(s) - k + 1 < (1 << k):
            return False

        seen = set()

        # Generate every window of length k
        for i in range(len(s) - k + 1):
            seen.add(s[i:i+k])

        # Need exactly 2^k unique codes
        return len(seen) == (1 << k)
```

### Complexity

```text
Time : O(N × K)
Space: O(2^k × K)
```

Why `O(N × K)`?

Each slice

```python
s[i:i+k]
```

copies `k` characters.

---

# 7. Optimal Solution (Rolling Hash / Bitmask)

Instead of storing strings,

store integers.

Example

```text
101

↓

5
```

Now every window becomes an integer.

This avoids substring creation.

---

### Idea

Maintain

```text
Current k-bit number
```

When window moves

```text
Shift left

Add new bit

Remove extra bit
```

Exactly like a rolling hash.

---

### Python

```python
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        if len(s) - k + 1 < (1 << k):
            return False

        seen = set()

        mask = (1 << k) - 1
        value = 0

        for i, ch in enumerate(s):

            # Shift previous bits left and add current bit
            value = ((value << 1) & mask) | int(ch)

            # Window becomes valid after k characters
            if i >= k - 1:
                seen.add(value)

        return len(seen) == (1 << k)
```

---

### Complexity

```text
Time : O(N)

Space : O(2^k)
```

No substring copying.

---

# 8. Step-by-Step Trace

Example

```text
s = "00110110"
k = 2
```

### String Solution

| Window | Seen           |
| ------ | -------------- |
| 00     | {00}           |
| 01     | {00,01}        |
| 11     | {00,01,11}     |
| 10     | {00,01,11,10}  |
| 01     | Already exists |
| 11     | Already exists |
| 10     | Already exists |

Final

```text
Seen =

00
01
10
11

Count = 4

2² = 4

Answer = True
```

---

### Rolling Bitmask Trace

Mask

```text
11 (binary)

mask = 3
```

| Index | Char | Value (Binary) | Stored |
| ----- | ---- | -------------- | ------ |
| 0     | 0    | 0              | -      |
| 1     | 0    | 00             | 0      |
| 2     | 1    | 01             | 1      |
| 3     | 1    | 11             | 3      |
| 4     | 0    | 10             | 2      |
| 5     | 1    | 01             | 1      |
| 6     | 1    | 11             | 3      |
| 7     | 0    | 10             | 2      |

Seen integers

```text
0
1
2
3
```

Exactly four values.

---

# 9. Related Problems

| Problem                                                           | Connection                                                            |
| ----------------------------------------------------------------- | --------------------------------------------------------------------- |
| **643. Maximum Average Subarray I**                               | Simplest fixed-size sliding window.                                   |
| **1456. Maximum Number of Vowels in a Substring of Given Length** | Fixed window with character updates.                                  |
| **187. Repeated DNA Sequences**                                   | Uses rolling hash/bitmask on fixed-length substrings.                 |
| **567. Permutation in String**                                    | Fixed window with frequency counting instead of storing windows.      |
| **30. Substring with Concatenation of All Words**                 | Advanced fixed-size sliding window with hashing and multiple windows. |

---

# Key Interview Takeaways

* **Pattern:** Fixed Size Sliding Window.
* **Invariant:** Window size always remains `k`.
* **Core idea:** Visit every substring of length `k` exactly once.
* **Optimization:** Store integer bitmasks instead of substring copies for true `O(N)` time.
* **Important Observation:** If `len(s) - k + 1 < 2^k`, it's impossible to contain all binary codes, so return `False` immediately.
