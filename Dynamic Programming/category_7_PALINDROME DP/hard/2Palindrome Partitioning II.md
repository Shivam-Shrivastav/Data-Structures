## 132. Palindrome Partitioning II
**Category:** **PALINDROME DP / MINIMUM CUTS**

**Problem:** Given a string `s`, partition it such that every substring is a palindrome. Return the **minimum cuts** needed for such a partition.

**Example:**
```
Input: s = "aab"
Output: 1
Explanation: ["aa","b"] needs 1 cut between "aa" and "b"
```

```
Input: s = "a"
Output: 0
Explanation: Already a palindrome, no cuts needed
```

```
Input: s = "ab"
Output: 1
Explanation: ["a","b"] needs 1 cut
```

```
Input: s = "ababa"
Output: 0
Explanation: Whole string is palindrome
```

---

### **Relation to Palindrome Problems**
**Similar to:** **Palindrome Partitioning (131)** but **minimize cuts** instead of generating all
**How it's different:**
1. **Palindrome Partitioning:** Generate all valid partitions
2. **Palindrome Partitioning II:** Find minimum number of cuts
3. **Key Insight:** Can use DP to avoid exponential generation

**Key Insight:** 
- Let `cuts[i]` = minimum cuts needed for prefix `s[0..i-1]`
- For each `i`, try all `j < i` where `s[j:i]` is palindrome
- Then `cuts[i] = min(cuts[j] + 1)` for all such j
- Need efficient way to check if `s[j:i]` is palindrome → precompute palindrome DP

---

### DP Intuition
- **State 1 (Palindrome):** `is_pal[i][j]` = whether `s[i..j]` is palindrome
- **State 2 (Cuts):** `cuts[i]` = minimum cuts for prefix of length i (`s[0..i-1]`)
- **Transition:**
  ```
  cuts[i] = min(cuts[j] + 1) for all j < i where is_pal[j][i-1] is True
  ```
- **Base:** 
  - `cuts[0] = -1` (conceptual: -1 cuts for empty string, so +1 gives 0 cuts for first palindrome)
  - Alternative: `cuts[0] = 0`, then when palindrome starts at 0, cuts[i] = 0
- **Answer:** `cuts[n]`

---

### 1. Recursive Solution (Exponential)
```python
def minCut(s):
    n = len(s)
    
    def is_palindrome(i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
    def dfs(i):
        # i is starting index
        if i == n or is_palindrome(i, n-1):
            return 0
        
        min_cuts = float('inf')
        for j in range(i, n):
            if is_palindrome(i, j):
                min_cuts = min(min_cuts, 1 + dfs(j + 1))
        
        return min_cuts
    
    return dfs(0)
```
**TC:** O(2ⁿ) | **SC:** O(n) recursion stack

---

### 2. Memoization with Palindrome Precomputation
```python
def minCut(s):
    n = len(s)
    
    # Precompute palindrome information
    is_pal = [[False] * n for _ in range(n)]
    
    # All single chars are palindromes
    for i in range(n):
        is_pal[i][i] = True
    
    # Length 2
    for i in range(n-1):
        if s[i] == s[i+1]:
            is_pal[i][i+1] = True
    
    # Longer lengths
    for length in range(3, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and is_pal[i+1][j-1]:
                is_pal[i][j] = True
    
    memo = [-1] * (n + 1)
    
    def dfs(i):
        if i == n:
            return 0
        if memo[i] != -1:
            return memo[i]
        
        if is_pal[i][n-1]:
            memo[i] = 0
            return 0
        
        min_cuts = float('inf')
        for j in range(i, n):
            if is_pal[i][j]:
                min_cuts = min(min_cuts, 1 + dfs(j + 1))
        
        memo[i] = min_cuts
        return min_cuts
    
    return dfs(0)
```
**TC:** O(n²) | **SC:** O(n²)

---

### 3. Tabulation (Bottom-Up DP) - Optimal
```python
def minCut(s):
    n = len(s)
    if n <= 1:
        return 0
    
    # Step 1: Precompute palindrome information
    is_pal = [[False] * n for _ in range(n)]
    
    # All single chars are palindromes
    for i in range(n):
        is_pal[i][i] = True
    
    # Length 2
    for i in range(n-1):
        if s[i] == s[i+1]:
            is_pal[i][i+1] = True
    
    # Longer lengths
    for length in range(3, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and is_pal[i+1][j-1]:
                is_pal[i][j] = True
    
    # Step 2: DP for minimum cuts
    cuts = [float('inf')] * (n + 1)
    cuts[0] = -1  # Conceptual: -1 cuts for empty string
    
    for i in range(1, n + 1):
        for j in range(i):
            if is_pal[j][i-1]:
                cuts[i] = min(cuts[i], cuts[j] + 1)
    
    return cuts[n]
```
**TC:** O(n²) | **SC:** O(n²)

---

