# Python — Functions & Lists
### Deep Theory Reference | Soham's Mentorship Log

---

## PART 1 — FUNCTIONS

---

### 1.1 What Actually Happens When You Call a Function

When Python hits a function call, it does three things under the hood:

1. **Creates a new stack frame** — a fresh isolated memory space
2. **Binds arguments to parameter names** inside that frame
3. **Executes**, then **destroys the frame** when it hits `return` or the end

This is why variables inside a function don't leak out. They don't exist after the frame is gone.

```python
def add(a, b):
    result = a + b   # 'result' lives only inside this frame
    return result

x = add(3, 4)        # frame created → executed → destroyed
# 'result' doesn't exist here
```

---

### 1.2 The Four Types of Arguments

```python
# 1. Positional — order matters
def greet(name, age):
    print(f"{name} is {age}")

greet("Soham", 20)   # ✅
greet(20, "Soham")   # ❌ wrong order = wrong output


# 2. Keyword — order doesn't matter
greet(age=20, name="Soham")   # ✅ explicitly named


# 3. Default — fallback if not provided
def greet(name, age=18):
    print(f"{name} is {age}")

greet("Soham")        # uses age=18
greet("Soham", 20)    # overrides to 20


# 4. *args — variable number of positional args (tuple inside)
def total(*nums):
    print(nums)        # it's a tuple: (1, 2, 3)
    return sum(nums)

total(1, 2, 3, 4)     # works for any count


# 5. **kwargs — variable keyword args (dict inside)
def profile(**info):
    print(info)        # {'name': 'Soham', 'age': 20}

profile(name="Soham", age=20)
```

**Rule:** Order in function signature must always be:
`positional → default → *args → **kwargs`

---

### 1.3 Return Values

```python
# Return nothing → returns None implicitly
def greet(name):
    print(f"Hello {name}")   # no return

x = greet("Soham")
print(x)   # None


# Return multiple values → actually returns a TUPLE
def stats(nums):
    return min(nums), max(nums), sum(nums)

lo, hi, total = stats([3, 1, 4, 1, 5])   # tuple unpacking
```

---

### 1.4 Scope — LEGB Rule

Python resolves variable names in this exact order:

```
L — Local       (inside the current function)
E — Enclosing   (outer function if nested)
G — Global      (module level)
B — Built-in    (len, print, range...)
```

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)   # local → "local"

    inner()
    print(x)       # enclosing → "enclosing"

outer()
print(x)           # global → "global"
```

**The `global` keyword** — lets you modify a global variable from inside a function:
```python
count = 0

def increment():
    global count
    count += 1   # without 'global' this crashes with UnboundLocalError

increment()
print(count)   # 1
```

**The `nonlocal` keyword** — same but for enclosing (not global) scope:
```python
def outer():
    x = 0
    def inner():
        nonlocal x
        x += 1
    inner()
    print(x)   # 1
```

---

### 1.5 Lambda Functions

One-liner anonymous functions. No `return` keyword — the expression IS the return value.

```python
# Regular
def square(x):
    return x ** 2

# Lambda equivalent
square = lambda x: x ** 2

# Most common real use — sorting with a custom key
names = ["Soham", "Alice", "Bob"]
names.sort(key=lambda name: len(name))   # sort by length
print(names)   # ['Bob', 'Alice', 'Soham']
```

---

### 1.6 Niche Things Most People Don't Know

**Function is an object** — you can pass it around like a variable:
```python
def apply(func, value):
    return func(value)

apply(len, "Soham")    # 5
apply(str.upper, "hi") # won't work this way — but apply(lambda s: s.upper(), "hi") works
```

**`*` to force keyword-only arguments:**
```python
def connect(host, *, port, timeout=30):   # port MUST be keyword
    pass

connect("localhost", port=8080)           # ✅
connect("localhost", 8080)                # ❌ TypeError
```

**Docstrings — accessed via `.__doc__`:**
```python
def add(a, b):
    """Returns the sum of a and b."""
    return a + b

print(add.__doc__)   # Returns the sum of a and b.
```

---

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