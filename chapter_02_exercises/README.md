# Chapter 2 Exercises: Mastering Variables and Data Types! 🎯

Welcome to your Chapter 2 practice arena! Think of this as your coding gymnasium where you'll strengthen the skills you learned about variables, data types, operators, and user input. These exercises are designed to help you go from understanding concepts to actually applying them in real programs.

Remember, the goal isn't to just complete these exercises - it's to understand WHY each line of code works and HOW you can apply these concepts to solve real-world problems. Let's dive in and make your programming muscles stronger! 💪

## 🌟 What Makes These Exercises Special?

These aren't just random coding tasks - they're carefully designed stepping stones that help you:
- **Solidify your understanding** of Chapter 2 concepts
- **Practice type conversion** in real scenarios
- **Work with user input** safely and effectively
- **Apply mathematical operations** in practical contexts
- **Debug common beginner mistakes** before they become habits
- **Build confidence** through achievable challenges

---

## 📋 Exercise Overview

| Exercise | Core Concept | Difficulty | Real-World Application |
|----------|-------------|------------|----------------------|
| Problem 1 | User Input + Math | ⭐ Beginner | Calculator basics |
| Problem 2 | Arithmetic Operators | ⭐ Beginner | Division operations |
| Problem 3 | Type Detection | ⭐ Beginner | Data validation |
| Problem 4 | Comparison Operators | ⭐ Beginner | Decision making |
| Problem 5 | Average Calculation | ⭐⭐ Intermediate | Statistical analysis |
| Problem 6 | Mathematical Operations | ⭐⭐ Intermediate | Scientific calculations |

---

## 🧮 Exercise 1: `problem1.py` - Your First Interactive Calculator!

### 🎯 **The Challenge**
*"Write a Python program to add two numbers."*

### 📖 **What's Inside**
```python
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
print(a + b)
```

### 🤔 **Why This Exercise Matters**

This simple exercise is actually a masterclass in three fundamental programming concepts all working together! Let's break down why this seemingly simple program is so important:

**1. User Interaction**: Your program now talks to people!
**2. Type Conversion**: You're safely handling user input
**3. Mathematical Operations**: You're performing calculations

### 🔍 **Line-by-Line Analysis**

**Line 1: `a = int(input("Enter first number : "))`**
This line is doing THREE things at once:
- `input()` asks the user for text and waits for their response
- `int()` converts that text into a number
- `a =` stores the number in a variable named 'a'

**Think of it like this:**
1. 📢 "Hey user, give me a number!"
2. 👤 User types "25" (but Python sees it as text "25")
3. 🔄 `int()` converts text "25" into number 25
4. 📦 Store number 25 in box labeled 'a'

**Line 2: `b = int(input("Enter second number : "))`**
Same process, but storing in variable 'b'

**Line 3: `print(a + b)`**
Now we can safely add the two numbers and display the result!

### ⚠️ **What Could Go Wrong? (And How to Fix It)**

**Problem**: User enters text instead of numbers
```python
# If user types "hello" instead of a number:
# ValueError: invalid literal for int() with base 10: 'hello'
```

**Solution**: Safe input handling
```python
def safe_add_numbers():
    """Add two numbers with error handling"""
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        result = a + b
        print(f"The sum is: {result}")
    except ValueError:
        print("Error: Please enter valid numbers only!")

# safe_add_numbers()
```

### 🎮 **Level Up Your Solution**

**Enhanced Version with Validation:**
```python
def interactive_adder():
    """An improved number adder with user-friendly features"""
    print("🧮 Interactive Number Adder")
    print("-" * 30)
    
    # Get first number safely
    while True:
        try:
            a = float(input("Enter first number: "))
            break
        except ValueError:
            print("❌ That's not a valid number. Try again!")
    
    # Get second number safely
    while True:
        try:
            b = float(input("Enter second number: "))
            break
        except ValueError:
            print("❌ That's not a valid number. Try again!")
    
    # Calculate and display result
    result = a + b
    print(f"\n✅ Result: {a} + {b} = {result}")
    
    # Show additional information
    if result > 100:
        print("🎉 Wow! That's a big number!")
    elif result < 0:
        print("📉 The result is negative!")
    else:
        print("👍 Nice calculation!")

# interactive_adder()
```

### 🌍 **Real-World Applications**

This simple addition concept is the foundation for:
- **Shopping carts** (adding item prices)
- **Grade calculators** (adding test scores)
- **Expense trackers** (adding daily expenses)
- **Game scoring systems** (adding points)
- **Scientific calculators** (basic arithmetic)

### 🎯 **Practice Variations**

1. **Four Basic Operations Calculator**:
   ```python
   def basic_calculator():
       a = float(input("Enter first number: "))
       b = float(input("Enter second number: "))
       print(f"Addition: {a + b}")
       print(f"Subtraction: {a - b}")
       print(f"Multiplication: {a * b}")
       if b != 0:
           print(f"Division: {a / b}")
       else:
           print("Division: Cannot divide by zero!")
   ```

2. **Multi-Number Adder**:
   ```python
   def add_multiple_numbers():
       numbers = []
       count = int(input("How many numbers to add? "))
       
       for i in range(count):
           num = float(input(f"Enter number {i+1}: "))
           numbers.append(num)
       
       total = sum(numbers)
       print(f"Sum of all numbers: {total}")
   ```

---

## 🔢 Exercise 2: `problem2.py` - The Remainder Detective!

### 🎯 **The Challenge**
*"Write a Python program to find remainder when a number is divided by z."*

