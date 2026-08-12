# 1456. Maximum Number of Vowels in a Substring of Given Length

**Pattern:** Fixed Size Sliding Window

---

# 1. Problem Statement

Given a string `s` and an integer `k`, return the **maximum number of vowels** in any substring of length `k`.

A substring must be **contiguous**, and only the vowels `{a, e, i, o, u}` are counted.

### Constraints

* `1 <= s.length <= 10^5`
* `1 <= k <= s.length`
* `s` contains lowercase English letters.
* Expected solution: **O(N)**

---

# 2. Diagram

Example:

```text
s = "abciiidef"
k = 3

Window 1
[a b c]
 1 vowel

Slide →

[a b c]
   [b c i]
     1 vowel

Slide →

[a b c i]
      [c i i]
        2 vowels

Slide →

[a b c i i]
        [i i i]
          3 vowels  ← Maximum

Slide →

[i i i d]
 [i i d]
 2 vowels
```

Instead of recounting every window, we:

* Remove the left character
* Add the new right character

---

# 3. Example I/O

### Example 1

```text
Input:
s = "abciiidef"
k = 3

Output:
3
```

Explanation

```text
"iii" contains 3 vowels.
```

---

### Example 2

```text
Input:
s = "aeiou"
k = 2

Output:
2
```

Explanation

```text
Every window has 2 vowels.
```

---

### Edge Case

```text
Input:
s = "rhythms"
k = 4

Output:
0
```

No vowels exist.

---

# 4. Intuition & Pattern Recognition

## How to recognize this pattern

Whenever you see:

* Every **subarray/substring of size K**
* Fixed window size
* Maximum/Minimum/Sum/Count
* O(N) expected

Immediately think:

> **Fixed Size Sliding Window**

### Interview Thinking

Tell yourself:

> Every window has exactly `k` characters.

Instead of recalculating the vowel count for every window,

```text
Remove left character

↓

Add right character

↓

Update answer
```

Each slide only changes **one outgoing** and **one incoming** character.

---

# 5. Simpler Version

## Simpler Question 1

### Count vowels in a string

```python
count = 0

for ch in s:
    if ch in vowels:
        count += 1
```

Learns:

* Detect vowels

---

## Simpler Question 2

### Maximum Sum Subarray of Size K

Classic fixed sliding window.

```text
Current Sum

↓

Subtract left

↓

Add right
```

Instead of maintaining a sum, here we maintain the **count of vowels**.

---

## Current Question

Replace

```text
Current Sum
```

with

```text
Current Vowel Count
```

Everything else remains identical.

---

### Thinking Progression

```text
Count Vowels

↓

Fixed Window

↓

Slide Window

↓

Remove Left

↓

Add Right

↓

Maximum Number of Vowels
```

---

# 6. Brute Force

Generate every substring of length `k`.

Count vowels inside each one.

```python
ans = 0

for i in range(len(s) - k + 1):
    count = 0

    for j in range(i, i + k):
        if s[j] in "aeiou":
            count += 1

    ans = max(ans, count)

return ans
```

### Complexity

```text
Time  : O(N × K)

Space : O(1)
```

---

# 7. Optimal Solution

```python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = {'a', 'e', 'i', 'o', 'u'}

        count = 0

        # First window
        for i in range(k):
            if s[i] in vowels:
                count += 1

        ans = count

        # Slide the window
        for right in range(k, len(s)):

            # Remove outgoing character
            if s[right - k] in vowels:
                count -= 1

            # Add incoming character
            if s[right] in vowels:
                count += 1

            ans = max(ans, count)

        return ans
```

### Complexity

```text
Time  : O(N)

Space : O(1)
```

---

# 8. Step-by-Step Trace

Example

```text
s = "abciiidef"
k = 3
```

| Window | Outgoing | Incoming | Vowel Count | Max |
| ------ | -------- | -------- | ----------: | --: |
| abc    | -        | -        |           1 |   1 |
| bci    | a        | i        |           1 |   1 |
| cii    | b        | i        |           2 |   2 |
| iii    | c        | i        |           3 |   3 |
| iid    | i        | d        |           2 |   3 |
| ide    | i        | e        |           2 |   3 |
| def    | i        | f        |           1 |   3 |

Final Answer

```text
3
```

---

# 9. Related Problems

| Problem                                                                       | Connection                                                  |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Maximum Average Subarray I                                                    | Classic fixed-size sliding window using a running sum.      |
| Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold | Same fixed-window template with averages.                   |
| Grumpy Bookstore Owner                                                        | Fixed-size window to maximize customers.                    |
| Sliding Window Maximum                                                        | Fixed window but uses a deque to maintain the maximum.      |
| Longest Substring Without Repeating Characters                                | Transition from fixed-size to variable-size sliding window. |

---

# 🎯 Interview Cheat Sheet

## Pattern Recognition

```text
Window size = K

↓

Fixed Size Sliding Window

↓

Build first window

↓

Slide

↓

Remove Left

↓

Add Right

↓

Update Answer
```

## Window Invariant

```text
Window size is ALWAYS exactly K.
```

## Core Template

```python
# Build first window

# Update answer

for right in range(k, len(arr)):

    remove(arr[right - k])

    add(arr[right])

    update_answer()
```

## Common Mistakes

* ❌ Recounting vowels for every window (O(N × K)).
* ❌ Forgetting to initialize the first window before sliding.
* ❌ Updating the answer before processing the incoming and outgoing characters.

## Complexity

```text
Time  : O(N)
Space : O(1)
```

---

# 🧠 Pattern Connection

This problem is the **starting point for Sliding Window** because it teaches the fixed-size template:

```text
Maximum Average Subarray I
        ↓
Maximum Number of Vowels in a Substring of Given Length
        ↓
Sliding Window Maximum
        ↓
Longest Substring Without Repeating Characters
        ↓
Minimum Window Substring
```

The key transition is:

* **Fixed Size Sliding Window** → window size never changes.
* **Variable Size Sliding Window** → expand the right pointer, then shrink the left pointer only when the window becomes invalid.
