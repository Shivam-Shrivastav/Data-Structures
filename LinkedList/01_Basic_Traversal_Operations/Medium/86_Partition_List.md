# 86. Partition List

## 1. Problem Statement with Example

Given the head of a singly linked list and an integer `x`, rearrange the list such that:

* All nodes with values `< x` appear before nodes with values `>= x`
* The **relative order** inside both groups must remain the same

Return the new head of the partitioned list.

### Example

Input:

```text
head = [1,4,3,2,5,2], x = 3
```

Output:

```text
[1,2,2,4,3,5]
```

Why?

* Nodes `< 3` → `1,2,2`
* Nodes `>= 3` → `4,3,5`
* Preserve original order inside both groups

### Constraints

* Number of nodes: `[0, 200]`
* `-100 <= Node.val <= 100`
* `-200 <= x <= 200`

The important constraint:

> Relative order must remain same → stable partitioning

---

# 2. Diagram

```text
Original List:
1 -> 4 -> 3 -> 2 -> 5 -> 2
             x = 3

Create 2 lists:

Less List (<3):
1 -> 2 -> 2

Greater/Equal List (>=3):
4 -> 3 -> 5

Join:
1 -> 2 -> 2 -> 4 -> 3 -> 5
```

---

# 3. Example I/O

## Example 1

Input:

```text
head = [1,4,3,2,5,2]
x = 3
```

Output:

```text
[1,2,2,4,3,5]
```

Explanation:

* Smaller nodes: `1,2,2`
* Larger/equal nodes: `4,3,5`

Maintain original ordering.

---

## Example 2 (Edge Case)

Input:

```text
head = [2,1]
x = 2
```

Output:

```text
[1,2]
```

Explanation:

* `<2` → `1`
* `>=2` → `2`

---

## Example 3

Input:

```text
head = [1,1,1]
x = 5
```

Output:

```text
[1,1,1]
```

Everything already belongs to the left partition.

---

# 4. Intuition & Pattern Recognition

This is a:

* **Linked List Construction**
* **Dummy Node**
* **Stable Partitioning** problem

## Key Interview Signal

Whenever you hear:

> “Preserve original order”

it usually means:

* Don’t sort
* Don’t swap randomly
* Build separate streams/lists

---

## Core Idea

Instead of rearranging nodes in-place aggressively:

Create:

* one linked list for nodes `< x`
* another for nodes `>= x`

Then connect them.

This preserves ordering naturally.

---

## Interview Thought Process

> “I need stable partitioning.
> Linked list insertion at tail preserves order.
> So I’ll build two lists and merge them.”

---

# 5. Simpler Version

## Simplest Version

### Array Version

Given array:

```text
[1,4,3,2]
x = 3
```

Create:

```text
less = [1,2]
greater = [4,3]

result = less + greater
```

Easy because arrays allow direct insertion.

---

## Move to Linked List

Now instead of arrays:

* maintain tail pointers
* append nodes directly

Same logic.

---

# Related Simpler Problems

## 1. Merge Two Sorted Lists

You learn:

* Building a new linked list using tail pointer

Connection:

* Same dummy node + tail manipulation

---

## 2. Remove Linked List Elements

You learn:

* Traversing and reconnecting nodes

Connection:

* Node filtering

---

## 3. Odd Even Linked List

You learn:

* Split into two lists and combine

Very close to this problem.

---

## Thinking Progression

```text
Filter nodes into arrays
    ↓
Filter nodes into linked lists
    ↓
Maintain order while appending
    ↓
Connect both lists
```

---

# 6. Brute Force

## Idea

* Store all node values in arrays
* Create:

  * `less`
  * `greater`
* Rebuild linked list

---

## Complexity

* Time: `O(N)`
* Space: `O(N)`

---

## Brute Force Code

```python
class Solution:
    def partition(self, head, x):
        less = []
        greater = []

        curr = head

        while curr:
            if curr.val < x:
                less.append(curr.val)
            else:
                greater.append(curr.val)

            curr = curr.next

        dummy = ListNode(0)
        tail = dummy

        for val in less + greater:
            tail.next = ListNode(val)
            tail = tail.next

        return dummy.next
```

---

# 7. Optimal Solution

## Idea

Create 2 dummy lists:

* `lessDummy`
* `greaterDummy`

Traverse original list:

* append node to appropriate list
* move tail forward

Finally:

* connect less list to greater list
* terminate greater list with `None`

---

## Optimal Code

```python
class Solution:
    def partition(self, head, x):
        
        # Dummy heads for both partitions
        lessDummy = ListNode(0)
        greaterDummy = ListNode(0)

        # Tail pointers
        less = lessDummy
        greater = greaterDummy

        curr = head

        while curr:

            if curr.val < x:
                less.next = curr
                less = less.next
            else:
                greater.next = curr
                greater = greater.next

            curr = curr.next

        # Important:
        # end greater list properly
        greater.next = None

        # Connect both lists
        less.next = greaterDummy.next

        return lessDummy.next
```

---

## Complexity

### Time

```text
O(N)
```

### Space

```text
O(1)
```

No extra nodes created.

---

# 8. Step-by-Step Trace

Input:

```text
1 -> 4 -> 3 -> 2 -> 5 -> 2
x = 3
```

---

## Initial

```text
lessDummy -> 0
greaterDummy -> 0
```

---

## Step 1

Current = 1

```text
1 < 3

Less:
0 -> 1

Greater:
0
```

---

## Step 2

Current = 4

```text
4 >= 3

Less:
0 -> 1

Greater:
0 -> 4
```

---

## Step 3

Current = 3

```text
3 >= 3

Greater:
0 -> 4 -> 3
```

---

## Step 4

Current = 2

```text
2 < 3

Less:
0 -> 1 -> 2
```

---

## Step 5

Current = 5

```text
Greater:
0 -> 4 -> 3 -> 5
```

---

## Step 6

Current = 2

```text
Less:
0 -> 1 -> 2 -> 2
```

---

## Final Connection

```text
Less:
1 -> 2 -> 2

Greater:
4 -> 3 -> 5

Result:
1 -> 2 -> 2 -> 4 -> 3 -> 5
```

---

# 9. Related Problems

## 1. Odd Even Linked List

Split nodes into two linked lists and combine them.

---

## 2. Remove Linked List Elements

Filtering nodes while traversing a linked list.

---

## 3. Merge Two Sorted Lists

Classic dummy-node and tail-pointer practice.

---

## 4. Reorder List

Advanced linked list pointer manipulation.

---

## 5. Sort List

More complex linked list rearrangement using merge sort.