### 📖 **What's Inside**
```python
n = 37
z = 10
rem = n // z
print(rem)
```

### 🚨 **Houston, We Have a Problem!**

There's actually a **bug** in this code! The comment says "find remainder" but the code uses `//` (floor division) instead of `%` (modulus/remainder). Let's fix this and understand both operations!

### 🔧 **The Corrected Version**
```python
n = 37
z = 10

# THIS is how you find the remainder:
rem = n % z
print(f"Remainder when {n} is divided by {z}: {rem}")

# The original code actually finds the quotient (whole number result):
quotient = n // z
print(f"Quotient when {n} is divided by {z}: {quotient}")

# Regular division gives the complete decimal result:
complete_division = n / z
print(f"Complete division {n} ÷ {z}: {complete_division}")
```

### 🎓 **Understanding Division Operations**

Let's break down the three different types of division in Python:

**1. Regular Division (`/`)**: 
```python
print(37 / 10)    # 3.7 (complete decimal result)
```

**2. Floor Division (`//`)**: 
```python
print(37 // 10)   # 3 (whole number part only)
```

**3. Modulus (`%`)**: 
```python
print(37 % 10)    # 7 (remainder part only)
```

### 🎭 **Real-World Analogy**

Imagine you have 37 cookies and want to put them in boxes of 10:
- **Regular division**: 37 ÷ 10 = 3.7 boxes
- **Floor division**: 37 // 10 = 3 complete boxes
- **Modulus**: 37 % 10 = 7 cookies left over

### 🎮 **Interactive Division Explorer**

```python
def division_explorer():
    """Explore all three types of division"""
    print("🔢 Division Explorer")
    print("-" * 20)
    
    try:
        # Get numbers from user
        dividend = int(input("Enter the number to be divided: "))
        divisor = int(input("Enter the number to divide by: "))
        
        if divisor == 0:
            print("❌ Cannot divide by zero!")
            return
        
        # Perform all three operations
        regular_div = dividend / divisor
        floor_div = dividend // divisor
        remainder = dividend % divisor
        
        # Display results with explanation
        print(f"\n📊 Division Results for {dividend} ÷ {divisor}:")
        print("-" * 40)
        print(f"Regular division (/):  {regular_div}")
        print(f"Floor division (//):   {floor_div} (whole boxes)")
        print(f"Remainder (%):         {remainder} (leftover items)")
        
        # Verification
        print(f"\n✅ Verification: {divisor} × {floor_div} + {remainder} = {divisor * floor_div + remainder}")
        
        # Real-world interpretation
        print(f"\n🌍 Real-world meaning:")
        print(f"If you have {dividend} items and put them in groups of {divisor}:")
        print(f"• You'll have {floor_div} complete groups")
        print(f"• With {remainder} items left over")
        
    except ValueError:
        print("❌ Please enter valid integers!")

# division_explorer()
```

### 🌟 **Amazing Uses of Modulus Operator**

**1. Check if a number is even or odd:**
```python
def is_even(number):
    return number % 2 == 0

print(is_even(8))   # True (even)
print(is_even(7))   # False (odd)
```

**2. Cycle through values:**
```python
# Create a repeating pattern: 0, 1, 2, 0, 1, 2, 0, 1, 2...
for i in range(10):
    cycle_value = i % 3
    print(f"Day {i}: Pattern value {cycle_value}")
```

**3. Time calculations:**
```python
def convert_minutes_to_time(total_minutes):
    hours = total_minutes // 60    # Complete hours
    minutes = total_minutes % 60   # Remaining minutes
    return f"{hours}h {minutes}m"

print(convert_minutes_to_time(150))  # "2h 30m"
```

**4. Check divisibility:**
```python
def is_divisible_by(number, divisor):
    return number % divisor == 0

print(is_divisible_by(15, 3))  # True
print(is_divisible_by(16, 3))  # False
```

### 🎯 **Practice Challenges**

1. **Clock Math**: Convert seconds to hours, minutes, and seconds
2. **Pagination**: Determine how many pages needed for a certain number of items
3. **Remainder Pattern**: Find patterns in remainders when dividing by different numbers

---

## 🔍 Exercise 3: `problem3.py` - The Type Detective!

### 🎯 **The Challenge**
*"Check the type of variable assigned using input() function."*

### 📖 **What's Inside**
```python
name = input("Enter your name ")
print("Your name is ", name)
print(type(name))  # <class 'str'>
```

### 🕵️ **What This Exercise Reveals**

This exercise demonstrates one of the most important concepts for new programmers: **ALL input from users is text (strings), even if it looks like a number!**

### 🎭 **The Great Input Mystery**

Let's investigate what happens with different types of input:

```python
def input_type_detective():
    """Investigate what type input() always returns"""
    print("🔍 Input Type Detective")
    print("-" * 25)
    
    # Test 1: Text input
    name = input("Enter your name: ")
    print(f"Name: '{name}' -> Type: {type(name)}")
    
    # Test 2: Number input (but still becomes string!)
    age_input = input("Enter your age: ")
    print(f"Age input: '{age_input}' -> Type: {type(age_input)}")
    
    # Test 3: Convert to actual number
    age_number = int(age_input)
    print(f"Converted age: {age_number} -> Type: {type(age_number)}")
    
    # Test 4: Boolean-looking input
    answer = input("Do you like Python? (True/False): ")
    print(f"Answer: '{answer}' -> Type: {type(answer)}")
    
    # Test 5: Decimal input
    height_input = input("Enter your height in feet: ")
    print(f"Height input: '{height_input}' -> Type: {type(height_input)}")
    height_number = float(height_input)
    print(f"Converted height: {height_number} -> Type: {type(height_number)}")

# input_type_detective()
```

