"""

📚 Topic: Named Tuple

This script demonstrates how to create and use named tuples.

💡 Key points:

    1️⃣ How to create a named tuple using namedtuple

    2️⃣ How to create a named tuple using keyword arguments

    3️⃣ How to use _asdict() and _replace()

🧠 Beginner tip:

    Run this file and change the values of x and y to see how

    the named tuple changes.

"""


from collections import namedtuple


def main():

    """

    This function provides examples of named tuples.

    """

    # Create a named tuple type

    Point = namedtuple("Point", ["x", "y"])

    # Create a Point object using positional arguments

    point = Point(10, 20)

    print(f"Point: {point}")

    print(f"X coordinate: {point.x}")

    print(f"Y coordinate: {point.y}")

    # Create a Point object using a dictionary

    data = {"x": 200, "y": 300}

    point_from_dict = Point(**data)

    print(f"Point from dictionary: {point_from_dict}")

    # Convert the named tuple to a dictionary
    print(f"As dictionary: {point_from_dict._asdict()}")

    # Create a new named tuple with a replaced value

    updated_point = point_from_dict._replace(x=43)

    print(f"Updated point: {updated_point}")

    # Original named tuple is unchanged

    print(f"Original point: {point_from_dict}")


if __name__ == "__main__":

    main()
