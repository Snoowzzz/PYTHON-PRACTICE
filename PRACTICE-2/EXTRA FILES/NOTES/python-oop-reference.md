# Python OOP — Reference Guide

---

## 1. What OOP Actually Is

Everything you've written so far: functions that take data, do something, return data. Data and behavior live separately.

OOP bundles them: a **class** is a blueprint that packages data (attributes) with the functions that act on that data (methods) into one unit.

```python
# Functional style (what you've been doing)
def get_area(width, height):
    return width * height

# OOP style
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
```

Same logic. Different packaging. The payoff shows up when you have many related pieces of data + behavior that need to travel together (a `Student`, a `BankAccount`, an `EC2Instance`) instead of passing five loose variables between ten functions.

---

## 2. Class vs Object

| Term | What it is | Analogy |
|---|---|---|
| **Class** | The blueprint/template | The `dict` type itself |
| **Object (instance)** | One concrete thing built from the blueprint | An actual `{"a": 1}` |

```python
class Dog:
    pass

d1 = Dog()   # object 1
d2 = Dog()   # object 2 — separate from d1
```

Every list, string, and dict you've used is already an object of a class (`list`, `str`, `dict`). You've been *using* OOP the whole time — now you're building the classes.

---

## 3. `__init__` and `self`

`__init__` runs automatically the moment an object is created. It sets up the object's starting attributes.

`self` = "this specific object." It's how a method refers to *its own* data, not some other instance's.

```python
class Student:
    def __init__(self, name, age):
        self.name = name   # attach to THIS object
        self.age = age

s1 = Student("Soham", 21)
s2 = Student("Riya", 22)

print(s1.name)  # Soham — s1's own copy
print(s2.name)  # Riya  — s2's own copy, unaffected by s1
```

`self` is always the first parameter of any instance method — Python passes it automatically. You never call `init` or `self` directly; `Student("Soham", 21)` does that for you.

---

## 4. Instance Attributes vs Class Attributes

| Type | Defined | Shared across objects? | Access |
|---|---|---|---|
| Instance attribute | Inside `__init__` via `self.x = ...` | No — each object has its own | `self.x` |
| Class attribute | Directly under the class, outside any method | Yes — one copy for all objects | `self.x` or `ClassName.x` |

```python
class Dog:
    species = "Canine"          # class attribute — same for every Dog

    def __init__(self, name, breed):
        self.name = name        # instance attribute — unique per Dog
        self.breed = breed

d1 = Dog("Tommy", "Labrador")
print(d1.species)   # Canine — inherited from the class
print(Dog.species)  # Canine — accessed via the class directly
```

Use class attributes for constants/defaults shared by every instance (a species, a bank's interest rate). Use instance attributes for anything that varies per object.

---

## 5. Instance Methods

Functions defined inside a class that operate on `self`'s data.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def scale(self, factor):
        self.width *= factor     # mutates the object's own state
        self.height *= factor
```

Note `scale()` doesn't `return` — it directly changes `self`'s attributes. This is the core OOP move: methods can mutate the object they belong to, no need to pass data back and forth.

---

## 6. Dunder Methods — `__str__`

Dunder ("double underscore") methods let your object plug into Python's built-in behavior. The one you'll use immediately:

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

b = Book("Dune", "Frank Herbert")
print(b)   # Dune by Frank Herbert  ← without __str__, this prints <Book object at 0x...>
```

`__str__` defines what `print(object)` shows. Every class you write from now on should probably have one — it's the difference between debuggable output and a memory address.

---

## 7. Encapsulation Conventions

Python has no real "private" keyword — it's convention-based (unlike Java's `private`).

| Prefix | Meaning | Enforced? |
|---|---|---|
| `self.name` | Public — access freely | — |
| `self._name` | "Protected" — internal use, please don't touch from outside | Convention only |
| `self.__name` | "Private" — name-mangled to `_ClassName__name` | Discourages, doesn't block |

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # discourage direct access

    def get_balance(self):
        return self.__balance
