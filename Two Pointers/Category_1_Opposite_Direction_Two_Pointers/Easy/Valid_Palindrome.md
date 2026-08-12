# Valid Palindrome (LeetCode 125)

**Pattern:** Two Pointers + String Processing

---

# 1. Problem Statement

Given a string `s`, determine whether it is a **palindrome** after:

* Converting all uppercase letters to lowercase.
* Removing all non-alphanumeric characters.

Return `true` if it is a palindrome, otherwise return `false`.

A palindrome reads the same forward and backward.

### Constraints

* `1 <= s.length <= 2 × 10^5`
* `s` consists of printable ASCII characters.

---

# 2. Diagram

Example:

```text
s = "A man, a plan, a canal: Panama"

After ignoring spaces & punctuation:

amanaplanacanalpanama

L                                         R
↓                                         ↓
a m a n a p l a n a c a n a l p a n a m a

Compare

a == a ✓

Move inward

m == m ✓

Move inward

...

Pointers meet

Palindrome ✓
```

Notice that we **don't actually create** the cleaned string. We simply skip invalid characters while moving the pointers.

---

# 3. Example I/O

### Example 1

```text
Input:
s = "A man, a plan, a canal: Panama"

Output:
true
```

Explanation

```text
Processed string:

amanaplanacanalpanama

Same forward and backward.
```

---

### Example 2

```text
Input:
s = "race a car"

Output:
false
```

Explanation

```text
Processed string:

raceacar

Forward != Backward
```

---

### Example 3 (Edge Case)

```text
Input:
s = " "

Output:
true
```

Explanation

```text
No alphanumeric characters remain.

Empty string is a palindrome.
```

---

### Example 4

```text
Input:
s = "0P"

Output:
false
```

---

# 4. Intuition & Pattern Recognition

### Signals

Whenever you see:

* Check if something reads the same from both ends.
* Compare first and last characters.
* Ignore certain characters while comparing.
* O(N) time required.

Think:

> **Two Pointers**

---

### Interview Thinking

Tell yourself:

```text
Palindrome means:

First character should match last.

Second should match second last.

Some characters don't matter,
so simply skip them.

Keep comparing until pointers cross.
```

---

# 5. Simpler Version

## Simpler Question 1

### Valid Palindrome (Only lowercase letters)

```text
Compare first and last.

Move inward.
```

---

## Simpler Question 2

### Reverse String

Introduces inward-moving pointers.

---

## Current Question

Now add preprocessing **on the fly**.

```text
Compare

↓

If left isn't valid

Skip

↓

If right isn't valid

Skip

↓

Compare lowercase versions

↓

Continue
```

---

### Thinking Progression

```text
Reverse String

↓

Two pointers

↓

Palindrome checking

↓

Need to ignore characters

↓

Skip invalid characters

↓

Compare lowercase

↓

Valid Palindrome
```

---

# 6. Brute Force

Create a cleaned string.

Reverse it.

Compare both strings.

```python
filtered = ""

for ch in s:
    if ch.isalnum():
        filtered += ch.lower()

return filtered == filtered[::-1]
```

### Complexity

```text
Time  : O(N)

Space : O(N)
```

---

# 7. Optimal Solution (Two Pointers)

### Idea

Maintain two pointers.

* Skip non-alphanumeric characters.
* Convert both characters to lowercase.
* Compare them.
* If different → return `False`.
* Otherwise continue.

---

### Python

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        while left < right:

            # Skip invalid characters from the left
            while left < right and not s[left].isalnum():
                left += 1

            # Skip invalid characters from the right
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
```

---

### Complexity

```text
Time  : O(N)

Space : O(1)
```

Each character is visited at most once.

---

# 8. Step-by-Step Trace

Example

```text
s = "A man, a plan, a canal: Panama"
```

| Left          | Right | Left Char   | Right Char | Action       |
| ------------- | ----- | ----------- | ---------- | ------------ |
| 0             | 29    | A           | a          | Match → Move |
| 1             | 28    | space       | m          | Skip left    |
| 2             | 28    | m           | m          | Match        |
| 3             | 27    | a           | a          | Match        |
| 4             | 26    | n           | n          | Match        |
| ...           | ...   | ...         | ...        | Continue     |
| Pointers meet | -     | Return True |            |              |

Final Answer

```text
true
```

---

# 9. Related Problems

| Problem                                              | Connection                                        |
| ---------------------------------------------------- | ------------------------------------------------- |
| **344. Reverse String**                              | Basic two-pointer movement from both ends.        |
| **345. Reverse Vowels of a String**                  | Skip unwanted characters before swapping.         |
| **680. Valid Palindrome II**                         | Same problem but one character may be removed.    |
| **917. Reverse Only Letters**                        | Skip non-letter characters while moving pointers. |
| **2108. Find First Palindromic String in the Array** | Uses palindrome checking as a subroutine.         |

---

# Key Interview Takeaways

* **Pattern:** Two Pointers.
* **Invariant:** Everything outside `[left, right]` has already been validated.
* **Rule:** Skip invalid characters, compare lowercase versions, and move inward.
* **Optimization:** No need to build a cleaned string—process characters directly.
* **Complexity:** **O(N)** time and **O(1)** extra space.

---

# Pattern Summary

```text
Need to compare first and last?

↓

Palindrome?

↓

Two Pointers

↓

Need to ignore some characters?

↓

Skip invalid characters

↓

Need case-insensitive comparison?

↓

Convert to lowercase

↓

Compare

↓

If mismatch → False

↓

Pointers cross

↓

True
```
