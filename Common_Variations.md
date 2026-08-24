Yes — **100%**. This is actually one of the best ways to get good at DSA.

Across Array, String, Linked List, Tree, Graph, Backtracking, DP, Binary Search, etc., the **problem statement changes**, but a relatively small set of **“variations / edge-case rules”** keeps repeating.

Your duplicate example:

```python
if i > start and nums[i] == nums[i-1]:
    continue
```

is one such **variation rule**.

I would organize the common variations into a **DSA Variation Cheat Sheet** like this:

---

# 1. Duplicates

### Variation

When elements can repeat, you often need to decide whether duplicates represent:

* the same solution
* different occurrences
* different states

### Backtracking / combinations

```python
if i > start and nums[i] == nums[i-1]:
    continue
```

Used in:

* 3Sum
* 4Sum
* Combination Sum II
* Subsets II
* Permutations II

### Key distinction

**Same value + same decision level → usually skip**

```text
[1, 1, 2]
     ↑
If we're deciding what to choose at this level,
choosing the second 1 produces the same branch.
```

But:

```python
used[i]
```

is often needed for **permutations**, because the same value at a different position can represent a different ordering.

---

# 2. "Use Once" vs "Can Reuse"

Extremely common.

### Use element once

```python
dfs(i + 1)
```

### Reuse current element

```python
dfs(i)
```

For example:

### Combination Sum

```python
path.append(nums[i])
dfs(i)       # can reuse
path.pop()
```

### Combination Sum II

```python
path.append(nums[i])
dfs(i + 1)   # cannot reuse
path.pop()
```

### Mental rule

```text
dfs(i)     → reuse
dfs(i+1)   → consume/use once
```

This pattern appears heavily in:

* Backtracking
* Knapsack
* Subset problems
* DP

---

# 3. Take vs Skip

This is probably the **most universal DSA variation**.

At every item:

```text
Take
Skip
```

For example:

```python
# Take
path.append(nums[i])
dfs(i + 1)
path.pop()

# Skip
dfs(i + 1)
```

Appears in:

* Subsets
* House Robber
* Knapsack
* Partition
* Decode ways
* String DP
* Stock problems
* Many tree DP problems

You should train yourself to ask:

> **What happens if I take this? What happens if I skip this?**

---

# 4. Previous State vs Current State

Very common in DP.

For example:

```python
dp[i] = dp[i-1] + dp[i-2]
```

You are asking:

```text
What previous states can reach i?
```

Examples:

### Climbing Stairs

```text
dp[i-1]
dp[i-2]
```

### House Robber

```text
dp[i-1]          # skip current
dp[i-2] + nums[i] # take current
```

### Grid DP

```text
dp[i-1][j]   # from top
dp[i][j-1]   # from left
```

### General variation

```text
1 previous state
2 previous states
multiple previous states
```

---

# 5. State Includes Extra Information

Sometimes `i` alone isn't enough.

You need:

```python
dfs(i, state)
```

Examples:

### Stock

```python
dfs(i, holding)
```

because:

```text
holding = 0
holding = 1
```

### Knapsack

```python
dfs(i, capacity)
```

### String decoding

```python
dfs(i)
```

because position determines remaining string.

### Graph

```python
dfs(node, visited)
```

### Tree

```python
dfs(node, parent)
```

### General question

Ask:

> **What information from the past changes what I can do next?**

That information becomes part of your state.

---

# 6. Boundary / Out-of-Bounds Handling

Appears everywhere.

### Array

```python
if i >= n:
    return
```

### Matrix

```python
if r < 0 or r >= m or c < 0 or c >= n:
    return
```

### Linked List

```python
if node is None:
    return
```

### Tree

```python
if root is None:
    return
```

### Binary Search

```python
while left <= right:
```

### General variation

```text
Have I gone outside the valid state?
```

This is basically the universal **base-case family**.

---

# 7. Visited / Already Processed

Extremely common in Graph + Matrix + Backtracking.

```python
visited.add(node)
```

or:

```python
if visited[r][c]:
    continue
```

Used when:

```text
A → B → C → A
```

could create a cycle.

