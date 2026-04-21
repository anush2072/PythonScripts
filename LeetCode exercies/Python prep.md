
# Python Interview Preparation

## Q: How Python Handles Memory Management?

**A:** Python manages memory automatically primarily using reference counting and a supplementary generational garbage collector. The memory is managed within a private heap, and developers typically do not need to manually allocate or deallocate memory.

- **Private Heap**: All Python objects and data structures are stored in a private heap, the management of which is handled internally by the Python memory manager.
- **Reference Counting**: Every object has a counter that tracks the number of references (variables, list entries, etc.) pointing to it. When the count drops to zero, the object is immediately deallocated, and the memory is reclaimed by the interpreter for reuse.
- **Garbage Collector**: Runs automatically when the number of object allocations exceeds the number of deallocations by a certain threshold.
- **Cyclic References**: The primary role of the garbage collector (accessible via the `gc` module) is to deal with cyclic references.

## Q: Mutable and Immutable Data Types (e.g., list vs. tuple)

**A:** Mutable objects, such as lists, can be modified in-place, while immutable objects, such as tuples, cannot.

### Mutable Types:
- `dict`
- `list`
- `set`
- `byteArray`

### Immutable Types:
- `int`
- `float`
- `str`
- `tuple`
- `bool`
- `frozenset`

**Key Points:**
- Immutable types cannot be changed after creation. Any "modification" actually creates a brand-new object.
- **Example**: Strings (`str`) - Operations like `upper()` or concatenation always return a new string.
- **Hashability**: Only immutable types (like `str`, `int`, and `frozenset`) are generally "hashable," meaning they can be used as keys in a dictionary.

## Q: What is the difference between a shallow copy and a deep copy in Python?

**A:** A shallow copy creates a new object but references the same objects as the original.
<br/> A deep copy creates a new object and recursively copies all objects, ensuring complete independence.

## Q: What is the Global Interpreter Lock (GIL) in Python, and why is it important?

**A:** The Global Interpreter Lock (GIL) is a mutex that protects access to Python objects, preventing multiple native threads from executing Python bytecodes at once. This lock is necessary because CPython's memory management is not thread-safe. The GIL is important for ensuring thread safety and preventing data corruption.

The threading library works very well despite the presence of the GIL. Python's threads are real threads — they are normal operating system threads running the Python interpreter. 
  - Concurrency is about dealing with multiple tasks at once (managing, switching between them). The GIL allows Python threads to be concurrent - they can take turns executing.
  - Parallelism is about executing multiple tasks simultaneously (truly at the same time). Due to the GIL, Python threads cannot run in parallel for CPU-bound work - only one thread executes Python bytecode at a time.

The GIL prevents parallel execution of Python threads but allows concurrent execution.

GIL can be a problem and make threading useless in programs that are CPU intensive while running pure Python code, such as a simple program that calculates Fibonacci sequences on different threads.

For true parallelism in Python, you need:
- multiprocessing (separate processes, each with own GIL)
- asyncio (single-threaded concurrency for I/O-bound work)

## Q: Python’s collections module

**A:** The collections module provides specialized container datatypes (e.g., `Counter`, `defaultdict`, `deque`) that offer optimized performance for common tasks.
- Counter is ideal for counting elements in an iterable, 
- defaultdict can initialize dictionary values without explicit checks.
- deque is an efficient double-ended queue implementation.

## Q: What are decorators in Python?

**A:** Decorators are a design pattern in Python that allow you to modify the behavior of a function or method. They are typically used to add functionality to existing code without modifying the code itself.

## Q: What are context managers in Python, and how are they implemented?

**A:** Context managers in Python are used to manage resources, ensuring that they are properly acquired and released. The most common use of context managers is the with statement.

## Q: Composition vs Inheritance

