# PART 3 — DICTIONARIES, SETS & TUPLES

---

## DICTIONARIES

### 3.1 What a Dictionary Actually Is in Memory

A dict is a **hash table**: each key is hashed to find its storage bucket directly, instead of being scanned for.

- Average O(1) lookup/insert/delete — that's the entire point of a dict over a list
- Since Python 3.7, **insertion order is preserved** — this is a language guarantee, not an implementation detail
- Keys must be **hashable** (immutable): `str`, `int`, `float`, `tuple` (of immutables) — never `list`, `dict`, or `set`
- Values can be anything, including other dicts/lists

```python
student = {"name": "Soham", "sem": 5, "gpa": 9.1}
```

### 3.2 Core Operations & Time Complexity

| Operation | Syntax | Time |
|---|---|---|
| Access | `d[key]` | O(1) avg |
| Insert / update | `d[key] = val` | O(1) avg |
| Delete | `del d[key]` | O(1) avg |
| Search by key | `key in d` | O(1) avg |
| Search by value | `val in d.values()` | O(n) |
| Length | `len(d)` | O(1) |

> Worst case is O(n) on heavy hash collisions, but this is rare enough to ignore in practice.

### 3.3 Creating & Core Methods

```python
d = {"name": "Soham", "sem": 5}
d2 = dict(name="Soham", sem=5)
d3 = dict([("a", 1), ("b", 2)])

d.get("name")             # "Soham"
d.get("gpa", "N/A")       # default if missing — no KeyError
d["gpa"]                  # KeyError if missing

d.keys()                  # dict_keys view
d.values()                # dict_values view
d.items()                 # dict_items view → (key, value) pairs

d.pop("sem")              # removes & returns the value
d.pop("x", None)          # safe pop, no error if missing
d.popitem()               # removes & returns the LAST inserted (key, value)
d.update({"gpa": 9.1})    # merge/overwrite existing keys
d.setdefault("city", "Pune")  # returns value if key exists, else sets it and returns default
```

### 3.4 Iterating

```python
for k in d:               # iterates keys by default
    ...
for k, v in d.items():    # keys + values together
    ...
```

### 3.5 Dict Comprehension

```python
squares = {i: i**2 for i in range(5)}
evens   = {i: i**2 for i in range(10) if i % 2 == 0}
inverted = {v: k for k, v in d.items()}   # swap keys and values
```

### 3.6 Niche Things Most People Don't Know

**Merging dicts (3.9+):**
```python
merged = d1 | d2     # d2's keys win on conflict
d1 |= d2             # in-place merge
merged = {**d1, **d2}  # pre-3.9 compatible version of the same thing
```

**`collections.defaultdict`** — auto-creates a missing key with a default factory, killing the "check if key exists first" boilerplate:
```python
from collections import defaultdict
counts = defaultdict(int)
for word in ["a", "b", "a"]:
    counts[word] += 1   # no KeyError, no manual check
```

**`collections.Counter`** — a dict subclass built for frequency counting:
```python
from collections import Counter
c = Counter(["a", "b", "a", "c", "a"])
c.most_common(2)   # [('a', 3), ('b', 1)]
```

**`zip()` into a dict:**
```python
d = dict(zip(["name", "sem"], ["Soham", 5]))
```

**Dict as a switch/case replacement** (cleaner than long if-elif chains):
```python
ops = {"add": lambda a, b: a + b, "sub": lambda a, b: a - b}
ops.get(cmd, lambda a, b: None)(3, 4)
```

**Nested dicts** are Python's native JSON-like structure (`d["a"]["b"]`) — but chained `.get()` on a missing intermediate key still throws, so guard each level if the structure isn't guaranteed.

---

## SETS

### 4.1 What a Set Actually Is in Memory

A set is a hash table that stores **only keys, no values** — think of it as a dict with the values stripped out.

- Unordered, no duplicate elements, elements must be hashable
- `{}` creates an **empty dict**, not an empty set — use `set()` for an empty set

### 4.2 Core Operations & Time Complexity

| Operation | Syntax | Time |
|---|---|---|
| Add | `s.add(x)` | O(1) avg |
| Remove | `s.remove(x)` | O(1) avg |
| Membership | `x in s` | O(1) avg |
| Union | `s1 \| s2` | O(len(s1)+len(s2)) |
| Intersection | `s1 & s2` | O(min(len(s1),len(s2))) |

### 4.3 Creating & Methods

```python
s = {1, 2, 3}
s2 = set([1, 2, 2, 3])    # dedups automatically → {1, 2, 3}
empty = set()              # NOT {}

s.add(4)
s.remove(2)      # KeyError if 2 isn't in s
s.discard(2)     # no error even if missing — safer than remove
s.pop()          # removes & returns an arbitrary element
s.clear()
```