### 4. Space Optimized (1D for cuts, still need 2D for pal)
```python
def minCut(s):
    n = len(s)
    if n <= 1:
        return 0
    
    # Precompute palindrome information
    is_pal = [[False] * n for _ in range(n)]
    
    for i in range(n):
        is_pal[i][i] = True
    
    for i in range(n-1):
        if s[i] == s[i+1]:
            is_pal[i][i+1] = True
    
    for length in range(3, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and is_pal[i+1][j-1]:
                is_pal[i][j] = True
    
    # cuts[i] = min cuts for s[0..i-1]
    cuts = [float('inf')] * (n + 1)
    cuts[0] = -1
    
    for i in range(1, n + 1):
        # Check if whole prefix is palindrome
        if is_pal[0][i-1]:
            cuts[i] = 0
        else:
            for j in range(1, i):
                if is_pal[j][i-1]:
                    cuts[i] = min(cuts[i], cuts[j] + 1)
    
    return cuts[n]
```
**TC:** O(n²) | **SC:** O(n²) (still need palindrome table)

---

### 5. Further Optimized - Compute palindrome and cuts together
```python
def minCut(s):
    n = len(s)
    if n <= 1:
        return 0
    
    cuts = [float('inf')] * n
    is_pal = [[False] * n for _ in range(n)]
    
    for i in range(n):
        # Odd length palindromes centered at i
        left = right = i
        while left >= 0 and right < n and s[left] == s[right]:
            is_pal[left][right] = True
            left -= 1
            right += 1
        
        # Even length palindromes centered between i and i+1
        left = i
        right = i + 1
        while left >= 0 and right < n and s[left] == s[right]:
            is_pal[left][right] = True
            left -= 1
            right += 1
    
    for i in range(n):
        if is_pal[0][i]:
            cuts[i] = 0
        else:
            for j in range(i):
                if is_pal[j+1][i]:
                    cuts[i] = min(cuts[i], cuts[j] + 1)
    
    return cuts[n-1]
```
**TC:** O(n²) | **SC:** O(n²)

---

**Key Formula:**
```
cuts[i] = min(cuts[j] + 1) for all j < i where s[j:i] is palindrome
cuts[0] = -1 (or cuts[i] = 0 if whole prefix is palindrome)
```

**Example Walkthrough:**
```
s = "aab", n=3

Precompute is_pal:
- Singles: [0,0]=T, [1,1]=T, [2,2]=T
- Length 2: [0,1]="aa" → T, [1,2]="ab" → F
- Length 3: [0,2]="aab" → s[0]!=s[2] → F

cuts[0] = -1

i=1 (prefix "a"):
  j=0: is_pal[0][0]=T → cuts[1] = min(inf, cuts[0]+1 = -1+1=0) = 0
  Also check if whole prefix is palindrome: is_pal[0][0]=T, so cuts[1]=0

i=2 (prefix "aa"):
  j=0: is_pal[0][1]=T → cuts[2] = min(inf, cuts[0]+1=0) = 0
  j=1: is_pal[1][1]=T → cuts[2] = min(0, cuts[1]+1=0+1=1) = 0
  Whole prefix "aa" is palindrome → cuts[2]=0

i=3 (prefix "aab"):
  j=0: is_pal[0][2]=F
  j=1: is_pal[1][2]=F
  j=2: is_pal[2][2]=T → cuts[3] = cuts[2]+1 = 0+1=1
  
  Also check whole prefix: "aab" not palindrome

Result = cuts[3] = 1
```

**Another Example:**
```
s = "ababa", n=5

Precompute is_pal: whole string is palindrome

cuts[0] = -1
i=1: "a" palindrome → cuts[1]=0
i=2: "ab" not palindrome → cuts[2]=1
i=3: "aba" palindrome → cuts[3]=0
i=4: "abab" not palindrome → cuts[4]=1
i=5: "ababa" palindrome → cuts[5]=0

Result = 0
```

**Comparison Table:**

| Aspect | Palindrome Partitioning (131) | Palindrome Partitioning II (132) |
|--------|------------------------------|---------------------------------|
**Objective** | Generate all partitions | Find minimum cuts |
**Approach** | Backtracking | DP minimization |
**Output** | List of lists | Integer |
**Time Complexity** | O(2ⁿ) | O(n²) |
**Space** | O(n² + output) | O(n²) |

**Palindrome Family:**

| Problem | Type | Key Difference |
|---------|------|---------------|
**5. Longest Palindromic Substring** | Find longest | Single substring |
**647. Palindromic Substrings** | Count all | Count, not cuts |
**131. Palindrome Partitioning** | All partitions | Generate all |
**132. Palindrome Partitioning II** | Min cuts | Minimize cuts |
**516. Longest Palindromic Subsequence** | Subsequence | Can skip chars |

**Edge Cases:**
- Empty string → 0
- Single char → 0
- Already palindrome → 0
- All different chars → n-1 cuts (each char separate)

**Why cuts[0] = -1:**
- Makes the math work: when we find a palindrome from 0 to i-1
- cuts[i] = cuts[0] + 1 = -1 + 1 = 0 cuts needed
- Alternative: initialize cuts[i] = i-1 (max cuts), then check if whole prefix is palindrome

**Optimization Insight:**
- Can compute palindrome information using center expansion while computing cuts
- But still need O(n²) space to store palindrome results for O(1) lookup
- Without palindrome precomputation, each check would be O(n) leading to O(n³)