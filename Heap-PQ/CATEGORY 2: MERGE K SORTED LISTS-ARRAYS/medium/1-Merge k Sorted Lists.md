    ## 🧠 **Merge k Sorted Lists (Using Heap)**

---

### 1. **Problem Statement with Example**

You are given an array of `k` sorted linked lists.

👉 Merge all lists into **one sorted linked list** and return its head.

---

#### Example:

```python
Input:
lists = [
  1 → 4 → 5,
  1 → 3 → 4,
  2 → 6
]

Output:
1 → 1 → 2 → 3 → 4 → 4 → 5 → 6
```

#### Constraints:

* `k <= 10^4`
* Total nodes ≤ `10^4`
* Each list is sorted

---

### 2. **Diagram**

```text
Initial heads:
[1(l1), 1(l2), 2(l3)]

Heap:
[1,1,2]

Step:
Pop → 1 → push 4
Heap → [1,2,4]

Pop → 1 → push 3
Heap → [2,3,4]

...
```

👉 Always picking **smallest among k heads**

---

### 3. **Example I/O**

#### ✅ Example 1

```python
Input: [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
```

#### ⚠️ Example 2 (Edge Case)

```python
Input: []
Output: []
```

---

### 4. **Intuition & Pattern Recognition**

👉 Signals:

* Multiple sorted lists
* Need global minimum repeatedly

💡 Key Insight:

* Each list is sorted → only head matters
* Use heap to track smallest among k candidates

🧠 Interview thought:

> “This is merging k sorted streams → classic heap problem”

---

### 5. **Simpler Version**

#### Step-by-step thinking:

1. Merge 2 sorted lists → two pointers
2. Merge k lists → repeatedly merge → slow
3. Better → use heap

---

#### Related simpler problems:

* Merge Two Sorted Lists
  → base case (k = 2)

* Merge Sorted Array
  → same idea with arrays

---

#### Transition:

```text
2 lists → pointers
k lists → heap
```

---

### 6. **Brute Force**

### Idea:

* Dump all values → sort → rebuild

```python
def mergeKLists(lists):
    arr = []
    
    for l in lists:
        while l:
            arr.append(l.val)
            l = l.next
    
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

### 🔑 Core Idea:

* Push first node of each list into heap
* Pop smallest → attach to result
* Push next node of popped list

---

### ⚠️ Trick:

Heap needs comparison → use `(val, id, node)`

---

### ✅ Code

```python
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    heap = []
    
    # Step 1: push heads
    for node in lists:
        if node:
            heapq.heappush(heap, (node.val, id(node), node))
    
    dummy = ListNode(0)
    curr = dummy
    
    # Step 2: process heap
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

* Time: `O(n log k)`
* Space: `O(k)`

---

### 8. **Step-by-Step Trace**

#### Input:

```python
lists = [[1,4,5],[1,3,4],[2,6]]
```

---

#### Heap Evolution:

| Step  | Heap    | Output  |
| ----- | ------- | ------- |
| Init  | [1,1,2] | []      |
| Pop 1 | [1,2,4] | 1       |
| Pop 1 | [2,3,4] | 1→1     |
| Pop 2 | [3,4,6] | 1→1→2   |
| Pop 3 | [4,4,6] | 1→1→2→3 |

---

### 9. **Related Problems**

1. Merge Two Sorted Lists
   → base building block

2. Kth Smallest Element in a Sorted Matrix
   → heap across sorted rows

3. Find K Pairs with Smallest Sums
   → heap + sorted combinations

4. Kth Smallest Number in Multiplication Table
   → merging sorted structures

5. Smallest Range Covering Elements from K Lists
   → advanced heap + k lists

---

## ⚡ Final Interview Takeaway

* Core pattern:

  ```
  Merge k sorted streams → Min Heap
  ```

* Why heap works:

  * Only k candidates at a time
  * Always extract smallest efficiently

* Key trick:

```python
(val, id(node), node)
```

---

If you want next level:

* 🔥 Divide & conquer solution (merge sort style)
* 🔥 When to prefer heap vs merge recursion
* 🔥 Real interview pitfalls (duplicates, empty lists, memory reuse)
