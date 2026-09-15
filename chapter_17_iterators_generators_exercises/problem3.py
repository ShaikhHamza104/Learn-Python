"""
📚 Topic: Memory Benchmarking: List vs Generator

This script benchmarks memory consumption between an eager list comprehension
and a lazy generator expression using `sys.getsizeof()`.

💡 Key points:
    1️⃣ Eager evaluation: lists allocate full sequence memory up-front
    2️⃣ Lazy evaluation: generators maintain constant O(1) memory footprint
    3️⃣ Quantifying memory differences using `sys.getsizeof()`
"""

import sys


def compare_memory(count: int = 100_000):
    """Compare memory sizes between list comprehension and generator."""
    # List comprehension allocates all 100,000 integers in RAM
    eager_list = [x ** 2 for x in range(count)]
    list_memory = sys.getsizeof(eager_list)

    # Generator expression produces values on demand
    lazy_gen = (x ** 2 for x in range(count))
    gen_memory = sys.getsizeof(lazy_gen)

    print(f"Memory for {count:,} items:")
    print(f"  List comprehension : {list_memory:,} bytes")
    print(f"  Generator expression: {gen_memory:,} bytes")
    print(f"  Ratio (List / Gen) : {list_memory / gen_memory:.1f}x larger")


def main():
    compare_memory()


if __name__ == "__main__":
    main()
