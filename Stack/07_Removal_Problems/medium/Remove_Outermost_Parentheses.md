# 1021. Remove Outermost Parentheses (Easy)

## 1. Problem Statement

You are given a valid parentheses string `s`.

A **primitive** valid parentheses string is one that **cannot be split into two non-empty valid parentheses strings**.

Your task is to remove the **outermost pair of parentheses from every primitive substring** and concatenate the results.

### Example

```
Input: s = "(()())(())"
Output: "()()()"

Explanation:
Primitive 1: (()())  -> remove outermost -> ()()
Primitive 2: (())    -> remove outermost -> ()
Final Answer: ()()()
```

### Constraints

* `1 <= s.length <= 10^5`
* `s` contains only `'('` and `')'`
* `s` is guaranteed to be a valid parentheses string.

---

# 2. Diagram

```
s = (()())(())

Primitive 1        Primitive 2
   ┌──────┐          ┌───┐
   (()())            (())

Remove outer layer

    ()()              ()

Final

()()()
```

Another way to visualize depth:

```
Char : ( ( ) ( ) ) ( ( ) )
Depth: 1 2 1 2 1 0 1 2 1 0

Only keep characters whose depth is NOT
moving between 0 and 1.
```

---

# 3. Example I/O

### Example 1

```
Input:
s = "(()())(())"

Output:
"()()()"
```

Explanation

```
(()()) → ()()
(())   → ()

Answer = ()()()
```

---

### Example 2 (Edge Case)

```
Input:
s = "()()"

Output:
""
```

Explanation

Each primitive is simply:

```
()
```

Removing the outermost parentheses leaves an empty string.

---

# 4. Intuition & Pattern Recognition

### Key Observation

The **outermost** parentheses are exactly those where:

* `'('` increases depth from **0 → 1**
* `')'` decreases depth from **1 → 0**

These are the parentheses we should skip.

Everything else belongs to the inside of a primitive.

### Interview Thought Process

> "The problem isn't asking me to identify primitives explicitly. It only wants me to remove the first '(' and last ')' of every primitive. A stack isn't actually necessary—I only need the current nesting depth."

This is a **Parentheses Depth / Counter** problem.

---

# 5. Simpler Version

## Simpler Thinking

Imagine there is only **one primitive**.

```
((()))
```

Remove the first and last parentheses.

```
(())
```

Now imagine there are multiple primitives.

```
(()())(())
```

Just repeat the same operation for each primitive.

Instead of splitting primitives manually, notice that depth becoming `0` naturally marks the end of one primitive.

---

## Related Simpler Questions

### 1. 20. Valid Parentheses

Learn how parentheses are matched.

Difference:

* Here validity is already guaranteed.
* We only track nesting depth.

---

### 2. Maximum Nesting Depth of Parentheses

Learn how depth changes.

Difference:

* There we compute maximum depth.
* Here we use depth to decide whether to keep characters.

---

### Thinking Evolution

```
Valid Parentheses
      ↓
Understand nesting

Maximum Nesting Depth
      ↓
Track current depth

Remove Outermost Parentheses
      ↓
Skip characters at depth transitions
```

---

# 6. Brute Force

### Idea

1. Find each primitive.
2. Store it.
3. Remove first and last character.
4. Append to answer.

Finding primitives requires tracking depth.

### Python

```python
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        start = 0
        depth = 0

        for i, ch in enumerate(s):
            if ch == '(':
                depth += 1
            else:
                depth -= 1

            if depth == 0:
                primitive = s[start:i+1]
                ans.append(primitive[1:-1])
                start = i + 1

        return "".join(ans)
```

### Complexity

* Time: **O(n)**
* Space: **O(n)**

---

# 7. Optimal Solution

## Idea

Maintain the current depth.

### Rules

For `'('`:

* If depth > 0 → keep it.
* Increase depth.

For `')'`:

* Decrease depth.
* If depth > 0 → keep it.

This automatically skips the outermost parentheses.

### Python

```python
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        depth = 0

        for ch in s:
            if ch == '(':
                # Keep only if it's not the outermost '('
                if depth > 0:
                    ans.append(ch)
                depth += 1
            else:
                depth -= 1
                # Keep only if it's not the outermost ')'
                if depth > 0:
                    ans.append(ch)

        return "".join(ans)
```

### Complexity

* **Time:** O(n)
* **Space:** O(n) (output buffer)

---

# 8. Step-by-Step Trace

Example

```
s = (()())(())
```

| Char | Depth Before | Action | Depth After | Answer   |
| ---- | ------------ | ------ | ----------- | -------- |
| (    | 0            | Skip   | 1           | ""       |
| (    | 1            | Keep   | 2           | "("      |
| )    | 2            | Keep   | 1           | "()"     |
| (    | 1            | Keep   | 2           | "()("    |
| )    | 2            | Keep   | 1           | "()()"   |
| )    | 1            | Skip   | 0           | "()()"   |
| (    | 0            | Skip   | 1           | "()()"   |
| (    | 1            | Keep   | 2           | "()()("  |
| )    | 2            | Keep   | 1           | "()()()" |
| )    | 1            | Skip   | 0           | "()()()" |

Final Answer

```
()()()
```

---

# 9. Related Problems (Increasing Difficulty)

1. **20. Valid Parentheses** *(Easy)*
   Learn how matching parentheses work using a stack.

2. **1614. Maximum Nesting Depth of the Parentheses** *(Easy)*
   Uses the same depth-counting idea as this problem.

3. **1249. Minimum Remove to Make Valid Parentheses** *(Medium)*
   Remove invalid parentheses while preserving a valid string.

4. **1190. Reverse Substrings Between Each Pair of Parentheses** *(Medium)*
   Traverse nested parentheses and process inner content.

5. **32. Longest Valid Parentheses** *(Hard)*
   Uses stack/DP to find the longest valid parentheses substring.

---

# Interview Cheat Sheet

* ✅ Valid parentheses are guaranteed.
* ✅ No stack needed.
* ✅ Maintain **current depth**.
* ✅ Skip `'('` when depth is `0`.
* ✅ Skip `')'` when depth becomes `0` after decrement.
* ✅ Everything else belongs to the inside of a primitive.
* **Pattern:** Parentheses + Nesting Depth Counter.