### 🎨 **The Art of Type Conversion**

Here's how to safely convert user input to different types:

```python
def safe_type_conversion():
    """Demonstrate safe type conversion from user input"""
    print("🛡️ Safe Type Conversion Demo")
    print("-" * 30)
    
    # Safe integer conversion
    def get_safe_int(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("❌ Please enter a valid whole number!")
    
    # Safe float conversion
    def get_safe_float(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("❌ Please enter a valid number!")
    
    # Safe boolean conversion
    def get_safe_bool(prompt):
        while True:
            answer = input(prompt + " (yes/no): ").lower()
            if answer in ['yes', 'y', 'true', '1']:
                return True
            elif answer in ['no', 'n', 'false', '0']:
                return False
            else:
                print("❌ Please answer yes or no!")
    
    # Collect different types of data safely
    name = input("Enter your name: ")  # Keep as string
    age = get_safe_int("Enter your age: ")
    height = get_safe_float("Enter your height in feet: ")
    likes_python = get_safe_bool("Do you like Python?")
    
    # Display results with types
    print(f"\n📊 Your Information:")
    print(f"Name: {name} ({type(name)})")
    print(f"Age: {age} ({type(age)})")
    print(f"Height: {height} ({type(height)})")
    print(f"Likes Python: {likes_python} ({type(likes_python)})")

# safe_type_conversion()
```

### 🌍 **Real-World Type Checking Applications**

**1. Form Validation:**
```python
def validate_user_registration():
    """Validate user registration data"""
    print("📝 User Registration")
    
    # Username (must be string, no empty)
    username = input("Username: ").strip()
    if not username:
        print("❌ Username cannot be empty!")
        return False
    
    # Age (must be integer, reasonable range)
    try:
        age = int(input("Age: "))
        if not (13 <= age <= 120):
            print("❌ Age must be between 13 and 120!")
            return False
    except ValueError:
        print("❌ Age must be a number!")
        return False
    
    # Email (must be string, contain @)
    email = input("Email: ").strip()
    if '@' not in email:
        print("❌ Please enter a valid email!")
        return False
    
    print("✅ Registration data is valid!")
    return True

# validate_user_registration()
```

**2. Data Type Analysis:**
```python
def analyze_input_data():
    """Analyze what type of data the user is trying to input"""
    user_input = input("Enter anything: ")
    
    print(f"\n🔬 Analysis of '{user_input}':")
    print(f"Original type: {type(user_input)}")
    print(f"Length: {len(user_input)} characters")
    
    # Test if it could be an integer
    try:
        int_version = int(user_input)
        print(f"✅ Can be integer: {int_version}")
    except ValueError:
        print("❌ Cannot be converted to integer")
    
    # Test if it could be a float
    try:
        float_version = float(user_input)
        print(f"✅ Can be float: {float_version}")
    except ValueError:
        print("❌ Cannot be converted to float")
    
    # Test if it's boolean-like
    if user_input.lower() in ['true', 'false', 'yes', 'no']:
        print(f"✅ Looks like boolean input")
    
    # Check if it's numeric
    if user_input.isdigit():
        print("✅ Contains only digits")
    elif user_input.isalpha():
        print("✅ Contains only letters")
    elif user_input.isalnum():
        print("✅ Contains letters and numbers")

# analyze_input_data()
```

### 🎯 **Key Takeaways**

1. **`input()` ALWAYS returns a string** - remember this!
2. **Type conversion is necessary** for mathematical operations
3. **Always validate user input** to prevent crashes
4. **Use `type()` for debugging** and understanding your data
5. **Plan your data types** before writing code

---

## ⚖️ Exercise 4: `problem4.py` - The Comparison Champion!

### 🎯 **The Challenge**
*"Use comparison operator to find out whether 'a' given variable a is greater than 'b' or not. Take a = 34 and b = 80"*

### 📖 **What's Inside**
```python
a = 34 
b = 80
print("a is grather then b is ", a > b)
print("b is grather then a is ", b > a)
```

### 📝 **Let's Fix the Typos and Enhance!**

The original code has some spelling errors. Let's create a polished version:

```python
a = 34
b = 80

print(f"a is greater than b: {a > b}")      # False
print(f"b is greater than a: {b > a}")      # True
print(f"a is equal to b: {a == b}")         # False
print(f"a is not equal to b: {a != b}")     # True
print(f"a is less than b: {a < b}")         # True
print(f"a is less than or equal to b: {a <= b}")  # True
print(f"b is greater than or equal to a: {b >= a}")  # True
```

### 🎭 **The Complete Comparison Operator Family**

Let's meet all the comparison operators and see them in action:

```python
def comparison_showcase():
    """Demonstrate all comparison operators"""
    print("⚖️ Comparison Operators Showcase")
    print("-" * 35)
    
    # Test values
    x = 15
    y = 25
    z = 15
    
    print(f"Test values: x = {x}, y = {y}, z = {z}")
    print("-" * 35)
    
    # Equal to (==)
    print(f"x == y: {x == y}")  # False
    print(f"x == z: {x == z}")  # True
    
    # Not equal to (!=)
    print(f"x != y: {x != y}")  # True
    print(f"x != z: {x != z}")  # False
    
    # Greater than (>)
    print(f"x > y: {x > y}")    # False
    print(f"y > x: {y > x}")    # True
    
    # Less than (<)
    print(f"x < y: {x < y}")    # True
    print(f"y < x: {y < x}")    # False
    
    # Greater than or equal (>=)
    print(f"x >= z: {x >= z}")  # True (because x equals z)
    print(f"y >= x: {y >= x}")  # True (because y is greater than x)
    
    # Less than or equal (<=)
    print(f"x <= z: {x <= z}")  # True (because x equals z)
    print(f"x <= y: {x <= y}")  # True (because x is less than y)

# comparison_showcase()
```

