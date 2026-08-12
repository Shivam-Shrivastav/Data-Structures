## 5. Longest Palindromic Substring
**Category:** **PALINDROME DP**

**Problem:** Given a string `s`, return the **longest palindromic substring** in `s`.

**Example:**
```
Input: s = "babad"
Output: "bab" or "aba" (both are valid)
```

```
Input: s = "cbbd"
Output: "bb"
```

```
Input: s = "a"
Output: "a"
```

---

### **Relation to Palindrome Problems**
**Similar to:** **Palindromic Substrings (647)** but find **longest** instead of count
**How it's different:**
1. **Palindromic Substrings:** Count all palindromes
2. **Longest Palindromic Substring:** Find the maximum length palindrome
3. **Can use:** Same DP table but track max length and indices

**Key Insight:** 
- A substring s[i:j+1] is palindrome if:
  - s[i] == s[j] AND (j-i ≤ 2 OR inner substring s[i+1:j] is palindrome)
- Build DP table where `dp[i][j]` = whether s[i:j+1] is palindrome
- Track maximum length and corresponding indices

---

### DP Intuition
- **State:** `dp[i][j]` = whether substring from i to j (inclusive) is palindrome
- **Transition:**
  ```
  if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
      dp[i][j] = True
  ```
- **Base:** Single chars `dp[i][i] = True`
- **Track:** `max_len` and `start` index of longest palindrome

---

### 1. Brute Force (Check all substrings)
```python
def longestPalindrome(s):
    n = len(s)
    
    def is_palindrome(i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
    max_len = 0
    start = 0
    
    for i in range(n):
        for j in range(i, n):
            if is_palindrome(i, j) and (j - i + 1) > max_len:
                max_len = j - i + 1
                start = i
    
    return s[start:start + max_len]
```
**TC:** O(n³) | **SC:** O(1)

---

### 2. Recursive with Memoization
```python
def longestPalindrome(s):
    n = len(s)
    memo = {}
    
    def is_palindrome(i, j):
        if i >= j:
            return True
        if (i, j) in memo:
            return memo[(i, j)]
        
        if s[i] == s[j]:
            memo[(i, j)] = is_palindrome(i+1, j-1)
        else:
            memo[(i, j)] = False
        
        return memo[(i, j)]
    
    max_len = 0
    start = 0
    
    for i in range(n):
        for j in range(i, n):
            if is_palindrome(i, j) and (j - i + 1) > max_len:
                max_len = j - i + 1
                start = i
    
    return s[start:start + max_len]
```
**TC:** O(n²) | **SC:** O(n²)

---

### 3. Tabulation (Bottom-Up DP)
```python
def longestPalindrome(s):
    n = len(s)
    if n <= 1:
        return s
    
    dp = [[False] * n for _ in range(n)]
    max_len = 1
    start = 0
    
    # All single characters are palindromes
    for i in range(n):
        dp[i][i] = True
    
    # Check palindromes of length 2
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            start = i
            max_len = 2
    
    # Check longer lengths
    for length in range(3, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                start = i
                max_len = length
    
    return s[start:start + max_len]
```
**TC:** O(n²) | **SC:** O(n²)

---

### 4. Expand Around Center (Optimal)
```python
def longestPalindrome(s):
    n = len(s)
    if n <= 1:
        return s
    
    def expand_around_center(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1  # length of palindrome
    
    start = 0
    max_len = 0
    
    for i in range(n):
        # Odd length palindrome
        len1 = expand_around_center(i, i)
        # Even length palindrome
        len2 = expand_around_center(i, i + 1)
        
        curr_max = max(len1, len2)
        if curr_max > max_len:
            max_len = curr_max
            start = i - (curr_max - 1) // 2
    
    return s[start:start + max_len]
```
**TC:** O(n²) | **SC:** O(1)

---

### 5. Manacher's Algorithm (O(n))
```python
def longestPalindrome(s):
    # Transform string to avoid even/odd handling
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    p = [0] * n  # p[i] = radius of palindrome centered at i
    
    center = right = 0
    max_len = 0
    center_index = 0
    
    for i in range(n):
        # Mirror of i around center
        mirror = 2 * center - i
        
        if i < right:
            p[i] = min(right - i, p[mirror])
        
        # Expand around center i
        a = i + (1 + p[i])
        b = i - (1 + p[i])
        while a < n and b >= 0 and t[a] == t[b]:
            p[i] += 1
            a += 1
            b -= 1
        
        # Update center and right boundary
        if i + p[i] > right:
            center = i
            right = i + p[i]
        
        # Track maximum
        if p[i] > max_len:
            max_len = p[i]
            center_index = i
    
    # Extract original palindrome
    start = (center_index - max_len) // 2
    return s[start:start + max_len]
```
**TC:** O(n) | **SC:** O(n)

