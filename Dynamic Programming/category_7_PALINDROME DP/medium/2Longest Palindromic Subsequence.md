## 516. Longest Palindromic Subsequence
**Category:** **PALINDROME DP / SUBSEQUENCE DP**

**Problem:** Given a string `s`, find the **length** of the **longest palindromic subsequence** (not necessarily contiguous).

**Example:**
```
Input: s = "bbbab"
Output: 4
Explanation: "bbbb" is the longest palindromic subsequence
```

```
Input: s = "cbbd"
Output: 2
Explanation: "bb" is the longest palindromic subsequence
```

```
Input: s = "a"
Output: 1
```

---

### **Relation to Palindrome Problems**
**Similar to:** **Longest Palindromic Substring (5)** but **subsequence** (not contiguous)
**How it's different:**
1. **Longest Palindromic Substring:** Contiguous, find actual substring
2. **Longest Palindromic Subsequence:** Can skip characters, find length only (usually)

**Key Insight:** 
- This is essentially the **LCS (Longest Common Subsequence)** between `s` and its reverse
- Or direct DP: if `s[i] == s[j]`, we can take 2 + LPS of middle
- Otherwise, take max of LPS without i or without j

---

### DP Intuition
- **State:** `dp[i][j]` = length of longest palindromic subsequence in `s[i..j]`
- **Transition:**
  ```
  if s[i] == s[j]:
      dp[i][j] = 2 + dp[i+1][j-1]  # take both ends
  else:
      dp[i][j] = max(dp[i+1][j], dp[i][j-1])  # skip either end
  ```
- **Base:** 
  - `dp[i][i] = 1` (single character)
  - `dp[i][j] = 0` if i > j
- **Answer:** `dp[0][n-1]`

---

### 1. Recursive Solution
```python
def longestPalindromeSubseq(s):
    n = len(s)
    
    def dfs(i, j):
        if i > j:
            return 0
        if i == j:
            return 1
        
        if s[i] == s[j]:
            return 2 + dfs(i+1, j-1)
        else:
            return max(dfs(i+1, j), dfs(i, j-1))
    
    return dfs(0, n-1)
```
**TC:** O(2ⁿ) | **SC:** O(n) recursion stack

---

### 2. Memoization (Top-Down DP)
```python
def longestPalindromeSubseq(s):
    n = len(s)
    memo = [[-1] * n for _ in range(n)]
    
    def dfs(i, j):
        if i > j:
            return 0
        if i == j:
            return 1
        if memo[i][j] != -1:
            return memo[i][j]
        
        if s[i] == s[j]:
            memo[i][j] = 2 + dfs(i+1, j-1)
        else:
            memo[i][j] = max(dfs(i+1, j), dfs(i, j-1))
        
        return memo[i][j]
    
    return dfs(0, n-1)
```
**TC:** O(n²) | **SC:** O(n²)

---

### 3. Tabulation (Bottom-Up DP)
```python
def longestPalindromeSubseq(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    
    # Base: single characters
    for i in range(n):
        dp[i][i] = 1
    
    # Build table bottom-up (by length)
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    
    return dp[0][n-1]
```
**TC:** O(n²) | **SC:** O(n²)

---

### 4. Space Optimized (2 rows)
```python
def longestPalindromeSubseq(s):
    n = len(s)
    
    # dp[i][j] depends on dp[i+1][j], dp[i][j-1], dp[i+1][j-1]
    # So we need current row and previous row
    dp = [0] * n
    dp_prev = [0] * n
    
    for i in range(n-1, -1, -1):
        dp[i] = 1  # single character
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[j] = 2 + dp_prev[j-1]
            else:
                dp[j] = max(dp_prev[j], dp[j-1])
        dp_prev = dp[:]  # copy for next iteration
    
    return dp[n-1]
```
**TC:** O(n²) | **SC:** O(n)

---

