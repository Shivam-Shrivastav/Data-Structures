    ## **🔹 Permutations II (LeetCode 47) — Backtracking with Duplicates**

---

### **1. Problem Statement with Example**

Given an array `nums` that **may contain duplicates**, return **all unique permutations**.

* Each permutation uses **all elements**
* No duplicate permutations allowed

#### Example:

```id="j3y2l1"
Input: nums = [1,1,2]

Output:
[
 [1,1,2],
 [1,2,1],
 [2,1,1]
]
```

#### Constraints:

* `1 <= nums.length <= 8`
* `-10 <= nums[i] <= 10`

---

### **2. Diagram (Key: Avoid Same Choice at Same Level)**

Sort first → `[1,1,2]`

```id="5xg7fr"
Level 0:
   choose 1 (index 0)
   skip 1 (index 1 ❌ duplicate at same level)
   choose 2

Tree:
          []
      /         \
    [1]         [2]
   /   \        /
[1,1] [1,2]  [2,1]
   |      |      |
[1,1,2] [1,2,1] [2,1,1]
```

---

### **3. Example I/O**

#### Example 1 (Typical)

```id="y6r5pw"
Input: [1,1,2]
Output: [[1,1,2], [1,2,1], [2,1,1]]
```

---

#### Example 2 (Edge Case)

```id="q2n9zt"
Input: [1,1]
Output: [[1,1]]
```

---

### **4. Intuition & Pattern Recognition**

💡 Signals:

* “Permutations”
* “Duplicates present”
* “Unique permutations required”

👉 Think:

> “Pick elements for positions, but avoid choosing same duplicate twice at same level”

---

### **5. Simpler Version**

#### 🔹 Start from:

* Permutations
  → no duplicates

#### 🔹 Add:

* duplicate control

#### 🧠 Transition:

```id="qprn0k"
Permutations I:
    use visited[]

Permutations II:
    use visited[] + skip duplicates smartly
```

---

### **6. Brute Force**

Generate all permutations and remove duplicates:

```python id="d3mb2y"
import itertools

def permuteUnique(nums):
    return list(set(itertools.permutations(nums)))
```

⏱ Time: `O(n! * n)`
📦 Space: high (set)

---

### **7. Optimal Solution (Backtracking + Sorting)**

```python id="f2wq8l"
class Solution:
    def permuteUnique(self, nums):
        nums.sort()  # sort to group duplicates
        res = []
        perm = []
        visited = [False] * len(nums)

        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for i in range(len(nums)):

                # skip used elements
                if visited[i]:
                    continue

                # 🔴 SKIP duplicates
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue

                # choose
                visited[i] = True
                perm.append(nums[i])

                dfs()

                # backtrack
                perm.pop()
                visited[i] = False

        dfs()
        return res
```

---

### **🔥 Key Condition Explained**

```python id="8m3h7x"
if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
    continue
```

👉 Meaning:

* Same number as previous
* Previous duplicate **NOT used in this path**
* → skip to avoid duplicate permutations

---

⏱ Time: `O(n! * n)`
📦 Space: `O(n)`

---

### **8. Step-by-Step Trace**

Input: `[1,1,2]`

| Step | perm       | visited   | Action        |
| ---- | ---------- | --------- | ------------- |
| 1    | []         | [F,F,F]   | start         |
| 2    | [1]        | [T,F,F]   | pick 1 (i=0)  |
| 3    | [1,1]      | [T,T,F]   | pick 1 (i=1)  |
| 4    | [1,1,2]    | [T,T,T]   | pick 2 → save |
| 5    | [1]        | backtrack |               |
| 6    | [1,2]      | [T,F,T]   | pick 2        |
| 7    | [1,2,1]    | [T,T,T]   | save          |
| 8    | []         | backtrack |               |
| 9    | skip i=1 ❌ | duplicate |               |
| 10   | [2]        | [F,F,T]   | pick 2        |
| 11   | [2,1]      | [T,F,T]   | pick 1        |
| 12   | [2,1,1]    | save      |               |

---

### **9. Related Problems (Pattern Building)**

1. Permutations
   → base version

2. Subsets II
   → duplicates but subsets

3. Combination Sum II
   → duplicates + sum constraint

4. N-Queens
   → permutations + constraints

5. Letter Tile Possibilities
   → permutations with duplicates

---

## 🔥 Interview Shortcut

### Core Rule:

```python id="ztv6r4"
Sort + visited[] + skip if previous duplicate not used
```

---

## ⚡ Subsets II vs Permutations II (IMPORTANT)

| Feature           | Subsets II  | Permutations II    |
| ----------------- | ----------- | ------------------ |
| Order matters?    | ❌ No        | ✅ Yes              |
| visited[] needed? | ❌ No        | ✅ Yes              |
| Skip condition    | `i > start` | `not visited[i-1]` |

---

## 🧠 Mental Model

```id="5q3qcg"
Subsets II:
    skip duplicates at same recursion level

Permutations II:
    skip duplicates unless previous identical element is used
```

---

If you want, I can give you:

* **1 universal backtracking template** that solves all 4:
  (Subsets, Subsets II, Permutations, Permutations II) 🚀
