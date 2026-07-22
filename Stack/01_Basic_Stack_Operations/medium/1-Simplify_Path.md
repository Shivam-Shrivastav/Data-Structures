# **71. Simplify Path (Stack)**

## **1. Problem Statement with Example**

You are given an **absolute Unix-style file path** as a string `path`.

Your task is to return the **canonical (simplified) path** by applying Unix path rules.

### Unix Rules

* `/` separates directories.
* `.` means **current directory** → ignore it.
* `..` means **parent directory** → go back one folder (if possible).
* Multiple consecutive slashes (`//`) are treated as a single slash.
* The canonical path:

  * Starts with exactly one `/`
  * Has only one slash between directory names
  * Does **not** end with `/` (unless it is the root `/`)

---

### Constraints

* `1 <= path.length <= 3000`
* Path consists of English letters, digits, `.`, `_`, `-`, and `/`.
* Path is always an **absolute path** (starts with `/`).

---

# **2. Diagram**

Example:

```text
path = "/home//foo/../bar/./"
```

Split by `/`

```text
["", "home", "", "foo", "..", "bar", ".", ""]
```

Process using stack:

```text
Start
Stack = []

home
↓

[home]

foo
↓

[home, foo]

..
↓

[home]

bar
↓

[home, bar]

.
↓

ignore
```

Final

```text
/home/bar
```

---

# **3. Example I/O**

### Example 1

**Input**

```text
path = "/home/"
```

**Output**

```text
"/home"
```

Explanation

Trailing slash is removed.

---

### Example 2

**Input**

```text
path = "/../"
```

**Output**

```text
"/"
```

Explanation

Already at root.

Cannot go above it.

---

### Example 3

**Input**

```text
path = "/home//foo/"
```

**Output**

```text
"/home/foo"
```

Multiple slashes become one.

---

### Example 4 (Edge Case)

**Input**

```text
path = "/a/../../b/../c//.//"
```

**Output**

```text
"/c"
```

---

# **4. Intuition & Pattern Recognition**

### Signals

The problem contains

* go inside folder
* go outside folder
* undo previous move

Whenever you see

* Undo
* Previous state
* Nested structure

Think:

> **Stack**

---

### Interview Thinking

Every directory entered should be remembered.

Whenever we see

```text
..
```

we remove the most recent directory.

That is exactly

```text
push
pop
```

---

### Why splitting works?

Example

```text
/a//b/./../c
```

Split by `/`

```text
["", "a", "", "b", ".", "..", "c"]
```

Now process each token independently.

---

# **5. Simpler Version**

## Simpler Problem

Given

```text
["a", "b", "..", "c"]
```

Construct the final folder list.

Solution

```text
Stack

[]

a
↓

[a]

b
↓

[a,b]

..
↓

[a]

c
↓

[a,c]
```

Return

```text
[a,c]
```

Now extend it.

Additional cases

```text
"."
```

Ignore.

```text
""
```

Ignore.

Finally

Join stack with

```text
/
```

---

## Simpler LeetCode Problems

### 1. 1598. Crawler Log Folder

Only keep track of depth.

↓

No need to remember folder names.

---

### 2. 844. Backspace String Compare

Undo previous item.

↓

Introduces stack pop.

---

### 3. 71. Simplify Path

Need actual folder names,

therefore store strings instead of just depth.

---

### Thinking Progression

```
Depth only
        ↓
Need folder names
        ↓
Store folders in stack
        ↓
Join stack to form path
```

---

# **6. Brute Force Solution**

Maintain the current path as a list and repeatedly modify it for each component.

Although conceptually simple, it still uses a stack-like list internally and performs the required operations directly.

### Python

```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        folders = []

        for part in path.split("/"):

            if part == "" or part == ".":
                continue

            elif part == "..":
                if folders:
                    folders.pop()

            else:
                folders.append(part)

        return "/" + "/".join(folders)
```

### Complexity

* **Time:** O(n)
* **Space:** O(n)

> This is also the optimal approach because every path component must be examined once.

---

# **7. Optimal Solution (Stack)**

### Algorithm

```
Split path by '/'

For every part

    ""  -> ignore

    "." -> ignore

    ".."
            if stack not empty
                pop

    folder
            push

Return "/" + join(stack)
```

---

### Python

```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        # Split path into directory names
        for folder in path.split("/"):

            # Ignore empty strings and current directory
            if folder == "" or folder == ".":
                continue

            # Move to parent directory
            elif folder == "..":
                if stack:
                    stack.pop()

            # Valid folder name
            else:
                stack.append(folder)

        # Build the canonical path
        return "/" + "/".join(stack)
```

---

### Complexity

* **Time:** O(n)
* **Space:** O(n)

---

# **8. Step-by-Step Trace**

Input

```text
path = "/a/../../b/../c//.//"
```

Split

```text
["", "a", "..", "..", "b", "..", "c", "", ".", "", ""]
```

| Step | Token | Stack Before | Action       | Stack After |
| ---- | ----- | ------------ | ------------ | ----------- |
| 1    | ""    | []           | Ignore       | []          |
| 2    | a     | []           | Push         | [a]         |
| 3    | ..    | [a]          | Pop          | []          |
| 4    | ..    | []           | Already root | []          |
| 5    | b     | []           | Push         | [b]         |
| 6    | ..    | [b]          | Pop          | []          |
| 7    | c     | []           | Push         | [c]         |
| 8    | ""    | [c]          | Ignore       | [c]         |
| 9    | .     | [c]          | Ignore       | [c]         |
| 10   | ""    | [c]          | Ignore       | [c]         |

Final stack

```text
[c]
```

Answer

```text
"/c"
```

---

# **9. Related Problems (Increasing Difficulty)**

1. **LeetCode 1598 – Crawler Log Folder**
   Simulates folder navigation but only tracks the current depth, not the actual path.

2. **LeetCode 844 – Backspace String Compare**
   Uses a stack to simulate undo (`pop`) operations on characters.

3. **LeetCode 71 – Simplify Path**
   Extends the same stack idea by storing directory names and rebuilding the canonical path.

4. **LeetCode 394 – Decode String**
   Uses stacks to process nested encoded strings with push/pop behavior.

5. **LeetCode 224 – Basic Calculator**
   Uses stacks to evaluate nested expressions with parentheses, another classic application of maintaining and restoring previous state.