### 🎮 **Interactive Comparison Game**

```python
def comparison_game():
    """A fun game to practice comparison operators"""
    import random
    
    print("🎯 Comparison Challenge Game!")
    print("-" * 30)
    
    score = 0
    rounds = 5
    
    for round_num in range(1, rounds + 1):
        # Generate random numbers
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        
        # Choose random comparison
        operations = [
            (">", "greater than"),
            ("<", "less than"),
            ("==", "equal to"),
            ("!=", "not equal to"),
            (">=", "greater than or equal to"),
            ("<=", "less than or equal to")
        ]
        
        op_symbol, op_name = random.choice(operations)
        
        print(f"\nRound {round_num}: Is {num1} {op_name} {num2}?")
        
        # Get user's guess
        while True:
            user_answer = input("Enter 'true' or 'false': ").lower()
            if user_answer in ['true', 'false']:
                break
            print("Please enter 'true' or 'false'")
        
        # Calculate correct answer
        if op_symbol == ">":
            correct = num1 > num2
        elif op_symbol == "<":
            correct = num1 < num2
        elif op_symbol == "==":
            correct = num1 == num2
        elif op_symbol == "!=":
            correct = num1 != num2
        elif op_symbol == ">=":
            correct = num1 >= num2
        elif op_symbol == "<=":
            correct = num1 <= num2
        
        # Check answer
        user_bool = user_answer == 'true'
        if user_bool == correct:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! {num1} {op_symbol} {num2} is {correct}")
    
    # Final score
    percentage = (score / rounds) * 100
    print(f"\n🎉 Game Over! Score: {score}/{rounds} ({percentage}%)")
    
    if percentage >= 80:
        print("🏆 Excellent! You're a comparison master!")
    elif percentage >= 60:
        print("👍 Good job! Keep practicing!")
    else:
        print("📚 Practice more with comparison operators!")

# comparison_game()
```

### 🌍 **Real-World Applications**

**1. Age Verification System:**
```python
def age_verification():
    """Check if user is old enough for different activities"""
    try:
        age = int(input("Enter your age: "))
        
        print(f"\n📋 Age Verification Results:")
        print(f"Can vote (18+): {age >= 18}")
        print(f"Can drive (16+): {age >= 16}")
        print(f"Can watch PG-13 movies (13+): {age >= 13}")
        print(f"Is senior citizen (65+): {age >= 65}")
        print(f"Is teenager (13-19): {13 <= age <= 19}")
        
    except ValueError:
        print("❌ Please enter a valid age!")

# age_verification()
```

**2. Grade Evaluation System:**
```python
def grade_evaluator():
    """Evaluate student performance"""
    try:
        score = float(input("Enter your test score (0-100): "))
        
        if not (0 <= score <= 100):
            print("❌ Score must be between 0 and 100!")
            return
        
        print(f"\n📊 Grade Analysis for score: {score}")
        print(f"A grade (90+): {score >= 90}")
        print(f"B grade (80-89): {80 <= score < 90}")
        print(f"C grade (70-79): {70 <= score < 80}")
        print(f"D grade (60-69): {60 <= score < 70}")
        print(f"F grade (below 60): {score < 60}")
        print(f"Passing grade (60+): {score >= 60}")
        print(f"Honor roll (95+): {score >= 95}")
        
    except ValueError:
        print("❌ Please enter a valid score!")

# grade_evaluator()
```

**3. Password Strength Checker:**
```python
def password_strength_checker():
    """Check password strength using comparisons"""
    password = input("Enter a password to check: ")
    
    # Check various criteria
    length_ok = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=" for c in password)
    
    print(f"\n🔐 Password Strength Analysis:")
    print(f"Length 8+ characters: {length_ok}")
    print(f"Has uppercase letter: {has_upper}")
    print(f"Has lowercase letter: {has_lower}")
    print(f"Has number: {has_digit}")
    print(f"Has special character: {has_special}")
    
    # Overall strength
    criteria_met = sum([length_ok, has_upper, has_lower, has_digit, has_special])
    
    if criteria_met >= 4:
        print("💪 Strong password!")
    elif criteria_met >= 3:
        print("👍 Good password!")
    elif criteria_met >= 2:
        print("⚠️ Weak password!")
    else:
        print("❌ Very weak password!")

# password_strength_checker()
```

---

## 📊 Exercise 5: `problem5.py` - The Average Calculator!

### 🎯 **The Challenge**
*"Write a Python program to find an average of two numbers entered by the user."*

### 📖 **What's Inside**
```python
num1 = int(input("Enter first number"))
num2 = int(input("Enter second  number"))
avg = (num1 + num2) / 2
print("The average of two numbers is", avg)
```

### 🎓 **Understanding Averages**

This exercise introduces you to one of the most fundamental concepts in mathematics and data analysis: calculating the **mean** (average). Let's enhance this program and explore different types of averages!

### 🌟 **Enhanced Average Calculator**

