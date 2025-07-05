Here’s the `.md` formatted solution for **LeetCode: Linked List Cycle**, using:

1. ✅ **Brute Force** (with visited set)
2. ✅ **Optimized Two Pointer (Floyd’s Cycle Detection)**

---

````markdown
# LeetCode Problem: Linked List Cycle

## Problem Statement

Given the `head` of a singly linked list, determine if the linked list contains a **cycle**.

A cycle exists if you can follow `next` pointers and reach the same node again.

---

### Example 1:
Input: `head = [3,2,0,-4], pos = 1`  
Output: `true`  
Explanation: Node at index 3 connects back to node at index 1 (cycle exists)

### Example 2:
Input: `head = [1,2], pos = 0`  
Output: `true`

### Example 3:
Input: `head = [1], pos = -1`  
Output: `false`

---

## ✅ Brute Force Solution (Using Hash Set)

### Code:
```python
class Solution:
    def hasCycle(self, head):
        visited = set()

        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next

        return False
````

### Explanation:

* Traverse the list and store visited nodes in a set.
* If a node is revisited, cycle exists.

### Time Complexity:

* **O(n)**

### Space Complexity:

* **O(n)** — due to hash set

---

### 🔍 Brute Force Significance:

1. Simple to implement and intuitive.
2. Not optimal due to extra space usage.

---

## ✅ Optimized Solution: Floyd’s Cycle Detection (Two Pointer)

### Code:

```python
class Solution:
    def hasCycle(self, head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
```

### Explanation:

* Two pointers:

  * `slow` moves one step
  * `fast` moves two steps
* If there's a cycle, they'll eventually meet.
* If no cycle, `fast` reaches `None`.

### Time Complexity:

* **O(n)**

### Space Complexity:

* **O(1)** — no extra space

---

### 🔍 Two Pointer Pattern Significance:

1. Efficiently detects cycles with constant space.
2. Based on the mathematical property that faster pointer will lap the slower one inside a loop.
3. Widely used for detecting cycles in linked structures.

---

## ✅ Final Notes

* Use **Floyd’s Algorithm** for optimal space/time trade-off.
* Hash set method is useful when node comparison or custom tracking is needed.

