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

