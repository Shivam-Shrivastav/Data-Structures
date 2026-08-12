# Remove Duplicates from Sorted List

LeetCode #83 — Easy
Pattern: Linked List Traversal, Two Pointers

---

# 1. Problem Statement with Example

Given the head of a **sorted linked list**, delete all duplicates such that each element appears only once.

Return the linked list in sorted order.

---

### Constraints

* Number of nodes: `0 <= n <= 300`
* `-100 <= Node.val <= 100`
* The linked list is sorted in ascending order.

---

### Example

Input:

```text id="13k0wk"
1 -> 1 -> 2 -> 3 -> 3
```

Output:

```text id="ll8pao"
1 -> 2 -> 3
```

---

# 2. Diagram

Because the list is sorted, duplicates are always adjacent.

```text id="7qksu5"
1 -> 1 -> 2 -> 3 -> 3
^
curr

Compare:
curr.val == curr.next.val

Duplicate found.

Skip next node:
curr.next = curr.next.next
```

After removal:

```text id="8n1gsp"
1 -> 2 -> 3
```

---

# 3. Example I/O

## Example 1 (Typical)

### Input

```text id="zq93zk"
head = [1,1,2,3,3]
```

### Output

```text id="v3d7s0"
[1,2,3]
```

### Why?

* Remove second `1`
* Remove second `3`

---

## Example 2 (Edge Case)

### Input

```text id="nvov7n"
head = []
```

### Output

```text id="a8s0pw"
[]
```

### Why?

Empty list remains empty.

---

# 4. Intuition & Pattern Recognition

### Key Observation

The list is already sorted.

That means:

```text id="adq6t7"
duplicates will always be adjacent
```

So we only need to compare:

```python id="q8g2fx"
curr.val == curr.next.val
```

---

### Pattern Signal

Whenever you see:

* Sorted linked list
* Remove duplicates
* Adjacent equal values

Think:

> “Single traversal + pointer skipping”

---

### Interview Thinking

If current node and next node have same value:

* Keep one
* Skip the duplicate node

Otherwise:

* Move forward normally

---

# 5. Simpler Version

## Simplest Version

Remove duplicates from a sorted array.

Example:

```text id="x8nnf0"
[1,1,2,3,3]
```

Since duplicates are adjacent:

* Compare current with previous
* Keep unique elements

---

## How it evolves into linked list version

### Array Version

```python id="7huy8f"
if nums[i] != nums[i-1]:
```

### Linked List Version

```python id="m9kpw3"
if curr.val != curr.next.val:
```

Instead of shifting elements:

* Rewire pointers

```python id="58q8mu"
curr.next = curr.next.next
```

---

## Related simpler problems

### 1. Remove Duplicates from Sorted Array

Same exact logic but arrays.

### 2. Linked List Cycle

Basic linked list traversal practice.

### 3. Remove Linked List Elements

Node deletion practice.

### 4. Merge Two Sorted Lists

Another sorted linked list traversal problem.

---

# 6. Brute Force

## Idea

* Traverse list
* Store unique values in a set
* Create a new linked list

---

## Brute Force Code

```python id="jlwm1k"
class Solution:
    def deleteDuplicates(self, head):

        seen = set()
        dummy = ListNode(0)
        tail = dummy

        curr = head

        while curr:

            if curr.val not in seen:
                seen.add(curr.val)

                tail.next = ListNode(curr.val)
                tail = tail.next

            curr = curr.next

        return dummy.next
```

---

## Complexity

### Time

```text id="ryxt1e"
O(n)
```

### Space

```text id="42tf1u"
O(n)
```

---

# 7. Optimal Solution

## Key Insight

Since list is sorted:

* Duplicates appear consecutively
* No extra data structure needed

Just skip duplicate nodes directly.

---

## Optimal Code

```python id="5j99r0"
class Solution:
    def deleteDuplicates(self, head):

        curr = head

        # Traverse until next node exists
        while curr and curr.next:

            # Duplicate found
            if curr.val == curr.next.val:

                # Skip duplicate node
                curr.next = curr.next.next

            else:
                # Move forward only when unique
                curr = curr.next

        return head
```

---

## Complexity

### Time

```text id="on3btl"
O(n)
```

Each node visited once.

---

### Space

```text id="yb7nkn"
O(1)
```

No extra space used.

---

# 8. Step-by-Step Trace

Input:

```text id="q9k9bm"
1 -> 1 -> 2 -> 3 -> 3
```

---

| Step | curr | curr.next | Action           | List          |
| ---- | ---- | --------- | ---------------- | ------------- |
| 1    | 1    | 1         | duplicate → skip | 1 → 2 → 3 → 3 |
| 2    | 1    | 2         | move curr        | 1 → 2 → 3 → 3 |
| 3    | 2    | 3         | move curr        | 1 → 2 → 3 → 3 |
| 4    | 3    | 3         | duplicate → skip | 1 → 2 → 3     |
| End  | 3    | None      | stop             | Final list    |

---

# 9. Related Problems

### 1. Remove Duplicates from Sorted Array

Same adjacent duplicate removal idea.

### 2. Remove Duplicates from Sorted List II

Harder version where all duplicates are removed completely.

### 3. Remove Linked List Elements

General node deletion problem.

### 4. Partition List

More advanced pointer rewiring.

### 5. Sort List

Linked list sorting + merging concepts.
