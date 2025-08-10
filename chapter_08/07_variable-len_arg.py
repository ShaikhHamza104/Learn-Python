def add(*args):
    return sum(args)

result = add(1, 2, 3, 4)  # *args collects all positional arguments into a tuple
print(result)  # Output: 10


def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Alice", age=30, city="New York")  # **kwargs collects all keyword arguments into a dictionary
# Output:
# name: Alice
# age: 30
# city: New York
