"""
📚 Topic: Custom Countdown Iterator Class

This script demonstrates building a custom iterator class adhering to Python's
iterator protocol using `__iter__()` and `__next__()`.

💡 Key points:
    1️⃣ Implementing `__iter__()` returning `self`
    2️⃣ Implementing `__next__()` to produce descending values
    3️⃣ Raising `StopIteration` when the countdown reaches zero
"""


class Countdown:
    """An iterator that counts down from a given start number to zero."""

    def __init__(self, start: int):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val


def main():
    print("Countdown from 5:")
    counter = Countdown(5)
    for number in counter:
        print(number)


if __name__ == "__main__":
    main()
