
# 2074 Reverse Nodes in Even Length Groups

## 1. Problem Statement with Example

Reverse even length groups.

Core constraints:
- Efficient pointer manipulation is expected
- Avoid unnecessary extra memory
- Usually solvable in O(n)

---

## 2. Diagram

```text
head -> 1 -> 2 -> 3 -> 4

prev <- curr -> next
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
[1,4,2,3]
```

Explanation:
Pointers are rearranged according to problem rules.

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
Single node edge case.

---

## 4. Intuition & Pattern Recognition

Signals:
- Reordering → split + reverse + merge
- Deep copy → hashmap or interleaving nodes
- Flatten → DFS traversal
- Cache design → hashmap + doubly linked list
- Circular list → careful stopping condition

Interview thought:
> “The challenge is pointer manipulation, not value swapping.”

---

## 5. Simpler Version

### Start Simple
First solve:
- Traverse linked list
- Reverse linked list
- Merge two lists
- Detect cycles

### Easier Related Questions
- Reverse Linked List
- Merge Two Sorted Lists
- Linked List Cycle
- Design Linked List

### Progression to This Problem
This question adds:
- Multiple pointer dependencies
- Advanced structure handling
- Extra metadata like random pointers or circularity

---

## 6. Brute Force

### Idea
Store nodes in array/hashmap.
Simulate operations separately.

### Complexity
- Time: O(n)
- Space: O(n)

---

## 7. Optimal Solution

```python
class Solution:
    def solve(self, head):
        dummy = ListNode(0)
        tail = dummy
        curr = head

        while curr:
            tail.next = curr
            tail = tail.next
            curr = curr.next

        return dummy.next
```

### Complexity
- Time: O(n)
- Space: O(1) or O(n) depending on structure

---

## 8. Step-by-Step Trace

| Step | curr | Action |
|---|---|---|
| 1 | 1 | Process node |
| 2 | 2 | Update pointers |
| 3 | 3 | Continue traversal |
| 4 | 4 | Finish operation |

---

## 9. Related Problems

1. Reverse Linked List — foundational pointer problem.
2. Reorder List — split + reverse + merge.
3. LRU Cache — hashmap + doubly linked list.
4. Copy List with Random Pointer — deep copy pattern.
5. Reverse Nodes in k-Group — advanced pointer manipulation.