Appears in:

* Graph DFS
* BFS
* Number of Islands
* Word Search
* Cycle Detection
* Connected Components

---

# 8. Don't Revisit Parent

A special graph/tree variation.

For undirected graph:

```python
def dfs(node, parent):
    for nei in graph[node]:
        if nei == parent:
            continue
```

Why?

Because:

```text
A → B
```

means B's adjacency contains A again.

Without parent tracking, you'd think:

```text
A → B → A → B → A...
```

This is particularly common in:

* Tree DFS
* Undirected Graph DFS
* Tree DP

---

# 9. Cycle Detection

Another common variation.

### DFS directed graph

```python
if node in path:
    return True
```

Usually represented with:

```text
0 = unvisited
1 = visiting
2 = completed
```

The important distinction:

```text
visited ≠ currently in recursion path
```

This is a very common interview trap.

---

# 10. In-place Modification

Instead of:

```python
visited = set()
```

you modify the input.

Example:

```python
grid[r][c] = '#'
```

Then:

```python
if grid[r][c] == '#':
    continue
```

Used in:

* Number of Islands
* Word Search
* Matrix DFS
* Backtracking

### Variation

```text
Extra memory
vs
modify input to store state
```

---

# 11. Restore State / Backtracking

The classic:

```python
path.append(x)

dfs(...)

path.pop()
```

But it applies much more broadly.

Example:

```python
grid[r][c] = '#'

dfs(...)

grid[r][c] = original
```

The pattern is:

```text
CHANGE
↓
EXPLORE
↓
UNDO
```

This is the fundamental backtracking variation.

---

# 12. Sorted Input Gives You Extra Power

Whenever you see:

```python
nums.sort()
```

think:

> **What problem does sorting allow me to solve more easily?**

It enables:

### Duplicate skipping

```python
if i > start and nums[i] == nums[i-1]:
```

### Two pointers

```text
left++
right--
```

### Early termination

```python
if nums[i] > target:
    break
```

### Binary search

Sorting is often what makes binary search possible.

### Greedy

Sorting frequently creates the ordering needed for a greedy solution.

---

# 13. Early Termination / Pruning

Huge variation in Backtracking, Binary Search, DP, Greedy.

Example:

```python
if nums[i] > remaining:
    break
```

Instead of exploring:

```text
1000 branches
```

you cut them off.

Backtracking:

```python
if current_sum > target:
    return
```

Binary search:

```python
if nums[mid] < target:
    left = mid + 1
```

DP:

```python
if dp[i] already gives a better answer:
    skip
```

The mental question:

> **Can I prove that this branch can never produce a better/valid answer?**

If yes → prune.

---

# 14. Min vs Max vs Count

Same structure, different operation.

A lot of DSA problems are actually just:

```text
Choose:
min
max
count
sum
boolean
```

For example:

### Minimum

```python
dp[i] = min(...)
```

### Maximum

```python
dp[i] = max(...)
```

### Number of ways

```python
dp[i] += ...
```

### Possible or not

```python
dp[i] = dp[i] or ...
```

This is a **very important DP variation**.

---

# 15. Exact vs At Most vs At Least

This variation appears everywhere.

### Exact

```text
sum == target
```

### At most

```text
sum <= target
```

### At least

```text
sum >= target
```

Examples:

* Knapsack
* Sliding Window
* Binary Search
* DP
* Greedy

Especially important in:

```text
"at most K"
"exactly K"
"at least K"
```

because the solution strategy can completely change.

---

# 16. Fixed Size vs Variable Size

Huge Sliding Window variation.

### Fixed

```python
right - left + 1 == k
```

Move both systematically.

### Variable

```python
while invalid:
    left += 1
```

Typical structure:

```python
for right in range(n):
    add(nums[right])

    while invalid:
        remove(nums[left])
        left += 1
```

Mental distinction:

```text
Fixed window → maintain size
Variable window → maintain condition
```

---

# 17. "At Most K" → "Exactly K"

A very powerful transformation.

For many counting problems:

```text
exactly(K)
=
atMost(K) - atMost(K-1)
```

Example:

```text
Subarrays with exactly K distinct elements
```

becomes:

```text
atMost(K) - atMost(K-1)
```

This is one of those **pattern transformations** worth memorizing.

---

# 18. Prefix / Running Information

Instead of repeatedly calculating the past:

```python
sum(nums[:i])
```

maintain:

```python
prefix += nums[i]
```

Appears in:

* Prefix Sum
* Subarray Sum
* Range Sum
* Difference Array
* DP
* String prefix techniques

Variation:

```text
running sum
running min
running max
running frequency
running state
```

---

# 19. HashMap as "Remember What I've Seen"

Very common.

Instead of searching backwards:

```python
for j in range(i):
```

remember information:

```python
seen[x] = ...
```

Examples:

### Two Sum

```python
seen[target - x]
```

### Prefix Sum

```python
seen[prefix]
```

### Frequency

```python
freq[x] += 1
```

### String

```python
last_seen[ch] = i
```

Mental rule:

> **If I repeatedly need to ask something about the past, can I store it in a hash map?**

---

# 20. Frequency Map vs Set

Important distinction.

### Set

```python
seen = set()
```

Question:

> Have I seen this?

### HashMap

```python
freq = {}
```

Question:

> How many / where / what information is associated with this?

Examples:

```text
Set → duplicate detection
Map → frequency
Map → index
Map → prefix count
Map → cached result
```

---

# 21. First / Last Occurrence

Extremely common with Binary Search.

Instead of:

```text
find target
```

you may need:

```text
first target
last target
```

Variation:

```python
if nums[mid] >= target:
    right = mid - 1
else:
    left = mid + 1
```

versus:

```python
if nums[mid] <= target:
    left = mid + 1
else:
    right = mid - 1
```

This becomes a broader pattern:

```text
Find ANY
Find FIRST
Find LAST
Find LOWER BOUND
Find UPPER BOUND
```

---

# 22. Binary Search on Answer

Very important variation.

Instead of searching:

```text
array
```

you search:

```text
possible answer
```

Structure:

```python
left = minimum_answer
right = maximum_answer

while left <= right:
    mid = (left + right) // 2

    if feasible(mid):
        ...
```

The key variation is:

```text
Can I answer "is X possible?"
```

If yes/no is monotonic:

```text
False False False True True True
```

→ Binary Search.

---

# 23. Stack: Monotonic Variation

A normal stack:

```python
stack.append(x)
stack.pop()
```

But sometimes maintain:

```text
increasing stack
```

or:

```text
decreasing stack
```

Then:

```python
while stack and nums[stack[-1]] < nums[i]:
    stack.pop()
```

This creates:

* Next Greater Element
* Next Smaller Element
* Previous Greater
* Previous Smaller
* Histogram
* Stock Span

---

# 24. Stack: Store Index vs Value

Another subtle but extremely common variation.

### Store value

```python
stack.append(nums[i])
```

Useful when you only need the value.

### Store index

```python
stack.append(i)
```

Useful when you need:

```text
distance
position
width
time
```

For example:

```python
i - stack[-1]
```

---

# 25. Linked List: Dummy Node

A tiny variation that solves many edge cases.

```python
dummy = ListNode(0)
dummy.next = head
```

Then:

```text
head deletion
middle deletion
tail deletion
```

can use the same logic.

Used heavily in:

* Remove Nth Node
* Merge Lists
* Partition List
* Reverse operations
* Insert/delete problems

Mental rule:

> **If head is a special case, try a dummy node.**

---

# 26. Linked List: Slow/Fast Pointers

Two speeds:

```python
slow = slow.next
fast = fast.next.next
```

Variations:

### Middle

```text
fast reaches end
slow reaches middle
```

### Cycle

```text
slow == fast
```

### Find cycle entry

After meeting:

```python
slow = head

while slow != fast:
    slow = slow.next
    fast = fast.next
```

One underlying idea:

> **Use different pointer speeds to extract positional information.**

---

# 27. Tree: Return Information Upward

Tree DFS often isn't about printing/visiting.

The child returns information:

```python
left = dfs(root.left)
right = dfs(root.right)
```