```python
def enhanced_average_calculator():
    """Calculate average with better user experience"""
    print("📊 Enhanced Average Calculator")
    print("-" * 30)
    
    try:
        # Get numbers with better prompts
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Calculate average
        average = (num1 + num2) / 2
        
        # Display results with formatting
        print(f"\n📈 Results:")
        print(f"First number: {num1}")
        print(f"Second number: {num2}")
        print(f"Average: {average}")
        print(f"Average (rounded): {round(average, 2)}")
        
        # Additional insights
        difference = abs(num1 - num2)
        print(f"\n💡 Additional Information:")
        print(f"Sum: {num1 + num2}")
        print(f"Difference: {difference}")
        print(f"Range: {min(num1, num2)} to {max(num1, num2)}")
        
        # Interpretation
        if num1 == num2:
            print("🎯 Both numbers are identical!")
        elif difference < 1:
            print("🤝 The numbers are very close!")
        elif difference > 50:
            print("📏 The numbers are quite far apart!")
        
    except ValueError:
        print("❌ Error: Please enter valid numbers!")

# enhanced_average_calculator()
```

### 🎮 **Multi-Number Average Calculator**

```python
def multi_number_average():
    """Calculate average of multiple numbers"""
    print("🔢 Multi-Number Average Calculator")
    print("-" * 35)
    
    numbers = []
    
    try:
        # Get count of numbers
        count = int(input("How many numbers do you want to average? "))
        
        if count <= 0:
            print("❌ Please enter a positive number!")
            return
        
        # Collect all numbers
        for i in range(count):
            num = float(input(f"Enter number {i + 1}: "))
            numbers.append(num)
        
        # Calculate statistics
        total = sum(numbers)
        average = total / count
        minimum = min(numbers)
        maximum = max(numbers)
        range_value = maximum - minimum
        
        # Display results
        print(f"\n📊 Statistical Summary:")
        print(f"Numbers entered: {numbers}")
        print(f"Count: {count}")
        print(f"Sum: {total}")
        print(f"Average: {average:.2f}")
        print(f"Minimum: {minimum}")
        print(f"Maximum: {maximum}")
        print(f"Range: {range_value}")
        
        # Grade interpretation (if numbers look like grades)
        if all(0 <= num <= 100 for num in numbers):
            print(f"\n🎓 If these are grades:")
            if average >= 90:
                letter_grade = 'A'
            elif average >= 80:
                letter_grade = 'B'
            elif average >= 70:
                letter_grade = 'C'
            elif average >= 60:
                letter_grade = 'D'
            else:
                letter_grade = 'F'
            print(f"Average grade: {letter_grade}")
        
    except ValueError:
        print("❌ Error: Please enter valid numbers!")

# multi_number_average()
```

### 🏆 **Grade Point Average (GPA) Calculator**

```python
def gpa_calculator():
    """Calculate GPA from course grades and credits"""
    print("🎓 GPA Calculator")
    print("-" * 20)
    
    total_points = 0
    total_credits = 0
    courses = []
    
    try:
        num_courses = int(input("How many courses? "))
        
        for i in range(num_courses):
            print(f"\nCourse {i + 1}:")
            course_name = input("Course name: ")
            
            # Get letter grade
            while True:
                grade = input("Letter grade (A, B, C, D, F): ").upper()
                if grade in ['A', 'B', 'C', 'D', 'F']:
                    break
                print("Please enter A, B, C, D, or F")
            
            # Convert to grade points
            grade_points = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
            points = grade_points[grade]
            
            # Get credit hours
            credits = float(input("Credit hours: "))
            
            # Calculate weighted points
            weighted_points = points * credits
            total_points += weighted_points
            total_credits += credits
            
            courses.append({
                'name': course_name,
                'grade': grade,
                'credits': credits,
                'points': points
            })
        
        # Calculate GPA
        if total_credits > 0:
            gpa = total_points / total_credits
            
            print(f"\n📋 Transcript Summary:")
            print("-" * 40)
            for course in courses:
                print(f"{course['name']}: {course['grade']} ({course['credits']} credits)")
            
            print(f"\n📊 GPA Calculation:")
            print(f"Total Grade Points: {total_points:.1f}")
            print(f"Total Credits: {total_credits:.1f}")
            print(f"GPA: {gpa:.2f}")
            
            # GPA interpretation
            if gpa >= 3.5:
                print("🏆 Excellent! Dean's List material!")
            elif gpa >= 3.0:
                print("👍 Good work! Solid performance!")
            elif gpa >= 2.0:
                print("📚 Keep working! You can improve!")
            else:
                print("⚠️ Academic probation territory. Study harder!")
        
    except ValueError:
        print("❌ Error: Please enter valid numbers!")

# gpa_calculator()
```

### 🌍 **Real-World Applications of Averages**

**1. Sports Statistics:**
```python
def batting_average_calculator():
    """Calculate baseball batting average"""
    print("⚾ Batting Average Calculator")
    
    try:
        hits = int(input("Number of hits: "))
        at_bats = int(input("Number of at-bats: "))
        
        if at_bats == 0:
            print("❌ Cannot calculate average with zero at-bats!")
            return
        
        batting_avg = hits / at_bats
        
        print(f"\n📊 Batting Statistics:")
        print(f"Hits: {hits}")
        print(f"At-bats: {at_bats}")
        print(f"Batting Average: {batting_avg:.3f}")
        
        # Performance evaluation
        if batting_avg >= 0.300:
            print("🌟 All-Star level!")
        elif batting_avg >= 0.250:
            print("👍 Good hitter!")
        else:
            print("📈 Room for improvement!")
            
    except ValueError:
        print("❌ Please enter valid numbers!")
```

