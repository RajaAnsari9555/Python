# Python Basics – README

This guide covers fundamental Python concepts: **Lists, Dictionaries, Sets, Tuples, Functions, Loops, and Conditional Statements** with simple explanations and examples.

---

## 📌 1. List

A **list** is an ordered, mutable collection of items.

### Key Features:

* Allows duplicate values
* Can store multiple data types
* Mutable (can be changed)

### Example:

```python
numbers = [1, 2, 3, 4]
numbers.append(5)
print(numbers)  # [1, 2, 3, 4, 5]
```

---

## 📌 2. Dictionary

A **dictionary** stores data in key-value pairs.

### Key Features:

* Keys must be unique
* Fast lookup
* Mutable

### Example:

```python
student = {
    "name": "Raja",
    "age": 21
}

print(student["name"])  # Raja
```

---

## 📌 3. Set

A **set** is an unordered collection of unique elements.

### Key Features:

* No duplicate values
* Unordered
* Useful for mathematical operations

### Example:

```python
nums = {1, 2, 3, 3}
print(nums)  # {1, 2, 3}
```

---

## 📌 4. Tuple

A **tuple** is an ordered, immutable collection.

### Key Features:

* Cannot be changed after creation
* Faster than lists

### Example:

```python
point = (10, 20)
print(point[0])  # 10
```

---

## 📌 5. Functions

A **function** is a reusable block of code.

### Key Features:

* Improves code reusability
* Makes code cleaner

### Example:

```python
def greet(name):
    return f"Hello {name}"

print(greet("Raja"))
```

---

## 📌 6. Loops

Loops are used to repeat a block of code.

### Types:

#### 🔹 For Loop

Used to iterate over sequences.

```python
for i in range(5):
    print(i)
```

#### 🔹 While Loop

Runs while a condition is true.

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

---

## 📌 7. Conditional Statements

Used to make decisions in code.

### Types:

* if
* if-else
* if-elif-else

### Example:

```python
age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

## 🎯 Summary

* **List** → Ordered & mutable
* **Dictionary** → Key-value pairs
* **Set** → Unique values only
* **Tuple** → Ordered & immutable
* **Function** → Reusable code block
* **Loops** → Repeat tasks
* **Conditionals** → Decision making

---

## 🚀 Keep Learning!

Practice these basics regularly to build a strong Python foundation.
