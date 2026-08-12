## **🔹 Subsets II (LeetCode 90) — Backtracking with Duplicates**

---

### **1. Problem Statement with Example**

Given an integer array `nums` that **may contain duplicates**, return **all possible unique subsets** (power set).

* Solution **must not contain duplicate subsets**
* Order of subsets doesn’t matter

#### Example:

```
Input: nums = [1,2,2]

Output:
[
  [], 
  [1], 
  [2], 
  [1,2], 
  [2,2], 
  [1,2,2]
]
```

#### Constraints:

* `1 <= nums.length <= 10`
* `-10 <= nums[i] <= 10`

---

### **2. Diagram (Key Idea: Skip Duplicates)**

👉 First sort: `[1,2,2]`

```
Start: []
 ├── [1]
 │    ├── [1,2]
 │    │     ├── [1,2,2]
 │    │     └── skip duplicate 2
 │    └── skip duplicate 2
 ├── [2]
 │    ├── [2,2]
 │    └── skip duplicate
 └── skip duplicate 2
```

💡 Core rule:

> At same recursion level → **skip duplicates**

---

### **3. Example I/O**

#### Example 1 (Typical)

```
Input: [1,2,2]
Output:
[[], [1], [2], [1,2], [2,2], [1,2,2]]
```

---

#### Example 2 (Edge Case)

```
Input: [2,2]
Output:
[[], [2], [2,2]]
```

---

### **4. Intuition & Pattern Recognition**

💡 Signals:

* “Subsets”
* “Duplicates present”
* “Unique results required”

👉 Think:

> “Same as Subsets I, but avoid duplicate branches”

---

### **5. Simpler Version**

#### 🔹 Start from:

* Subsets
  → no duplicates

#### 🔹 Then add:

* duplicate handling

#### 🧠 Key transition:

```
Subsets I:
    always explore both choices

Subsets II:
    skip if same number used at same level
```

---

### **6. Brute Force**

Generate all subsets and use a set to remove duplicates:

```python
def subsetsWithDup(nums):
    n = len(nums)
    res = set()

    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])
        res.add(tuple(sorted(subset)))

    return [list(x) for x in res]
```

⏱ Time: `O(n * 2^n + sorting)`
📦 Space: high (set storage)

---

### **7. Optimal Solution (Backtracking + Sorting)**

```python
class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()  # sort to group duplicates
        res = []
        subset = []

        def dfs(start):
            # store current subset
            res.append(subset.copy())

                for i in range(start, len(nums)):
                # 🔴 SKIP duplicates at same level
                if i > start and nums[i] == nums[i - 1]:
                    continue

                # choose
                subset.append(nums[i])

                # explore next
                dfs(i + 1)

                # backtrack
                subset.pop()

        dfs(0)
        return res
```

---

### **Why this works**

👉 Condition:

```python
if i > start and nums[i] == nums[i - 1]:
    continue
```

Means:

* Same level (same `start`)
* Same number repeated → skip

---

⏱ Time: `O(n * 2^n)`
📦 Space: `O(n)`

---

### **8. Step-by-Step Trace**

Input: `[1,2,2]`

| Step | start | subset         | Action    |
| ---- | ----- | -------------- | --------- |
| 1    | 0     | []             | add []    |
| 2    | 0     | [1]            | choose 1  |
| 3    | 1     | [1,2]          | choose 2  |
| 4    | 2     | [1,2,2]        | choose 2  |
| 5    | 3     | save           |           |
| 6    | 2     | [1,2]          | backtrack |
| 7    | 2     | skip duplicate | 🚫        |
| 8    | 1     | [1]            | backtrack |
| 9    | 1     | skip duplicate | 🚫        |
| 10   | 0     | [2]            | choose 2  |
| 11   | 1     | [2,2]          | choose 2  |
| 12   | 2     | save           |           |

---

### **9. Related Problems (Pattern Building)**

1. Subsets
   → base version (no duplicates)

2. Permutations II
   → duplicates + ordering

3. Combination Sum II
   → duplicates + target sum

4. Combination Sum
   → reuse allowed

5. Combinations
   → fixed size subsets

---

## 🔥 Interview Shortcut

### Core Template:

```python
nums.sort()

for i in range(start, len(nums)):
    if i > start and nums[i] == nums[i - 1]:
        continue
```

👉 **Golden Rule:**

```
Sort + skip duplicates at same level
```

---

## ⚡ Mental Model

```
Subsets I  → binary decisions
Subsets II → binary decisions + prune duplicate branches
```

---

If you want next:
I can show **exact difference between Subsets II vs Permutations II** (very common confusion in interviews) 🚀
