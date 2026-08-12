## 🧠 **Word Pattern II (LeetCode Premium) — Backtracking + HashMap**

---

## 1. **Problem Statement**

Given a pattern string `pattern` and a string `s`, determine if:

- Each character in `pattern` maps to a **non-empty substring** of `s`
- Mapping is **bijective**:
  - One char → one unique substring
  - No two chars map to the same substring
- The concatenation of mapped substrings must equal `s`

---

### ⚠️ Constraints
- `1 <= pattern.length <= 20`
- `1 <= s.length <= 20`
- Backtracking required (exponential search space)

---

## 2. **Diagram (Mapping Exploration Tree)**

Example: `pattern = "ab", s = "redblue"`

```text
Start: {}
 ├── a → "r"
 │    ├── b → "edblue" ✅
 │
 ├── a → "re"
 │    ├── b → "dblue" ✅
 │
 ├── a → "red"
 │    ├── b → "blue" ✅ (valid)
 │
 ├── a → "redb"
 │    ├── b → "lue"
 │
 ...
```

👉 Key idea:
- Try **all possible substrings** for each pattern char
- Maintain:
  - `char → substring`
  - `used substrings`

---

## 3. **Example I/O**

### ✅ Example 1
```text
Input: pattern = "abab", s = "redblueredblue"
Output: True
```

✔ Mapping:
- a → "red"
- b → "blue"

---

### ❌ Example 2
```text
Input: pattern = "aaaa", s = "asdasdasdasd"
Output: True
```

✔ Mapping:
- a → "asd"

---

### ⚠️ Edge Case
```text
Input: pattern = "ab", s = "aa"
Output: False
```

✔ Explanation:
- a → "a"
- b cannot map to "a" (bijection violated)

---

## 4. **Intuition & Pattern Recognition**

### 🔑 Signals:
- "Match pattern with string" → mapping problem
- "All possibilities" → backtracking
- "Bijective mapping" → need:
  - hashmap
  - set

### 🧠 Interview Thought:
> “This is DFS where each pattern char tries all substring splits, while maintaining a bijection using a map + set.”

---

## 5. **Simpler Version**

### 🔹 Step 1:
👉 **entity["leetcode_problem","Word Pattern","LeetCode problem"]**  
- Fixed mapping with words split by space

### 🔹 Step 2:
👉 Remove fixed splitting → now substrings can be anything

### 🔹 Current Problem:
👉 **entity["leetcode_problem","Word Pattern II","LeetCode problem"]**

---

### 🧠 Transition Thinking:
- Word Pattern → direct mapping (no backtracking)
- Here → need to **try all substring partitions**

---

## 6. **Brute Force**

- Generate all partitions of `s`
- Check if mapping fits pattern

### ⏱ Complexity:
- Time: **O(N^N)** (very large)

---

## 7. **Optimal Solution (Backtracking + HashMap + Set)**

```python
class Solution:
    def wordPatternMatch(self, pattern, s):
        char_to_str = {}
        used = set()
        
        def dfs(i, j):
            # i → index in pattern
            # j → index in string
            
            # ✅ both consumed
            if i == len(pattern) and j == len(s):
                return True
            
            # ❌ mismatch
            if i == len(pattern) or j == len(s):
                return False
            
            ch = pattern[i]
            
            # 🔹 already mapped
            if ch in char_to_str:
                word = char_to_str[ch]
                
                # check if it matches current substring
                if not s.startswith(word, j):
                    return False
                
                return dfs(i + 1, j + len(word))
            
            # 🔹 try all possible substrings
            for k in range(j, len(s)):
                word = s[j:k+1]
                
                # 🚫 already used
                if word in used:
                    continue
                
                # 🔹 choose
                char_to_str[ch] = word
                used.add(word)
                
                if dfs(i + 1, k + 1):
                    return True
                
                # 🔙 backtrack
                del char_to_str[ch]
                used.remove(word)
            
            return False
        
        return dfs(0, 0)
```

---

### ⏱ Complexity:
- Time: **O(N^N)** worst case
- Space: **O(N)** recursion + map

---

## 8. **Step-by-Step Trace**

Input: `pattern="ab", s="redblue"`

| Step | i | j | map         | used       | Action |
|------|--|--|-------------|------------|--------|
| 1 | 0 | 0 | {} | {} | try a → "r" |
| 2 | 1 | 1 | {a:r} | {r} | try b → "edblue" |
| 3 | success? yes |

Alternate:
| Step | i | j | map         | used       |
|------|--|--|-------------|------------|
| 1 | 0 | 0 | {} | {} |
| 2 | 0 | 0 | a → "red" | {red} |
| 3 | 1 | 3 | b → "blue" | {red, blue} |
| 4 | 2 | 7 | ✅ |

---

## 9. **Related Problems (Pattern Build-Up)**

1. **entity["leetcode_problem","Word Pattern","LeetCode problem"]**  
   → Fixed mapping (no backtracking)

2. **entity["leetcode_problem","Matchsticks to Square","LeetCode problem"]**  
   → Partitioning with constraints

3. **entity["leetcode_problem","Palindrome Partitioning","LeetCode problem"]**  
   → String partitioning + backtracking

4. **entity["leetcode_problem","Split Array into Fibonacci Sequence","LeetCode problem"]**  
   → Try all splits + validate

5. **entity["leetcode_problem","Expression Add Operators","LeetCode problem"]**  
   → Build expressions with DFS

---

## 🔥 Final Interview Insight

### 💥 Core Pattern:
```python
dfs(pattern_index, string_index)
```

### 💥 Golden Rules:
- Use **map + set** → enforce bijection
- Try **all substring splits**
- Always **backtrack properly**

---

### 🧠 One-line intuition:
> “At each pattern char, try mapping it to every possible substring that hasn’t been used yet.”

---

If you want next:
- 🔥 I can give you a **single reusable backtracking template** covering all problems you've asked
- 🔥 Or a **visual recursion tree breakdown (like your DFS confusion earlier)**