```

You'll mostly see single-underscore in real code. Double-underscore mangling matters more for interviews than daily use — know it exists, don't overuse it.

---

## 8. Inheritance Basics

A class can inherit attributes/methods from another, then add or override its own.

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):              # Dog inherits from Animal
    def speak(self):            # overrides Animal's version
        return f"{self.name} barks."

class Cat(Animal):
    pass                        # no override — uses Animal's speak()

print(Dog("Tommy").speak())  # Tommy barks.
print(Cat("Whiskers").speak())  # Whiskers makes a sound.
```

`super()` calls the parent's version when you want to extend, not replace, it:

```python
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # let Animal set self.name
        self.breed = breed       # Dog adds its own attribute
```

This is later-phase material (per the pending list) — noted here for completeness, not in this batch's practice set.

---

## 9. `classmethod` and `staticmethod` (brief)

| Decorator | First param | Use case |
|---|---|---|
| (normal method) | `self` | Needs access to a specific object's data |
| `@classmethod` | `cls` | Needs access to the class itself (e.g. alternate constructors) |
| `@staticmethod` | none | Utility function that logically belongs in the class but touches no instance/class data |

```python
class Circle:
    pi = 3.14159

    @staticmethod
    def is_valid_radius(r):
        return r > 0
```

Low-priority for now — you'll meet these naturally once you're writing more classes.

---

## Quick Syntax Reference

```python
class ClassName:
    class_attr = "shared"              # class attribute

    def __init__(self, x):
        self.x = x                     # instance attribute

    def method(self):                  # instance method
        return self.x

    def __str__(self):                 # controls print(obj)
        return f"ClassName({self.x})"

obj = ClassName(5)      # creates object, runs __init__
obj.method()             # call a method
obj.x                    # access attribute directly
ClassName.class_attr     # access class attribute via the class
```

---

*Reference file — Phase: OOP intro | Generated 24-08-2026*
# Operator Overloading (Dunder Methods)

# What it is: Python's built-in types (int, str, list) all support
# ==, <, +, len() because they implement special methods under the 
# hood — __eq__, __lt__, __add__, __len__. You can implement the
# same methods on your own classes, and suddenly your custom 
# objects work with those same operators.

# python
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

# p1 = Point(2, 3)
# p2 = Point(2, 3)
# print(p1 == p2)   # True — without __eq__, this would 
# be False (compares identity, not values)

# Why it exists — the actual problem: Without __eq__, == on 
# two objects checks whether they're the same object in memory,
# not whether they hold the same data. p1 == p2 above would 
# be False by default even though both points are (2, 3) — 
# because Python has no idea what "equal" should mean for your
# Point class unless you tell it.

# Where this actually matters:

# __eq__ / __lt__ — the moment you try sorted(list_of_my_objects) or 
# check obj in my_list, Python needs to know how to compare your objects.
# Without these, sorted() on a list of custom objects just crashes 
# (TypeError: '<' not supported).

# __add__ — domain objects that should combine, like 
# Money(50) + Money(30), or Vector(1,2) + Vector(3,4) in any 
# physics/graphics/ML code. Without it, + raises TypeError.

# __len__ — lets len(my_object) work naturally, e.g. len(cart) for
# a shopping cart's item count — reads far cleaner than 
# cart.get_item_count().

# __repr__ — the debugging twin of __str__. __str__ is 
# for humans (print(obj)); __repr__ is what shows up when you 
# inspect an object in a debugger, a REPL, or inside a 
# list/dict (print([obj1, obj2]) uses __repr__ on each element, 
# not __str__). Real convention: __repr__ should ideally 
# look like valid Python code that could recreate the object,
# e.g. Point(2, 3).

# This is exactly how libraries like NumPy, Pandas, and datetime 
# let you write df1 + df2 or date1 < date2 — none of that is special-cased by Python; it's all dunder methods on their classes,
# same mechanism you're about to write yourself.