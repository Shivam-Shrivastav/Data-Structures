## 647. Palindromic Substrings
**Category:** **STRING DP / PALINDROME**

**Problem:** Given a string `s`, return the number of **palindromic substrings** in it. A substring is a contiguous sequence of characters.

**Example:**
```
Input: s = "abc"
Output: 3
Explanation: "a", "b", "c" → 3 palindromes
```

```
Input: s = "aaa"
Output: 6
Explanation: "a", "a", "a", "aa", "aa", "aaa" → 6 palindromes
```

```
Input: s = "ababa"
Output: 7? Actually let's count: all single chars (5) + "aba" (2) + "bab" + "ababa" = 9
Wait: "a","b","a","b","a" (5)
     "aba" at (0,2) and (2,4) → (2)
     "bab" at (1,3) → (1)
     "ababa" at (0,4) → (1)
     Total = 5+2+1+1 = 9
```

---

### **Relation to Palindrome Problems**
**Similar to:** **Longest Palindromic Substring** but counting all
**How it's different:**
1. **Longest Palindromic Substring:** Find max length palindrome
2. **Palindromic Substrings:** Count **all** palindromic substrings
3. **Key Insight:** Can use same DP table but count all true entries

**Key Insight:** 
- A substring s[i:j+1] is palindrome if:
  - s[i] == s[j] AND (j-i ≤ 2 OR inner substring s[i+1:j] is palindrome)
- Build DP table where `dp[i][j]` = whether s[i:j+1] is palindrome
- Count all `dp[i][j] = True`

---

### DP Intuition
- **State:** `dp[i][j]` = whether substring from i to j (inclusive) is palindrome
- **Transition:**
  ```
  if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
      dp[i][j] = True
  ```
- **Base:** Single chars `dp[i][i] = True`, length 2 if chars equal
- **Answer:** Count of all `dp[i][j] = True`

---

### 1. Recursive Solution
```python
def countSubstrings(s):
    n = len(s)
    
    def is_palindrome(i, j):
        if i > j:
            return True
        if i == j:
            return True
        
        if s[i] == s[j]:
            return is_palindrome(i+1, j-1)
        return False
    
    count = 0
    for i in range(n):
        for j in range(i, n):
            if is_palindrome(i, j):
                count += 1
    
    return count
```
**TC:** O(n³) | **SC:** O(n) recursion stack

---

### 2. Memoization (Top-Down DP)
```python
def countSubstrings(s):
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
    
    count = 0
    for i in range(n):
        for j in range(i, n):
            if is_palindrome(i, j):
                count += 1
    
    return count
```
**TC:** O(n²) | **SC:** O(n²)

---

### 3. Tabulation (Bottom-Up DP)
```python
def countSubstrings(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    count = 0
    
    # All single characters are palindromes
    for i in range(n):
        dp[i][i] = True
        count += 1
    
    # Check palindromes of length 2
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            count += 1
    
    # Check longer lengths
    for length in range(3, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                count += 1
    
    return count
```
**TC:** O(n²) | **SC:** O(n²)

---

### 4. Space Optimized (Expand Around Center)
```python
def countSubstrings(s):
    n = len(s)
    count = 0
    
    def expand_around_center(left, right):
        nonlocal count
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
    
    for i in range(n):
        # Odd length palindromes (center at i)
        expand_around_center(i, i)
        # Even length palindromes (center between i and i+1)
        expand_around_center(i, i+1)
    
    return count
```
**TC:** O(n²) | **SC:** O(1)

---

### 5. Manacher's Algorithm (O(n))
```python
def countSubstrings(s):
    # Transform string to handle even/odd uniformly
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    p = [0] * n  # p[i] = radius of palindrome centered at i
    
    center = right = 0
    count = 0
    
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
        
        # Each palindrome radius contributes (p[i] + 1) // 2 to count
        # Because in transformed string, each real palindrome length = p[i]
        # Number of real palindromes centered here = (p[i] + 1) // 2
        count += (p[i] + 1) // 2
    
    return count
```
**TC:** O(n) | **SC:** O(n)