---

**Key Formula (DP):**
```
dp[i][j] = (s[i] == s[j]) and (j - i <= 2 or dp[i+1][j-1])
```

**Key Formula (Expand Around Center):**
```
For each center (odd or even), expand outward while characters match
Length = right - left - 1 after expansion stops
```

**Example Walkthrough (DP):**
```
s = "babad", n=5

Initialize singles: dp[i][i]=True for all i

Length 2:
  i=0,j=1: "ba" → False
  i=1,j=2: "ab" → False
  i=2,j=3: "ba" → False
  i=3,j=4: "ad" → False

Length 3:
  i=0,j=2: "bab" → s[0]==s[2]='b' and dp[1][1]=True → True, start=0, max_len=3
  i=1,j=3: "aba" → s[1]==s[3]='a' and dp[2][2]=True → True, start=1, max_len=3
  i=2,j=4: "bad" → False

Length 4:
  i=0,j=3: "baba" → s[0]!=s[3] → False
  i=1,j=4: "abad" → s[1]!=s[4] → False

Length 5:
  i=0,j=4: "babad" → s[0]!=s[4] → False

Longest length = 3, starting at 0 or 1
Return "bab" or "aba"
```

**Example Walkthrough (Expand Around Center):**
```
s = "babad", n=5

i=0 (center for odd):
  expand(0,0): "b" → length=1
  expand(0,1): "ba" → stop → length=0
  max=1

i=1 (center for odd):
  expand(1,1): "a" → length=1
  expand(1,2): "ab" → stop → length=0
  Actually expand(1,1) with i=1,l=r=1: 
    l=0,r=2 → "bab" matches → length=3
    l=-1,r=3 stop
  So len1=3
  
  expand(1,2) even: l=1,r=2 → "ab" no → len2=0
  curr_max=3, start = 1 - (3-1)//2 = 1-1=0? Wait formula:
  start = i - (max_len - 1)//2 = 1 - (3-1)//2 = 1-1=0
  So palindrome "bab" from index 0

i=2 (center for odd):
  expand(2,2): "b" → length=1
  expand(2,3): "ba" no → 0
  Actually expand(2,2): l=2,r=2 → length=1, then l=1,r=3 → "aba" matches → length=3
  start = 2 - (3-1)//2 = 2-1=1 → "aba"

i=3,4 similar, no longer palindromes

Max length = 3, start=0 or 1
```

**Comparison Table:**

| Aspect | Palindromic Substrings (647) | Longest Palindromic Substring (5) |
|--------|------------------------------|----------------------------------|
**Objective** | Count all palindromes | Find longest palindrome |
**DP State** | Same dp[i][j] boolean | Same dp[i][j] boolean |
**Result** | Sum all true | Track max length and indices |
**Center Expand** | Sum all radii | Track max radius |
**Time Complexity** | O(n²) or O(n) | O(n²) or O(n) with Manacher |

**Palindrome Family:**

| Problem | Type | Key Difference |
|---------|------|---------------|
**5. Longest Palindromic Substring** | Find one | Track max length |
**647. Palindromic Substrings** | Count all | Sum all palindromes |
**131. Palindrome Partitioning** | All partitions | Backtracking |
**132. Palindrome Partitioning II** | Min cuts | DP + palindrome check |
**516. Longest Palindromic Subsequence** | Subsequence | Not contiguous |
**214. Shortest Palindrome** | Add to front | KMP or rolling hash |

**Edge Cases:**
- Empty string → ""
- Single char → itself
- All same chars → entire string
- No palindrome beyond singles → first char

**Why Expand Around Center is Better than DP:**
- O(n²) time but O(1) space
- Simpler to implement
- For finding longest, we don't need full table
- Can stop early in some cases

**Manacher's Algorithm:**
- Linear time algorithm for longest palindromic substring
- Uses symmetry property of palindromes
- More complex but optimal for very long strings
- Good to know for interviews but implement only if confident