Then parent combines it:

```python
return ...
```

Examples:

```text
height
diameter
max path sum
balanced tree
subtree sum
robber
```

This is essentially:

```text
child → parent information flow
```

Very similar to DP.

---

# 28. Tree: Global Answer vs Returned Answer

Classic tree variation.

### Return value

```python
def dfs(node):
    return height
```

### Global answer

```python
self.ans = max(self.ans, left + right)
```

Why?

Because sometimes the answer:

```text
passes THROUGH the node
```

but isn't the value that should be returned to the parent.

Example:

```text
       A
      / \
     B   C
```

Diameter:

```text
left_height + right_height
```

but parent can only receive:

```text
max(left_height, right_height) + 1
```

---

# 29. Graph: Directed vs Undirected

This changes the rules.

### Undirected

Need:

```python
parent
```

or visited handling.

### Directed

Need to consider:

```text
edge direction
```

and often:

```text
cycle states
```

This affects:

* DFS
* BFS
* Cycle detection
* Topological sort
* Shortest path

---

# 30. Graph: BFS Levels

Normal BFS:

```python
queue.append(start)

while queue:
    node = queue.popleft()
```

But sometimes you need **distance/level**:

```python
for _ in range(len(queue)):
    node = queue.popleft()
```

Now each outer iteration means:

```text
distance + 1
```

Used in:

* Shortest path in unweighted graph
* Rotting Oranges
* Word Ladder
* Level-order problems

---

# 31. Graph: Multi-Source BFS

Instead of:

```text
one starting node
```

start with:

```text
all starting nodes
```

```python
for source in sources:
    queue.append(source)
```

Then BFS expands simultaneously.

Used in:

* Rotting Oranges
* Walls and Gates
* Distance to nearest 0
* Multi-source spreading problems

Mental pattern:

> **If multiple things spread simultaneously, initialize BFS with all sources.**

---

# 32. DP: Top-Down vs Bottom-Up

Same recurrence, different implementation.

### Top-down

```python
@cache
def dfs(i):
    ...
```

### Bottom-up

```python
dp[i] = ...
```

Think:

```text
Recursion + memoization
        ↓
      DP
```

and:

```text
dependency order
        ↓
bottom-up DP
```

---

# 33. DP: Impossible State

Very important.

Sometimes:

```python
0
```

is a valid answer, so you **cannot use 0 to mean impossible**.

Instead:

```python
INF = float('inf')
```

for minimization.

Or:

```python
NEG_INF = float('-inf')
```

for maximization.

Example:

```python
dp = [float('inf')] * (amount + 1)
dp[0] = 0
```

This is a recurring DP variation:

```text
valid zero
vs
unreachable
```

---

# 34. DP: Number of Ways vs Best Answer

Same state, completely different transition.

### Number of ways

```python
dp[i] += dp[previous]
```

### Maximum value

```python
dp[i] = max(dp[i], ...)
```

### Minimum value

```python
dp[i] = min(dp[i], ...)
```

### Boolean possibility

```python
dp[i] |= dp[previous]
```

Recognizing this quickly is extremely useful.

---

# 35. DP: Ordering Matters

This one is **very important for Knapsack**.

Compare:

```python
for coin in coins:
    for amount in range(...):
```

versus:

```python
for amount in range(...):
    for coin in coins:
```

They can represent different things:

```text
combinations
vs
permutations
```

Similarly:

```python
range(capacity, weight - 1, -1)
```

often means:

```text
use item once
```

while:

```python
range(weight, capacity + 1)
```

means:

```text
item can potentially be reused
```

---

# 36. String: Character vs Substring

Another common variation.

Character:

```python
s[i]
```

Substring:

```python
s[i:j]
```

But DP often asks:

```text
prefix
suffix
interval
```

Examples:

```text
decode → position
palindrome → interval [l, r]
LCS → i, j
edit distance → i, j
```

So the state can change from:

```text
one index
```

to:

```text
two indices
```

---

# 37. Interval DP

Special but extremely reusable.

State:

```python
dp[l][r]
```

means:

> Answer for substring/subarray from `l` to `r`.

