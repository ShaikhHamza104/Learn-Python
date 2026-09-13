"""
📚 Topic: Iterator Protocol

This script demonstrates what iteration, iterables and iterators are,
and how Python's for loop actually works behind the scenes using
iter() and next().

💡 Key points:
    1️⃣ the basic syntax for iter() and next()
    2️⃣ how a custom __iter__ / __next__ class fits into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    the iterator protocol affects the result.
"""

import sys

# ---------------------------------------------------
# What is Iteration?
# ---------------------------------------------------
# Iteration just means taking each item of something, one after another.
# Any time you use a loop (explicit or implicit) to go over a group of
# items, that is iteration.
num = [1, 2, 3]

for i in num:
    print(i)

# ---------------------------------------------------
# What is an Iterator?
# ---------------------------------------------------
# An Iterator is an object that lets you go through a sequence of data
# WITHOUT storing the entire data in memory at once.
# This is why range() is so much lighter than a full list.
L = [x for x in range(1, 10000)]
print(sys.getsizeof(L) / 64)  # a real list takes real memory

x = range(1, 10000000000)
print(sys.getsizeof(x) / 64)  # range barely takes any memory

# ---------------------------------------------------
# What is an Iterable?
# ---------------------------------------------------
# An Iterable is any object you CAN loop over.
# It becomes an Iterator only when you pass it to iter().
L = [1, 2, 3]
print(type(L))  # L is an iterable -> list
print(type(iter(L)))  # iter(L) turns it into an iterator -> list_iterator

# ---------------------------------------------------
# Point to remember
# ---------------------------------------------------
# - Every Iterator is also an Iterable
# - Not all Iterables are Iterators
# - Every Iterable has an __iter__ method
# - Every Iterator has BOTH __iter__ AND __next__ methods

# ---------------------------------------------------
# Understanding how the for loop REALLY works
# ---------------------------------------------------
num = [1, 2, 3]

# step 1: get the iterator
iter_num = iter(num)

# step 2: keep calling next() until it runs out
print(next(iter_num))
print(next(iter_num))
print(next(iter_num))
# calling next() one more time here would raise StopIteration


# ---------------------------------------------------
# Making our own for loop using iter() and next()
# ---------------------------------------------------
def mera_khudka_for_loop(iterable):
    iterator = iter(iterable)

    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break


mera_khudka_for_loop([1, 2, 3])


# ---------------------------------------------------
# Building our own range() using the iterator protocol
# ---------------------------------------------------
class MeraRange:
    """A custom iterable that behaves like Python's built-in range()."""

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return MeraRangeIterator(self)


class MeraRangeIterator:
    """The iterator that actually walks through MeraRange's numbers."""

    def __init__(self, iterable_obj):
        self.iterable = iterable_obj

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterable.start >= self.iterable.end:
            raise StopIteration

        current = self.iterable.start
        self.iterable.start += 1
        return current


for number in MeraRange(1, 6):
    print(number)


# ---------------------------------------------------
# 💡 Why this matters for Data Science
# ---------------------------------------------------
# Real datasets can be huge. Iterators let you process data one item at
# a time without loading everything into memory - exactly how range()
# stays small even for 10 billion numbers above.
