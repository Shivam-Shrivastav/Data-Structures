# Valid Palindrome II (LeetCode 680)

## 1. Problem Statement

Given a string `s`, return `true` if the string can become a palindrome after **deleting at most one character**.

You may delete **zero or one** character.

### Constraints

* `1 <= s.length <= 10^5`
* `s` contains only lowercase English letters.
* Need an **O(N)** solution.

---

# 2. Diagram

Example:

```text
s = "abca"

L         R
a b c a
↑       ↑

a == a ✓

Move inward

b c
↑ ↑

Mismatch!

Option 1:
Delete left ('b')

c
✓

Option 2:
Delete right ('c')

b
✓

At least one option works.

Answer = True
```

---

# 3. Example I/O

### Example 1

**Input**

```text
s = "aba"
```

**Output**

```text
true
```

Explanation

```text
Already a palindrome.
```

---

### Example 2

**Input**

```text
s = "abca"
```

**Output**

```text
true
```

Explanation

```text
Delete 'b'

aca

or

Delete 'c'

aba
```

---

### Example 3

**Input**

```text
s = "abc"
```

**Output**

```text
false
```

Explanation

```text
Delete 'a' → "bc"

Delete 'b' → "ac"

Delete 'c' → "ab"

None are palindromes.
```

---

### Example 4 (Edge Case)

**Input**

```text
s = "deeee"
```

**Output**

```text
true
```

Delete `'d'` to obtain `"eeee"`.

---

# 4. Intuition & Pattern Recognition

### Signals

Whenever you see:

* Palindrome
* Delete one character
* At most one modification

Think:

> **Two Pointers + One Chance**

### Why?

Normally, palindrome checking is straightforward with two pointers.

The only difference here is that you're allowed **one mistake**.

When the first mismatch occurs, there are only **two possibilities**:

1. Delete the left character.
2. Delete the right character.

If either remaining substring is a palindrome, the answer is `true`.

### Interview Thinking

Tell yourself:

```text
I'll compare from both ends.

If characters match,
continue.

If they don't,

I only get one deletion.

So I'll try:

Skip left

OR

Skip right

If either works,

return True.
```

---

# 5. Simpler Version

## Simpler Question 1

### Valid Palindrome

```text
racecar

L       R

Compare inward.
```

No deletion allowed.

---

## Simpler Question 2

### Reverse String

Learn basic two-pointer movement.

---

## Current Question

Now allow **one deletion**.

```text
Compare

↓

Mismatch?

↓

Skip Left

OR

Skip Right

↓

Check remaining substring
```

---

### Thinking Progression

```text
Reverse String

↓

Valid Palindrome

↓

Allow One Deletion

↓

Try Both Possibilities

↓

Valid Palindrome II
```

---

# 6. Brute Force

Delete every character once.

For each new string,

check if it is a palindrome.

```text
For i in range(N):

Remove s[i]

Check palindrome
```

### Python

```python
class Solution:
    def isPalindrome(self, t):
        return t == t[::-1]

    def validPalindrome(self, s: str) -> bool:

        if self.isPalindrome(s):
            return True

        for i in range(len(s)):
            if self.isPalindrome(s[:i] + s[i+1:]):
                return True

        return False
```

### Complexity

```text
Time : O(N²)

Space: O(N)
```

---

# 7. Optimal Solution (Two Pointers)

### Idea

Move inward with two pointers.

If characters differ,

check whether either of these substrings is a palindrome:

* `left + 1 ... right`
* `left ... right - 1`

Only one mismatch handling is needed.

### Python

```python
class Solution:

    def isPal(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def validPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        while left < right:

            if s[left] != s[right]:

                # Skip either left or right character
                return (
                    self.isPal(s, left + 1, right) or
                    self.isPal(s, left, right - 1)
                )

            left += 1
            right -= 1

        return True
```

### Complexity

```text
Time  : O(N)

Space : O(1)
```

> **Why O(N)?**
>
> The main loop runs once. After the **first mismatch**, we perform at most **two linear palindrome checks**, each over a remaining substring. Since this happens only once, the total work is still proportional to `N`.

---

# 8. Step-by-Step Trace

Example

```text
s = "abca"
```

| Left | Right | Characters | Action      |
| ---- | ----- | ---------- | ----------- |
| 0    | 3     | a == a     | Move inward |
| 1    | 2     | b != c     | Mismatch    |

Try deleting **left**:

```text
c

Palindrome ✓
```

Try deleting **right**:

```text
b

Palindrome ✓
```

One valid option exists.

Return

```text
True
```

---

### Another Example

```text
s = "abc"
```

| Left | Right | Characters | Action   |
| ---- | ----- | ---------- | -------- |
| 0    | 2     | a != c     | Mismatch |

Delete `'a'`

```text
bc

Not palindrome
```

Delete `'c'`

```text
ab

Not palindrome
```

Return

```text
False
```

---

# 9. Related Problems

| Problem                              | Connection                                                           |
| ------------------------------------ | -------------------------------------------------------------------- |
| **125. Valid Palindrome**            | Basic two-pointer palindrome checking.                               |
| **234. Palindrome Linked List**      | Same palindrome concept on linked lists.                             |
| **5. Longest Palindromic Substring** | Find the longest palindrome using expand-around-center.              |
| **647. Palindromic Substrings**      | Count all palindromic substrings.                                    |
| **1216. Valid Palindrome III**       | Generalization allowing up to **K deletions** (Dynamic Programming). |

---

# Key Interview Takeaways

* **Pattern:** Two Pointers.
* **Core Insight:** At the **first mismatch**, there are only **two possible deletions**—skip the left character or skip the right character.
* **Invariant:** Before the first mismatch, the prefix and suffix already match, so no earlier deletion is beneficial.
* **Optimization:** Check both remaining substrings in-place using two pointers instead of creating new strings.
* **Complexity:** **O(N)** time and **O(1)** extra space.