---

**Key Formula (DP):**
```
dp[i][j] = (s[i] == s[j]) and (j - i <= 2 or dp[i+1][j-1])
```

**Key Formula (Expand Around Center):**
```
For each center (odd or even), expand while characters match and count
```

**Example Walkthrough (DP):**
```
s = "aaa", n=3

Initialize single chars: dp[0][0]=T, dp[1][1]=T, dp[2][2]=T → count=3

Length 2:
  i=0,j=1: s[0]==s[1]='a' → dp[0][1]=T, count=4
  i=1,j=2: s[1]==s[2]='a' → dp[1][2]=T, count=5

Length 3:
  i=0,j=2: s[0]==s[2]='a' and dp[1][1]=T → dp[0][2]=T, count=6

Answer = 6
```

**Example Walkthrough (Expand Around Center):**
```
s = "aaa", n=3

i=0 (odd): expand(0,0) → "a" (count=1), "aaa" (count=2)
i=0 (even): expand(0,1) → "aa" (count=3)
i=1 (odd): expand(1,1) → "a" (count=4), "aaa" (count=5)
i=1 (even): expand(1,2) → "aa" (count=6)
i=2 (odd): expand(2,2) → "a" (count=7)
i=2 (even): expand(2,3) → out of bounds

Answer = 7? Wait we double-counted? Let's track carefully:

Odd centers (i,i):
i=0: "a" (0,0), expand left/right: (0,2) "aaa" → +2
i=1: "a" (1,1), expand: (1,1) only? Actually from (1,1) we can't expand to (0,2) because that would require s[0]==s[2] which is true but we're at center 1? This approach counts each palindrome once by expanding from its center.

Better to implement as in code: for each i, call expand(i,i) and expand(i,i+1)
Let's trace code:

count=0
i=0: expand(0,0): l=0,r=0 → s[0]==s[0] → count=1, l=-1,r=1 stop
      expand(0,1): l=0,r=1 → s[0]==s[1] → count=2, l=-1,r=2 stop
i=1: expand(1,1): l=1,r=1 → s[1]==s[1] → count=3, l=0,r=2 → s[0]==s[2] → count=4, l=-1,r=3 stop
      expand(1,2): l=1,r=2 → s[1]==s[2] → count=5, l=0,r=3 stop
i=2: expand(2,2): l=2,r=2 → s[2]==s[2] → count=6, l=1,r=3 stop
      expand(2,3): l=2,r=3 out of bounds

Total = 6 ✓
```

**Comparison Table:**

| Aspect | Longest Palindromic Substring | Palindromic Substrings |
|--------|------------------------------|----------------------|
**Objective** | Find max length | Count all |
**DP State** | Same dp[i][j] boolean | Same dp[i][j] boolean |
**Result** | Track max length where true | Sum all true entries |
**Center Expand** | Track max radius | Sum all radii |
**Time Complexity** | O(n²) | O(n²) or O(n) with Manacher |

**Palindrome Family:**

| Problem | Type | Key Difference |
|---------|------|---------------|
**5. Longest Palindromic Substring** | Find one | Track max length |
**647. Palindromic Substrings** | Count all | Sum all palindromes |
**131. Palindrome Partitioning** | All partitions | Backtracking |
**132. Palindrome Partitioning II** | Min cuts | DP + palindrome check |
**516. Longest Palindromic Subsequence** | Subsequence | Not contiguous |

**Edge Cases:**
- Empty string → 0
- Single char → 1
- All same chars → n*(n+1)/2
- No palindromes beyond singles → n

**Why Expand Around Center is Better:**
- O(n²) time but O(1) space
- Simpler to implement
- For counting, it's equally efficient as DP
- No need for 2D table

**Manacher's Algorithm:**
- Originally for longest palindromic substring
- Can be adapted for counting
- O(n) time, O(n) space
- Overkill for most interviews but good to know