Used in:

* Palindrome
* Burst Balloons
* Matrix Chain Multiplication
* Strange Printer
* Merge Stones

Typical variation:

```text
expand interval
shrink interval
split interval
```

For example:

```python
for length in range(2, n + 1):
    for l in range(n - length + 1):
        r = l + length - 1
```

---

# 38. Graph / Grid: 4 Directions vs 8 Directions

Classic variation.

4-direction:

```text
up
down
left
right
```

8-direction adds:

```text
4 diagonals
```

Reusable template:

```python
directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]
```

The important thing is to recognize:

> **Movement constraints define the graph.**

---

# 39. Negative Values

A surprisingly important variation.

Algorithms often silently assume:

```text
positive numbers
```

but negative numbers change things.

For example, Sliding Window often works for:

```text
positive numbers
```

but fails with:

```text
negative numbers
```

Then you may need:

* Prefix Sum
* HashMap
* Monotonic Deque
* DP

Similarly, Kadane's algorithm must correctly handle:

```text
all negative
```

Example:

```python
best = nums[0]
current = nums[0]
```

rather than:

```python
best = 0
```

---

# 40. Overflow / Large Values

More relevant in languages like C++/Java, but conceptually universal.

Think:

```text
Can intermediate values become much larger than input values?
```

Examples:

```text
mid = left + (right-left)//2
```

rather than:

```text
(left + right)//2
```

And in DP:

```text
INF + something
```

needs care.

---

# The Bigger Picture

Instead of memorizing **40 independent tricks**, I would group them into about **10 meta-variations**.

| Meta variation                 | Examples                                      |
| ------------------------------ | --------------------------------------------- |
| **Duplicates**                 | skip duplicate, frequency                     |
| **Reuse**                      | `dfs(i)` vs `dfs(i+1)`                        |
| **State**                      | `dfs(i)`, `dfs(i,state)`, `dp[l][r]`          |
| **Direction**                  | take/skip, left/right, parent/child           |
| **Memory**                     | visited, hash map, memo                       |
| **Ordering**                   | sorted, traversal order, loop order           |
| **Boundaries**                 | null, out-of-range, base case                 |
| **Optimization**               | prune, early break, monotonicity              |
| **Counting/Optimization type** | count/min/max/boolean                         |
| **Special constraints**        | negative values, cycles, reuse, exact/at-most |

---

# The Most Important Mental Checklist

When you see **any new DSA problem**, before coding, run through this:

```text
1. Are there duplicates?
        ↓
2. Can I reuse an element?
        ↓
3. Is it TAKE / SKIP?
        ↓
4. What is my STATE?
        ↓
5. What information from the past matters?
        ↓
6. Do I need visited / parent?
        ↓
7. Can I sort?
        ↓
8. Can I prune / early terminate?
        ↓
9. Is this asking for:
      - existence?
      - count?
      - min?
      - max?
      - exact?
      - at most?
      - at least?
        ↓
10. Is the answer based on:
      - previous state?
      - range/interval?
      - neighbors?
      - levels?
      - prefix?
        ↓
11. Are there special constraints?
      - negative?
      - duplicate?
      - cycle?
      - reuse?
      - ordering?
```

### And there's an even more useful way to think about it:

**DSA patterns are mostly "base pattern + variation".**

For example:

```text
Backtracking
    +
    ├── duplicates
    ├── reuse
    ├── use once
    ├── take/skip
    ├── pruning
    └── ordering

DP
    +
    ├── 1D state
    ├── 2D state
    ├── interval state
    ├── take/skip
    ├── count/min/max
    ├── impossible state
    └── ordering

Graph
    +
    ├── directed/undirected
    ├── visited
    ├── parent
    ├── cycle
    ├── levels
    ├── multi-source
    └── weighted/unweighted

Binary Search
    +
    ├── exact
    ├── first
    ├── last
    ├── lower bound
    ├── upper bound
    └── binary search on answer
```

**This is the level I would recommend you revise at**: don't memorize 100 LeetCode solutions; memorize the **base pattern + its variations**. Then a new problem becomes much easier to classify.
