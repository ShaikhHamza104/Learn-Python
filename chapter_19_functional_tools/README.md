# 📚 Topic: Functional Tools

Python treats functions as first-class citizens, meaning they can be passed as arguments, assigned to variables, returned from other functions, and nested inside one another. This foundational behavior unlocks powerful programming paradigms including **namespaces & variable scope (the LEGB rule)**, **closures**, **custom decorators**, and standard library utilities from `functools` such as `@lru_cache`, `partial()`, `reduce()`, and `@wraps`.

---

## 📂 What's in this folder

| File | What it teaches |
| --- | --- |
| `01_decorators_basics.py` | First-class functions, manual wrapper functions, and syntactic sugar with `@decorator` |
| `02_decorators_with_args.py` | Passing variable arguments with `*args`, execution timers, and 3-tier decorator factories |
| `03_functools.py` | Standard library functional tools: `reduce()`, `partial()`, `@lru_cache` memoization, and `@wraps` |
| `04_namespace.py` | Namespaces, the LEGB scope lookup order, variable shadowing, `global`, and `nonlocal` |
| `05_closure.py` | Function closures, enclosing scope memory retention, stateful factory functions, and counter patterns |

---

## 💡 Key points

1. **First-Class Functions (`01_decorators_basics.py`)**: Python functions can be passed into other functions as arguments (e.g., `modify(square, 2)`) and returned as values, enabling higher-order functional patterns.
2. **Decorator Mechanics & `@` Syntax (`01_decorators_basics.py`)**: A decorator is a higher-order function that takes a target function, wraps it with pre/post execution behavior, and returns the wrapper. Prepending `@my_decorator` above a function definition provides syntactic sugar for `hello = my_decorator(hello)`.
3. **Accepting Arguments via `*args` (`02_decorators_with_args.py`)**: Wrapping decorated functions with `def wrapper(*args):` enables decorators to work transparently on functions with any number of positional parameters.
4. **Decorator Factories (`02_decorators_with_args.py`)**: To write a decorator that accepts configuration arguments (e.g. `@sanity_check(int)`), construct three nested function tiers: the outermost factory receiving configuration, the middle decorator receiving the function, and the innermost wrapper receiving the arguments.
5. **Functional Utilities with `functools` (`03_functools.py`)**:
   - `reduce(func, iterable)` folds an entire sequence into a single cumulative value.
   - `partial(func, **kwargs)` freezes selected function arguments, producing a specialized callable.
   - `@lru_cache(maxsize=None)` memoizes return values for repeated expensive function calls.
   - `@wraps(func)` preserves original function docstrings and `__name__` metadata that would otherwise be masked by wrapper functions.
6. **The LEGB Scope Lookup Rule (`04_namespace.py`)**: Python resolves identifiers by checking scopes in strict order: **L**ocal -> **E**nclosing -> **G**lobal -> **B**uilt-in. If an identifier is not found across all four tiers, Python raises `NameError`.
7. **Modifying Scope Variables with `global` and `nonlocal` (`04_namespace.py`)**: Modifying an identifier defined outside the local scope requires explicit declaration: `global var` targets the module-level namespace, while `nonlocal var` targets the immediate enclosing function's namespace.
8. **Closures Retaining Enclosing State (`05_closure.py`)**: A closure is a nested function that retains access to variables from its parent's enclosing scope even after the parent function has completed execution. Decorators function as closures because wrapper functions capture references to `func`.

---

## 🧠 Beginner tip

Whenever you write a custom decorator, always decorate your inner wrapper with `@wraps(func)` from `functools`. Without `@wraps(func)`, the decorated function's `__name__` becomes `"wrapper"` and its docstring is overwritten. This quietly breaks debugging traces, auto-generated documentation, and unit-testing assertions that inspect function metadata.

---

## 📊 Where this is used in Data Science

- **Function Profiling & Execution Benchmarks**: Data engineering workflows use `@timer` decorators to profile data transformation steps, database queries, and feature extraction functions across large datasets without cluttering business logic.
- **Memoization of Expensive Calculations**: `@lru_cache` caches expensive deterministic functions such as hyperparameter evaluations, distance matrices, token embeddings, or API calls, eliminating redundant computations across iterations.
- **Partial Application for Parallel Mappers**: When using multiprocessing pools (`multiprocessing.Pool.map`), `functools.partial()` pre-binds static configuration parameters (e.g., model weights, lookup tables) so workers accept single-argument iterables.

---

## 🛠️ Code Examples

### Execution Timer Decorator with `@wraps`
```python
import time
from functools import wraps

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        print(f"[{func.__name__}] executed in {duration:.4f}s")
        return result
    return wrapper

@timing_decorator
def compute_sum(n):
    """Calculates the sum of first n integers."""
    return sum(range(n))

compute_sum(1_000_000)
```

### Memoization with `@lru_cache`
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(50))  # Evaluates near-instantaneously thanks to caching
```

### Function Closure for Multipliers
```python
def make_multiplier(factor):
    # Enclosing scope retains 'factor'
    def multiply(x):
        return x * factor
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print("Double 10:", double(10))  # 20
print("Triple 10:", triple(10))  # 30
```

---

## 🏋️ Practice Exercises

Apply decorators, closures, and functional utilities across hands-on practice problems in **[chapter_19_functional_tools_exercises/](../chapter_19_functional_tools_exercises/README.md)**!

---

## ⏭️ What's Next

Learn how to fetch data from web APIs, parse JSON responses, and work with external data sources in **[Chapter 20 — APIs & Data Handling](../chapter_20_apis_and_data/README.md)**!
