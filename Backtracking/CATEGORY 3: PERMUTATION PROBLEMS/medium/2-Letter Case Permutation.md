## 🧠 **Letter Case Permutation — Backtracking Pattern**

---

## 1. **Problem Statement**

Given a string `s` containing **letters and digits**, return all possible strings formed by:

* Changing each **letter** to **lowercase or uppercase**
* Keeping **digits unchanged**

Return all combinations in any order.

### ⚠️ Constraints

* `1 <= s.length <= 12`
* `s` consists of letters + digits

---

## 2. **Diagram (Decision Tree)**

Example: `s = "a1b"`

```text
                ""
           /          \
        "a"           "A"
        |              |
      "a1"           "A1"
     /    \         /     \
  "a1b" "a1B"   "A1b"  "A1B"
```

👉 Key idea:

* At each character:

  * If digit → only 1 choice
  * If letter → 2 choices (lower + upper)

---

## 3. **Example I/O**

### ✅ Example 1

```text
Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
```

✔ Explanation:

* 2 letters → 2² = 4 combinations

---

### ⚠️ Edge Case

```text
Input: s = "123"
Output: ["123"]
```

✔ Explanation:

* No letters → only one output

---

## 4. **Intuition & Pattern Recognition**

### 🔑 Signals:

* "Generate all combinations" → backtracking
* "Binary choice per character" → classic DFS tree
* No constraints like sum → simple branching

### 🧠 Interview Thought:

> “Each letter gives me 2 choices → I can do DFS and build strings character by character.”

---

## 5. **Simpler Version**

### 🔹 Step 1:

👉 **Subsets**

* Each element → pick or not pick

### 🔹 Step 2:

👉 Instead of pick/not pick → choose **lower/upper**

### 🔹 Current Problem:

👉 **Letter Case Permutation**

---

### 🧠 Transition Thinking:

* Subsets → include/exclude
* Here → lowercase/uppercase

---

## 6. **Brute Force**

* Generate all `2^n` strings
* Filter valid ones

### ⏱ Complexity:

* Time: **O(2^n)**
* Space: **O(2^n)**

---

## 7. **Optimal Solution (Backtracking)**

```python
class Solution:
    def letterCasePermutation(self, s):
        res = []
        
        def dfs(i, path):
            # ✅ reached end
            if i == len(s):
                res.append(path)
                return
            
            # 🔹 if digit → only one choice
            if s[i].isdigit():
                dfs(i + 1, path + s[i])
            else:
                # 🔹 lowercase
                dfs(i + 1, path + s[i].lower())
                
                # 🔹 uppercase
                dfs(i + 1, path + s[i].upper())
        
        dfs(0, "")
        return res
```

---

### ⏱ Complexity:

* Time: **O(2^L)** (L = number of letters)
* Space: **O(2^L)**

---

## 8. **Step-by-Step Trace**

Input: `"a1b"`

| Step | i         | path  | Action        |
| ---- | --------- | ----- | ------------- |
| 1    | 0         | ""    | start         |
| 2    | 0         | "a"   | lowercase     |
| 3    | 1         | "a1"  | digit         |
| 4    | 2         | "a1b" | lowercase → ✅ |
| 5    | 2         | "a1B" | uppercase → ✅ |
| 6    | backtrack |       |               |
| 7    | 0         | "A"   | uppercase     |
| 8    | 1         | "A1"  | digit         |
| 9    | 2         | "A1b" | lowercase → ✅ |
| 10   | 2         | "A1B" | uppercase → ✅ |

Final:

```
["a1b","a1B","A1b","A1B"]
```

---

## 9. **Related Problems (Pattern Build-Up)**

1. **Subsets**
   → Base binary decision tree

2. **Permutations**
   → Order-based DFS

3. **Letter Combinations of a Phone Number**
   → Multiple branching per digit

4. **Generate Parentheses**
   → Backtracking with constraints

5. **Palindrome Partitioning**
   → String partitioning DFS

---

## 🔥 Final Interview Insight

### 💥 Core Pattern:

```python
dfs(index, path)
```

### 💥 Decision:

* Letter → 2 branches
* Digit → 1 branch

---

### 🧠 One-line intuition:

> “At each character, branch into lowercase and uppercase if it's a letter.”

---

If you want next:

* 🔥 I can show **iterative BFS version (queue-based)**
* 🔥 Or give you **one template that solves all subset/backtracking problems**