**2. Finance - Investment Returns:**
```python
def investment_return_calculator():
    """Calculate average investment return"""
    print("💰 Investment Return Calculator")
    
    try:
        initial_investment = float(input("Initial investment ($): "))
        final_value = float(input("Final value ($): "))
        years = float(input("Number of years: "))
        
        if years <= 0:
            print("❌ Years must be greater than zero!")
            return
        
        total_return = final_value - initial_investment
        annual_return = total_return / years
        return_percentage = (total_return / initial_investment) * 100
        
        print(f"\n📈 Investment Analysis:")
        print(f"Initial Investment: ${initial_investment:.2f}")
        print(f"Final Value: ${final_value:.2f}")
        print(f"Total Return: ${total_return:.2f}")
        print(f"Average Annual Return: ${annual_return:.2f}")
        print(f"Total Return Percentage: {return_percentage:.1f}%")
        
    except ValueError:
        print("❌ Please enter valid numbers!")
```

### 🔬 **Different Types of Averages**

```python
def advanced_averages():
    """Demonstrate different types of averages"""
    numbers = [2, 4, 6, 8, 10]
    
    print("📐 Different Types of Averages")
    print(f"Numbers: {numbers}")
    print("-" * 30)
    
    # Arithmetic Mean (regular average)
    arithmetic_mean = sum(numbers) / len(numbers)
    print(f"Arithmetic Mean: {arithmetic_mean}")
    
    # Geometric Mean (multiply all, then take nth root)
    import math
    geometric_mean = math.prod(numbers) ** (1/len(numbers))
    print(f"Geometric Mean: {geometric_mean:.2f}")
    
    # Harmonic Mean (for rates and ratios)
    harmonic_mean = len(numbers) / sum(1/x for x in numbers)
    print(f"Harmonic Mean: {harmonic_mean:.2f}")
    
    # Median (middle value)
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        median = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        median = sorted_numbers[n//2]
    print(f"Median: {median}")

# advanced_averages()
```

---

## 🔲 Exercise 6: `problem6.py` - The Square Master!

### 🎯 **The Challenge**
*"Write a Python program to calculate the square of a number entered by the user."*

### 📖 **What's Inside**
```python
num = int(input("Enter a number : "))

# First method
print("The square of the number is", num**2)

# Second method
print("The square of the number is", num*num)

# print("The square of the number is", num^2)  # invalid 
```

### 🎓 **Understanding Exponentiation**

This exercise teaches you about **exponentiation** - one of the most powerful mathematical operations in programming! Let's explore why there are different ways to calculate squares and when to use each.

### ⚠️ **Important Note About the `^` Operator**

The commented line `num^2` is **correctly marked as invalid**! In Python:
- `**` is the exponentiation operator (power)
- `^` is the XOR (exclusive or) bitwise operator - completely different!

```python
print(5 ** 2)  # 25 (five squared)
print(5 ^ 2)   # 7 (binary XOR: 101 XOR 010 = 111)
```

### 🌟 **Enhanced Square Calculator**

```python
def enhanced_square_calculator():
    """Calculate squares with multiple methods and insights"""
    print("🔲 Enhanced Square Calculator")
    print("-" * 30)
    
    try:
        num = float(input("Enter a number to square: "))
        
        # Method 1: Exponentiation operator (**)
        square_power = num ** 2
        
        # Method 2: Multiplication
        square_multiply = num * num
        
        # Method 3: Using math.pow()
        import math
        square_math = math.pow(num, 2)
        
        # Display results
        print(f"\n📊 Square of {num}:")
        print(f"Using ** operator: {square_power}")
        print(f"Using * operator: {square_multiply}")
        print(f"Using math.pow(): {square_math}")
        
        # Verify they're all the same
        print(f"\n✅ All methods give same result: {square_power == square_multiply == square_math}")
        
        # Additional insights
        print(f"\n💡 Mathematical Insights:")
        print(f"Original number: {num}")
        print(f"Square: {square_power}")
        print(f"Square root of square: {math.sqrt(square_power)}")
        
        # Visual representation for small positive integers
        if num == int(num) and 1 <= num <= 10:
            print(f"\n🎨 Visual representation ({int(num)} × {int(num)}):")
            for i in range(int(num)):
                print("■ " * int(num))
        
    except ValueError:
        print("❌ Error: Please enter a valid number!")

# enhanced_square_calculator()
```

### 🎮 **Power Calculator - Beyond Just Squares**

```python
def power_calculator():
    """Calculate any power, not just squares"""
    print("⚡ Universal Power Calculator")
    print("-" * 30)
    
    try:
        base = float(input("Enter the base number: "))
        exponent = float(input("Enter the exponent: "))
        
        # Calculate power
        result = base ** exponent
        
        # Display result with special cases
        print(f"\n📊 Result: {base}^{exponent} = {result}")
        
        # Special case interpretations
        if exponent == 2:
            print("📦 This is a square!")
        elif exponent == 3:
            print("📦 This is a cube!")
        elif exponent == 0.5:
            print("√ This is a square root!")
        elif exponent == 1:
            print("🔄 Any number to the power of 1 is itself!")
        elif exponent == 0:
            print("✨ Any number to the power of 0 is 1!")
        elif exponent < 0:
            print("🔄 Negative exponent means 1 divided by the positive power!")
            positive_result = base ** abs(exponent)
            print(f"   = 1 / {positive_result} = {result}")
        
        # Show related calculations
        if exponent == 2 and base > 0:
            print(f"\n🔍 Related calculations:")
            print(f"Square root: ±{math.sqrt(result)}")
            print(f"Cube: {base ** 3}")
            
    except ValueError:
        print("❌ Error: Please enter valid numbers!")
    except ZeroDivisionError:
        print("❌ Error: 0 to a negative power is undefined!")

# power_calculator()
```

