## **🔹 Maximum Length of a Concatenated String with Unique Characters (LeetCode 1239)**

---

### **1. Problem Statement with Example**

Given an array of strings `arr`, you can **concatenate any subsequence of strings** such that:

* The final string has **all unique characters (no duplicates)**
* Return the **maximum possible length**

---

#### Example:

```
Input: arr = ["un","iq","ue"]
Output: 4
Explanation:
"uniq" or "ique" → both length 4
```

---

#### Constraints:

* `1 <= arr.length <= 16`
* `1 <= arr[i].length <= 26`
* Only lowercase English letters

---

### **2. Diagram (Subset Decision Tree)**

Each string → **take or skip**

```
arr = ["un", "iq", "ue"]

                 ""
           /              \
        "un"              ""
      /      \         /       \
 "un+iq"   "un"   "iq"        ""
   |         |      |          |
"uniq"   "un+ue"  "iq+ue"    "ue"
```

👉 At each step:

* Include string (if valid)
* Exclude string

---

### **3. Example I/O**

#### Example 1 (Typical)

```
Input: ["un","iq","ue"]
Output: 4
```

---

#### Example 2 (Edge Case)

```
Input: ["aa","bb"]
Output: 0
```

Explanation:

* "aa" invalid (duplicate inside itself)
* "bb" invalid
  → no valid concatenation

---

### **4. Intuition & Pattern Recognition**

💡 Signals:

* “Subsequence / choose subset”
* “Maximize something”
* “Constraint on uniqueness”

👉 Think:

> “This is Subsets + validity check”

---

### **5. Simpler Version**

#### 🔹 Start from:

* Subsets
  → generate all subsets

#### 🔹 Add constraint:

* Only keep subsets where characters are unique

---

### 🧠 Transition Thinking

```
Subsets:
    include / exclude

This problem:
    include if VALID
```

---

### **6. Brute Force**

Generate all subsets and check uniqueness:

```python
def maxLength(arr):
    def is_unique(s):
        return len(set(s)) == len(s)

    n = len(arr)
    res = 0

    for mask in range(1 << n):
        s = ""
        for i in range(n):
            if mask & (1 << i):
                s += arr[i]

        if is_unique(s):
            res = max(res, len(s))

    return res
```

⏱ Time: `O(2^n * n * 26)`
📦 Space: high

---

### **7. Optimal Solution (Backtracking + Pruning)**

👉 Key idea:

* Track characters using **set**
* Skip invalid paths early

```python
class Solution:
    def maxLength(self, arr):
        res = 0

        def dfs(i, char_set):
            nonlocal res

            # update max
            res = max(res, len(char_set))

            for j in range(i, len(arr)):
                s = arr[j]

                # check if valid to add
                if len(set(s)) != len(s):
                    continue  # skip invalid string itself

                if any(c in char_set for c in s):
                    continue  # conflict with existing

                # choose
                for c in s:
                    char_set.add(c)

                dfs(j + 1, char_set)

                # backtrack
                for c in s:
                    char_set.remove(c)

        dfs(0, set())
        return res
```

---

### **🔥 Optimization Insight**

Instead of string:
👉 Use **bitmask (26 bits)** for faster checks

---

⏱ Time: `O(2^n)`
📦 Space: `O(n)`

---

### **8. Step-by-Step Trace**

Input: `["un","iq","ue"]`

| Step | i                                | char_set  | Action               |
| ---- | -------------------------------- | --------- | -------------------- |
| 1    | 0                                | {}        | start                |
| 2    | 0                                | {u,n}     | include "un"         |
| 3    | 1                                | {u,n,i,q} | include "iq" → valid |
| 4    | update res = 4                   |           |                      |
| 5    | try "ue" → conflict (u) ❌        |           |                      |
| 6    | backtrack to {u,n}               |           |                      |
| 7    | include "ue" → conflict ❌        |           |                      |
| 8    | backtrack to {}                  |           |                      |
| 9    | include "iq" → {i,q}             |           |                      |
| 10   | include "ue" → {i,q,u,e} → res=4 |           |                      |

---

### **9. Related Problems (Pattern Building)**

1. Subsets
   → base subset generation

2. Subsets II
   → subsets + constraints

3. Combination Sum
   → choose valid combinations

4. Partition to K Equal Sum Subsets
   → subset + constraint pruning

---

## 🔥 Interview Shortcut

### Core Idea:

```
Subsets + constraint check + pruning
```

---

### ⚡ Key Template

```python
for j in range(i, n):
    if valid:
        choose
        dfs(j+1)
        backtrack
```

---

## 🧠 Mental Model

```
Subsets → explore all

This problem → explore only VALID subsets
```

---

## 🚀 Key Insight

```
Prune early = huge speedup
```

---

If you want next level:
I can show **bitmask version (VERY IMPORTANT for interviews)** which turns this into a super clean solution 🚀