### 5. LCS with Reverse (Alternative)
```python
def longestPalindromeSubseq(s):
    # LPS of s = LCS of s and reverse(s)
    rev = s[::-1]
    n = len(s)
    
    # LCS DP
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i-1] == rev[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[n][n]
```
**TC:** O(n²) | **SC:** O(n²) (can be optimized to O(n))

---

**Key Formula:**
```
dp[i][j] = 
    2 + dp[i+1][j-1]      if s[i] == s[j]
    max(dp[i+1][j], dp[i][j-1])  otherwise
```

**Example Walkthrough (Tabulation):**
```
s = "bbbab", n=5

Initialize diagonal: dp[i][i]=1

length=2:
  i=0,j=1: "bb" → s[0]==s[1] → 2 + dp[1][0]=2+0=2
  i=1,j=2: "bb" → s[1]==s[2] → 2 + dp[2][1]=2
  i=2,j=3: "ba" → s[2]!=s[3] → max(dp[3][3]=1, dp[2][2]=1) = 1
  i=3,j=4: "ab" → s[3]!=s[4] → max(dp[4][4]=1, dp[3][3]=1) = 1

length=3:
  i=0,j=2: "bbb" → s[0]==s[2] → 2 + dp[1][1]=2+1=3
  i=1,j=3: "bba" → s[1]!=s[3] → max(dp[2][3]=1, dp[1][2]=2) = 2
  i=2,j=4: "bab" → s[2]!=s[4] → max(dp[3][4]=1, dp[2][3]=1) = 1

length=4:
  i=0,j=3: "bbba" → s[0]!=s[3] → max(dp[1][3]=2, dp[0][2]=3) = 3
  i=1,j=4: "bbab" → s[1]!=s[4] → max(dp[2][4]=1, dp[1][3]=2) = 2

length=5:
  i=0,j=4: "bbbab" → s[0]==s[4] → 2 + dp[1][3]=2+2=4

Answer = 4 ("bbbb")
```

**Example Walkthrough (LCS method):**
```
s = "bbbab", rev = "babbb"

LCS DP:
    b a b b b
  b 1 1 1 1 1
  b 1 1 2 2 2
  b 1 1 2 3 3
  a 1 2 2 3 3
  b 1 2 3 3 4

Result = 4
```

**Comparison Table:**

| Aspect | Longest Palindromic Substring | Longest Palindromic Subsequence |
|--------|------------------------------|--------------------------------|
**Contiguous?** | ✅ Yes | ❌ No |
**DP State** | dp[i][j] = is palindrome? | dp[i][j] = length of LPS |
**Transition** | s[i]==s[j] AND inner | s[i]==s[j] → 2+inner else max(skip) |
**Base** | Single chars = True | Single chars = 1 |
**Time** | O(n²) | O(n²) |
**Space** | O(n²) or O(1) | O(n²) or O(n) |

**Palindrome Family:**

| Problem | Type | Key Difference |
|---------|------|---------------|
**5. Longest Palindromic Substring** | Substring (contiguous) | Must be consecutive |
**516. Longest Palindromic Subsequence** | Subsequence | Can skip chars |
**647. Palindromic Substrings** | Count all | Count, not length |
**131. Palindrome Partitioning** | All partitions | Backtracking |
**132. Palindrome Partitioning II** | Min cuts | Minimize partitions |

**Edge Cases:**
- Empty string → 0
- Single char → 1
- All same chars → n
- No palindrome beyond singles → 1

**Why LCS with Reverse Works:**
- A palindrome reads same forwards and backwards
- If we take subsequence of s and its reverse, it must be common
- The longest common subsequence between s and reverse(s) is the LPS
- Because any palindrome appears in both in reverse order

**Space Optimization Insight:**
- dp[i][j] depends on:
  - dp[i+1][j-1] (diagonal previous)
  - dp[i+1][j] (below)
  - dp[i][j-1] (left)
- Processing i from n-1 down to 0 allows 1D optimization
- Need to keep previous row for dp[i+1][j-1]