    ## **🔹 Generalized Abbreviation (LeetCode 320) — Backtracking Pattern**

---

### **1. Problem Statement with Example**

Given a string `word`, return **all possible generalized abbreviations**.

👉 Rule:

* You can replace **any substring of consecutive characters** with its **length (count)**

---

#### Example:

```text
Input: word = "word"

Output:
[
 "word", "1ord", "w1rd", "wo1d", "wor1",
 "2rd", "w2d", "wo2",
 "1o1d", "1or1", "w1r1",
 "1o2", "2r1",
 "3d", "w3",
 "4"
]
```

#### Constraints:

* `1 <= word.length <= 15`

---

### **2. Diagram (Decision Tree)**

Each character → **2 choices**

* Abbreviate (increase count)
* Keep character (flush count)

```text
Index: 0   1   2
Word:  w   o   r

                ""
        /                 \
   "w" (keep)         "1" (abbr)
    /     \             /      \
 "wo"   "w1"         "1o"     "2"
```

👉 Key: maintain a **count of abbreviated chars**

---

### **3. Example I/O**

#### Example 1 (Typical)

```
Input: "ab"
Output:
["ab", "1b", "a1", "2"]
```

Explanation:

* keep both → "ab"
* abbreviate 'a' → "1b"
* abbreviate 'b' → "a1"
* abbreviate both → "2"

---

#### Example 2 (Edge Case)

```
Input: "a"
Output: ["a", "1"]
```

---

### **4. Intuition & Pattern Recognition**

💡 Signals:

* “Generate all possibilities”
* “Each character → choice”
* “Abbreviation count merging”

👉 Think:

> “At each index → either take char OR count it”

---

### **5. Simpler Version**

#### 🔹 Simplest:

Binary decision (like subsets):

* include char OR skip

#### 🔹 Related problems:

* Subsets
  → include/exclude
* Letter Case Permutation
  → toggle decisions
* Permutations
  → arrangement

---

### 🧠 Transition Thinking

```text
Subsets:
    pick or skip element

Here:
    pick char OR increase abbreviation count
```

---

### **6. Brute Force**

Generate all subsets of indices to abbreviate, then build strings.

* Complicated merging of counts
* Inefficient

⏱ Time: ~`O(2^n * n)`

---

### **7. Optimal Solution (Backtracking)**

👉 Track:

* `i` → current index
* `cur` → current string
* `count` → number of abbreviated chars

```python
class Solution:
    def generateAbbreviations(self, word):
        res = []

        def dfs(i, cur, count):
            # base case
            if i == len(word):
                # append remaining count if exists
                if count > 0:
                    cur += str(count)
                res.append(cur)
                return

            # 🔹 Option 1: Abbreviate this char
            dfs(i + 1, cur, count + 1)

            # 🔹 Option 2: Keep this char
            new_cur = cur
            if count > 0:
                new_cur += str(count)  # flush count

            new_cur += word[i]

            dfs(i + 1, new_cur, 0)  # reset count

        dfs(0, "", 0)
        return res
```

---

### **Key Idea**

```text
count accumulates skipped characters
flush count only when adding a real character
```

---

⏱ Time: `O(2^n * n)`
📦 Space: `O(n)`

---

### **8. Step-by-Step Trace**

Input: `"ab"`

| Step | i   | cur   | count | Action         |
| ---- | --- | ----- | ----- | -------------- |
| 1    | 0   | ""    | 0     | start          |
| 2    | 1   | ""    | 1     | abbreviate 'a' |
| 3    | 2   | ""    | 2     | abbreviate 'b' |
| 4    | end | "2"   |       | save           |
| 5    | 1   | "1a"  | 0     | keep 'a'       |
| 6    | 2   | "1a"  | 1     | abbreviate 'b' |
| 7    | end | "1a1" |       | save           |

... continues

---

### **9. Related Problems (Pattern Building)**

1. Subsets
   → base binary decision

2. Letter Case Permutation
   → toggle choices

3. Permutations
   → ordering decisions

4. Restore IP Addresses
   → segmentation + constraints

---

## 🔥 Interview Shortcut

### Core Template:

```python
dfs(i, cur, count):
    if end:
        append result

    # abbreviate
    dfs(i+1, cur, count+1)

    # keep
    cur += count (if any)
    cur += char
    dfs(i+1, cur, 0)
```

---

## ⚡ Mental Model

```text
Subsets:
    include / exclude

Generalized Abbreviation:
    include char / count it
```

---

## 🚀 Key Insight

```text
Count is lazy — only convert to string when needed
```

---

If you want, I can give you:
👉 a **universal backtracking template** covering:
(Subsets, Permutations, Combination Sum, Abbreviation) in ONE pattern — super useful in interviews
