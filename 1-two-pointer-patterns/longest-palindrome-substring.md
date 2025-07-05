Here’s the `.md` formatted solution for **LeetCode: Longest Palindromic Substring** using:

1. ✅ **Brute force**
2. ✅ **Two Pointer** (Expand Around Center technique)

---

````markdown
# LeetCode Problem: Longest Palindromic Substring

## Problem Statement

Given a string `s`, return the longest palindromic substring in `s`.

---

### Example 1:
Input: `"babad"`  
Output: `"bab"` (or `"aba"`)

### Example 2:
Input: `"cbbd"`  
Output: `"bb"`

---

## ✅ Brute Force Solution

### Code:
```python
class Solution:
    def longestPalindrome(self, s):
        def is_palindrome(sub):
            return sub == sub[::-1]
        
        max_len = 0
        result = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]
                if is_palindrome(substring) and len(substring) > max_len:
                    max_len = len(substring)
                    result = substring
        return result
````

### Explanation:

* Iterate through all possible substrings `s[i:j+1]`.
* For each substring, check if it’s a palindrome.
* Keep track of the longest palindrome found.

### Time Complexity:

* **O(n³)** — O(n²) for all substrings × O(n) to check each palindrome.

### Space Complexity:

* **O(n)** — For slicing and temporary strings.

---

### 🔍 Brute Force Significance:

1. Checks all combinations — helpful for understanding problem deeply.
2. Inefficient for large inputs but conceptually simple.

---

## ✅ Two Pointer (Expand Around Center) Solution

### Code:

```python
class Solution:
    def longestPalindrome(self, s):
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]  # actual palindrome found

        result = ""
        for i in range(len(s)):
            # Odd length palindrome
            temp1 = expandAroundCenter(i, i)
            # Even length palindrome
            temp2 = expandAroundCenter(i, i + 1)

            # Update result if we find longer palindrome
            if len(temp1) > len(result):
                result = temp1
            if len(temp2) > len(result):
                result = temp2

        return result
```

### Explanation:

* A palindrome mirrors around its center.
* There are `2n-1` possible centers in a string of length `n`.
* For each center, expand outwards using two pointers as long as characters match.
* Track the longest one found.

### Time Complexity:

* **O(n²)** — Each center can expand up to the length of the string.

### Space Complexity:

* **O(1)** — Only constant extra space used.

---

### 🔍 Two Pointer Pattern Significance:

1. Avoids unnecessary string slicing and comparisons.
2. Efficient and elegant for palindrome problems by expanding around possible centers.

```

---

Let me know the **next question** and **pattern** you'd like!
```
