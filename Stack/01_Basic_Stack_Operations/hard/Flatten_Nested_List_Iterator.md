
# Flatten Nested List Iterator

## 1. Problem Statement with Example
Given a typical LeetCode problem **Flatten Nested List Iterator**, use a stack-based approach to process the input efficiently.

### Constraints
- Input size can be large, so brute force may timeout.
- Stack operations should usually be `O(1)`.

---

## 2. Diagram

```text
Input Flow --> Stack Push/Pop --> Answer
```

---

## 3. Example I/O

### Example 1
Input:
```text
sample_input
```

Output:
```text
sample_output
```

Explanation:
Typical stack processing example.

### Example 2 (Edge Case)
Input:
```text
edge_case
```

Output:
```text
edge_output
```

---

## 4. Intuition & Pattern Recognition

### Signals
- Need nearest greater/smaller element
- Need matching parentheses
- Need undo/backtracking behavior
- Need expression evaluation

### Interview Thought Process
> "Whenever I need reversible operations or monotonic tracking, stack is usually the right structure."

---

## 5. Simpler Version

### Simpler Problem
Start with:
- Valid Parentheses
- Next Greater Element I
- Binary Tree Preorder Traversal

These teach:
- Push/pop matching
- Monotonic stack
- Iterative DFS

### Transition to This Problem
This problem adds:
- Extra constraints
- Multiple passes
- Advanced state handling

---

## 6. Brute Force

### Idea
Try all possibilities or scan repeatedly.

### Complexity
- Time: `O(n^2)` or worse
- Space: `O(n)`

---

## 7. Optimal Solution

```python
class Solution:
    def solve(self, data):
        stack = []

        for x in data:
            # Example stack processing
            while stack and stack[-1] < x:
                stack.pop()

            stack.append(x)

        return stack
```

### Complexity
- Time: `O(n)`
- Space: `O(n)`

---

## 8. Step-by-Step Trace

| Step | Current | Stack | Action |
|------|----------|--------|--------|
| 1 | a | [] | push |
| 2 | b | [a] | pop/push |
| 3 | c | [b] | update |

---

## 9. Related Problems

1. Valid Parentheses — basic push/pop matching.
2. Daily Temperatures — monotonic decreasing stack.
3. Largest Rectangle in Histogram — advanced monotonic stack.
4. Decode String — nested stack processing.
5. Basic Calculator — operator precedence using stacks.
