# 22. Generate Parentheses (Backtracking)

---

# 1. Problem Statement

Given `n` pairs of parentheses, generate **all combinations** of well-formed (balanced) parentheses.

Return the answer in **any order**.

### Constraints

* `1 <= n <= 8`
* The number of valid combinations is the **nth Catalan Number**.

---

## Example

```text
Input:
n = 3

Output:
[
 "((()))",
 "(()())",
 "(())()",
 "()(())",
 "()()()"
]
```

---

# 2. Diagram

For `n = 3`

```
Start
 ""

                ""
              /     \
            "("      ")" ❌
             |
            "("
          /      \
      "(( "      "()"
      /   \       /   \
   "(((" "(()" "()(" "())" ❌
```

Continue only if the string can still become valid.

One complete path:

```
""

↓

"("

↓

"(("

↓

"((("

↓

"((()"

↓

"((())"

↓

"((()))" ✅
```

Notice that invalid branches (starting with `')'` or having more `')'` than `'('`) are **pruned immediately**.

---

# 3. Example I/O

### Example 1

```
Input
n = 1

Output
["()"]
```

---

### Example 2

```
Input
n = 2

Output

[
"(())",
"()()"
]
```

---

### Example 3 (Edge Case)

```
Input
n = 3

Output

[
"((()))",
"(()())",
"(())()",
"()(())",
"()()()"
]
```

---

# 4. Intuition & Pattern Recognition

### Interview Hint

Whenever you hear:

> **"Generate all valid..."**

or

> **"Return every possible combination..."**

Think:

> **Backtracking (DFS)**

because we must explore all possible choices while discarding invalid ones early.

---

### Key Observation

At every position we have only two choices:

```
(
or
)
```

But not every choice is valid.

We maintain:

* `open` = number of `'('` used.
* `close` = number of `')'` used.

Rules:

* Can add `'('` if `open < n`.
* Can add `')'` only if `close < open`.

This ensures we never create an invalid prefix.

---

### Recognition Pattern

Problems asking to:

* Generate all combinations
* Generate all valid strings
* Explore all possibilities with constraints

usually use **Backtracking**.

---

# 5. Simpler Version

### Simpler Problem

Generate all binary strings of length 4.

```
0000
0001
0010
...
1111
```

Decision tree:

```
"" 
 / \
0   1
```

Every position has two choices.

---

Now add a constraint:

Generate only **balanced parentheses**.

Instead of exploring every branch, prune invalid ones.

```
(
)

Cannot start with ')'
```

Backtracking naturally fits.

---

### Simpler Questions Leading Here

1. Subsets (78)
2. Letter Combinations of a Phone Number (17)
3. Permutations (46)
4. Combination Sum (39)
5. Generate Parentheses (22)

---

# 6. Brute Force

Generate **all** strings of length `2n`.

Example (`n=3`)

```
((((((
((((()
...
))))))
```

There are

```
2^(2n)
```

strings.

Check each string for validity.

Checking one string:

```
O(n)
```

Total:

### Complexity

Time

```
O(2^(2n) * n)
```

Space

```
O(n)
```

---

# 7. Optimal Solution (Backtracking)

### Idea

Keep track of:

* `open`
* `close`
* current string

Rules:

### Add '('

Only if

```
open < n
```

---

### Add ')'

Only if

```
close < open
```

---

### Base Case

When

```
len(curr) == 2 * n
```

store the answer.

---

### Python

```python
class Solution:
    def generateParenthesis(self, n: int):
        result = []

        def backtrack(curr, open_count, close_count):

            # Found a valid combination
            if len(curr) == 2 * n:
                result.append(curr)
                return

            # Add '(' if we still have some left
            if open_count < n:
                backtrack(curr + "(", open_count + 1, close_count)

            # Add ')' only if it won't make the string invalid
            if close_count < open_count:
                backtrack(curr + ")", open_count, close_count + 1)

        backtrack("", 0, 0)

        return result
```

---

### Complexity

The number of valid strings is the **nth Catalan Number**:

```
Cn ≈ 4^n / (n^(3/2))
```

Time

```
O(Cn)
```

(or more precisely `O(Cn × n)` because building each string takes `O(n)`)

Space

```
O(n)
```

(recursion depth, excluding output)

---

# 8. Step-by-Step Trace

Example

```
n = 2
```

| Current | Open | Close | Action              |
| ------- | ---- | ----- | ------------------- |
| ""      | 0    | 0     | Start               |
| "("     | 1    | 0     | Add '('             |
| "(("    | 2    | 0     | Add '('             |
| "(()"   | 2    | 1     | Add ')'             |
| "(())"  | 2    | 2     | ✅ Store             |
| "()"    | 1    | 1     | Backtrack & Add ')' |
| "()("   | 2    | 1     | Add '('             |
| "()()"  | 2    | 2     | ✅ Store             |

Answer

```
[
"(())",
"()()"
]
```

---

## Decision Tree

```
                   ""
                 /
               "("
            /       \
         "(("       "()"
          |          |
       "(()"      "()("
          |          |
      "(())"      "()()"
```

Only valid branches are explored.

---

# 9. Related Problems

| Problem                                       | Connection                                               |
| --------------------------------------------- | -------------------------------------------------------- |
| **78. Subsets**                               | Basic backtracking with include/exclude choices.         |
| **17. Letter Combinations of a Phone Number** | Generate all combinations using DFS.                     |
| **46. Permutations**                          | Backtracking over all arrangements.                      |
| **39. Combination Sum**                       | Backtracking with constraints and pruning.               |
| **93. Restore IP Addresses**                  | Generate all valid strings while pruning invalid states. |

---

# Interview Takeaway

Whenever you see:

> **"Generate all valid combinations"**

Think:

* **Backtracking**
* Build the answer incrementally.
* Prune invalid choices as early as possible.

### Core Rules

```text
If open < n:
    add '('

If close < open:
    add ')'

If length == 2 * n:
    store answer
```

The crucial interview insight is that **we never generate invalid prefixes**. By enforcing `close <= open` during recursion, we avoid exploring impossible branches, making the solution efficient and elegant. This pruning is what transforms an exponential brute-force search into the standard backtracking solution for this problem.