### 4.4 Set Algebra — the actual reason sets exist

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b   # union             {1, 2, 3, 4, 5, 6}
a & b   # intersection      {3, 4}
a - b   # difference        {1, 2}         (in a, not in b)
b - a   # difference        {5, 6}
a ^ b   # symmetric diff    {1, 2, 5, 6}   (in one but not both)

a.issubset(b)     # is a fully inside b?
a.issuperset(b)   # does a fully contain b?
a.isdisjoint(b)   # no elements in common?
```

### 4.5 Set Comprehension

```python
evens = {i for i in range(20) if i % 2 == 0}
```

### 4.6 Niche Things Most People Don't Know

**`frozenset`** — an immutable, hashable set. Regular sets can't nest inside other sets or be dict keys (they're unhashable); frozensets can:
```python
fs = frozenset([1, 2, 3])
d = {fs: "a group of numbers"}   # valid
```

**Sets can't hold mutable/unhashable items** — no lists, dicts, or other sets inside a set. Use tuples or frozensets instead.

**Order-preserving dedup** — `list(set(x))` dedups but scrambles order. To dedup and keep order, use a dict (insertion-ordered since 3.7):
```python
deduped_ordered = list(dict.fromkeys(my_list))
```

**Always reach for a set over a list when repeatedly checking `x in collection`** on anything non-trivially sized — it's the single biggest easy performance win in everyday scripts.

---

## TUPLES

### 5.1 What a Tuple Actually Is in Memory

An immutable, ordered sequence. Once created, elements can't be added, removed, or reassigned.

- Being immutable makes it **hashable** — usable as a dict key or set element, unlike a list
- Slightly faster and smaller in memory than an equivalent list (no over-allocation for future growth)

### 5.2 Core Operations & Time Complexity

| Operation | Syntax | Time |
|---|---|---|
| Access | `t[i]` | O(1) |
| Slice | `t[a:b]` | O(b-a) |
| Search | `x in t` | O(n) |
| Concatenate | `t1 + t2` | O(n+m), new tuple |

No `append`/`insert`/`remove`/`pop` — tuples support zero in-place mutation methods.

### 5.3 Creating & The Comma Gotcha

```python
t = (1, 2, 3)
t2 = 1, 2, 3          # parentheses are optional
single = (1,)         # comma is REQUIRED — (1) is just the int 1
empty = ()
```

### 5.4 Packing & Unpacking

```python
point = (3, 4)
x, y = point                  # unpacking

a, b = 1, 2
a, b = b, a                   # classic swap — packing/unpacking under the hood

first, *rest = (1, 2, 3, 4)   # first=1, rest=[2, 3, 4]  (rest becomes a list)
```

### 5.5 Methods (there are only two)

```python
t = (1, 2, 2, 3)
t.count(2)     # 2
t.index(3)     # 2
```

### 5.6 Niche Things Most People Don't Know

**Tuples as dict keys** — the #1 real-world reason to reach for a tuple: composite/coordinate keys.
```python
grid = {}
grid[(0, 0)] = "origin"
grid[(1, 2)] = "point"
```

**`collections.namedtuple`** — a tuple with named fields: still immutable, still lightweight, but readable by name instead of index.
```python
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
p.x, p.y          # 3, 4  — instead of p[0], p[1]
```

**A tuple is only immutable at the top level.** If it holds a mutable object, that inner object can still change:
```python
t = ([1, 2], 3)
t[0].append(99)   # legal — the tuple's slot still points to the same list, the list itself changed
```

**"Returning multiple values" is really returning one tuple** that gets unpacked at the call site — that's why `return a, b` works at all.

---

## QUICK REFERENCE CHEATSHEET

```
DICTIONARIES
─────────────────────────────────────────────────
d[key]                  → access          O(1) avg
d[key] = val             → insert/update   O(1) avg
d.get(key, default)      → safe access
d.pop(key)                → remove & return
{k: v for k in ...}       → comprehension
d1 | d2                    → merge (3.9+)
defaultdict / Counter       → collections helpers

SETS
─────────────────────────────────────────────────
s.add(x) / s.remove(x)    → O(1) avg
x in s                     → O(1) avg
a|b  a&b  a-b  a^b          → union / intersect / diff / symdiff
frozenset(s)                 → immutable, hashable set
{i for i in ...}              → comprehension

TUPLES
─────────────────────────────────────────────────
t[i]                        → access   O(1)
t = (1,)                     → single-element (comma required)
a, b = b, a                   → swap via unpacking
namedtuple("N", [...])         → tuple with named fields
d[(x, y)] = val                 → tuple as dict key (hashable)
```

---

*Log: Dictionaries + Sets + Tuples theory loaded — Aug 19, 2026.*