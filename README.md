# Learn Python

A structured, beginner-friendly path to learn Python from fundamentals to intermediate topics, with clear chapters, dedicated exercises, and hands-on projects. The repository uses consistent, lower_snake_case folder names with zero‑padded chapter numbers for easy navigation.

## Table of Contents
- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Folder Structure](#folder-structure)
- [Naming Conventions](#naming-conventions)
- [Chapters Index](#chapters-index)
- [Chapter Summaries](#chapter-summaries)
- [Projects](#projects)
- [Contributing](#contributing)
- [Resources](#resources)
- [License](#license)

## Introduction
Python is a versatile language used in web development, data science, automation, scripting, and more. This repository is organized by chapters, with exercises and projects that reinforce learning by doing.

## Getting Started

Prerequisites:
- Python 3.10+ (download from https://www.python.org/)
- A code editor like VS Code (https://code.visualstudio.com/) or PyCharm (https://www.jetbrains.com/pycharm/)

Clone and run:
```bash
git clone <your-repo-url>
cd Learn-Python
# Optional: create a virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Run a sample script
python chapter_01/01_hello_world.py
```

Tip: If you use VS Code, repository settings in `.vscode/` will be auto-detected.

## Folder Structure

```text
Learn-Python/
│
├── .vscode/
├── projects/
│
├── chapter_01/
├── chapter_01_exercises/
├── chapter_02/
├── chapter_02_exercises/
├── chapter_03/
├── chapter_03_exercises/
├── chapter_04/
├── chapter_04_exercises/
├── chapter_05/
├── chapter_05_exercises/
├── chapter_06/
├── chapter_06_exercises/
├── chapter_07/
├── chapter_07_exercises/
├── chapter_08/
├── chapter_08_exercises/
├── chapter_09/
├── chapter_09_exercises/
├── chapter_10/
├── chapter_10_exercises/
├── chapter_11/
├── chapter_11_exercises/
├── chapter_12/
├── chapter_12_exercises/
├── chapter_13/
├── chapter_14/
│
└── README.md
```

Notes:
- Chapters 01–12 include corresponding `chapter_XX_exercises/` folders.
- Add exercises for later chapters as `chapter_13_exercises/` and `chapter_14_exercises/` when available.

## Naming Conventions
- Use lower_snake_case for all folder and file names.
- Zero‑pad chapter numbers to two digits: `chapter_01`, `chapter_02`, …, `chapter_14`.
- Use `exercises` (not abbreviations like `pr`) for practice folders: `chapter_01_exercises/`.
- Prefer descriptive file names inside each chapter or exercises folder.

## Chapters Index
- Chapter 01: [chapter_01/](./chapter_01)
  - Exercises: [chapter_01_exercises/](./chapter_01_exercises)
- Chapter 02: [chapter_02/](./chapter_02)
  - Exercises: [chapter_02_exercises/](./chapter_02_exercises)
- Chapter 03: [chapter_03/](./chapter_03)
  - Exercises: [chapter_03_exercises/](./chapter_03_exercises)
- Chapter 04: [chapter_04/](./chapter_04)
  - Exercises: [chapter_04_exercises/](./chapter_04_exercises)
- Chapter 05: [chapter_05/](./chapter_05)
  - Exercises: [chapter_05_exercises/](./chapter_05_exercises)
- Chapter 06: [chapter_06/](./chapter_06)
  - Exercises: [chapter_06_exercises/](./chapter_06_exercises)
- Chapter 07: [chapter_07/](./chapter_07)
  - Exercises: [chapter_07_exercises/](./chapter_07_exercises)
- Chapter 08: [chapter_08/](./chapter_08)
  - Exercises: [chapter_08_exercises/](./chapter_08_exercises)
- Chapter 09: [chapter_09/](./chapter_09)
  - Exercises: [chapter_09_exercises/](./chapter_09_exercises)
- Chapter 10: [chapter_10/](./chapter_10)
  - Exercises: [chapter_10_exercises/](./chapter_10_exercises)
- Chapter 11: [chapter_11/](./chapter_11)
  - Exercises: [chapter_11_exercises/](./chapter_11_exercises)
- Chapter 12: [chapter_12/](./chapter_12)
  - Exercises: [chapter_12_exercises/](./chapter_12_exercises)
- Chapter 13: [chapter_13/](./chapter_13)
  - Exercises: Add later as `chapter_13_exercises/` if needed
- Chapter 14: [chapter_14/](./chapter_14)
  - Exercises: Add later as `chapter_14_exercises/` if needed

## Chapter Summaries

### Chapter 1: Basics
- 01_hello_world.py: Introduction to Python syntax.
- 02_module.py: Using modules in a simple script.
- 03_comment.py: Writing comments in Python.

### Chapter 2: Variables and Data Types
- 01_variable.py: Introduction to variables.
- 02_datatype.py: Understanding data types.
- 03_ruleofvariable.py: Rules for naming variables.
- 04_operator.py: Operators in Python.
- 05_type_function.py: Using the type function.
- 07_input.py: Taking user input.

### Chapter 3: Strings
- 01_intro_string.py: Introduction to strings.
- 02_slicing.py: Slicing strings.
- 03_negative_slicing.py: Negative slicing in strings.
- 04_string_method.py: String methods.
- 05_Formatting_strings.py: Formatting strings.
- 06_escape.py: Escape sequences in strings.

### Chapter 4: Lists and Tuples
- 01_list.py: Introduction to lists.
- 02_operation_list.py: Operations on lists.
- 03_list_method.py: List methods.
- 04_tuple.py: Introduction to tuples.
- 05_operation_tuple.py: Operations on tuples.
- 06_tuple_method.py: Tuple methods.
- 07_enumerate.py: Using the enumerate function.
- 08_dir_method.py: Using the dir function.

### Chapter 5: Dictionaries and Sets
- 01_dict.py: Introduction to dictionaries.
- 02_operation_dict.py: Operations on dictionaries.
- 03_dict_method.py: Dictionary methods.
- 04_set.py: Introduction to sets.
- 05_set_method.py: Set methods.
- 06_operation_set.py: Operations on sets.

### Chapter 6: Control Flow
- 01_if.py: Using if statements.
- 02_if_else.py: Using if-else statements.
- 03_if_elif_else.py: Using if-elif-else statements.
- 04_short_hand_if_else.py: Short-hand if-else statements.
- 05_calculator.py: Calculator program.
- 06_leap_year.py: Leap year checker.
- 07_multiple_if.py: Using multiple if statements.

### Chapter 7: Loops
- 01_loop.py: Introduction to loops.
- 02_while_loop.py: Using while loops.
- 03_list_using_while.py: Working with lists using while loops.
- 04_for_loop.py: Using for loops.
- 05_range.py: Using the range function.
- 06_for_with_else.py: Using else with for loops.
- 07_break_and_continue.py: Using break and continue.
- 08_pass.py: Using the pass statement.

### Chapter 8: Functions
- 01_intro_function.py: Introduction to functions.
- 02_quick.py: Quick quiz.
- 03_function_with_arg.py: Functions with arguments.
- 04_return.py: Return statements.
- 05_keyword_arg.py: Keyword arguments.
- 06_positional_arg.py: Positional arguments.
- 07_variable_len_arg.py: Variable length arguments.
- 08_recursion.py: Recursion.
- 09_lambda.py: Lambda functions.

### Chapter 9: File Handling
- 01_file.py: Introduction to file handling.
- 02_file_read_mode.py: Reading files.
- 03_file_write_mode.py: Writing files.
- 04_file_append_mode.py: Appending to files.
- 05_file_x_mode.py: Exclusive file mode.
- 06_with_statement.py: Using the with statement.

### Chapter 10: Object-Oriented Programming (OOP)
- 01_class.py: Introduction to classes.
- 02_instance_vs_class_attribute.py: Instance vs class attributes.
- 03_method.py: Methods in classes.
- 04_constructor.py: Constructors.
- 05_pass_para_in_cons.py: Passing parameters in constructors.
- 06_static_method.py: Static methods.
- 07_class_method.py: Class methods.
- 08_property.py: Using properties.
- 09_setter_and_getter.py: Setters and getters.
- 10_protected_member.py: Protected members.
- 11_private_method.py: Private methods.
- 12_magic_method.py: Magic methods.
- 13_dic_help_method.py: Dictionary helper methods.

### Chapter 11: Inheritance
- 01_intro_to_inheritance.py: Introduction to inheritance.
- 02_single_inheritance.py: Single inheritance.
- 03_multiple_inheritance.py: Multiple inheritance.
- 04_multiple_level_inheritance.py: Multilevel inheritance.
- 05_super_method.py: Using the super method.
- 06_method_overloading.py: Method overloading.
- 07_method_overriding.py: Method overriding.
- 08_abstract_class.py: Abstract classes.
- 09_polymorphism.py: Polymorphism.
- 10_operator_overloading.py: Operator overloading.

### Chapter 12: Exception Handling
- 01_intro_exception.py: Introduction to exception handling.
- 02_multiple_except_block.py: Multiple except blocks.
- 03_try_except_else.py: Using try, except, and else.
- 04_finally_block.py: Using the finally block.
- 05_file_handling.py: File handling with exceptions.
- 06_class_error.py: Class-based exceptions.
- 07_raise_error.py: Raising exceptions.
- 08_custom_error_without_using_constructor.py: Custom exceptions without constructors.
- 09_custom_error_with_using_constructor.py: Custom exceptions with constructors.
- 10_zero_division_error.py: Handling division by zero.

### Chapter 13: Modules
- m01_intro_module.py: Introduction to modules.
- m02_module_use.py: Using modules.
- n03_if_name_main.py: The `if __name__ == '__main__'` construct.
- n04_use.py: Using modules in scripts.

### Chapter 14: OS Module
- 01_getcwd.py: Returns the current working directory.
- 02_chdir.py: Changes the current working directory.
- 03_listdir.py: Returns a list of files and subdirectories in the specified path.
- 04_mkdir.py: Creates a new directory.
- 05_makedirs.py: Creates a directory and its parent directories if they don't exist.
- 06_rmdir.py: Removes an empty directory.
- 07_removedirs.py: Removes an empty directory and its parent directories.
- 08_rename.py: Renames a file or directory.
- 09_remove.py: Deletes a file.
- 10_path_exists.py: Checks if a path exists.
- 11_isfile.py: Checks if a path is a file.
- 12_isdir.py: Checks if a path is a directory.
- 13_dirname.py: Returns the directory name of a path.
- 14_getsize.py: Returns the size of a file.
- 15_getmtime.py: Returns the last modification time of a file.
- 16_environ.py: Working with environment variables (e.g., PATH).
- 17_system.py: Executes a command in a subshell and returns the exit status.

## Projects
Explore practical, hands-on mini‑apps and utilities in [projects/](./projects):

- Band Name Generator
- Head and Tail
- India's Railway Enquiry
- Library Management System
- Number Guessing Game
- Pizza Delivery System
- Rock Paper Scissors
- Snake Water Gun Game
- Task Manager
- Trip Calculator
- Password Generator
- Randomized Message Encoder and Decoder
- Silent Auction
- KBC Game
- Robo Speaker
- Miles to Kilometers Converter GUI

## Contributing
Contributions are welcome! Please:

1. Create a branch:
   - feat/chapter_XX_short_description
   - fix/chapter_XX_short_description
2. Follow naming conventions (see above).
3. Use clear commit messages (Conventional Commits encouraged), e.g.:
   - feat(chapter_03): add slicing examples
   - fix(chapter_05_exercises): correct task 4 solution
4. Open a Pull Request describing:
   - What changed and why
   - Affected chapter(s)
   - Any screenshots or outputs if helpful

Guidelines:
- Keep chapter material in `chapter_XX/`.
- Put practice and solutions in `chapter_XX_exercises/`.
- Use `projects/` for multi‑chapter or larger work.

## Resources
- Official Python Documentation: https://docs.python.org/3/
- Real Python: https://realpython.com/
- Python for Everybody: https://www.py4e.com/
- Automate the Boring Stuff with Python: https://automatetheboringstuff.com/

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.