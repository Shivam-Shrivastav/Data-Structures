Here’s the `.md` formatted solution for **LeetCode: Backspace String Compare**, using:

1. ✅ **Brute Force** (simulate stacks)
2. ✅ **Optimized Two Pointer Approach** (O(n) time and O(1) space)

---

````markdown
# LeetCode Problem: Backspace String Compare

## Problem Statement

Given two strings `s` and `t`, return `true` if they are equal when typed into text editors.
- `'#'` means a backspace character.
- After backspacing an empty text, it remains empty.

---

### Example 1:
Input: `s = "ab#c"`, `t = "ad#c"`  
Output: `true`  
Explanation: Both become `"ac"`

### Example 2:
Input: `s = "ab##"`, `t = "c#d#"`  
Output: `true`  
Explanation: Both become `""`

### Example 3:
Input: `s = "a#c"`, `t = "b"`  
Output: `false`

---

## ✅ Brute Force Solution (Stack Simulation)

### Code:
```python
class Solution:
    def backspaceCompare(self, s, t):
        def build(string):
            stack = []
            for char in string:
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()
            return stack

        return build(s) == build(t)
````

### Explanation:

* Simulate text editor behavior using stacks.
* Push characters, and pop on `'#'`.
* Compare final stack contents.

### Time Complexity:

* **O(n + m)**

### Space Complexity:

* **O(n + m)**

---

### 🔍 Brute Force Significance:

1. Simple and readable.
2. Not optimal in space, but useful for correctness and intuition.

---

## ✅ Optimized Two Pointer Solution (O(n) Time, O(1) Space)

### Code:

```python
class Solution:
    def backspaceCompare(self, s, t):
        def get_next_valid_char_index(string, index):
            skip = 0
            while index >= 0:
                if string[index] == '#':
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    return index
                index -= 1
            return -1

        i, j = len(s) - 1, len(t) - 1

        while i >= 0 or j >= 0:
            i = get_next_valid_char_index(s, i)
            j = get_next_valid_char_index(t, j)

            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False

            i -= 1
            j -= 1

        return True
```

### Explanation:

* Traverse from the end of both strings.
* Use a `skip` counter to track backspaces.
* Find the next valid character (ignoring backspaces).
* Compare characters one by one from the back.

### Time Complexity:

* **O(n + m)**

### Space Complexity:

* **O(1)** — no extra data structures.

---

### 🔍 Two Pointer Pattern Significance:

1. Enables in-place-like behavior with constant space.
2. Ideal for problems where **backwards traversal** simulates correct state (e.g., backspaces).
3. Efficient and clean for **string back-editing**.

---

## ✅ Final Note:

* Use the brute force approach for simplicity and debugging.
* Use two-pointer approach in interviews or high-performance applications.

