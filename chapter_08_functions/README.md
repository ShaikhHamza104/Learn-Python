# 📚 Topic: Functions

Functions are modular, reusable blocks of code designed to perform specific operations, eliminate duplication, and structure application logic. This chapter covers function definitions (`def`), argument passing (positional, keyword, and default), capturing return values, handling arbitrary arguments (`*args`, `**kwargs`), recursive function design, inline anonymous lambda expressions, and modern type annotations.

## 📂 What's in this folder

| File | What it teaches |
|---|---|
| `01_intro_function.py` | Declaring a basic function (`def avg()`) and calling it multiple times to avoid duplicating code. |
| `02_quick_quiz.py` | Greeting function demonstrating user input collection inside a function body. |
| `03_function_with_arg.py` | Passing parameters into a function (`def goodDay(name)`) and calling it with arguments. |
| `04_return.py` | Returning computed values back to the calling scope using the `return` statement. |
| `05_keyword_arg.py` | Invoking functions with explicit parameter names via keyword arguments (`sum(a=10, b=20, ...)`). |
| `06_positional_arg.py` | Passing arguments by position where parameter assignment is determined strictly by order. |
| `07_variable_len_arg.py` | Accepting flexible argument lists with `*args` (positional tuple) and `**kwargs` (keyword dictionary). |
| `08_recursion.py` | Factorial calculation using recursion, demonstrating base cases (`n == 0 or n == 1`) and recursive self-calls. |
| `09_lambda_fun.py` | Defining single-expression anonymous functions using `lambda` for mathematical transformations like square and cube. |
| `10_type_hints.py` | In-depth reference for type annotations: built-in types, PEP 585/604 union types (`|`), generics, and Protocols. |

## 💡 Key points

1. **Return vs. Print**: `print()` outputs text to the terminal; `return` sends a value back to the caller so it can be assigned to variables and used in further logic.
2. **Positional vs. Keyword Arguments**: Positional arguments bind strictly in sequential order, while keyword arguments specify parameter names directly and can be passed in any order.
3. **Variable-Length Arguments**: `*args` collects extra positional arguments into a tuple, while `**kwargs` collects extra named arguments into a dictionary.
4. **Base Case in Recursion**: Every recursive function must define a base case; without one, the function will execute indefinitely until raising a `RecursionError`.
5. **Type Annotations**: Type hints (`def func(x: int) -> int:`) document expected input and return types for IDE autocompletion and static analysis without altering runtime execution.

## 🧠 Beginner tip

Don't confuse `return` with `print()`! If your function only calls `print()`, its return value is actually `None`. To store or reuse a function's output in another calculation (e.g., `total = compute(data)`), make sure the function ends with an explicit `return` statement.

## 📊 Where this is used in Data Science

Functions are essential for creating repeatable data preprocessing pipelines, custom aggregations, and model evaluation metrics. Lambda functions are routinely passed into Pandas methods (`df['col'].apply(lambda x: ...)`) for quick column operations, and type annotations are standard practice in machine learning libraries to ensure robust data contracts across complex pipelines.

## 🛠️ Code Examples

### Positional Arguments & Return Value (`06_positional_arg.py`)
```python
def add(a, b):
    return a + b

result = add(5, 3)  # a=5, b=3 -> returns 8
print(result)
```

### Arbitrary Arguments with *args and **kwargs (`07_variable_len_arg.py`)
```python
def add(*args):
    return sum(args)

print(add(1, 2, 3, 4))  # args is (1, 2, 3, 4) -> returns 10

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Alice", age=30, city="New York")
```

### Recursion (`08_recursion.py`)
```python
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

### Lambda Functions (`09_lambda_fun.py`)
```python
square = lambda x: x * x
cube = lambda x: x * x * x
print(square(4), cube(3))  # 16, 27
```

## 🏋️ Practice Exercises

Sharpen your function design skills with the exercises in the practice folder:
- [Chapter 08 Exercises](../chapter_08_functions_exercises/README.md)

## ⏭️ What's Next

- [Chapter 09 - File Handling](../chapter_09_file_handling/README.md)
