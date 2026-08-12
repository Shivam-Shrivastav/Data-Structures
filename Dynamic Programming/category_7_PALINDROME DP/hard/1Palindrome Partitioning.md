## 131. Palindrome Partitioning
**Category:** **PALINDROME DP / BACKTRACKING**

**Problem:** Given a string `s`, partition it such that every substring of the partition is a palindrome. Return **all possible palindrome partitions** of `s`.

**Example:**
```
Input: s = "aab"
Output: [["a","a","b"], ["aa","b"]]
```

```
Input: s = "a"
Output: [["a"]]
```

```
Input: s = "efe"
Output: [["e","f","e"], ["efe"]]
```

---

### **Relation to Palindrome Problems**
**Similar to:** **Palindromic Substrings (647)** but **partition into palindromes**
**How it's different:**
1. **Palindromic Substrings:** Count all palindromes
2. **Palindrome Partitioning:** Split string into palindrome segments (all possible ways)
3. **Key Insight:** Need to try all possible cuts and check if each segment is palindrome

**Key Insight:** 
- This is a **backtracking** problem where at each position, we try all possible ending indices that form a palindrome
- We can precompute palindrome information using DP for O(1) checks
- DFS to explore all valid partitions

---

### DP/Backtracking Intuition
- **State:** Current position `start` in string, current `path` of partitions
- **Transition:**
  ```
  For each end from start to n-1:
      if s[start:end+1] is palindrome:
          add it to path
          recurse on end+1
          backtrack
  ```
- **Base:** When `start == n`, add current path to result
- **Optimization:** Precompute `is_pal[i][j]` using DP

---

### 1. Backtracking with Palindrome Check (No Precomputation)
```python
def partition(s):
    n = len(s)
    result = []
    
    def is_palindrome(i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
    def backtrack(start, path):
        if start == n:
            result.append(path[:])
            return
        
        for end in range(start, n):
            if is_palindrome(start, end):
                path.append(s[start:end+1])
                backtrack(end + 1, path)
                path.pop()
    
    backtrack(0, [])
    return result
```
**TC:** O(n × 2ⁿ) | **SC:** O(n) for recursion + O(n²) for output

---

### 2. Backtracking with DP Precomputation (Optimal)
```python
def partition(s):
    n = len(s)
    result = []
    
    # Precompute palindrome information
    is_pal = [[False] * n for _ in range(n)]
    
    # All single chars are palindromes
    for i in range(n):
        is_pal[i][i] = True
    
    # Check length 2
    for i in range(n-1):
        if s[i] == s[i+1]:
            is_pal[i][i+1] = True
    
    # Check longer lengths
    for length in range(3, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and is_pal[i+1][j-1]:
                is_pal[i][j] = True
    
    def backtrack(start, path):
        if start == n:
            result.append(path[:])
            return
        
        for end in range(start, n):
            if is_pal[start][end]:
                path.append(s[start:end+1])
                backtrack(end + 1, path)
                path.pop()
    
    backtrack(0, [])
    return result
```
**TC:** O(n² + 2ⁿ) | **SC:** O(n²) for DP table + O(n) for recursion

---

### 3. Memoization (Store all partitions from position)
```python
def partition(s):
    n = len(s)
    memo = {}  # start -> list of partitions from start
    
    # Precompute palindrome info
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
    
    def dfs(start):
        if start == n:
            return [[]]  # One empty partition
        if start in memo:
            return memo[start]
        
        result = []
        for end in range(start, n):
            if is_pal[start][end]:
                prefix = s[start:end+1]
                suffixes = dfs(end + 1)
                for suffix in suffixes:
                    result.append([prefix] + suffix)
        
        memo[start] = result
        return result
    
    return dfs(0)
```
**TC:** O(n² + 2ⁿ) | **SC:** O(n² + total_output)

---

### 4. BFS Approach (Level-order)
```python
from collections import deque

def partition(s):
    n = len(s)
    
    # Precompute palindrome info
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
    
    # BFS: queue stores (start, path_so_far)
    queue = deque([(0, [])])
    result = []
    
    while queue:
        start, path = queue.popleft()
        
        if start == n:
            result.append(path)
            continue
        
        for end in range(start, n):
            if is_pal[start][end]:
                new_path = path + [s[start:end+1]]
                queue.append((end + 1, new_path))
    
    return result
```
**TC:** O(2ⁿ) | **SC:** O(2ⁿ) for queue

---

### 5. DP + Backtracking (Bottom-up path building)
```python
def partition(s):
    n = len(s)
    
    # dp[i] = list of all partitions of s[i:]
    dp = [[] for _ in range(n + 1)]
    dp[n] = [[]]  # empty partition at end
    
    # Precompute palindrome info
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
    
    # Build from end to start
    for start in range(n-1, -1, -1):
        for end in range(start, n):
            if is_pal[start][end]:
                prefix = s[start:end+1]
                for suffix in dp[end + 1]:
                    dp[start].append([prefix] + suffix)
    
    return dp[0]
```
**TC:** O(2ⁿ) | **SC:** O(n² + total_output)

---

**Key Insight:**
```
At each position start, we try all end >= start where s[start:end+1] is palindrome
Then recursively partition the rest from end+1
```

**Example Walkthrough:**
```
s = "aab", n=3

Precompute is_pal:
- Singles: [0,0]=T, [1,1]=T, [2,2]=T
- Length 2: [0,1]="aa" → T, [1,2]="ab" → F
- Length 3: [0,2]="aab" → s[0]!=s[2] → F

Backtracking from start=0:
  end=0: "a" is palindrome → path=["a"], recurse on start=1
    
    start=1:
      end=1: "a" is palindrome → path=["a","a"], recurse on start=2
        start=2:
          end=2: "b" is palindrome → path=["a","a","b"], start=3 → add to result
      end=2: "ab" not palindrome
    
  end=1: "aa" is palindrome → path=["aa"], recurse on start=2
    start=2:
      end=2: "b" is palindrome → path=["aa","b"], start=3 → add to result
  
  end=2: "aab" not palindrome

Result: [["a","a","b"], ["aa","b"]]
```

**Comparison Table:**

| Aspect | Palindromic Substrings (647) | Palindrome Partitioning (131) |
|--------|------------------------------|-------------------------------|
**Objective** | Count palindromes | Generate all partitions |
**Approach** | DP or center expand | Backtracking + palindrome check |
**Output** | Integer | List of lists |
**Time Complexity** | O(n²) | O(2ⁿ) (exponential output) |
**Space** | O(1) or O(n²) | O(n² + total_output) |

**Palindrome Family:**

| Problem | Type | Key Difference |
|---------|------|---------------|
**5. Longest Palindromic Substring** | Find longest | Single substring |
**647. Palindromic Substrings** | Count all | Count, not generate |
**131. Palindrome Partitioning** | All partitions | Generate all splits |
**132. Palindrome Partitioning II** | Min cuts | Minimize partitions |
**516. Longest Palindromic Subsequence** | Subsequence | Can skip chars |

**Edge Cases:**
- Empty string → [[]] (one empty partition)
- Single char → [["a"]]
- All same chars → 2ⁿ⁻¹ partitions? Actually number of ways to split n identical chars

**Why Backtracking is Necessary:**
- Need to explore all possible valid cuts
- Number of valid partitions can be exponential
- Can't use pure DP for generation (need to store all paths)

**Optimization Tips:**
- Precompute palindrome info for O(1) checks
- Use memoization to avoid recomputing same suffix
- Output size can be huge, so algorithm must handle it