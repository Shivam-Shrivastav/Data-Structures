## **🔹 Find Unique Binary String (LeetCode 1980) — Backtracking / Math Insight**

---

### **1. Problem Statement with Example**

Given an array `nums` of **n unique binary strings**, each of length `n`, return **any binary string of length `n` that does NOT appear in `nums`.**

* Each string contains only `'0'` and `'1'`
* All strings in `nums` are unique

#### Example:

```
Input: nums = ["01","10"]
Output: "00"  (or "11")
```

#### Constraints:

* `1 <= n <= 16`
* Each string length = `n`

---

### **2. Diagram (Search Space of Binary Strings)**

For `n = 3`, all possible binary strings:

```
000
001
010
011
100
101
110
111
```

👉 Total = `2^n` possibilities
👉 Given only `n` strings → **many missing**

---

### **3. Example I/O**

#### Example 1 (Typical)

```
Input: ["01","10"]
Output: "00"
```

Explanation:
All possible → {00,01,10,11}
Given → {01,10}
Missing → {00,11}

---

#### Example 2 (Edge Case)

```
Input: ["0"]
Output: "1"
```

Explanation:
Only 1-bit strings → {0,1} → pick missing

---

### **4. Intuition & Pattern Recognition**

💡 Signals:

* “Find missing string”
* “Binary strings of length n”
* “Given n strings but total possibilities = 2^n”

👉 Key realization:

```
n << 2^n  → guaranteed missing exists
```

---

### **5. Simpler Version**

#### 🔹 Simplest:

n = 2 → find missing from {00,01,10,11}

#### 🔹 Related problems:

* Subsets
  → generate all combinations
* Permutations
  → generate all arrangements

#### 🧠 Transition:

```
Generate all binary strings → check which is missing
→ optimize using clever observation
```

---

### **6. Brute Force (Backtracking)**

Generate all binary strings and check:

```python
class Solution:
    def findDifferentBinaryString(self, nums):
        n = len(nums)
        num_set = set(nums)

        def dfs(path):
            if len(path) == n:
                s = "".join(path)
                if s not in num_set:
                    return s
                return None

            # try '0'
            res = dfs(path + ['0'])
            if res:
                return res

            # try '1'
            res = dfs(path + ['1'])
            return res

        return dfs([])
```

⏱ Time: `O(2^n * n)`
📦 Space: `O(n)`

---

### **7. Optimal Solution (Diagonal Trick 🔥)**

👉 Inspired by **Cantor’s Diagonal Argument**

```python
class Solution:
    def findDifferentBinaryString(self, nums):
        res = []

        for i in range(len(nums)):
            # flip diagonal bit
            if nums[i][i] == '0':
                res.append('1')
            else:
                res.append('0')

        return "".join(res)
```

---

### **🔥 Why this works**

Given:

```
nums = ["01",
        "10"]
```

Construct:

```
Take nums[0][0] → flip → 1
Take nums[1][1] → flip → 1
Result = "11"
```

👉 This string differs from every string at **at least one index**

---

⏱ Time: `O(n)`
📦 Space: `O(n)`

---

### **8. Step-by-Step Trace**

Input:

```
["01", "10"]
```

| i | nums[i][i] | flip | result |
| - | ---------- | ---- | ------ |
| 0 | '0'        | '1'  | "1"    |
| 1 | '0'        | '1'  | "11"   |

Output: `"11"`

---

### **9. Related Problems (Pattern Building)**

1. Subsets
   → generate all combinations

2. Gray Code
   → binary sequence generation

3. Maximum XOR of Two Numbers in an Array
   → bit manipulation thinking

4. Single Number
   → bit tricks

---

## 🔥 Interview Shortcut

### Two approaches:

#### 1. Backtracking

```
Generate all binary strings → check missing
```

#### 2. Optimal (Expected)

```
Diagonal flip trick (Cantor)
```

---

## ⚡ Key Insight

```
We don’t need to search entire space

Just construct a string that differs from each given string
at least at one position
```

---

If you want:
I can show how this **connects to subsets / recursion tree thinking** so you never forget it in interview 🚀
