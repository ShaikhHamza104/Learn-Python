"""
📚 Topic: Generator Functions

This script demonstrates how to create generators using the yield
keyword, and why they are easier and more memory-friendly than writing
a full iterator class.

💡 Key points:
    1️⃣ the basic syntax for yield inside a function
    2️⃣ how next() and for loops fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    generator functions affects the result.
"""


# ---------------------------------------------------
# A simple generator example
# ---------------------------------------------------
# A generator function looks just like a normal function, but it uses
# "yield" instead of "return". Each yield pauses the function and
# remembers exactly where it left off.
def gen_demo():
    yield "first statement"
    yield "second statement"
    yield "third statement"


gen = gen_demo()

for statement in gen:
    print(statement)


# ---------------------------------------------------
# Example 2: generating squares one at a time
# ---------------------------------------------------
def square(num):
    for i in range(1, num + 1):
        yield i**2


gen = square(10)

# you can call next() manually...
print(next(gen))
print(next(gen))
print(next(gen))

# ...and then keep going with a normal for loop from where it left off
for value in gen:
    print(value)


# ---------------------------------------------------
# Recreating range() using a generator (much shorter than a class!)
# ---------------------------------------------------
def mera_range(start, end):
    for i in range(start, end):
        yield i


for number in mera_range(15, 21):
    print(number)


# ---------------------------------------------------
# Benefit 1: Ease of implementation
# ---------------------------------------------------
# Compare this ONE function...
def mera_range_generator(start, end):
    for i in range(start, end):
        yield i


# ...to the TWO full classes (MeraRange + MeraRangeIterator) we had to
# write in 01_iterator_protocol.py to do the exact same thing.
# Generators give you the iterator protocol for free.


# ---------------------------------------------------
# Benefit 2: Representing infinite streams
# ---------------------------------------------------
# A generator can represent something that never ends - a list never could.
def all_even():
    n = 0
    while True:
        yield n
        n += 2


even_num_gen = all_even()
print(next(even_num_gen))
print(next(even_num_gen))
print(next(even_num_gen))
# this could keep going forever - we just stop asking for more


# ---------------------------------------------------
# Benefit 3: Chaining generators together
# ---------------------------------------------------
def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x + y
        yield x


def square_each(nums):
    for num in nums:
        yield num**2


# fibonacci_numbers() feeds directly into square_each() - nothing is
# ever fully stored in memory at once
print(sum(square_each(fibonacci_numbers(10))))


# ---------------------------------------------------
# ⚠️ Common mistake
# ---------------------------------------------------
# Trying to reuse a generator after it's exhausted - once a generator
# has yielded everything (or hit StopIteration), it's empty forever.
# You need to call the generator function again to get a fresh one.
