## 🔹 Palindrome Partitioning (Backtracking Pattern)

---

## 1. Problem Statement with Example

Given a string `s`, partition it such that **every substring is a palindrome**.
Return **all possible palindrome partitionings**.

---

### Example

```
Input: s = "aab"

Output:
[
 ["a","a","b"],
 ["aa","b"]
]
```

---

### Constraints

* 1 ≤ len(s) ≤ ~16
* Need **all possible partitions** → exponential search
* Substring must be **palindrome**

---

## 2. Diagram (Decision Tree)

At each index → we choose a substring and recurse

```
s = "aab"

Start at index 0:

           []
        /       \
      "a"       "aa"
      /           \
   ["a"]        ["aa"]
   /   \           \
 "a"   "ab"        "b"
 /       X          \
["a","a"]         ["aa","b"]
   |
  "b"
   |
["a","a","b"]
```

👉 We try all cuts, but only proceed if substring is palindrome

---

## 3. Example I/O

### Example 1 (Typical)

```
Input: "aab"
Output:
[
 ["a","a","b"],
 ["aa","b"]
]
```

---

### Example 2 (Edge Case)

```
Input: "a"
Output: [["a"]]
```

---

### Example 3

```
Input: "aba"
Output:
[
 ["a","b","a"],
 ["aba"]
]
```

---

## 4. Intuition & Pattern Recognition

### 🚨 Signals

* “Partition string”
* “Return all possibilities”
* “Constraint on substring”

👉 This is classic:

> **Backtracking + substring validation**

---

### Core Idea

At index `i`, try all possible substrings:

```
s[i:j]  for j = i → n-1
```

👉 If substring is palindrome:

* choose it
* recurse from `j+1`

---

### Interview Thought

> “This is a partition problem where I explore all possible cuts and prune using palindrome checks.”

---

## 5. Simpler Version

### Step 1: Basic Partitioning

👉 **Subsets**

* Try all splits (no constraint)

---

### Step 2: Palindrome Check

👉 **Valid Palindrome**

* Check if substring is valid

---

### Step 3: Combine

👉 Current problem =

* Generate all partitions
* Keep only palindrome ones

---

### Thinking Flow

```
Try all cuts
   ↓
Check palindrome
   ↓
Recurse
```

---

## 6. Brute Force

### Idea

* Generate all partitions (2^(n-1))
* Check each partition fully

### Complexity

* Time: **O(2^n * n)**

---

## 7. Optimal Solution (Backtracking)

---

### Code

```python
class Solution:
    def partition(self, s: str):
        res = []
        path = []
        
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def backtrack(start):
            if start == len(s):
                res.append(path[:])
                return
            
            for end in range(start, len(s)):
                if isPalindrome(start, end):
                    path.append(s[start:end+1])
                    backtrack(end + 1)
                    path.pop()
        
        backtrack(0)
        return res
```

---

### Complexity

* Time: **O(2^n * n)**
* Space: O(n) recursion

---

### 🔥 Optimization (DP + Backtracking)

Precompute palindrome:

```python
dp[i][j] = True if s[i:j] is palindrome
```

👉 reduces repeated checks

---

## 8. Step-by-Step Trace

### Input: `"aab"`

---

### Start

```
path = []
start = 0
```

---

### Step 1

Try substrings from index 0:

* `"a"` ✅

```
path = ["a"]
```

---

### Step 2

From index 1:

* `"a"` ✅

```
path = ["a","a"]
```

---

### Step 3

From index 2:

* `"b"` ✅

```
path = ["a","a","b"] → ADD
```

---

### Backtrack

```
path = ["a"]
```

Try:

* `"ab"` ❌

---

### Back to start

Try:

* `"aa"` ✅

```
path = ["aa"]
```

Then:

* `"b"` → ["aa","b"] ✔

---

## 9. Related Problems

1. **Palindrome Partitioning II**
   → Min cuts (DP optimization)

2. **Word Break**
   → Partition string with dictionary

3. **Word Break II**
   → Return all partitions (similar structure)

4. **Restore IP Addresses**
   → Partition with constraints

5. **Subsets**
   → Base backtracking pattern

---

## 🔥 Interview One-Liner

👉 *“I try all substring cuts using backtracking and only continue recursion when the chosen substring is a palindrome.”*

---

If you want, I can also show:

* ⚡ DP table visualization (very important for follow-up)
* ⚡ How this evolves into **Palindrome Partitioning II (harder)**
* ⚡ Trick to reduce time from O(n³) → O(n²)
