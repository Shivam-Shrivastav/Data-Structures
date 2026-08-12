## 🧠 **Merge Two Sorted Lists (Using Heap)**

---

### 1. **Problem Statement with Example**

You are given two sorted linked lists `l1` and `l2`.

👉 Merge them into a **single sorted linked list** and return its head.

---

#### Example:

```python
Input:
l1 = 1 → 2 → 4
l2 = 1 → 3 → 4

Output:
1 → 1 → 2 → 3 → 4 → 4
```

#### Constraints:

* Number of nodes: `[0, 50]`
* Values: `-100 <= Node.val <= 100`

---

### 2. **Diagram**

```text
l1: 1 → 2 → 4
l2: 1 → 3 → 4

Heap (min):
[1(l1), 1(l2)]

Step-by-step:
Pop → 1 → push next (2)
Heap → [1(l2), 2]

Pop → 1 → push next (3)
Heap → [2,3]

...
```

---

### 3. **Example I/O**

#### ✅ Example 1 (Typical)

```python
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

#### ⚠️ Example 2 (Edge Case)

```python
Input: l1 = [], l2 = []
Output: []
```

---

### 4. **Intuition & Pattern Recognition**

👉 Signals:

* Multiple sorted sources
* Need smallest element each time

💡 Insight:

* Heap always gives **minimum element quickly**

🧠 Interview thought:

> “This is like merging k sorted lists → heap works naturally”

Even though for 2 lists, **two pointers is better**, heap generalizes.

---

### 5. **Simpler Version**

#### Simpler Problem:

* Merge 2 sorted arrays → two pointers

#### Related:

* Merge Sorted Array

#### Thinking flow:

```
Arrays → Linked Lists → Multiple lists → Heap
```

#### Difference:

* Arrays: random access
* Linked list: pointer-based → heap helps unify approach

---

### 6. **Brute Force**

### Idea:

* Copy all nodes → sort → rebuild

```python
def mergeTwoLists(l1, l2):
    arr = []
    
    while l1:
        arr.append(l1.val)
        l1 = l1.next
    
    while l2:
        arr.append(l2.val)
        l2 = l2.next
    
    arr.sort()
    
    dummy = ListNode(0)
    curr = dummy
    
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    
    return dummy.next
```

#### Complexity:

* Time: `O(n log n)`
* Space: `O(n)`

---

### 7. **Optimal Solution (Heap)** ⭐

---

### 🔑 Idea:

* Push heads of both lists into heap
* Always pop smallest
* Push next node of popped element

---

### ⚠️ Trick:

Heap needs comparable elements → store `(val, id, node)`

---

### ✅ Code

```python
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    heap = []
    
    # push initial nodes
    if l1:
        heapq.heappush(heap, (l1.val, id(l1), l1))
    if l2:
        heapq.heappush(heap, (l2.val, id(l2), l2))
    
    dummy = ListNode(0)
    curr = dummy
    
    while heap:
        val, _, node = heapq.heappop(heap)
        
        curr.next = node
        curr = curr.next
        
        if node.next:
            heapq.heappush(heap, (node.next.val, id(node.next), node.next))
    
    return dummy.next
```

---

### Complexity:

* Time: `O(n log k)` → here `k = 2` → `O(n)`
* Space: `O(k)` → `O(2)`

---

### ⚠️ Interview Note

👉 This is **NOT the best solution** for 2 lists

Best:

* Two pointers → `O(n)` without heap

But heap is useful when:

* k lists → generalizes

---

### 8. **Step-by-Step Trace**

#### Input:

```
l1 = 1 → 2 → 4
l2 = 1 → 3 → 4
```

---

#### Heap evolution:

| Step  | Heap          | Output  |
| ----- | ------------- | ------- |
| Init  | [1(l1),1(l2)] | []      |
| Pop 1 | [1(l2),2]     | 1       |
| Pop 1 | [2,3]         | 1→1     |
| Pop 2 | [3,4]         | 1→1→2   |
| Pop 3 | [4,4]         | 1→1→2→3 |

---

### 9. **Related Problems**

1. Merge k Sorted Lists
   → Exact extension → heap essential

2. Kth Smallest Element in a Sorted Matrix
   → Heap across sorted rows

3. Find K Pairs with Smallest Sums
   → Heap for merging pairs

4. Sort List
   → Merge sort on linked list

---

## ⚡ Final Interview Takeaway

* Heap is **overkill for 2 lists**, but:

  ```
  2 lists → pointers
  k lists → heap
  ```
* Pattern:

  ```
  Merge k sorted streams → min heap
  ```
* Trick:

```python
(val, id(node), node)
```

---

If you want, I can also show:

* 🔥 clean **two-pointer solution (must know)**
* 🔥 how this becomes **Merge K Sorted Lists instantly**
* 🔥 common heap pitfalls interviewers test
