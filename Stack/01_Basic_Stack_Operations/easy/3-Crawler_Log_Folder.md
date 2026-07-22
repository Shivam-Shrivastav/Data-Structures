# **1598. Crawler Log Folder (Simulation / Stack)**

## **1. Problem Statement with Example**

You are given an array of strings `logs`, where each string represents an operation performed by a file system crawler.

Each operation can be:

* `"../"` → Move to the parent folder (if already at the main folder, stay there).
* `"./"` → Stay in the current folder.
* `"x/"` → Move into a child folder named `x`.

Return the **minimum number of operations needed to go back to the main folder** after performing all the operations.

### **Constraints**

* `1 <= logs.length <= 1000`
* `2 <= logs[i].length <= 10`
* `logs[i]` consists of lowercase English letters, digits, '.', and '/'.
* Folder names are unique enough that their names don't matter—only the operation type matters.

---

## **2. Diagram**

```
Start at Root

        Root
         |
      d1/
         |
      d2/
         |
      d3/

Logs:
["d1/","d2/","../","d21/","./"]

Step 1: d1/
Root -> d1

Step 2: d2/
Root -> d1 -> d2

Step 3: ../
Root -> d1

Step 4: d21/
Root -> d1 -> d21

Step 5: ./
Stay at d21

Need 2 operations (../, ../) to reach Root.
```

---

# **3. Example I/O**

### Example 1

**Input**

```text
logs = ["d1/","d2/","../","d21/","./"]
```

**Output**

```text
2
```

**Explanation**

Current path:

```
Root -> d1 -> d21
```

Need two `"../"` operations.

---

### Example 2 (Edge Case)

**Input**

```text
logs = ["../","../","./"]
```

**Output**

```text
0
```

**Explanation**

Already at root. Going up further has no effect.

---

# **4. Intuition & Pattern Recognition**

### Signals

* Folder navigation
* Parent/child relationship
* Undo previous move

These are classic **Stack Simulation** signals.

Think:

> Whenever I enter a folder, I push it.

> Whenever I go back (`../`), I pop.

> `./` does nothing.

Interestingly...

The folder names themselves are irrelevant.

We only need to know **how deep** we are.

That means instead of storing folder names, we can simply maintain a **depth counter**.

---

### Interview Thinking

"I don't actually care which folder I'm inside.

I only care how many levels deep I currently am."

That immediately leads to an integer solution.

---

# **5. Simpler Version**

## Simpler Problem

Given operations:

```
+
-
```

Return how many items remain after processing them.

Example:

```
++-++
```

Depth changes like

```
0
1
2
1
2
3
```

Answer = 3.

Now add one more rule:

```
cannot go below zero
```

This becomes

```
depth = max(depth-1,0)
```

Finally,

replace

```
+
```

with

```
folder/
```

replace

```
-
```

with

```
../
```

and add

```
./
```

which changes nothing.

That's exactly this problem.

---

### Related Simpler LeetCode Problems

### 1. Baseball Game (682)

Stack simulation using push/pop.

↓

Learn stack operations.

---

### 2. Backspace String Compare (844)

Undo previous character using stack.

↓

Introduces "go back" operation.

---

### 3. Crawler Log Folder (1598)

Instead of storing values,

store only the current depth.

---

# **6. Brute Force Solution (Actual Stack)**

Store every folder entered.

* Push for `"x/"`
* Pop for `"../"`
* Ignore `"./"`

Return stack size.

### Python

```python
class Solution:
    def minOperations(self, logs):
        stack = []

        for log in logs:

            if log == "../":
                if stack:
                    stack.pop()

            elif log == "./":
                continue

            else:
                stack.append(log)

        return len(stack)
```

### Complexity

* Time: **O(n)**
* Space: **O(n)**

---

# **7. Optimal Solution (Depth Counter)**

Instead of storing folder names,

just store the current depth.

Algorithm:

```
depth = 0

for every log

    "../"
        if depth > 0
            depth -= 1

    "./"
        ignore

    folder/
        depth += 1

return depth
```

### Python

```python
class Solution:
    def minOperations(self, logs):
        depth = 0

        for log in logs:

            # Move to parent folder (if possible)
            if log == "../":
                if depth > 0:
                    depth -= 1

            # Stay in current folder
            elif log == "./":
                continue

            # Move into a child folder
            else:
                depth += 1

        return depth
```

### Complexity

* **Time:** O(n)
* **Space:** O(1)

---

# **8. Step-by-Step Trace**

Input

```text
["d1/","d2/","../","d21/","./"]
```

| Step | Log  | Depth Before | Action       | Depth After |
| ---- | ---- | ------------ | ------------ | ----------- |
| 1    | d1/  | 0            | Enter folder | 1           |
| 2    | d2/  | 1            | Enter folder | 2           |
| 3    | ../  | 2            | Go parent    | 1           |
| 4    | d21/ | 1            | Enter folder | 2           |
| 5    | ./   | 2            | Stay         | 2           |

Final answer:

```
depth = 2
```

Need

```
../
../
```

to return to root.

---

# **9. Related Problems**

1. **LeetCode 682 — Baseball Game**
   Uses a stack to process operations that modify previous state.

2. **LeetCode 844 — Backspace String Compare**
   Simulates undo operations with stack behavior.

3. **LeetCode 71 — Simplify Path**
   A more advanced filesystem navigation problem where you maintain the canonical path using a stack.

4. **LeetCode 20 — Valid Parentheses**
   Classic stack problem for matching nested structures.

5. **LeetCode 150 — Evaluate Reverse Polish Notation**
   Another stack simulation problem where operations are processed sequentially.
