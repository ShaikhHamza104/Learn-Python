"""
📚 Topic: Memory-Efficient Fibonacci Generator

This script demonstrates implementing a generator function with `yield` to
produce Fibonacci numbers on demand without storing the full sequence.

💡 Key points:
    1️⃣ Using `yield` to emit values lazily one at a time
    2️⃣ Maintaining state locally across invocations
    3️⃣ Terminating naturally when reaching the specified limit
"""


def fibonacci_gen(limit: int):
    """Yield Fibonacci numbers up to the specified count limit."""
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


def main():
    print("First 10 Fibonacci numbers:")
    for num in fibonacci_gen(10):
        print(num, end=" ")
    print()


if __name__ == "__main__":
    main()
