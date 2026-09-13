# 🐍 Learn Python

[![Python Version](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Chapters](https://img.shields.io/badge/Chapters-23%20(00--22)-0052CC?style=flat)](#-chapters-index)
[![Lesson Scripts](https://img.shields.io/badge/Lesson%20Scripts-150%2B-2ea44f?style=flat)](#-chapter-summaries)
[![Exercises](https://img.shields.io/badge/Exercise%20Problems-108-orange?style=flat)](#-exercises--practice-index)
[![Projects](https://img.shields.io/badge/Mini%20Projects-22-purple?style=flat)](#️-projects)
[![Documentation](https://img.shields.io/badge/READMEs-Full%20Coverage-brightgreen?style=flat)](#-chapters-index)
[![Code Style](https://img.shields.io/badge/Code%20Style-PEP%208%20%2F%20Flake8-blueviolet?style=flat)](#-code-quality--standards)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat)](./LICENSE)

A structured, beginner-to-advanced roadmap to master modern Python. Every chapter features clear runnable code examples, comprehensive step-by-step documentation, dedicated hands-on exercise suites with full solutions, and practical mini-projects so you learn by **building**, not just reading.

> 💬 **New to programming?** Start with [chapter_00_setup/](./chapter_00_setup), configure your environment, and progress sequentially. Practice every exercise before advancing to the next chapter!
>
> 📖 **Full Documentation Coverage**: Every chapter lesson folder and exercise folder contains its own dedicated `README.md` complete with concept breakdowns, method tables, problem statements, expected outputs, and terminal execution commands.

---

## 📑 Table of Contents
- [🚀 Getting Started](#-getting-started)
- [📂 Repository Architecture](#-repository-architecture)
- [📚 Chapters Index](#-chapters-index)
- [📖 Chapter Summaries](#-chapter-summaries)
- [🎯 Exercises & Practice Index](#-exercises--practice-index)
- [🛠️ Projects](#️-projects)
- [🧪 Code Quality & Standards](#-code-quality--standards)
- [🤝 Contributing](#-contributing)
- [🔗 Resources](#-resources)
- [📜 License](#-license)

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.11+**: Download from [python.org](https://www.python.org/downloads/)
- **Code Editor**: [VS Code](https://code.visualstudio.com/) (recommended) or [PyCharm](https://www.jetbrains.com/pycharm/)

### Setup and First Run
```bash
# 1. Clone the repository
git clone https://github.com/ShaikhHamza104/Learn-Python.git
cd Learn-Python

# 2. Create a virtual environment
python -m venv .venv

# 3. Activate the virtual environment
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# Windows (cmd.exe):
.venv\Scripts\activate.bat
# macOS / Linux:
source .venv/bin/activate

# 4. Run your first lesson script
python chapter_01_basics/01_hello_world.py

# 5. Run your first exercise
python chapter_01_basics_exercises/problem1.py
```

> 💡 **First time setting up Python?** Check out [chapter_00_setup/](./chapter_00_setup) for deep dives into `venv`, the high-speed `uv` package manager, dependency freezing, and `.gitignore` setup.

---

## 📂 Repository Architecture

```text
Learn-Python/
│
├── chapter_00_setup/                 # Environment setup, venv, uv, gitignore
│
├── chapter_01_basics/ ... chapter_14_os_pathlib/  # Core Python foundations (Basics to OS)
├── chapter_01_basics_exercises/ ...              # 14 Dedicated exercise suites with complete solutions
│
├── chapter_15_regex/                 # Regular Expressions & pattern matching
├── chapter_15_exercises/             # Practical regex extraction exercises
│
├── chapter_16_collections/           # Specialized data structures (Counter, deque, etc.)
│
├── chapter_17_iterators_generators/  # Iterator protocol, yield, generator expressions
├── chapter_17_exercises/             # Custom iterators & lazy pipeline exercises
│
├── chapter_18_itertools/             # High-performance iterator algebra (16 methods)
│
├── chapter_19_functional_tools/      # Decorators, wraps, partial, lru_cache
├── chapter_19_exercises/             # Timing & validation decorator exercises
│
├── chapter_20_apis_and_data/         # HTTP requests, API consuming & JSON persistence
├── chapter_20_exercises/             # API data fetching & parsing exercises
│
├── chapter_21_capstone/              # Production-style capstone project template
│
├── chapter_22_pydantic/              # Data validation, type enforcement & schema modeling
├── chapter_22_exercises/             # Pydantic models, custom validators & dataset cleaning
│
└── projects/                         # 22 Standalone mini-projects and CLI games
```

---

## 📚 Chapters Index

Every chapter and exercise folder includes a dedicated, beginner-friendly `README.md` guide:

| # | Chapter / Topic | Lessons | Exercises | Docs |
|---|-----------------|:-------:|:---------:|:----:|
| **00** | [chapter_00_setup/](./chapter_00_setup) — Environment Setup & Tooling | 4 Guides | — | [README](./chapter_00_setup/README.md) |
| **01** | [chapter_01_basics/](./chapter_01_basics) — Basics & First Program | 3 Scripts | [chapter_01_basics_exercises/](./chapter_01_basics_exercises) (5 Problems) | [README](./chapter_01_basics/README.md) |
| **02** | [chapter_02_variables_datatypes/](./chapter_02_variables_datatypes) — Variables, Data Types & Operators | 7 Scripts | [chapter_02_variables_datatypes_exercises/](./chapter_02_variables_datatypes_exercises) (6 Problems) | [README](./chapter_02_variables_datatypes/README.md) |
| **03** | [chapter_03_strings/](./chapter_03_strings) — Strings & Slicing | 6 Scripts | [chapter_03_strings_exercises/](./chapter_03_strings_exercises) (5 Problems) | [README](./chapter_03_strings/README.md) |
| **04** | [chapter_04_lists_tuples/](./chapter_04_lists_tuples) — Lists, Tuples & NamedTuples | 10 Scripts | [chapter_04_lists_tuples_exercises/](./chapter_04_lists_tuples_exercises) (5 Problems) | [README](./chapter_04_lists_tuples/README.md) |
| **05** | [chapter_05_dicts_sets/](./chapter_05_dicts_sets) — Dictionaries, Sets & TypedDict | 9 Scripts | [chapter_05_dicts_sets_exercises/](./chapter_05_dicts_sets_exercises) (9 Problems) | [README](./chapter_05_dicts_sets/README.md) |
| **06** | [chapter_06_control_flow/](./chapter_06_control_flow) — Control Flow (`if`, `elif`, `else`) | 7 Scripts | [chapter_06_control_flow_exercises/](./chapter_06_control_flow_exercises) (7 Problems) | [README](./chapter_06_control_flow/README.md) |
| **07** | [chapter_07_loops/](./chapter_07_loops) — Loops (`for`, `while`, `range`) | 8 Scripts | [chapter_07_loops_exercises/](./chapter_07_loops_exercises) (10 Problems) | [README](./chapter_07_loops/README.md) |
| **08** | [chapter_08_functions/](./chapter_08_functions) — Functions, Scope & Recursion | 10 Scripts | [chapter_08_functions_exercises/](./chapter_08_functions_exercises) (8 Problems) | [README](./chapter_08_functions/README.md) |
| **09** | [chapter_09_file_handling/](./chapter_09_file_handling) — File Handling, CSV, JSON & Enums | 10 Scripts | [chapter_09_file_handling_exercises/](./chapter_09_file_handling_exercises) (11 Problems) | [README](./chapter_09_file_handling/README.md) |
| **10** | [chapter_10_oop/](./chapter_10_oop) — Object-Oriented Programming (OOP) | 13 Scripts | [chapter_10_oop_exercises/](./chapter_10_oop_exercises) (4 Problems) | [README](./chapter_10_oop/README.md) |
| **11** | [chapter_11_inheritance_polymorphism/](./chapter_11_inheritance_polymorphism) — Inheritance & Polymorphism | 11 Scripts | [chapter_11_inheritance_polymorphism_exercises/](./chapter_11_inheritance_polymorphism_exercises) (7 Problems) | [README](./chapter_11_inheritance_polymorphism/README.md) |
| **12** | [chapter_12_exception_handling/](./chapter_12_exception_handling) — Exception Handling & Logging | 12 Scripts | [chapter_12_exception_handling_exercises/](./chapter_12_exception_handling_exercises) (10 Problems) | [README](./chapter_12_exception_handling/README.md) |
| **13** | [chapter_13_modules_packages/](./chapter_13_modules_packages) — Modules, Packages & Imports | 6 Scripts | — | [README](./chapter_13_modules_packages/README.md) |
| **14** | [chapter_14_os_pathlib/](./chapter_14_os_pathlib) — OS Module & Pathlib Filesystem | 18 Scripts | [chapter_14_os_pathlib_exercises/](./chapter_14_os_pathlib_exercises) (5 Problems) | [README](./chapter_14_os_pathlib/README.md) |
| **15** | [chapter_15_regex/](./chapter_15_regex) — Regular Expressions | 3 Scripts | [chapter_15_exercises/](./chapter_15_exercises) (5 Problems) | [README](./chapter_15_regex/README.md) |
| **16** | [chapter_16_collections/](./chapter_16_collections) — Collections Module | 5 Scripts | — | [README](./chapter_16_collections/README.md) |
| **17** | [chapter_17_iterators_generators/](./chapter_17_iterators_generators) — Iterators & Generators | 3 Scripts | [chapter_17_exercises/](./chapter_17_exercises) (3 Problems) | [README](./chapter_17_iterators_generators/README.md) |
| **18** | [chapter_18_itertools/](./chapter_18_itertools) — Itertools Module | 16 Scripts | — | [README](./chapter_18_itertools/README.md) |
| **19** | [chapter_19_functional_tools/](./chapter_19_functional_tools) — Functional Tools & Decorators | 3 Scripts | [chapter_19_exercises/](./chapter_19_exercises) (3 Problems) | [README](./chapter_19_functional_tools/README.md) |
| **20** | [chapter_20_apis_and_data/](./chapter_20_apis_and_data) — APIs, Requests & JSON | 3 Scripts | [chapter_20_exercises/](./chapter_20_exercises) (2 Problems) | [README](./chapter_20_apis_and_data/README.md) |
| **21** | [chapter_21_capstone/](./chapter_21_capstone) — Capstone Project | 1 App | — | [README](./chapter_21_capstone/README.md) |
| **22** | [chapter_22_pydantic/](./chapter_22_pydantic) — Pydantic & Data Validation | 4 Scripts | [chapter_22_exercises/](./chapter_22_exercises) (3 Problems) | [README](./chapter_22_pydantic/README.md) |

---

## 📖 Chapter Summaries

### Chapter 00: Environment Setup 🛠️
Comprehensive setup guides for professional development workflows:
- `01_venv_create.md` — Creating, activating, and deactivating virtual environments across Windows, macOS, and Linux.
- `02_uv_package_manager.md` — Ultra-fast package management and dependency resolution using Astral's `uv`.
- `03_requirements_freeze.md` — Reproducible dependency pinning via `pip freeze` and `requirements.txt`.
- `04_gitignore.md` — Crafting clean `.gitignore` files to prevent committing caches, `.venv`, and temporary files.

### Chapter 01: Basics
- `01_hello_world.py` — Your first Python program, syntax rules, and terminal execution.
- `02_comment_example.py` — Single-line (`#`) and multi-line (`"""`) documentation practices.
- `02_module_example.py` — Installing and importing external third-party libraries (`pyjokes`).

### Chapter 02: Variables & Data Types
- `01_variable.py` — Creating variables and understanding memory references.
- `02_datatype.py` — Primitive types: integers, floats, strings, booleans, and `None`.
- `03_ruleofvariable.py` — Python identifier naming rules, snake_case convention, and reserved keywords.
- `04_operator.py` — Arithmetic, assignment, comparison, and logical operators.
- `05_type_function.py` — Inspecting runtime types using `type()`.
- `06_type_casting.py` — Implicit conversion and explicit casting (`int()`, `float()`, `str()`).
- `07_input.py` — Capturing and converting terminal user input via `input()`.

### Chapter 03: Strings
- `01_intro_string.py` — String creation, quotes, and immutability.
- `02_slicing.py` — Indexing and slice syntax: `[start:stop:step]`.
- `03_negative_slicing.py` — Reverse indexing and negative step slicing (`[::-1]`).
- `04_string_method.py` — Built-in methods (`upper()`, `lower()`, `strip()`, `replace()`, `find()`, `split()`).
- `05_formatting_strings.py` — Modern f-strings, `.format()`, and `%` formatting.
- `06_escape.py` — Escape sequences (`\n`, `\t`, `\\`, `\'`, `\"`) and raw strings (`r"..."`).

### Chapter 04: Lists and Tuples
- `01_list.py` — Mutable ordered sequences and indexing.
- `02_operation_list.py` — Concatenation, repetition, and membership testing (`in`, `not in`).
- `03_list_method.py` — Methods: `append()`, `extend()`, `insert()`, `pop()`, `remove()`, `sort()`, `reverse()`.
- `04_tuple.py` — Immutable sequences, single-element tuples, and memory advantages.
- `05_operation_tuple.py` — Slicing, concatenation, and indexing tuples.
- `06_tuple_method.py` — Tuple operations: `count()` and `index()`.
- `07_enumerate.py` — Getting index-value pairs cleanly with `enumerate()`.
- `08_dir_method.py` — Inspecting available attributes and methods using `dir()`.
- `09_list_comprehension.py` — Concise list creation with conditionals (`[x for x in data if condition]`).
- `10_namedtuple.py` — Self-documenting lightweight records using `namedtuple`, `_asdict()`, and `_replace()`.

### Chapter 05: Dictionaries and Sets
- `01_dict.py` — Key-value hash maps, hashing requirements, and access.
- `02_operation_dict.py` — Updating values, adding keys, and deletion (`del`).
- `03_dict_method.py` — Safe access with `.get()`, `.keys()`, `.values()`, `.items()`, and `.update()`.
- `04_set.py` — Unordered collections of unique elements.
- `05_set_method.py` — `.add()`, `.discard()`, `.remove()`, `.pop()`, and `.clear()`.
- `06_operation_set.py` — Mathematical set operations: union (`|`), intersection (`&`), difference (`-`), and symmetric difference (`^`).
- `07_set_comprehension.py` — Comprehensions for creating distinct sets.
- `08_typed_dict.py` — Static typing for structured dictionaries using `typing.TypedDict`.
- `10_dict_comprehension.py` — Dynamic dictionary construction, filtering, `zip` transformations, and the walrus operator (`:=`).

### Chapter 06: Control Flow
- `01_if.py` — Boolean conditions and conditional execution blocks.
- `02_if_else.py` — Binary decision branching.
- `03_if_elif_else.py` — Multi-way branching chains.
- `04_short_hand_if_else.py` — Ternary conditional expressions (`a if cond else b`).
- `05_calculator.py` — Interactive menu-driven calculator implementation.
- `06_leap_year.py` — Gregorian leap-year logic implementation.
- `07_multiple_if.py` — Independent conditional checks vs connected `elif` ladders.

### Chapter 07: Loops
- `01_loop.py` — Fundamentals of iteration and DRY code.
- `02_while_loop.py` — Condition-controlled loops and avoiding infinite execution.
- `03_list_using_while.py` — Index-based sequence traversal using `while`.
- `04_for_loop.py` — Collection iteration across strings, lists, tuples, and ranges.
- `05_range.py` — Numeric sequences: `range(stop)`, `range(start, stop)`, `range(start, stop, step)`.
- `06_for_with_else.py` — The loop `else` block (triggers when no `break` occurred).
- `07_break_and_continue.py` — Premature loop exit (`break`) and skipping iterations (`continue`).
- `08_pass.py` — Syntactic placeholder statement for future logic.

### Chapter 08: Functions
- `01_intro_function.py` — Defining and calling reusable blocks (`def`).
- `02_quick_quiz.py` — Hands-on function greeting exercises.
- `03_function_with_arg.py` — Input parameters and arguments.
- `04_return.py` — Returning single and multiple values via tuples.
- `05_keyword_arg.py` — Calling functions with named arguments for readability.
- `06_positional_arg.py` — Order-dependent arguments and default parameter values.
- `07_variable_len_arg.py` — Arbitrary arguments (`*args` and `**kwargs`).
- `08_recursion.py` — Recursive functions, base cases, and call stack behavior (factorial).
- `09_lambda_fun.py` — Anonymous one-liner functions for sorting and mapping.
- `10_type_hints.py` — Modern PEP 484 type annotations for parameters and return types.

### Chapter 09: File Handling, Formats & Enums
- `01_file.py` — File system interaction, paths, and encoding standards.
- `02_file_read_mode.py` — Reading files (`read()`, `readline()`, `readlines()`).
- `03_file_write_mode.py` — Writing files with `"w"` mode (overwriting).
- `04_file_append_mode.py` — Appending data with `"a"` mode.
- `05_file_x_mode.py` — Exclusive creation with `"x"` mode (fails if file exists).
- `06_with_statement.py` — Context managers for automatic, safe file closure.
- `07_csv_read_write.py` — Reading and writing structured tabular data with `csv.reader` and `csv.DictWriter`.
- `08_json_read_write.py` — Serializing and deserializing JSON (`json.dump`, `json.dumps`, `json.load`, `json.loads`).
- `09_pathlib_basics.py` — Object-oriented filesystem operations using `pathlib.Path`.
- `10_enum.py` — Defining enumerations with `enum.Enum`, `auto()`, `@unique`, iteration, and value conversions.

### Chapter 10: Object-Oriented Programming (OOP)
- `01_class.py` — Classes as blueprints and object instantiation.
- `02_instance_vs_class_attribute.py` — Memory differences between class-level and instance-level state.
- `03_method.py` — Instance methods and the `self` reference.
- `04_constructor.py` — Initializing instances with `__init__()`.
- `05_pass_para_in_cons.py` — Parameterized constructors and dynamic object configuration.
- `06_static_method.py` — Utility methods using `@staticmethod` (no `self`/`cls`).
- `07_class_method.py` — Alternative constructors and class state access with `@classmethod` and `cls`.
- `08_property.py` — Pythonic getters using the `@property` decorator.
- `09_setter_and_getter.py` — Encapsulation, validation, and `@<name>.setter`.
- `10_protected_member.py` — Encapsulation conventions using single leading underscore (`_protected`).
- `11_private_method.py` — Information hiding and name mangling with double leading underscore (`__private`).
- `12_magic_method.py` — Dunder methods: `__str__`, `__repr__`, `__len__`, `__eq__`.
- `13_dic_help_method.py` — Introspection via `__dict__`, `dir()`, and `help()`.

### Chapter 11: Inheritance & Polymorphism
- `01_intro_to_inheritance.py` — Code reuse via parent and child classes.
- `02_single_inheritance.py` — Deriving one subclass from a single base class.
- `03_multiple_inheritance.py` — Inheriting from multiple classes and Method Resolution Order (MRO).
- `04_multiple_level_inheritance.py` — Multi-tiered class hierarchies (`Grandparent -> Parent -> Child`).
- `05_super_method.py` — Delegating initialization and method calls via `super()`.
- `06_method_overloading.py` — Emulating overloading using default arguments and variable-length arguments.
- `07_method_overriding.py` — Replacing parent implementations in child classes.
- `08_abstract_class.py` — Defining interfaces and enforcing contracts using `abc.ABC` and `@abstractmethod`.
- `09_polymorphism.py` — Duck typing and polymorphic interface consumption.
- `10_operator_overloading.py` — Custom arithmetic and comparison dunders (`__add__`, `__lt__`).
- `11_composition.py` — "Has-A" relationship vs "Is-A" inheritance.

### Chapter 12: Exception Handling & Logging
- `01_intro_exception.py` — Syntax errors vs runtime exceptions; basic `try...except`.
- `02_multiple_except_block.py` — Catching distinct exception types individually.
- `03_try_except_else.py` — Running code only when no exceptions occur using `else`.
- `04_finally_block.py` — Guaranteed cleanup actions using `finally`.
- `05_file_handling.py` — Robust file I/O protected by `FileNotFoundError` handling.
- `06_class_error.py` — Capturing exception object details with `as e`.
- `07_raise_error.py` — Triggering exceptions manually with `raise`.
- `08_custom_error_without_using_constructor.py` — Creating custom exceptions inheriting from `Exception`.
- `09_custom_error_with_using_constructor.py` — Custom exceptions with rich attributes and custom error messages.
- `10_zero_division_error.py` — Handling arithmetic edge cases (`ZeroDivisionError`).
- `11_logging_basics.py` — Python's standard `logging` module (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`).
- `12_exception_logging.py` — Capturing full stack traces in log files via `logging.exception()`.

### Chapter 13: Modules & Packages
- `mod1_intro_module.py` — Creating and importing user-defined Python files.
- `mod2_module_use.py` — Selective imports (`from module import item`).
- `mod3_if_name_main.py` — The `if __name__ == '__main__':` idiom explained.
- `mod4_module_imports.py` — Aliasing modules with `as` and namespace management.
- `mod5_package_init.py` — Organizing multi-module folders into packages using `__init__.py`.
- `mod6_use_exam.py` — Practical package structure and inter-module imports (`Exam/`).

### Chapter 14: OS Module & Pathlib Filesystem
- `01_getcwd.py` — Retrieving the current working directory.
- `02_chdir.py` — Changing directories programmatically.
- `03_listdir.py` — Listing files and subfolders.
- `04_mkdir.py` — Creating single directories.
- `05_makedirs.py` — Recursively creating nested folder trees.
- `06_rmdir.py` — Deleting empty directories safely.
- `07_removedirs.py` — Recursively removing nested empty directories.
- `08_rename.py` — Renaming and moving files.
- `09_remove.py` — Deleting files.
- `10_path_exists.py` — Checking path existence with `os.path.exists`.
- `11_isfile.py` — Checking if a path is a file.
- `12_isdir.py` — Checking if a path is a directory.
- `13_dirname.py` — Extracting directory names and basenames.
- `14_getsize.py` — Reading file sizes in bytes.
- `15_getmtime.py` — Inspecting modification timestamps.
- `16_environ.py` — Reading environment variables (`os.environ`).
- `17_system.py` — Running system shell commands.
- `18_pathlib_paths.py` — Modern object-oriented path traversal with `pathlib.Path`.

### Chapter 15: Regular Expressions
- `01_intro_re.py` — Regex fundamentals: `re.match()`, `re.search()`, and `re.findall()`.
- `02_groups_and_substitution.py` — Capturing groups `()`, named groups `(?P<name>)`, and text replacement via `re.sub()`.
- `03_common_patterns.py` — Practical production regex patterns: email validation, phone number extraction, and date verification (`re.fullmatch()`).

### Chapter 16: Collections Module
- `01_chainmap.py` — Grouping multiple mappings into a single view with `collections.ChainMap`.
- `02_counter.py` — High-performance frequency counting, most common items (`.most_common()`), and multiset arithmetic.
- `03_defaultdict.py` — Automatically initializing missing dictionary keys with factory functions (`list`, `int`, `set`).
- `04_namedtuple_via_collections.py` — Defining immutable record types with field names via `collections.namedtuple`.
- `05_deque.py` — Double-ended queues with $O(1)$ appends and pops on both ends, rotating, and fixed-length ring buffers with `maxlen`.

### Chapter 17: Iterators & Generators
- `01_iterator_protocol.py` — The iterator protocol (`__iter__()`, `__next__()`, `iter()`, `next()`, `StopIteration`, custom `MeraRange`).
- `02_generator_functions.py` — Generator functions using `yield`, execution state suspension, and infinite streams.
- `03_generator_expressions.py` — Memory-efficient generator expressions `(...)` vs list comprehensions `[...]` profiled with `sys.getsizeof()`.

### Chapter 18: Itertools Module
Comprehensive guide to standard library iterator algebra:
- Infinite iterators: `04_count.py`, `05_cycle.py`, `12_repeat.py`
- Terminating iterators: `01_accumulate.py`, `02_chain.py`, `03_compress.py`, `06_dropwhile.py`, `07_filterfalse.py`, `08_groupby.py`, `09_islice.py`, `13_starmap.py`, `14_takewhile.py`, `15_tee.py`, `16_zip_longest.py`
- Combinatoric iterators: `10_permutations.py`, `11_product.py`

### Chapter 19: Functional Tools
- `01_decorators_basics.py` — Function decorators, closure mechanics, and `@` syntax.
- `02_decorators_with_args.py` — Parameterized decorator factories (`@repeat(n=3)`).
- `03_functools.py` — Standard library functional tools: `lru_cache`, `partial`, `wraps`, and `reduce`.

### Chapter 20: APIs & Data
- `01_requests_get.py` — Sending HTTP GET requests, inspecting status codes, and parsing JSON payloads.
- `02_requests_error_handling.py` — Handling network timeouts, HTTP errors, and connection failures using `try...except` and `raise_for_status()`.
- `03_save_api_response_to_json.py` — Consuming public API data and persisting sanitized JSON output to disk.

### Chapter 21: Capstone Project 🎓
A modular, production-structured project tying together everything learned from Chapters 01 through 20:
- Architecture guide in [chapter_21_capstone/README.md](./chapter_21_capstone/README.md)
- Complete starter template in `main.py`
- Dependency management and extension project ideas (Expense Tracker, GitHub CLI, Weather Dashboard).

### Chapter 22: Pydantic & Data Validation 🛡️
Runtime data parsing, schema enforcement, and validation using Pydantic:
- `01_basic_models.py` — Defining `BaseModel` schemas, type annotations, automatic type coercion, and `ValidationError` handling.
- `02_field_validation.py` — Adding field constraints with `Field()` (`gt`, `ge`, `lt`, `le`, `min_length`, `max_length`), defaults, and `Annotated`.
- `03_custom_validators.py` — Custom business logic validation using `@field_validator` and cross-field validation with `@model_validator(mode="after")`.
- `04_pydantic_for_data_science .py` — Data science workflows: nested model composition, batch record validation, and filtering corrupted CSV/JSON rows before DataFrame loading.

---

## 🎯 Exercises & Practice Index

Practice makes permanent! This repository provides **108 hands-on exercise problems** across 18 dedicated exercise suites:

| Exercise Suite | Problems | Core Topics Practiced |
|----------------|:--------:|-----------------------|
| [chapter_01_basics_exercises/](./chapter_01_basics_exercises) | 5 | Twinkle poem, Python version, circle area, string reverse, list/tuple parsing |
| [chapter_02_variables_datatypes_exercises/](./chapter_02_variables_datatypes_exercises) | 6 | Arithmetic sums, remainder calculation, input type detection, comparisons, averages, squares |
| [chapter_03_strings_exercises/](./chapter_03_strings_exercises) | 5 | Name greeting templates, letter template replacement, space detection, escape sequences |
| [chapter_04_lists_tuples_exercises/](./chapter_04_lists_tuples_exercises) | 5 | Storing user fruits, sorting marks, tuple immutability verification, list sums, zero counting |
| [chapter_05_dicts_sets_exercises/](./chapter_05_dicts_sets_exercises) | 9 | Hindi-English dictionary, unique number inputs, set type mixes, dictionary length, favorite language mappings |
| [chapter_06_control_flow_exercises/](./chapter_06_control_flow_exercises) | 7 | Greatest of four numbers, student pass/fail logic, spam detection, username validation, post topic matching |
| [chapter_07_loops_exercises/](./chapter_07_loops_exercises) | 10 | Multiplication tables, prefix greeting filters, prime number checks, sum of natural numbers, factorial, star patterns |
| [chapter_08_functions_exercises/](./chapter_08_functions_exercises) | 8 | Greatest of 3 numbers, Celsius to Fahrenheit converter, recursion sums, pattern printing, inches to cms, strip & remove words |
| [chapter_09_file_handling_exercises/](./chapter_09_file_handling_exercises) | 11 | Reading poems for keywords, updating high score records, generating tables 2–20, word censoring, log analysis, file copying |
| [chapter_10_oop_exercises/](./chapter_10_oop_exercises) | 4 | Programmer database, math calculator class (square/cube/sqrt), train ticket booking system, attribute modification |
| [chapter_11_inheritance_polymorphism_exercises/](./chapter_11_inheritance_polymorphism_exercises) | 7 | 2D/3D vectors, pet/dog inheritance, employee salary increments, complex numbers dunder methods, vector dot/cross products |
| [chapter_12_exception_handling_exercises/](./chapter_12_exception_handling_exercises) | 10 | Opening missing files, printing 3rd/5th/7th elements, division by zero handling, custom exceptions, list comprehension exports |
| [chapter_14_os_pathlib_exercises/](./chapter_14_os_pathlib_exercises) | 5 | Automated desktop file organizer, recursive file searcher, directory size profiler, bulk file renamer, backup manager |
| [chapter_15_exercises/](./chapter_15_exercises) | 5 | Email extraction, phone number formatting, date format conversion, hashtag parsing, sensitive data masking |
| [chapter_17_exercises/](./chapter_17_exercises) | 3 | Custom countdown iterator, infinite Fibonacci generator, lazy text file log processing pipeline |
| [chapter_19_exercises/](./chapter_19_exercises) | 3 | Execution timer decorator, input validation decorator, cache lookup utility |
| [chapter_20_exercises/](./chapter_20_exercises) | 2 | REST API user fetcher, live currency converter with JSON cache |
| [chapter_22_exercises/](./chapter_22_exercises) | 3 | MovieReview schema validation, Password strength field validator, and batch StudentScore dataset splitting |

---

## 🛠️ Projects

Explore **22 practical, interactive mini-projects** in [projects/](./projects):

| Category | Projects |
|----------|----------|
| 🎮 **Games & Fun** | [KBC Game](./projects/KBC%20Game), [Number Guessing Game](./projects/Number%20Guessing%20Game), [Rock paper Scissors](./projects/Rock%20paper%20Scissors), [Snake Water Gun Game](./projects/Snake%20Water%20Gun%20Game), [Word Guessing Game](./projects/Word%20Guessing%20Game), [head and tail](./projects/head%20and%20tail) |
| 🧰 **CLI Utilities** | [Band Name Generator](./projects/Band%20Name%20Generator), [Coffee Machine](./projects/Coffee%20Machine), [Email sender](./projects/Email%20sender), [Library Management System](./projects/Library%20Management%20System), [password generator](./projects/password%20generator), [pizza delvery](./projects/pizza%20delvery), [Randomized Message Encoder and Decoder](./projects/Randomized%20Message%20Encoder%20and%20Decoder), [Silent Auction](./projects/Silent%20Auction), [trip calculator](./projects/trip%20calculator) |
| 🖥️ **GUI & Visual Apps** | [Miles to Kilometers Converter GUI](./projects/Miles%20to%20Kilometers%20Converter%20GUI), [Spell checker app](./projects/Spell%20checker%20app), [Task Manager App](./projects/Task%20Manager%20App), [qr](./projects/qr) |
| 🔔 **Automation & System** | [Drink Water Notification Reminder App](./projects/Drink%20Water%20Notification%20Reminder%20App), [India's Railway app](./projects/India's%20Railway%20app), [Robo speaker](./projects/Robo%20speaker) |

---

## 🧪 Code Quality & Standards

This repository adheres strictly to **PEP 8** style guidelines:

- **Style & Consistency**: Clean snake_case naming conventions, explicit imports, and proper whitespace formatting.
- **Linting**: Verified against `flake8` to maintain clean, readable code.
- **Type Annotations**: Utilizing modern Python type hints (`int`, `str`, `list[str]`, `TypedDict`).

To verify code quality locally:
```bash
# Install flake8
pip install flake8

# Run linter on any chapter or exercise
flake8 chapter_14_os_pathlib_exercises
flake8 chapter_17_iterators_generators
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. **Create a branch**:
   ```bash
   git checkout -b feat/chapter_XX_short_description
   ```
2. **Follow repository conventions**:
   - `lower_snake_case` for filenames.
   - Place educational lessons in `chapter_XX/`.
   - Place exercises in `chapter_XX_exercises/`.
   - Include a dedicated `README.md` in any new folder.
   - Maintain PEP 8 compliance.
3. **Open a Pull Request** describing what changed and which chapters are affected.

See [CONTRIBUTING.md](./CONTRIBUTING.md) for full contribution details.

---

## 🔗 Resources

- 🐍 [Official Python Documentation](https://docs.python.org/3/)
- 📰 [Real Python Tutorials](https://realpython.com/)
- 🎓 [Python for Everybody (PY4E)](https://www.py4e.com/)
- 📖 [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
- ⚡ [Astral uv Documentation](https://docs.astral.sh/uv/)

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.