### 🏗️ **Geometric Area Calculator**

```python
def geometric_calculator():
    """Calculate areas of different shapes (many involve squares!)"""
    print("📐 Geometric Area Calculator")
    print("-" * 30)
    
    shapes = {
        "1": "Square",
        "2": "Circle", 
        "3": "Rectangle",
        "4": "Triangle"
    }
    
    print("Choose a shape:")
    for key, shape in shapes.items():
        print(f"{key}. {shape}")
    
    choice = input("\nEnter your choice (1-4): ")
    
    try:
        if choice == "1":  # Square
            side = float(input("Enter side length: "))
            area = side ** 2  # This is where squaring is used!
            perimeter = 4 * side
            print(f"\n🔲 Square Results:")
            print(f"Side length: {side}")
            print(f"Area: {area} (side²)")
            print(f"Perimeter: {perimeter}")
            
        elif choice == "2":  # Circle
            radius = float(input("Enter radius: "))
            import math
            area = math.pi * (radius ** 2)  # π × r²
            circumference = 2 * math.pi * radius
            print(f"\n⭕ Circle Results:")
            print(f"Radius: {radius}")
            print(f"Area: {area:.2f} (π × radius²)")
            print(f"Circumference: {circumference:.2f}")
            
        elif choice == "3":  # Rectangle
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            area = length * width
            perimeter = 2 * (length + width)
            print(f"\n📱 Rectangle Results:")
            print(f"Length: {length}, Width: {width}")
            print(f"Area: {area}")
            print(f"Perimeter: {perimeter}")
            
        elif choice == "4":  # Triangle
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            area = 0.5 * base * height
            print(f"\n🔺 Triangle Results:")
            print(f"Base: {base}, Height: {height}")
            print(f"Area: {area} (½ × base × height)")
            
        else:
            print("❌ Invalid choice!")
            
    except ValueError:
        print("❌ Error: Please enter valid numbers!")

# geometric_calculator()
```

### 🧮 **Perfect Squares Explorer**

```python
def perfect_squares_explorer():
    """Explore perfect squares and their properties"""
    print("✨ Perfect Squares Explorer")
    print("-" * 30)
    
    try:
        limit = int(input("Show perfect squares up to what number? "))
        
        if limit <= 0:
            print("❌ Please enter a positive number!")
            return
        
        print(f"\n🔢 Perfect squares from 1 to {limit}:")
        print("-" * 40)
        
        perfect_squares = []
        
        # Find all perfect squares up to the limit
        i = 1
        while i * i <= limit:
            square = i * i
            perfect_squares.append((i, square))
            print(f"{i}² = {square}")
            i += 1
        
        print(f"\n📊 Summary:")
        print(f"Found {len(perfect_squares)} perfect squares up to {limit}")
        print(f"Perfect squares: {[sq[1] for sq in perfect_squares]}")
        
        # Check if user's limit is a perfect square
        import math
        sqrt_limit = math.sqrt(limit)
        if sqrt_limit == int(sqrt_limit):
            print(f"🎯 {limit} is a perfect square! ({int(sqrt_limit)}²)")
        else:
            next_perfect = int(sqrt_limit + 1) ** 2
            prev_perfect = int(sqrt_limit) ** 2
            print(f"📍 {limit} is between {prev_perfect} and {next_perfect}")
        
    except ValueError:
        print("❌ Error: Please enter a valid integer!")

# perfect_squares_explorer()
```

### 🎯 **Number Properties Analyzer**

```python
def number_properties_analyzer():
    """Analyze various properties of a number including its square"""
    print("🔬 Number Properties Analyzer")
    print("-" * 30)
    
    try:
        num = float(input("Enter a number to analyze: "))
        
        print(f"\n📋 Analysis of {num}:")
        print("-" * 25)
        
        # Basic properties
        print(f"Original number: {num}")
        print(f"Absolute value: {abs(num)}")
        print(f"Square: {num ** 2}")
        print(f"Cube: {num ** 3}")
        
        if num >= 0:
            import math
            print(f"Square root: {math.sqrt(num):.4f}")
        else:
            print("Square root: Not real (negative number)")
        
        # Integer properties (if it's a whole number)
        if num == int(num):
            num_int = int(num)
            print(f"\n🔢 Integer Properties:")
            print(f"Is even: {num_int % 2 == 0}")
            print(f"Is odd: {num_int % 2 != 0}")
            
            # Check if it's a perfect square
            if num_int >= 0:
                sqrt_val = int(math.sqrt(num_int))
                is_perfect_square = sqrt_val * sqrt_val == num_int
                print(f"Is perfect square: {is_perfect_square}")
                if is_perfect_square:
                    print(f"Square root: {sqrt_val}")
        
        # Powers table
        print(f"\n⚡ Powers of {num}:")
        for power in range(1, 6):
            result = num ** power
            print(f"{num}^{power} = {result}")
        
        # Special mathematical constants comparison
        import math
        if abs(num - math.pi) < 0.01:
            print("\n🥧 This is very close to π!")
        elif abs(num - math.e) < 0.01:
            print("\n📊 This is very close to e (Euler's number)!")
        
    except ValueError:
        print("❌ Error: Please enter a valid number!")

# number_properties_analyzer()
```

