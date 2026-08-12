## 🔹 Word Squares (HARD) — Backtracking + Trie

---

## 1. Problem Statement with Example

Given a list of **unique words** (all same length), return all possible **word squares**.

A **word square** is a sequence of words such that:

👉 The **k-th row = k-th column**

---

### Example

```
Input: ["area","lead","wall","lady","ball"]

Output:
[
 ["wall","area","lead","lady"],
 ["ball","area","lead","lady"]
]
```

---

## 2. Diagram (Core Constraint)

```
Square (4x4):

w a l l
a r e a
l e a d
l a d y

Column check:
col 0 → w a l l  ✔ matches row 0
col 1 → a r e a  ✔ matches row 1
col 2 → l e a d  ✔ matches row 2
col 3 → l a d y  ✔ matches row 3
```

---

## 3. Example I/O

### Example 1 (Typical)

```
Input: ["area","lead","wall","lady","ball"]

Output:
[
 ["wall","area","lead","lady"],
 ["ball","area","lead","lady"]
]
```

---

### Example 2 (Edge Case)

```
Input: ["ab","cd"]
Output: []
```

👉 No valid square possible

---

## 4. Intuition & Pattern Recognition

### 🚨 Signals

* “Build sequences step-by-step”
* “Constraint depends on previous choices”
* “Prefix must match dynamically”

👉 This screams:

> **Backtracking + Prefix lookup optimization**

---

### Core Insight

When building square:

At step `k`, we already have:

```
row0
row1
...
row(k-1)
```

👉 Next word must satisfy:

```
word[k][i] == word[i][k]  for all i < k
```

So we construct a **prefix**:

```
prefix = square[0][k] + square[1][k] + ... + square[k-1][k]
```

👉 Now we need words that start with this prefix

---

## 5. Simpler Version

### Step 1: Basic Backtracking

👉 **Permutations**

* Try all combinations

---

### Step 2: Prefix Matching

👉 **Implement Trie (Prefix Tree)**

* Efficient prefix lookup

---

### Step 3: Combine

👉 Current problem =

* Backtracking + pruning using prefix

---

### Thinking Flow

```
Try all words
   ↓
At each step enforce prefix constraint
   ↓
Use Trie to speed up prefix search
```

---

## 6. Brute Force

### Idea

* Generate all permutations of words
* Check if square valid

### Complexity

* Time: **O(n! * n²)**

❌ Completely infeasible

---

## 7. Optimal Solution (Backtracking + Trie)

---

### Step 1: Build Trie (prefix → words)

---

### Code

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []  # words with this prefix


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.words.append(word)
    
    def find_prefix(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        return node.words


class Solution:
    def wordSquares(self, words):
        n = len(words[0])
        
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        res = []
        
        def backtrack(square):
            if len(square) == n:
                res.append(square[:])
                return
            
            # build prefix
            k = len(square)
            prefix = "".join([word[k] for word in square])
            
            # get candidates
            for candidate in trie.find_prefix(prefix):
                square.append(candidate)
                backtrack(square)
                square.pop()
        
        for word in words:
            backtrack([word])
        
        return res
```

---

### Complexity

* Time: ~ **O(n * (branching^n))**
* Much faster due to pruning

---

## 8. Step-by-Step Trace

### Input:

```
["wall","area","lead","lady","ball"]
```

---

### Start

```
square = ["wall"]
```

---

### Step 1 (k=1)

```
prefix = "a"   (column 1)

Candidates: ["area"]
```

```
square = ["wall","area"]
```

---

### Step 2 (k=2)

```
prefix = "le"

Candidates: ["lead"]
```

```
square = ["wall","area","lead"]
```

---

### Step 3 (k=3)

```
prefix = "lad"

Candidates: ["lady"]
```

```
square = ["wall","area","lead","lady"] ✔
```

---

## 9. Related Problems

1. **Implement Trie (Prefix Tree)**
   → Core data structure for prefix search

2. **Word Search II**
   → Trie + DFS on grid

3. **Palindrome Pairs**
   → String matching with clever pruning

4. **Concatenated Words**
   → Recursive prefix decomposition

5. **Word Break II**
   → Backtracking + prefix pruning

---

## 🔥 Interview One-Liner

👉 *"At each step I enforce the row=column constraint by building a prefix and use a Trie to efficiently fetch only valid candidates, drastically pruning the search space."*

---

If you want next level mastery, I can show:

* ❗ Why Trie is mandatory (vs hashmap)
* ❗ How to reduce memory using prefix map
* ❗ Common interview pitfalls (very important for HARD)
