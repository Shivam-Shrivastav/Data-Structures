## **🔹 Permutations (LeetCode 46) — Backtracking Pattern**

---

### **1. Problem Statement with Example**

Given an array `nums` of **distinct integers**, return **all possible permutations**.

* A permutation = arrangement of all elements
* Order **matters**

#### Example:

```
Input: nums = [1,2,3]

Output:
[
 [1,2,3],
 [1,3,2],
 [2,1,3],
 [2,3,1],
 [3,1,2],
 [3,2,1]
]
```

#### Constraints:

* `1 <= nums.length <= 6`
* All elements are unique

---

### **2. Diagram (Permutation Tree)**

Each level → pick one unused element

```
                []
        /        |        \
      [1]       [2]       [3]
     /   \     /   \     /   \
 [1,2] [1,3] [2,1] [2,3] [3,1] [3,2]
   |      |      |      |      |      |
[1,2,3][1,3,2]...[3,2,1]
```

👉 Depth = length of nums
👉 Each level → choose from remaining elements

---

### **3. Example I/O**

#### Example 1 (Typical)

```
Input: [1,2]
Output: [[1,2], [2,1]]
```

---

#### Example 2 (Edge Case)

```
Input: [1]
Output: [[1]]
```

---

### **4. Intuition & Pattern Recognition**

💡 **Signals for Permutations:**

* “arrangements”
* “order matters”
* “use all elements”

👉 Think:

> “At each step, choose any unused element”

This is:

* Not include/exclude (like subsets)
* Instead → **choose from remaining options**

---

### **5. Simpler Version**

#### 🔹 Simplest:

Permutations of `[1,2]`

```
[1,2]
[2,1]
```

#### 🔹 Related simpler problems:

* Subsets
  → choose or skip
* Combinations
  → fixed size
* Permutations
  → use ALL elements
* Permutations II
  → handle duplicates

#### 🧠 Thinking progression:

```
Subsets → choose/not choose
Permutations → choose from remaining pool
```

---

### **6. Brute Force**

Use built-in:

```python
import itertools

def permute(nums):
    return list(itertools.permutations(nums))
```

⏱ Time: `O(n! * n)`
📦 Space: depends on output

---

### **7. Optimal Solution (Backtracking)**

### ✅ Approach 1: Using `visited`

```python
class Solution:
    def permute(self, nums):
        res = []
        perm = []
        visited = [False] * len(nums)

        def dfs():
            # Base case: permutation complete
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for i in range(len(nums)):
                if visited[i]:
                    continue  # skip already used elements

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

### ✅ Approach 2: In-place swapping (Most optimal)

```python
class Solution:
    def permute(self, nums):
        res = []

        def dfs(start):
            if start == len(nums):
                res.append(nums.copy())
                return

            for i in range(start, len(nums)):
                # swap
                nums[start], nums[i] = nums[i], nums[start]

                dfs(start + 1)

                # backtrack (undo swap)
                nums[start], nums[i] = nums[i], nums[start]

        dfs(0)
        return res
```

⏱ Time: `O(n! * n)`
📦 Space: `O(n)` recursion

---

### **8. Step-by-Step Trace**

Input: `[1,2,3]` (swap approach)

| Step | start | nums    | Action           |
| ---- | ----- | ------- | ---------------- |
| 1    | 0     | [1,2,3] | start            |
| 2    | 0     | [1,2,3] | swap(0,0)        |
| 3    | 1     | [1,2,3] | swap(1,1)        |
| 4    | 2     | [1,2,3] | swap(2,2) → save |
| 5    | 1     | [1,3,2] | swap(1,2)        |
| 6    | 2     | [1,3,2] | save             |
| 7    | 0     | [2,1,3] | swap(0,1)        |
| 8    | ...   | ...     | continues        |

---

### **9. Related Problems (Pattern Building)**

1. Permutations II
   → duplicates → skip same choices

2. Subsets
   → include/exclude pattern

3. Combination Sum
   → choose multiple times

4. N-Queens
   → permutations + constraints

5. Letter Combinations of a Phone Number
   → cartesian product style

---

## 🔥 Interview Shortcut

| Problem Type | Pattern             |
| ------------ | ------------------- |
| Subsets      | include / exclude   |
| Permutations | pick from remaining |
| Combinations | pick k elements     |

---

## ⚡ Key Insight

```
Subsets → decision per element
Permutations → decision per position
```

---

If you want next level:
I can show you:

* exact template to convert subsets → permutations instantly
* how to handle duplicates (very common trap)
* pruning tricks for faster backtracking 🚀