### 🌍 **Real-World Applications of Squares**

**1. Area Calculations:**
- Square rooms, plots of land
- Quadratic equations in physics
- Statistical variance calculations

**2. Physics:**
- Kinetic energy: KE = ½mv²
- Distance formula: d = √[(x₂-x₁)² + (y₂-y₁)²]
- Pythagorean theorem: a² + b² = c²

**3. Computer Graphics:**
- Pixel calculations
- Distance measurements
- 3D rendering

---

## 🎓 Chapter Summary: From Beginner to Problem Solver!

Congratulations! You've just completed an incredible journey through the practical application of variables, data types, and operators. Let's celebrate what you've accomplished!

### ✅ **Skills You've Mastered**

1. **Interactive Programming** - Your programs now talk to users!
2. **Safe Input Handling** - You can prevent crashes from invalid input
3. **Type Conversion** - You understand when and how to convert data types
4. **Mathematical Operations** - From basic arithmetic to complex calculations
5. **Comparison Logic** - You can make programs that make decisions
6. **Real-World Problem Solving** - You've built actual useful programs!

### 🌟 **Programs You Can Now Build**

- ✨ **Calculators** - Basic to advanced mathematical tools
- 🎯 **Quiz Games** - Interactive educational programs
- 📊 **Data Analyzers** - Statistical calculation tools
- 🔐 **Validation Systems** - Input checking and verification
- 🎮 **Simple Games** - Number guessing, comparison challenges
- 📈 **Financial Tools** - GPA calculators, investment analyzers

### 🚀 **Real-World Skills Gained**

- **Problem Decomposition** - Breaking complex problems into simple steps
- **Error Handling** - Making robust programs that don't crash
- **User Experience** - Creating programs that are easy to use
- **Data Validation** - Ensuring input is correct and safe
- **Mathematical Thinking** - Applying math concepts in code

### 💡 **Key Programming Concepts Internalized**

1. **Always validate user input** - Users will type unexpected things!
2. **Plan your data types** - Know what kind of data you're working with
3. **Use meaningful variable names** - Your future self will thank you
4. **Test edge cases** - What happens with zero, negative numbers, very large numbers?
5. **Provide clear feedback** - Users should know what to expect

### 🎯 **Common Patterns You've Learned**

**The Input-Process-Output Pattern:**
```python
# Input: Get data from user
data = input("Enter something: ")

# Process: Transform or analyze the data
result = process_data(data)

# Output: Show results to user
print(f"Result: {result}")
```

**The Validation Loop:**
```python
while True:
    try:
        value = int(input("Enter a number: "))
        break  # Exit loop if successful
    except ValueError:
        print("Please enter a valid number!")
```

**The Menu-Driven Program:**
```python
print("Choose an option:")
print("1. Option A")
print("2. Option B")
choice = input("Your choice: ")

if choice == "1":
    # Do option A
elif choice == "2":
    # Do option B
```

### 🔧 **Debugging Skills Developed**

- **Reading error messages** - Understanding what Python is telling you
- **Type checking** - Using `type()` to investigate your data
- **Step-by-step testing** - Breaking problems into smaller pieces
- **Edge case thinking** - Considering unusual inputs

### 🌍 **Professional Programming Practices**

- **Code organization** - Grouping related functionality
- **User-friendly interfaces** - Clear prompts and helpful error messages
- **Documentation** - Comments that explain the why, not just the what
- **Error handling** - Graceful handling of unexpected situations

### 🎮 **Fun Challenges to Continue Learning**

1. **Temperature Converter** - Celsius, Fahrenheit, Kelvin
2. **BMI Calculator** - With health category interpretation
3. **Compound Interest Calculator** - For financial planning
4. **Distance Calculator** - Between two points
5. **Unit Converter** - Length, weight, volume conversions
6. **Tip Calculator** - For restaurant bills
7. **Loan Payment Calculator** - Monthly payment estimator

### 💭 **Reflection Questions**

- Which exercise challenged you the most? Why?
- What concept clicked for you during these exercises?
- How would you explain variables to a friend who's never programmed?
- What real-world problem would you like to solve with programming?

### 🚀 **What's Next?**

You're now ready for **Chapter 3: Strings** where you'll learn to:
- Manipulate and format text
- Search and replace text patterns
- Build text-based applications
- Handle complex string operations

The foundation you've built with variables, types, and operators will be essential as you dive into the world of text processing!

---

## 🎉 Celebration Time!

You've just completed exercises that many programming students find challenging. You've gone from simple variable assignments to building interactive programs that solve real problems. This is no small achievement!

**Remember:**
- Every expert programmer started with exercises just like these
- The skills you've learned here are the building blocks for everything else in programming
- You're developing problem-solving abilities that go far beyond just coding

### 💪 **You Are Now Capable Of:**

- Creating programs that interact with users
- Handling different types of data safely
- Performing mathematical calculations programmatically  
- Building simple but useful tools
- Debugging common programming issues
- Writing code that others can understand

Keep this momentum going! The journey gets more exciting from here as you learn to work with text, make decisions with if statements, and create loops that can process large amounts of data.

You're not just learning Python - you're becoming a problem solver! 🐍✨

---

**Previous Chapter:** [Chapter 2 - Variables and Data Types](../chapter_02/README.md)  
**Next Chapter:** [Chapter 3 - Strings](../chapter_03/README.md)  
**Main Concepts:** [Chapter 2 Overview](../chapter_02/README.md)

---

*"Programming is not about what you know; it's about what you can figure out."* - Chris Pine 🌟