**A:**
- **Composition** is a design pattern where a class is composed of other classes to achieve a specific functionality. It is a more flexible and reusable approach, as it allows you to combine the functionality of multiple classes without inheriting their behavior.
- **Inheritance** is a design pattern where a class inherits the behavior and properties of another class. It is a more rigid approach, as it enforces a strict relationship between the classes.

---

# Q: Pandas dataframes

### pd.isnull()
identify missing values in the DataFrame by using the isnull() function

### pd.fillna() or dropna() or replace()
- **Drop** the entire row or the columns if it consists of missing values using `dropna()`
- **Replace** missing values with a constant String, Integer, or Float using the `replace()` function
- **Fill** the missing values using the `fillna()` method

**fillna() examples:**
```python
import pandas as pd
import numpy as np

# DataFrame with missing values
df = pd.DataFrame({'A': [1, np.nan, 3], 'B': [4, 5, np.nan]})
print(df)
# Output:      A    B
#         0  1.0  4.0
#         1  NaN  5.0
#         2  3.0  NaN

# Fill with specific value
df_filled = df.fillna(0)  # Replace NaN with 0
print(df_filled)
# Output:      A    B
#         0  1.0  4.0
#         1  0.0  5.0
#         2  3.0  0.0

# Fill with mean/median
df_mean = df.fillna(df.mean())  # Replace with column means
print(df_mean)
# Output:      A    B
#         0  1.0  4.0
#         1  2.0  5.0  (mean of A: (1+3)/2=2, mean of B: (4+5)/2=4.5)
#         2  3.0  4.5

# Forward fill (propagate last valid observation)
df_ffill = df.fillna(method='ffill')
print(df_ffill)
# Output:      A    B
#         0  1.0  4.0
#         1  1.0  5.0  (A: 1.0 from above, B: 5.0 from same row)
#         2  3.0  5.0  (B: 5.0 from above)

# Backward fill (use next valid observation)
df_bfill = df.fillna(method='bfill')
print(df_bfill)
# Output:      A    B
#         0  1.0  4.0
#         1  3.0  5.0  (A: 3.0 from below, B: 5.0 from same row)
#         2  3.0  NaN  (B: no value below, stays NaN)
```


### difference between merge, join, and concatenate
**A:** 
- **Merge**: Combines DataFrames based on common columns or indices (similar to SQL JOINs). Use `pd.merge()` for database-style joins.
- **Join**: Combines DataFrames based on their indices. Use `df.join()` for index-based operations.
- **Concatenate**: Stacks DataFrames vertically or horizontally. Use `pd.concat()` for appending/combining along axes.

**Examples:**
```python
import pandas as pd

# Merge example
df1 = pd.DataFrame({'id': [1, 2], 'name': ['Alice', 'Bob']})
df2 = pd.DataFrame({'id': [1, 2], 'age': [25, 30]})
merged = pd.merge(df1, df2, on='id')  # Combines on 'id' column
# Output:   id   name  age
#         0   1  Alice   25
#         1   2    Bob   30

# Join example  
df3 = pd.DataFrame({'salary': [50000, 60000]}, index=[1, 2])
joined = df1.set_index('id').join(df3)  # Combines on index
# Output:      name  salary
#         id               
#         1   Alice   50000
#         2     Bob   60000

# Concatenate example
concatenated = pd.concat([df1, df2], axis=1)  # Stacks horizontally
# Output:   id   name  id   age
#         0   1  Alice   1    25
#         1   2    Bob   2    30
```

**Key Differences:**
- **Merge** = SQL-style joins on **columns** (more flexible, can join on any columns)
- **Join** = Index-based combination (only works on DataFrame indices)
- **Concatenate** = Simple stacking operation

**When to use:**
- Use **merge()** when joining on specific columns (most common)
- Use **join()** when DataFrames already have meaningful indices
- Use **concat()** for simple stacking without matching keys

**Key distinction:** `merge()` can join on any columns you specify, while `join()` only works on indices. `merge()` is more versatile and commonly used.
