## PART 2 — LISTS

---

### 2.1 What a List Actually Is in Memory

A Python list is **not** a fixed array. It's a **dynamic array of pointers**.

- Each element is a pointer (reference) to an object in memory
- The list stores the pointers contiguously, not the objects themselves
- This is why a list can hold mixed types — it's just storing addresses

```python
nums = [1, "hello", 3.14, True]   # totally valid — mixed types
```

---

### 2.2 Core Operations & Their Time Complexity

| Operation | Syntax | Time |
|---|---|---|
| Access by index | `lst[i]` | O(1) |
| Append to end | `lst.append(x)` | O(1) amortized |
| Insert at index | `lst.insert(i, x)` | O(n) — shifts everything |
| Delete by index | `del lst[i]` | O(n) — shifts everything |
| Search (in) | `x in lst` | O(n) — linear scan |
| Length | `len(lst)` | O(1) |
| Slice | `lst[a:b]` | O(b-a) |

> **Critical insight:** `append` is O(1) but `insert(0, x)` is O(n). If you're inserting at the front constantly, you're using the wrong data structure (use `collections.deque`).

---

### 2.3 Slicing — Full Syntax

```python
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lst[2:6]      # [2, 3, 4, 5]       → start to end (exclusive)
lst[:4]       # [0, 1, 2, 3]       → from beginning
lst[6:]       # [6, 7, 8, 9]       → to end
lst[::2]      # [0, 2, 4, 6, 8]    → every 2nd element
lst[::-1]     # [9, 8, 7, 6, 5...] → reversed
lst[1:8:3]    # [1, 4, 7]          → start:stop:step
```

Slicing **always returns a new list** — it never modifies the original.

---

### 2.4 All the Methods You Actually Need

```python
lst = [3, 1, 4, 1, 5, 9, 2, 6]

lst.append(7)          # add to end → [3,1,4,1,5,9,2,6,7]
lst.insert(2, 99)      # insert 99 at index 2
lst.pop()              # remove & return last element
lst.pop(0)             # remove & return element at index 0
lst.remove(1)          # removes FIRST occurrence of value 1
lst.index(5)           # returns index of first 5
lst.count(1)           # how many times 1 appears
lst.sort()             # sort in place (modifies list)
lst.sort(reverse=True) # descending
lst.reverse()          # reverse in place
lst.copy()             # shallow copy
lst.clear()            # empties the list
lst.extend([10, 11])   # adds multiple items (vs append adds one)
```

**`sort()` vs `sorted()`:**
```python
lst.sort()         # modifies in place, returns None
new = sorted(lst)  # returns NEW sorted list, original unchanged
```

---

### 2.5 List Comprehension — The Python Way

```python
# Regular loop
squares = []
for i in range(10):
    squares.append(i**2)

# Comprehension — same result, one line
squares = [i**2 for i in range(10)]

# With condition (filter)
evens = [i for i in range(20) if i % 2 == 0]

# Nested (flattening a 2D list)
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flat = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

### 2.6 Niche Things Most People Don't Know

**Shallow copy trap — the #1 beginner bug:**
```python
a = [1, 2, 3]
b = a            # NOT a copy — both point to same list
b.append(4)
print(a)         # [1, 2, 3, 4] ← a got modified too!

# Fix:
b = a.copy()     # or b = a[:]  or b = list(a)
```

**Unpacking:**
```python
first, *rest = [1, 2, 3, 4, 5]
# first = 1, rest = [2, 3, 4, 5]

first, *middle, last = [1, 2, 3, 4, 5]
# first=1, middle=[2,3,4], last=5
```

**`enumerate()` — index + value together:**
```python
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(i, fruit)   # 0 apple, 1 banana, 2 cherry
```

**`zip()` — iterate two lists in parallel:**
```python
names = ["Soham", "Alice"]
scores = [95, 88]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

**Membership check on sorted list:** `in` is O(n). If you're checking membership repeatedly on a large list — convert to a `set` first (O(1) lookup).

```python
big_list = list(range(100000))
big_set = set(big_list)

99999 in big_list   # O(n) — slow
99999 in big_set    # O(1) — instant
```

---

## QUICK REFERENCE CHEATSHEET

```
FUNCTIONS
─────────────────────────────────────────────────
def name(pos, default=val, *args, **kwargs)
return a, b          → tuple
global x             → modify global inside function
nonlocal x           → modify enclosing scope
lambda x: expression → one-liner, no return keyword

LISTS
─────────────────────────────────────────────────
lst[i]               → access       O(1)
lst.append(x)        → add end      O(1)
lst.insert(i, x)     → add middle   O(n)
lst.pop(i)           → remove       O(n)
lst[a:b:step]        → slice        new list
[expr for x in lst if cond]  → comprehension
b = a.copy()         → actual copy (not b=a)
first, *rest = lst   → unpacking
```

---

*Log: Functions + Lists theory loaded — Aug 18, 2026. Questions session follows.*