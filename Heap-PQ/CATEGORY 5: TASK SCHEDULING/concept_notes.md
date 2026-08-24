# Task Scheduling Pattern (Heap + Priority Queue)

---

# 1. Pattern in One Minute

### Core Idea

You have multiple tasks with **dependencies, priorities, arrival times, or cooldowns**, and at every step you must choose **the "best" available task**.

A **heap** efficiently maintains the current candidate tasks while another data structure (queue/sorted list/graph) determines **when tasks become available**.

### Why does this pattern exist?

Without a heap, selecting the next task costs **O(n)** every time.

Heap reduces it to **O(log n)**.

### Think of this pattern when

* Tasks become available over time.
* Some tasks must finish before others.
* CPU/server picks one task at a time.
* Need highest/lowest priority task.
* Scheduling simulation.

---

# 2. Recognition Signals

### Strong clues

* "Execute tasks"
* "Schedule jobs"
* "CPU"
* "Server"
* "Meeting rooms"
* "Available tasks"
* "Earliest start"
* "Dependencies"
* "Cooldown"
* "Idle time"

---

### Common disguises

* Assign workers
* Pick project
* Process requests
* Execute commands
* Allocate machines
* Handle events

---

### Usually involves

* Heap
* Queue
* Graph (Topological Sort)
* Sorting by start time
* Simulation

---

### Don't use when

* Tasks are independent and no ordering matters.
* Only need sorting once.
* DP/Greedy solves directly.

---

# 3. Mental Model

Think of scheduling as maintaining **two worlds**.

### World 1

Tasks **not yet available**

Examples

* Future arrival time
* Dependency not satisfied
* Cooling period not over

---

### World 2

Tasks ready to execute

Heap stores these.

Every iteration

```
Move newly available tasks
        ↓
Insert into heap
        ↓
Pick best task
        ↓
Process task
        ↓
Repeat
```

The heap always represents

> "Among everything I can do right now, what is the best choice?"

---

Typical loop

```
while tasks remain:

    unlock new tasks

    push into heap

    pop best task

    execute

    update state
```

---

# 4. Boilerplate Template

```python
import heapq

tasks.sort()          # usually by arrival/start time

heap = []
i = 0
time = 0

while i < len(tasks) or heap:

    # If no available task, jump time
    if not heap:
        time = max(time, tasks[i][0])

    # Add all tasks that are now available
    while i < len(tasks) and tasks[i][0] <= time:
        arrival, duration = tasks[i]
        heapq.heappush(heap, (duration, arrival))
        i += 1

    # Execute best task
    duration, arrival = heapq.heappop(heap)

    time += duration
```

---

### Generic template

```python
unlock available tasks

push into heap

pop best candidate

update answer

repeat
```

---

# 5. Variations

## 1. Single Threaded CPU (LC 1834) ⭐⭐⭐

Heap stores

```
(process_time, index)
```

Sort by enqueue time.

---

## 2. Process Tasks Using Servers (LC 1882) ⭐⭐⭐

Two heaps

```
available servers

busy servers
```

Busy heap releases servers when work finishes.

---

## 3. Task Scheduler (LC 621)

Need cooldown.

Use

* Max Heap
* Queue

Queue stores

```
(task, nextAvailableTime)
```

---

## 4. Meeting Rooms II

Min Heap

Stores

```
meeting end times
```

Remove finished meetings.

---

## 5. Meeting Rooms III

Heap of

```
available rooms

occupied rooms
```

Delay meetings if necessary.

---

## 6. IPO (LC 502)

Sort projects by capital.

Heap stores profits.

---

## 7. Course Schedule III

Sort deadlines.

Heap stores durations.

Remove longest course if necessary.

---

## 8. Maximum Performance of Team

Sort efficiency.

Heap keeps fastest engineers.

---

## 9. Topological Scheduling

Graph +

Heap of zero indegree nodes.

---

# 6. Common Pitfalls

### Forgetting to advance time

Wrong

```
time += 1
```

Correct

```
time = next arrival
```

when heap is empty.

---

### Not unlocking all tasks

Wrong

```
if arrival <= time:
```

Correct

```
while arrival <= time:
```

Unlock everything.

---

### Wrong heap ordering

Heap key should exactly match priority.

Examples

```
(processTime, index)

(endTime)

(-count)

(profit)

(duration)
```

---

### Forgetting tie-breaking

Many problems require

```
(processTime, index)
```

instead of

```
(processTime)
```

---

### Mixing available and unavailable tasks

Always separate them.

---

# 7. Interview Checklist

✓ Tasks become available over time

✓ Need to repeatedly choose best task

✓ Events happen chronologically

✓ Current best changes dynamically

✓ Need efficient insertion/removal

✓ Simulation involved

→ Think **Heap + Scheduling**

---

# 8. Must-Do Problems

## Easy

* 🟢 Task Scheduler *(Medium despite the name; no true Easy canonical scheduling problem in this pattern)*

## Medium

⭐ **Top 3**

1. Single-Threaded CPU ⭐⭐⭐
2. Process Tasks Using Servers ⭐⭐⭐
3. Meeting Rooms II ⭐⭐⭐

Other important ones

* Meeting Rooms III
* IPO

## Hard

* Course Schedule III
* Maximum Performance of a Team

---

# 9. 30-Second Cheat Sheet

### Recognition

* CPU
* Servers
* Scheduling
* Arrival time
* Available tasks
* Simulation
* Priority execution

---

### Core Idea

```
Future Tasks
      ↓
Unlock
      ↓
Heap
      ↓
Pick Best
      ↓
Execute
      ↓
Repeat
```

---

### Generic Template

```python
sort tasks

while tasks or heap:

    unlock available tasks

    push into heap

    pop best task

    process

    update time
```

---

### Complexity

* Sorting: **O(n log n)**
* Heap operations: **O(n log n)**
* Space: **O(n)**

---

### Common Variations

* Arrival time → Sort + Heap
* Cooldown → Heap + Queue
* Servers → Two Heaps
* Meetings → Min Heap
* Dependencies → Graph + Heap
* Capital constraints → Sort + Heap

---

### Pitfalls

* ❌ Forget time jump
* ❌ Unlock only one task
* ❌ Wrong heap key
* ❌ Ignore tie-breakers
* ❌ Mix unavailable tasks into the heap

> **Mental shortcut:** Almost every scheduling problem follows the same pattern: **sort events → unlock available work → maintain a heap of candidates → repeatedly execute the best available task**. Once you recognize this flow, the specific heap key (processing time, end time, profit, server weight, etc.) is usually the only thing that changes.
