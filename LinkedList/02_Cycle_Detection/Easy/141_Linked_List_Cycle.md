# 141. Linked List Cycle

**Pattern:** Fast & Slow Pointer (Floyd’s Cycle Detection)

---

# 1. Problem Statement with Example

Given the head of a linked list, determine whether the linked list has a cycle.

A cycle exists if some node can be reached again by continuously following `next` pointers.

Return:

* `True` → if cycle exists
* `False` → otherwise

---

## Example

Input:

```text id="1d6y8y"
3 -> 2 -> 0 -> -4
     ^         |
     |_________|
```

Output:

```text id="hnhn3v"
True
```

Because node `-4` points back to node `2`.

---

## Constraints

* Number of nodes: `[0, 10^4]`
* Node values: `[-10^5, 10^5]`

Need:

* efficient detection
* preferably `O(1)` space

---

# 2. Diagram

## No Cycle

```text id="a2s2nq"
1 -> 2 -> 3 -> 4 -> None
```

Fast pointer eventually hits `None`.

---

## With Cycle

```text id="h8m3fv"
1 -> 2 -> 3 -> 4
     ^         |
     |_________|
```

Fast pointer laps slow pointer and meets it.

---

# 3. Example I/O

## Example 1 (Cycle Exists)

Input:

```text id="tm7jlwm"
head = [3,2,0,-4]
tail connects to node index = 1
```

Output:

```text id="s0hskv"
True
```

---

## Example 2 (No Cycle)

Input:

```text id="9a14kr"
head = [1,2,3]
```

Output:

```text id="1a8s1x"
False
```

---

## Example 3 (Single Node Cycle)

Input:

```text id="n7jlwm"
1
↑|
```

Output:

```text id="d7yj5n"
True
```

---

# 4. Intuition & Pattern Recognition

# Key Signal

Whenever a problem asks:

* detect loop
* detect cycle
* repeated traversal
* circular linked list

Think immediately:

```text id="18itqj"
Fast & Slow Pointer
```

---

# Why Does It Work?

Suppose:

* slow moves `1 step`
* fast moves `2 steps`

If cycle exists:

* fast eventually catches slow
* just like runners on circular track

If no cycle:

* fast reaches `None`

---

# Mental Interview Shortcut

If:

```text id="yt3whp"
linked list + cycle detection
```

→ Floyd’s Algorithm instantly.

---

# 5. Simpler Version

---

# Simpler Question

Imagine array circular race track:

```text id="a2h5ul"
slow = +1 step
fast = +2 steps
```

Will they meet?

YES — if movement is circular.

Same exact idea applied to linked list.

---

# Related Simpler Problem

### Middle of the Linked List

Uses same:

```python id="43i3hm"
slow = slow.next
fast = fast.next.next
```

Difference:

* there we stop at middle
* here we check collision

---

# Simpler Thinking → Full Problem

## Step 1

Use one pointer:

```text id="mq7ndq"
cannot detect cycle efficiently
```

Need memory (`set`) to remember visited nodes.

---

## Step 2

Can two runners detect loop without memory?

YES.

That becomes Floyd’s Algorithm.

---

# 6. Brute Force

# Idea

Store visited nodes in hash set.

If node repeats:

* cycle exists

---

# Brute Force Code

```python id="x48vv5"
class Solution:
    def hasCycle(self, head):

        visited = set()

        curr = head

        while curr:

            if curr in visited:
                return True

            visited.add(curr)

            curr = curr.next

        return False
```

---

# Complexity

* Time: `O(n)`
* Space: `O(n)`

---

# 7. Optimal Solution

# Floyd’s Cycle Detection Algorithm

Use:

* slow pointer → 1 step
* fast pointer → 2 steps

If they meet:

* cycle exists

If fast reaches `None`:

* no cycle

---

# Optimal Code (Python)

```python id="z07k8x"
class Solution:
    def hasCycle(self, head):

        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next           # Move 1 step

            fast = fast.next.next      # Move 2 steps

            if slow == fast:
                return True

        return False
```

---

# Why This Works

Suppose cycle length = `k`.

Fast gains:

```text id="s1mz4g"
1 extra step per iteration
```

Eventually:

```text id="cl4bgd"
distance difference becomes multiple of k
```

They collide.

---

# Mathematical Intuition

Inside cycle:

```text id="4g3b5o"
fast speed = 2
slow speed = 1
relative speed = 1
```

So fast keeps gaining on slow.

Meeting is guaranteed.

---

# 8. Step-by-Step Trace

Input:

```text id="tjlwmm"
1 -> 2 -> 3 -> 4
     ^         |
     |_________|
```

---

# Initial

| Step | Slow | Fast |
| ---- | ---- | ---- |
| 0    | 1    | 1    |

---

# Iteration 1

| Step | Slow | Fast |
| ---- | ---- | ---- |
| 1    | 2    | 3    |

---

# Iteration 2

| Step | Slow | Fast |
| ---- | ---- | ---- |
| 2    | 3    | 2    |

---

# Iteration 3

| Step | Slow | Fast |
| ---- | ---- | ---- |
| 3    | 4    | 4    |

Pointers meet.

Return:

```text id="7bqg6z"
True
```

---

# 9. Related Problems

1. Middle of the Linked List
   Same fast & slow pointer foundation.

2. Linked List Cycle II
   Find exact starting node of cycle.

3. Happy Number
   Floyd’s cycle detection on numbers.

4. Find the Duplicate Number
   Converts array into cycle detection problem.

5. Palindrome Linked List
   Another major fast & slow pointer problem.
