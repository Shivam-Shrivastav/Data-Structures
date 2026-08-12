
# 986 Interval List Intersections

## 1. Problem Statement with Example
Interval intersections using two pointers.

Typical constraint signals:
- List size can be up to 10^5
- O(n^2) is usually too slow
- Pointer manipulation is the main focus

---

## 2. Diagram

```text
1 -> 2 -> 3 -> 4

slow ---->
fast ---------->
```

---

## 3. Example I/O

### Example 1
Input:
```text
head = [1,2,3,4]
```

Output:
```text
[4,3,2,1]
```

Explanation:
Pointers are rearranged in-place.

### Example 2 (Edge Case)
Input:
```text
head = [1]
```

Output:
```text
[1]
```

Explanation:
Single node remains unchanged.

---

## 4. Intuition & Pattern Recognition

Interview signals:
- “Linked list” + “one pass” → think fast/slow pointers
- “Reverse” → iterative pointer manipulation
- “Merge” → dummy node pattern
- “Cycle” → Floyd’s algorithm
- “Nth from end” → gap between pointers

What to say in interview:
> “Since random access is unavailable, I should solve this using pointer traversal rather than indexing.”

---

## 5. Simpler Version

### Simpler Thinking
Start with:
- Traverse a linked list
- Reverse a small part
- Use two pointers
- Build result using dummy node

### Related Easier Problems
- Reverse Linked List
- Middle of Linked List
- Merge Two Sorted Lists

### Transition to This Problem
The full problem adds:
- More pointer conditions
- Boundary handling
- Multiple traversals or partial reversal

---

## 6. Brute Force

### Idea
Convert linked list into array/vector.
Perform operation on array.
Rebuild linked list if needed.

### Complexity
- Time: O(n)
- Space: O(n)

---

## 7. Optimal Solution

```python
class Solution:
    def solve(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next      # store next node
            curr.next = prev     # reverse pointer
            prev = curr          # move prev
            curr = nxt           # move current

        return prev
```

### Complexity
- Time: O(n)
- Space: O(1)

Why optimal?
- Single traversal
- In-place pointer manipulation
- Constant extra memory

---

## 8. Step-by-Step Trace

| Step | curr | prev | Remaining |
|---|---|---|---|
| 1 | 1 | None | 2->3->4 |
| 2 | 2 | 1 | 3->4 |
| 3 | 3 | 2->1 | 4 |
| 4 | 4 | 3->2->1 | None |

Final:
```text
4 -> 3 -> 2 -> 1
```

---

## 9. Related Problems

1. Reverse Linked List — base reversal pattern.
2. Reverse Linked List II — reverse subrange.
3. Reverse Nodes in k-Group — grouped reversal.
4. Reorder List — combine middle + reverse.
5. Merge k Sorted Lists — advanced merge pattern.

