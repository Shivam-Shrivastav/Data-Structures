# 225. Implement Stack using Queues (Stack Design)

---

# 1. Problem Statement

Design a stack that supports the standard stack operations using **only queues**.

Implement the `MyStack` class:

* `push(x)` → Push element `x` onto the stack.
* `pop()` → Remove and return the top element.
* `top()` → Return the top element.
* `empty()` → Return `True` if the stack is empty.

You may use only standard queue operations:

* push to back
* pop from front
* peek/front
* size
* empty

## Constraints

* `1 <= x <= 9`
* At most **100** operations.
* All `pop()` and `top()` calls are valid.

---

## Example

```text
Input:
["MyStack","push","push","top","pop","empty"]

[[],[1],[2],[],[],[]]

Output:
[null,null,null,2,2,false]
```

Explanation

```text
push(1)
Stack = [1]

push(2)
Stack = [1,2]

top() -> 2

pop() -> 2

empty() -> False
```

---

# 2. Diagram

## Normal Stack

```text
      Top
       ↓
+-----+
|  3  |
+-----+
|  2  |
+-----+
|  1  |
+-----+
```

Push → Top

Pop → Top

---

## Queue

```text
Front                     Back

1 ----> 2 ----> 3
↑                    ↑
Pop               Push
```

Queue removes from the **front**, but stack removes from the **back**.

So we must somehow make the newest element come to the front.

---

## Rotation Idea

Suppose queue contains

```text
Front

1 2 3

Back
```

Now push(4)

Queue becomes

```text
1 2 3 4
```

Rotate first 3 elements

Move

```text
1 → back

Queue:
2 3 4 1
```

Move

```text
2 → back

Queue:
3 4 1 2
```

Move

```text
3 → back

Queue:
4 1 2 3
```

Now front is

```text
4
```

Exactly what a stack needs.

---

# 3. Example I/O

### Example 1

```text
Input:

push(1)
push(2)
push(3)

top()

Output:

3
```

---

### Example 2

```text
push(5)

pop()

Output:

5
```

---

### Edge Case

```text
push(10)

empty()

Output:

False
```

---

# 4. Intuition & Pattern Recognition

## Interview Hint

Whenever a problem says

> Implement one data structure using another

Think:

* simulate behavior
* rearrange elements after every operation

---

Here

Queue gives

```text
FIFO
```

Stack requires

```text
LIFO
```

So we must reorder the queue.

---

### Key Observation

If we always keep the newest element at the **front** of the queue,

then

```text
queue.pop()
```

becomes

```text
stack.pop()
```

---

### Interview Thinking

"I cannot remove from the back of a queue.

So after inserting a new element,
I'll rotate the previous elements behind it."

---

# 5. Simpler Version

## Simpler Problem

Implement stack using a list.

```python
push -> append()

pop -> pop()

top -> stack[-1]
```

Easy.

---

Now replace list with queue.

Queue only allows

```text
Front removal
Back insertion
```

Need to rearrange after every push.

---

## Related Simpler Questions

### Easy

232. Implement Queue using Stacks

Reverse problem.

---

Current

225. Implement Stack using Queues

---

### Medium

622. Design Circular Queue

Another queue implementation problem.

---

### Harder

155. Min Stack

Store additional information while maintaining stack behavior.

---

# Simpler Thinking → Current Thinking

```text
Normal Stack

↓

Need LIFO

↓

Only FIFO available

↓

Newest element should always reach front

↓

Rotate queue

↓

Done
```

---

# 6. Brute Force

Using **two queues**

### Push

Move everything to second queue

Insert new element

Move everything back

Simple but uses two queues.

---

### Time Complexity

| Operation | Complexity |
| --------- | ---------- |
| push      | O(n)       |
| pop       | O(1)       |
| top       | O(1)       |
| empty     | O(1)       |

Space

```text
O(n)
```

---

# 7. Optimal Solution (One Queue)

## Idea

After inserting

Rotate queue

Exactly

```python
size-1
```

times.

This makes newly inserted element become front.

---

## Python Code

```python
from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        # Insert new element at the back
        self.q.append(x)

        # Rotate older elements behind the new one
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        # Front of queue represents stack top
        return self.q.popleft()

    def top(self) -> int:
        # Front of queue is current stack top
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0
```

---

## Time Complexity

| Operation | Complexity |
| --------- | ---------- |
| push      | **O(n)**   |
| pop       | **O(1)**   |
| top       | **O(1)**   |
| empty     | **O(1)**   |

---

## Space Complexity

```text
O(n)
```

---

# 8. Step-by-Step Trace

Suppose

```text
push(1)
push(2)
push(3)
```

---

### Initially

```text
Queue = []
```

---

### push(1)

Append

```text
1
```

Rotate

```text
0 times
```

Queue

```text
1
```

---

### push(2)

Append

```text
1 2
```

Rotate once

Move

```text
1
```

to back

Queue

```text
2 1
```

---

### push(3)

Append

```text
2 1 3
```

Rotate twice

Move

```text
2

Queue

1 3 2
```

Move

```text
1

Queue

3 2 1
```

Now

```text
Front

3 2 1
```

Stack order

```text
Top

3
2
1
```

---

### pop()

Remove front

```text
Returns 3

Queue

2 1
```

Correct.

---

### top()

```text
Front = 2
```

Correct.

---

# 9. Related Problems

### 1. LeetCode 232 — Implement Queue using Stacks (Easy)

Reverse of this problem: simulate FIFO behavior using two LIFO stacks.

---

### 2. LeetCode 155 — Min Stack (Medium)

Augments a stack with constant-time minimum retrieval while preserving stack operations.

---

### 3. LeetCode 622 — Design Circular Queue (Medium)

Implements queue behavior efficiently using a fixed-size circular buffer.

---

### 4. LeetCode 641 — Design Circular Deque (Medium)

Extends queue design by supporting insertion and deletion at both ends.

---

### 5. LeetCode 146 — LRU Cache (Medium)

Uses a combination of data structures (hash map + doubly linked list) to simulate required access behavior efficiently.

---

# Interview Cheat Sheet

### Recognition

* Implement one data structure using another.
* Queue is FIFO, but stack requires LIFO.
* Rearrangement is needed after insertion.

→ **Rotate the queue after every push.**

---

### Core Idea

```text
push(x)

↓

Append x

↓

Rotate all previous elements

↓

Newest element reaches front

↓

Queue front always equals Stack top
```

---

### Pattern Template

```python
q.append(x)

for _ in range(len(q) - 1):
    q.append(q.popleft())
```

Then:

```python
pop  -> q.popleft()

top  -> q[0]

empty -> len(q) == 0
```

**Key takeaway:** The trick is to make the queue's **front** always represent the stack's **top**. By rotating the queue after every `push`, all other operations become straightforward `O(1)` queue operations.
