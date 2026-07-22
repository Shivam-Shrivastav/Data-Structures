# 214. Shortest Palindrome

**Pattern:** String Matching (KMP Prefix Function) / Rolling Hash (Alternative)

---

# 1. Problem Statement

Given a string `s`, return the **shortest palindrome** you can form by **adding characters only in front** of the string.

You may prepend as many characters as needed.

### Constraints

* `0 <= s.length <= 5 × 10⁴`
* String contains lowercase English letters.
* Need better than **O(N²)**. 

---

# 2. Diagram

### Example

```text
s = "aacecaaa"

Original

a a c e c a a a
|---------------|

Longest Palindromic Prefix

a a c e c a a
|-----------|

Remaining suffix

              a

Reverse suffix

a

Add in front

a + aacecaaa

↓

aaacecaaa
```

---

### Another Example

```text
s = "abcd"

Longest Palindromic Prefix

a

Remaining

b c d

Reverse

d c b

Add in front

d c b + a b c d

↓

dcbabcd
```

---

# 3. Example I/O

### Example 1

```text
Input:
s = "aacecaaa"

Output:
"aaacecaaa"
```

Explanation

```text
Longest palindromic prefix = "aacecaa"

Suffix = "a"

Reverse suffix = "a"

Answer = "aaacecaaa"
```

---

### Example 2

```text
Input:
s = "abcd"

Output:
"dcbabcd"
```

Explanation

```text
Longest palindromic prefix = "a"

Need to prepend reverse("bcd")

Result = "dcbabcd"
```

---

### Edge Case

```text
Input:
s = ""

Output:
""
```

---

### Edge Case

```text
Input:
s = "aaaa"

Output:
"aaaa"
```

Already a palindrome.

---

# 4. Intuition & Pattern Recognition

### Signals

Whenever you see

* Add minimum characters
* Only at beginning
* Palindrome
* Large constraints (50k)

Ask yourself:

> **Which part is already correct?**

Instead of asking

> "What should I add?"

Ask

> **"What is the longest prefix that is already a palindrome?"**

Everything after that prefix is "wrong".

Simply reverse that remaining suffix and place it in front.

So the entire problem reduces to

> **Find the longest palindromic prefix.**

Finding this naively is O(N²).

KMP allows us to do it in O(N).

---

### Interview Thinking

```text
I don't want to rebuild the whole palindrome.

I only need to know where the longest
palindromic prefix ends.

Everything after it is reversed
and inserted at the front.
```

---

# 5. Simpler Version

## Simpler Question 1

### Valid Palindrome (LeetCode 125)

Check if an entire string is a palindrome.

```text
Compare left and right.
```

---

## Simpler Question 2

### Longest Palindromic Prefix

```text
Try every prefix

Check palindrome

Take longest
```

Works but O(N²).

---

## Simpler Question 3

### KMP Prefix Function (LeetCode 28)

Find longest prefix which is also suffix.

This introduces

```text
LPS Array
```

---

## Current Question

Create

```text
s + "#" + reverse(s)
```

Now,

the longest prefix-suffix in this new string equals

> **Longest palindromic prefix**

---

### Thinking Progression

```text
Check palindrome

↓

Longest palindromic prefix

↓

Need faster than O(N²)

↓

KMP Prefix Function

↓

Shortest Palindrome
```

---

# 6. Brute Force

Try every prefix.

```text
abcd

Check

abcd

abc

ab

a
```

Find first prefix that is palindrome.

Reverse remaining suffix.

### Python

```python
class Solution:
    def shortestPalindrome(self, s: str) -> str:

        def isPalindrome(x):
            return x == x[::-1]

        for i in range(len(s), -1, -1):
            if isPalindrome(s[:i]):
                return s[i:][::-1] + s

        return s
```

### Complexity

```text
Time  : O(N²)

Space : O(N)
```

---

# 7. Optimal Solution (KMP Prefix Function)

### Key Observation

Construct

```text
temp = s + "#" + reverse(s)
```

Example

```text
s = "abcd"

temp

abcd#dcba
```

The last value of the LPS array gives

```text
Length of longest palindromic prefix.
```

Then

```text
suffix = s[lps[-1]:]

answer = reverse(suffix) + s
```

---

### Python

```python
class Solution:
    def shortestPalindrome(self, s: str) -> str:

        rev = s[::-1]
        temp = s + "#" + rev

        lps = [0] * len(temp)

        j = 0

        for i in range(1, len(temp)):

            # Move back using previously computed LPS values
            while j > 0 and temp[i] != temp[j]:
                j = lps[j - 1]

            # Characters match, extend current prefix
            if temp[i] == temp[j]:
                j += 1

            lps[i] = j

        # Length of longest palindromic prefix
        longest = lps[-1]

        # Reverse remaining suffix and prepend
        return s[longest:][::-1] + s
```

---

### Complexity

```text
Time  : O(N)

Space : O(N)
```

---

# 8. Step-by-Step Trace

Example

```text
s = "abcd"
```

### Step 1

```text
rev = "dcba"

temp

abcd#dcba
```

---

### Build LPS

| Index | Char | LPS |
| ----- | ---- | --- |
| 0     | a    | 0   |
| 1     | b    | 0   |
| 2     | c    | 0   |
| 3     | d    | 0   |
| 4     | #    | 0   |
| 5     | d    | 0   |
| 6     | c    | 0   |
| 7     | b    | 0   |
| 8     | a    | 1   |

Final

```text
lps[-1] = 1
```

Meaning

```text
Longest palindromic prefix

"a"
```

---

### Remaining suffix

```text
bcd
```

Reverse

```text
dcb
```

Add in front

```text
dcb + abcd

↓

dcbabcd
```

---

### Another Trace

```text
s = "aacecaaa"

Longest palindromic prefix

aacecaa

Remaining

a

Reverse

a

Result

aaacecaaa
```

---

# 9. Related Problems

| Problem                                                          | Connection                                                                               |
| ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **125. Valid Palindrome**                                        | Learn palindrome checking using two pointers.                                            |
| **5. Longest Palindromic Substring**                             | Find the longest palindrome anywhere in the string, not just at the start.               |
| **647. Palindromic Substrings**                                  | Count all palindromic substrings; expands palindrome intuition.                          |
| **28. Find the Index of the First Occurrence in a String (KMP)** | Introduces the prefix-function (LPS) used in this solution.                              |
| **1392. Longest Happy Prefix**                                   | Uses the same KMP prefix-function idea to find the longest prefix that is also a suffix. |

---

# Key Interview Takeaways

* **Pattern:** KMP Prefix Function (LPS Array).
* **Core Insight:** Reduce the problem to finding the **longest palindromic prefix**.
* **Transformation:** Build `s + "#" + reverse(s)` and compute its LPS array.
* **Why it works:** The last LPS value represents the longest prefix of `s` that matches a suffix of `reverse(s)`, which is exactly the longest palindromic prefix.
* **Final Construction:** Reverse the non-palindromic suffix and prepend it.
* **Complexity:** **O(N)** time and **O(N)** space. 
