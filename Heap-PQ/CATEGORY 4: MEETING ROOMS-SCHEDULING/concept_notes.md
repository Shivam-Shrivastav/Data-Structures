# Meeting Rooms Scheduling - Heap & Priority Queue

---

# 1. Pattern in One Minute

### Core Idea

When multiple resources (rooms) are available, always assign the meeting to the room that becomes available the earliest.

A **min-heap** efficiently answers:

* Which room becomes free first?
* Which room ID should be assigned?
* Which meeting finishes first?

Usually you'll maintain:

* **Available rooms heap** → ordered by room number.
* **Occupied rooms heap** → ordered by end time.

---

### Why does this pattern exist?

Instead of scanning every room for every meeting (**O(N × Rooms)**), heaps let us find the next available room in **O(log n)**.

---

### Think of this pattern when

* Rooms
* Servers
* CPUs
* Workers
* Machines
* Resources
* Booking systems
* Scheduling tasks

Whenever a resource is occupied for some duration.

---

# 2. Recognition Signals

## Strong clues

* "n meeting rooms"
* "assign meeting"
* "minimum rooms"
* "smallest available room"
* "first available room"
* "conference room"
* "bookings"
* "servers"
* "CPU scheduling"
* "resource allocation"

---

## Constraints

Usually:

* Up to 10^5 meetings
* Intervals sorted or sortable
* Need efficient assignment

O(n²) won't pass.

---

## Common disguises

Instead of rooms:

* Servers
* CPUs
* Threads
* Workers
* Machines
* Gates
* Chairs
* Seats
* Parking spots

Same pattern.

---

## Don't use when

* Only checking interval overlap.
* Just counting overlaps.
* No resource assignment involved.

Then sweep line or interval merging may be enough.

---

# 3. Mental Model

* Meetings arrive in chronological order.
* Every room has a "free at" time.
* Before assigning a meeting, free every room whose end time ≤ meeting start.
* Among free rooms, pick the smallest-numbered room.
* If no room is free:

  * Wait for the earliest finishing room.
  * Delay the meeting.
* Update the room's new finish time.
* Push it back into occupied heap.

Think of the occupied heap as:

> "Who finishes first?"

---

# 4. Boilerplate Template

```python
import heapq

meetings.sort()

# Available room numbers
available = list(range(n))
heapq.heapify(available)

# (end_time, room)
occupied = []

for start, end in meetings:

    # Free completed rooms
    while occupied and occupied[0][0] <= start:
        finish, room = heapq.heappop(occupied)
        heapq.heappush(available, room)

    duration = end - start

    if available:
        room = heapq.heappop(available)
        heapq.heappush(occupied, (end, room))

    else:
        finish, room = heapq.heappop(occupied)

        # Delay meeting
        new_end = finish + duration
        heapq.heappush(occupied, (new_end, room))
```

---

### Complexity

Sorting:
**O(n log n)**

Each heap operation:
**O(log rooms)**

Overall:

**O(n log n)**

Space:

**O(rooms)**

---

# 5. Variations

## 1. Meeting Rooms II

Need minimum rooms.

Instead of assigning IDs:

* Heap stores only end times.
* Heap size = rooms needed.

---

## 2. Meeting Rooms III

Need:

* Room assignment.
* Delay meetings.
* Count usage.

Need **two heaps**.

---

## 3. Most Booked Room

Same as Meeting Rooms III.

Maintain:

```python
count[room] += 1
```

Return room with highest count.

---

## 4. Smallest Unoccupied Chair

Exactly same idea.

Resources become:

* Chairs

Need two heaps.

---

## 5. Process Tasks Using Servers

Resources become:

* Servers

Busy heap:

```python
(freeTime, weight, index)
```

Free heap:

```python
(weight, index)
```

Very similar.

---

## 6. Single-Threaded CPU

Looks similar but is actually a **different heap pattern**.

There is **one CPU**, not multiple resources.

Heap chooses:

* shortest processing time

instead of

* earliest available room.

---

# 6. Common Pitfalls

### ❌ Forgetting to sort meetings

Always process chronologically.

---

### ❌ Using one heap

Most assignment problems need:

* available resources
* occupied resources

Two heaps.

---

### ❌ Wrong freeing condition

Correct:

```python
while occupied and occupied[0][0] <= start:
```

NOT

```python
<
```

Meetings ending exactly at the start time free the room.

---

### ❌ Delaying incorrectly

Wrong:

```python
new_end = end
```

Correct:

```python
duration = end - start
new_end = finish + duration
```

---

### ❌ Losing room number

Occupied heap should usually contain

```python
(end_time, room)
```

otherwise you won't know which room became free.

---

# 7. Interview Checklist

✓ Meetings are intervals.

✓ Resources remain busy until end time.

✓ Need to repeatedly know which resource frees first.

✓ Need to assign the smallest available resource.

✓ Meetings processed chronologically.

✓ Multiple resources exist.

→ **Think: Two Min-Heaps (Available + Occupied).**

---

# 8. Must-Do Problems

## 🟢 Easy

* None that directly teach this pattern.

---

## 🟡 Medium

⭐ **Meeting Rooms II (LC 253)** *(Top 3)*

⭐ **Meeting Rooms III (LC 2402)** *(Top 3)*

⭐ **Smallest Unoccupied Chair (LC 1942)** *(Top 3)*

* Process Tasks Using Servers (LC 1882)

---

## 🔴 Hard

* The Skyline Problem (different interval/heap flavor, optional)

---

### Pattern Mapping

| Problem                     | Pattern                     |
| --------------------------- | --------------------------- |
| Meeting Rooms II            | Single Min-Heap (end times) |
| Meeting Rooms III           | Two Heaps                   |
| Smallest Unoccupied Chair   | Two Heaps                   |
| Process Tasks Using Servers | Two Heaps                   |
| Seat Reservation Manager    | Available-resource heap     |

---

# 9. 30-Second Cheat Sheet

## Recognition

* Meeting rooms
* Servers
* Workers
* CPUs (multiple)
* Resource allocation
* Smallest available resource
* Earliest available resource

---

## Core Idea

Maintain:

* **Available heap** → free resources
* **Occupied heap** → `(end_time, resource)`

Free completed resources before every assignment.

If none are free, delay using the earliest finishing resource.

---

## Template

```python
sort intervals

free_heap = rooms
busy_heap = (end, room)

for meeting:
    free completed rooms

    if free room:
        assign immediately
    else:
        delay until earliest room finishes
```

---

## Complexity

* **Time:** `O(n log n)`
* **Space:** `O(n)` (or `O(rooms)` for the heaps)

---

## Common Variations

* Meeting Rooms II → one heap
* Meeting Rooms III → two heaps + usage count
* Smallest Unoccupied Chair → identical
* Process Tasks Using Servers → identical with server weights
* Seat Reservation Manager → available-resource heap

---

## Pitfalls

* Don't forget to sort meetings.
* Use `<=` when freeing rooms.
* Preserve meeting duration when delaying.
* Use **two heaps** for assignment problems.
* Store both `end_time` and `room_id` in the occupied heap.
