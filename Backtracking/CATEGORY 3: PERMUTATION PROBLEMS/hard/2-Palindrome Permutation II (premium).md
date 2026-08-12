## 🔹 Palindrome Permutation II (Backtracking Pattern)

---

## 1. Problem Statement with Example

Given a string `s`, return **all possible palindromic permutations** of `s`.
If no palindromic permutation exists, return an empty list.

### Key Constraints

* Length of string ≤ ~16 (important → factorial explosion)
* Characters can repeat
* Need **unique permutations only**

---

### Example

```
Input: s = "aabb"
Output: ["abba", "baab"]
```

---

## 2. Diagram (Half Construction Idea)

Instead of permuting full string → we only permute **half** and mirror it.

```
s = "aabb"

freq = {a:2, b:2}

Half = "ab"

Permutations of half:
    ab      → ab + reverse(ab) = abba
    ba      → ba + reverse(ba) = baab
```

If odd character exists:

```
s = "aabbc"

Half = "ab"
Middle = "c"

ab + c + ba = abcba
```

---

## 3. Example I/O

### Example 1 (Typical)

```
Input: "aabb"
Output: ["abba", "baab"]
```

👉 Both are valid palindromes

---

### Example 2 (Edge Case)

```
Input: "abc"
Output: []
```

👉 More than one odd frequency → impossible

---

### Example 3 (Odd Length)

```
Input: "aabbc"
Output: ["abcba", "bacab"]
```

---

## 4. Intuition & Pattern Recognition

### 🚨 Key Observations

* A palindrome:

  * Left half = reverse(right half)
* So instead of permuting full string →
  👉 **Permute only half**

---

### When to recognize this pattern in interview:

* "Generate all palindromes"
* "Rearrange string to palindrome"
* "Permutations with symmetry"

---

### Core Idea

1. Count frequencies
2. Check palindrome possible:

   * At most **one odd count**
3. Build:

   * `half string`
   * `middle character (if odd)`
4. Generate **unique permutations of half**
5. Mirror them

---

## 5. Simpler Version

### Step 1: Basic Problem

👉 **Palindrome Permutation**

* Just check if palindrome possible
* Rule: ≤ 1 odd frequency

---

### Step 2: Permutations

👉 **Permutations II**

* Generate unique permutations with duplicates

---

### Step 3: Combine both

👉 Current problem =

* Filter valid palindrome
* Then apply permutation on half

---

### Thinking Flow

```
Check valid palindrome
   ↓
Reduce to half
   ↓
Apply permutations II
   ↓
Mirror result
```

---

## 6. Brute Force

### Idea

* Generate all permutations of string
* Filter palindromes

### Code

```python
def generatePalindromes(s):
    from itertools import permutations
    
    res = set()
    for p in permutations(s):
        p = "".join(p)
        if p == p[::-1]:
            res.add(p)
    return list(res)
```

### Complexity

* Time: **O(n! * n)**
* Space: O(n!)

❌ Too slow

---

## 7. Optimal Solution (Backtracking)

### Key Trick

* Use **half string**
* Handle duplicates using sorting + skip logic

---

### Code

```python
from collections import Counter

class Solution:
    def generatePalindromes(self, s: str):
        freq = Counter(s)
        
        # Step 1: check validity
        odd_char = ""
        half = []
        
        for ch, count in freq.items():
            if count % 2 != 0:
                if odd_char:
                    return []  # more than one odd
                odd_char = ch
            
            half.extend([ch] * (count // 2))
        
        # Step 2: generate unique permutations of half
        half.sort()
        res = []
        used = [False] * len(half)
        
        def backtrack(path):
            if len(path) == len(half):
                # build palindrome
                left = "".join(path)
                res.append(left + odd_char + left[::-1])
                return
            
            for i in range(len(half)):
                if used[i]:
                    continue
                
                # skip duplicates
                if i > 0 and half[i] == half[i-1] and not used[i-1]:
                    continue
                
                used[i] = True
                path.append(half[i])
                
                backtrack(path)
                
                path.pop()
                used[i] = False
        
        backtrack([])
        return res
```

---

### Complexity

* Time: **O((n/2)!)**
* Space: O(n)

✅ Huge improvement over n!

---

## 8. Step-by-Step Trace

### Input: `"aabb"`

```
freq = {a:2, b:2}

half = ['a', 'b']
odd_char = ""
```

---

### Backtracking

| Step | Path  | Used   | Action   |
| ---- | ----- | ------ | -------- |
| 1    | []    | [F, F] | start    |
| 2    | [a]   | [T, F] | pick 'a' |
| 3    | [a,b] | [T, T] | pick 'b' |
| 4    | DONE  |        | → "abba" |
| 5    | [b]   | [F, T] | pick 'b' |
| 6    | [b,a] | [T, T] | pick 'a' |
| 7    | DONE  |        | → "baab" |

---

## 9. Related Problems

1. **Palindrome Permutation**
   → Only check feasibility (no generation)

2. **Permutations II**
   → Core duplicate-handling backtracking

3. **Valid Palindrome II**
   → Palindrome validation with modification

4. **Generate Parentheses**
   → Backtracking with constraints

5. **Letter Tile Possibilities**
   → Permutations with frequency pruning

---

## 🔥 Interview One-Liner

👉 *"Instead of permuting the whole string, I reduce it to half using frequency symmetry, generate unique permutations, and mirror them to form palindromes."*

---

If you want, I can **visually animate the recursion tree** like we did for subsets — that makes this super intuitive.
