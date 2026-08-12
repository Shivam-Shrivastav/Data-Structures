# LRU Cache

LeetCode 146 — Design a data structure that follows the Least Recently Used (LRU) cache policy.

---

# 1. Problem Statement with Example

Design an LRU Cache with the following operations:

* `get(key)`

  * Return value if key exists
  * Otherwise return `-1`

* `put(key, value)`

  * Insert/update key
  * If capacity exceeded:

    * remove Least Recently Used item

Both operations must work in:

```text id="lrureq"
O(1)
```

time.

---

# Example

```text id="lruexample"
LRUCache(2)

put(1,1)
put(2,2)

get(1) -> 1

put(3,3)
# evicts key 2

get(2) -> -1

put(4,4)
# evicts key 1

get(1) -> -1
get(3) -> 3
get(4) -> 4
```

---

# Constraints

* `1 <= capacity <= 3000`
* Up to `2 * 10^5` operations
* Must achieve:

  * `O(1)` get
  * `O(1)` put

---

# 2. Diagram

# Core Structure

LRU needs:

## 1. Fast lookup

Use:

```text id="fastlookup"
HashMap
key -> node
```

---

## 2. Fast removal + insertion order

Use:

```text id="dll"
Doubly Linked List
```

---

# Why Doubly Linked List?

Because we need:

```text id="ops"
Remove any node in O(1)
Move node to front in O(1)
Delete least recently used in O(1)
```

Singly linked list cannot remove arbitrary node in O(1).

---

# Structure

```text id="lruorder"
Most Recently Used                    Least Recently Used

HEAD <-> 5 <-> 2 <-> 8 <-> 1 <-> TAIL
```

* Front = recently used
* Back = least recently used

---

# Accessing Existing Node

```text id="movefront"
get(8)

HEAD <-> 5 <-> 2 <-> 8 <-> 1 <-> TAIL

Remove 8
Move to front

HEAD <-> 8 <-> 5 <-> 2 <-> 1 <-> TAIL
```

---

# Capacity Exceeded

```text id="evict"
Capacity full

Remove node before TAIL
```

That is least recently used node.

---

# 3. Example I/O

# Example 1

```text id="eg1"
Input:
LRUCache(2)

put(1,1)
put(2,2)
get(1)

Output:
1
```

Because key `1` exists.

It also becomes most recently used.

---

# Example 2

```text id="eg2"
put(3,3)
```

Cache full.

Least recently used = key `2`

Evict it.

---

# Example 3 (Update Existing Key)

```text id="eg3"
put(1,10)
```

Do NOT create new node.

Update existing value and move to front.

---

# 4. Intuition & Pattern Recognition

# Signals for This Pattern

Whenever problem says:

* `O(1)` insert
* `O(1)` delete
* maintain usage/order
* recently used / oldest / eviction

Think:

> "HashMap + Doubly Linked List"

This is an extremely classic system design + DSA combo.

---

# Why HashMap Alone Fails

HashMap gives:

```text id="hashmap"
O(1) lookup
```

But NOT:

```text id="order"
usage ordering
```

---

# Why Linked List Alone Fails

Linked list gives ordering.

But lookup becomes:

```text id="badlookup"
O(n)
```

---

# Combination Solves Everything

| Structure          | Purpose           |
| ------------------ | ----------------- |
| HashMap            | key → node lookup |
| Doubly Linked List | maintain order    |

---

# Interview Recognition

The moment you hear:

```text id="interviewsignal"
Least Recently Used
```

immediately think:

```text id="correctpattern"
HashMap + Doubly Linked List
```

---

# 5. Simpler Version

# Simplest Version

## Using Array/List

```python id="arraylru"
cache = []

get(x):
    search linearly

put(x):
    remove old occurrence
    insert at front
```

Works logically.

But:

```text id="badcomplex"
O(n)
```

operations.

---

# Next Improvement

Use:

```text id="hm"
HashMap
```

for lookup.

Still need ordering.

---

# Final Insight

Need BOTH:

```text id="both"
Fast lookup + fast ordering updates
```

Hence:

```text id="finalcombo"
HashMap + Doubly Linked List
```

---

# Simpler Problems That Build This

---

## 1. Design HashMap

Learn constant-time lookup.

---

## 2. Design Linked List

Learn node insertion/removal mechanics.

---

## 3. LRU Cache

Combines both structures together.

---

# Thinking Progression

```text id="thinking"
Need fast lookup
    ↓
Use HashMap
    ↓
Need usage ordering
    ↓
Use Doubly Linked List
    ↓
Need O(1) removal
    ↓
Store node references in hashmap
```

---

# 6. Brute Force

# Idea

Use array/list.

Most recent at front.

---

# Brute Force Code

```python id="brutecode"
class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []

    def get(self, key):

        for i, (k, v) in enumerate(self.cache):

            if k == key:

                # move to front
                self.cache.pop(i)
                self.cache.insert(0, (k, v))

                return v

        return -1

    def put(self, key, value):

        for i, (k, v) in enumerate(self.cache):

            if k == key:
                self.cache.pop(i)
                self.cache.insert(0, (key, value))
                return

        if len(self.cache) == self.capacity:
            self.cache.pop()

        self.cache.insert(0, (key, value))
```

---

# Complexity

## Get

O(n)

## Put

O(n)

---

# 7. Optimal Solution

# Core Operations

We need:

```text id="coreops"
remove(node)
insert_front(node)
```

Both in `O(1)`.

---

# Node Structure

```text id="nodestruct"
node:
    key
    value
    prev
    next
```

---

# Optimal Code

```python id="optimalcode"
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):

        self.cap = capacity
        self.cache = {}

        # Dummy nodes
        self.left = Node(0, 0)   # LRU side
        self.right = Node(0, 0)  # MRU side

        self.left.next = self.right
        self.right.prev = self.left

    # Remove node from list
    def remove(self, node):

        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    # Insert at MRU side
    def insert(self, node):

        prev = self.right.prev
        nxt = self.right

        prev.next = node
        node.prev = prev

        node.next = nxt
        nxt.prev = node

    def get(self, key):

        if key in self.cache:

            node = self.cache[key]

            # move to recent
            self.remove(node)
            self.insert(node)

            return node.val

        return -1

    def put(self, key, value):

        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)

        self.cache[key] = node
        self.insert(node)

        # remove LRU
        if len(self.cache) > self.cap:

            lru = self.left.next

            self.remove(lru)

            del self.cache[lru.key]
```

---

# Complexity

## Get

O(1)

## Put

O(1)

## Space

O(capacity)

---

# 8. Step-by-Step Trace

# Capacity = 2

---

# put(1,1)

```text id="trace1"
HEAD <-> 1 <-> TAIL
```

Map:

```text id="map1"
{1: node1}
```

---

# put(2,2)

```text id="trace2"
HEAD <-> 1 <-> 2 <-> TAIL
```

2 is most recent.

---

# get(1)

Move `1` to recent.

```text id="trace3"
HEAD <-> 2 <-> 1 <-> TAIL
```

Return `1`.

---

# put(3,3)

Insert 3:

```text id="trace4"
HEAD <-> 2 <-> 1 <-> 3 <-> TAIL
```

Capacity exceeded.

LRU = `2`

Remove it:

```text id="trace5"
HEAD <-> 1 <-> 3 <-> TAIL
```

---

# 9. Related Problems

## 1. Design HashMap

Learn hash-based constant-time lookup.

---

## 2. Design Linked List

Learn insertion/removal mechanics.

---

## 3. LFU Cache

Advanced cache design.

Uses:

* frequency counts
* multiple linked lists
* hashmap combos

Hard problem.

---

## 4. Insert Delete GetRandom O(1)

Another classic:

* combine structures
* achieve O(1) operations

---

## 5. All O`one Data Structure

One of the hardest linked list + hashmap design problems.

Very strong follow-up after LRU/LFU.
