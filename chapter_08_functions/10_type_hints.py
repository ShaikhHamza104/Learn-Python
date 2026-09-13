"""
📚 Topic: Type Hints in Python

This script demonstrates type hints in python using basic Python syntax.

💡 Key points:
    1️⃣ the basic syntax for type hints in python
    2️⃣ how basic Python syntax fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how type
    hints in python affects the result.
"""

from __future__ import annotations

import abc
import dataclasses
from collections.abc import Callable, Iterable, Iterator
from typing import (
    Annotated,
    Any,
    ClassVar,
    Concatenate,
    Final,
    Generic,
    Literal,
    Never,
    NewType,
    NoReturn,
    NotRequired,
    ParamSpec,
    Protocol,
    Required,
    Self,
    TypeAlias,
    TypedDict,
    TypeGuard,
    TypeVar,
    overload,
    runtime_checkable,
)

# ============================================================
# 1. BASIC TYPE HINTS (Built-in types)
# ============================================================
print("=" * 60)
print("1. BASIC TYPE HINTS")
print("=" * 60)


def basic_hints(
    name: str,
    age: int,
    height: float,
    is_active: bool,
    data: bytes,
    items: list[int],  # Generic alias (PEP 585 - 3.9+)
    mapping: dict[str, int],  # Generic alias (PEP 585)
    pair: tuple[int, str],  # Generic alias (PEP 585)
    unique: set[str],  # Generic alias (PEP 585)
) -> None:
    """Basic type hints using built-in types and PEP 585 generics."""
    print(f"  name={name}, age={age}, items={items}")


basic_hints("Hamza", 30, 5.6, True, b"data", [1, 2], {"a": 1}, (1, "x"), {"a"})


# ============================================================
# 2. OPTIONAL, UNION, AND ANY
# ============================================================
print("\n" + "=" * 60)
print("2. OPTIONAL, UNION, AND ANY")
print("=" * 60)


def find_user(user_id: int) -> str | None:
    """Returns a user name or None."""
    return "Hamza" if user_id == 1 else None


def process(value: str | float) -> str:
    """Accepts multiple types using Union."""
    return f"{value} (type: {type(value).__name__})"


def flexible(data: Any) -> Any:
    """Any allows any type - use sparingly."""
    return data


# PEP 604 syntax (Python 3.10+) - cleaner alternative to Union/Optional
def modern_union(value: int | str) -> int | None:
    if isinstance(value, int):
        return value
    return None


print(f"  find_user(1) = {find_user(1)}")
print(f"  process(42) = {process(42)}")
print(f"  modern_union('hi') = {modern_union('hi')}")


# ============================================================
# 3. TYPE ALIASES (TypeAlias - PEP 613)
# ============================================================
print("\n" + "=" * 60)
print("3. TYPE ALIASES")
print("=" * 60)

# Simple alias
UserId: TypeAlias = int
Vector: TypeAlias = list[float]
Matrix: TypeAlias = list[Vector]


def scale_vector(v: Vector, factor: float) -> Vector:
    return [x * factor for x in v]


scaled = scale_vector([1.0, 2.0, 3.0], 2.0)
print(f"  scale_vector([1.0, 2.0, 3.0], 2.0) = {scaled}")


# ============================================================
# 4. NEW TYPE (Distinct type for type checking)
# ============================================================
print("\n" + "=" * 60)
print("4. NEW TYPE")
print("=" * 60)

UserId2 = NewType("UserId2", int)
ProductId = NewType("ProductId", str)


def get_user(uid: UserId2) -> str:
    return f"User-{uid}"


# These are still ints/strs at runtime, but distinct for type checkers
uid = UserId2(42)
pid = ProductId("P-001")
print(f"  get_user(uid) = {get_user(uid)}")
print(f"  pid = {pid}")


# ============================================================
# 5. CALLABLE TYPES
# ============================================================
print("\n" + "=" * 60)
print("5. CALLABLE TYPES")
print("=" * 60)


def apply_function(
    func: Callable[[int, int], int],
    a: int,
    b: int,
) -> int:
    """func takes two ints and returns an int."""
    return func(a, b)


# Callable with variable arguments
def variadic_func(operations: Callable[..., None]) -> None:
    operations(1, 2, 3, key="value")


applied_result = apply_function(lambda x, y: x + y, 3, 4)
print(f"  apply_function(lambda x, y: x + y, 3, 4)={applied_result}")


# ============================================================
# 6. GENERIC TYPES (TypeVar and Generic)
# ============================================================
print("\n" + "=" * 60)
print("6. GENERIC TYPES")
print("=" * 60)

T = TypeVar("T")
U = TypeVar("U")
V = TypeVar("V")


class Stack(Generic[T]):
    """A generic Stack class."""

    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()


# Bounded TypeVar
Number = TypeVar("Number", int, float)


def add_numbers(a: Number, b: Number) -> Number:
    return a + b


# Constrained TypeVar with multiple parameters
def zip_pairs(
    first: Iterable[T],
    second: Iterable[U],
) -> Iterator[tuple[T, U]]:
    return zip(first, second)


stack: Stack[int] = Stack()
stack.push(1)
stack.push(2)
print(f"  Stack pop: {stack.pop()}")
print(f"  add_numbers(3, 4): {add_numbers(3, 4)}")


# ============================================================
# 7. PARAMSPEC AND CONCATENATE (PEP 612)
# ============================================================
print("\n" + "=" * 60)
print("7. PARAMSPEC AND CONCATENATE")
print("=" * 60)

P = ParamSpec("P")
R = TypeVar("R")


def decorator(func: Callable[P, R]) -> Callable[P, R]:
    """A decorator that preserves the function's signature."""

    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"    [decorator] Calling {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@decorator
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"


print(f"  greet('Hamza'): {greet('Hamza')}")


# Concatenate - for adding parameters
def with_logging(
    func: Callable[Concatenate[str, P], R],
) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"    [logging] {func.__name__} called")
        return func("LOG_PREFIX", *args, **kwargs)

    return wrapper


# ============================================================
# 8. LITERAL TYPES (PEP 586)
# ============================================================
print("\n" + "=" * 60)
print("8. LITERAL TYPES")
print("=" * 60)

Mode = Literal["read", "write", "append"]
Status = Literal[200, 404, 500]


def open_file(path: str, mode: Mode) -> str:
    return f"Opening {path} in mode '{mode}'"


print(f"  {open_file('file.txt', 'read')}")


# ============================================================
# 9. FINAL AND CLASSVAR
# ============================================================
print("\n" + "=" * 60)
print("9. FINAL AND CLASSVAR")
print("=" * 60)

MAX_SIZE: Final = 100  # Cannot be reassigned


class Configuration:
    """Class demonstrating ClassVar and Final."""

    VERSION: ClassVar[str] = "1.0"  # Shared by all instances
    name: str  # Instance variable
    MAX_CONNECTIONS: Final[int] = 10  # Cannot be overridden


cfg = Configuration()
cfg.name = "test"
print(f"  Configuration.VERSION = {Configuration.VERSION}")
print(f"  cfg.name = {cfg.name}")


# ============================================================
# 10. TYPEDDICT (PEP 589)
# ============================================================
print("\n" + "=" * 60)
print("10. TYPEDDICT")
print("=" * 60)


class UserDict(TypedDict):
    """A TypedDict for user information."""

    name: str
    age: int
    email: str


class FlexibleDict(TypedDict, total=False):
    name: str
    age: NotRequired[int]  # Optional in total=False context
    email: Required[str]  # Required even in total=False


user: UserDict = {"name": "Bob", "age": 25, "email": "bob@example.com"}
print(f"  user dict: {user}")


# ============================================================
# 11. PROTOCOLS (Structural subtyping - PEP 544)
# ============================================================
print("\n" + "=" * 60)
print("11. PROTOCOLS (Structural Subtyping)")
print("=" * 60)


@runtime_checkable
class Drawable(Protocol):
    """Any class with a draw method implements this protocol."""

    def draw(self) -> None: ...


class Circle:
    def draw(self) -> None:
        print("    Drawing a circle")


class Square:
    def draw(self) -> None:
        print("    Drawing a square")


def render(shape: Drawable) -> None:
    shape.draw()


# Both Circle and Square satisfy the Drawable protocol structurally
render(Circle())
render(Square())


# ============================================================
# 12. ANNOTATED (PEP 593)
# ============================================================
print("\n" + "=" * 60)
print("12. ANNOTATED")
print("=" * 60)


def validate_age(
    name: Annotated[str, "must not be empty"],
    age: Annotated[int, "must be >= 0", "max value is 150"],
) -> None:
    print(f"    Validating: {name} is {age} years old")


validate_age("Charlie", 30)


# ============================================================
# 13. SELF TYPE (PEP 673 - Python 3.11)
# ============================================================
print("\n" + "=" * 60)
print("13. SELF TYPE (Python 3.11+)")
print("=" * 60)


class Builder:
    """Demonstrates Self type for fluent interfaces."""

    items: list[str]

    def __init__(self) -> None:
        self.items = []

    def add(self, item: str) -> Self:
        self.items.append(item)
        return self

    def build(self) -> list[str]:
        return self.items


b: Builder = Builder().add("a").add("b").add("c")
print(f"  Builder chain result: {b.build()}")


# ============================================================
# 14. NEVER TYPE AND NORETURN (Python 3.11+)
# ============================================================
print("\n" + "=" * 60)
print("14. NEVER TYPE (Python 3.11+)")
print("=" * 60)


def assert_never(value: Never) -> NoReturn:
    """Used in exhaustive checks - value should be of type Never
    (impossible)."""
    raise AssertionError(f"Unexpected value: {value}")


def handle_status(status: int) -> str:
    if status == 200:
        return "OK"
    elif status == 404:
        return "Not Found"
    # If more statuses are added, type checker will flag this
    return assert_never(status)  # type: ignore[arg-type]


print(f"  handle_status(200) = {handle_status(200)}")


# ============================================================
# 15. DATACLASSES WITH TYPE HINTS
# ============================================================
print("\n" + "=" * 60)
print("15. DATACLASSES WITH TYPE HINTS")
print("=" * 60)


@dataclasses.dataclass(frozen=True, slots=True)
class Point:
    """A frozen dataclass with slots - immutable."""

    x: float
    y: float

    def distance_from_origin(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5


@dataclasses.dataclass
class Person:
    """A regular dataclass with defaults and field metadata."""

    name: str
    age: int = 0
    email: str | None = None
    tags: list[str] = dataclasses.field(default_factory=list)


p = Point(3.0, 4.0)
person = Person("Diana", 28)
print(f"  Point(3,4) distance: {p.distance_from_origin()}")
print(f"  Person: {person}")


# ============================================================
# 16. VARIANCE ANNOTATIONS (TypeVar with variance)
# ============================================================
print("\n" + "=" * 60)
print("16. VARIANCE ANNOTATIONS")
print("=" * 60)

# Covariant - T is produced (output only)
T_co = TypeVar("T_co", covariant=True)

# Contravariant - T is consumed (input only)
T_contra = TypeVar("T_contra", contravariant=True)

# Invariant - default (both input and output)
T_in = TypeVar("T_in")


class Producer(Generic[T_co]):
    """Producer - covariant: if Cat is Animal, Producer[Cat] is
    Producer[Animal]."""

    def get(self) -> T_co: ...


class Consumer(Generic[T_contra]):
    """Consumer - contravariant: if Cat is Animal, Consumer[Animal] is
    Consumer[Cat]."""

    def consume(self, item: T_contra) -> None: ...


print("""
Producer[T] is covariant; Consumer[T] is contravariant;
Box[T] is invariant.""")

# ============================================================
# 17. ABSTRACT BASE CLASSES WITH TYPE HINTS
# ============================================================
print("\n" + "=" * 60)
print("17. ABSTRACT BASE CLASSES")
print("=" * 60)


class Animal(abc.ABC):
    @abc.abstractmethod
    def speak(self) -> str: ...


class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"


animals: list[Animal] = [Dog()]
print(f"  Animal speaks: {animals[0].speak()}")


# ============================================================
# 18. TYPE GUARDS (PEP 647)
# ============================================================
print("\n" + "=" * 60)
print("18. TYPE GUARDS")
print("=" * 60)


def is_string_list(val: list[object]) -> TypeGuard[list[str]]:
    """Narrowing: if returns True, the value is list[str]."""
    return all(isinstance(x, str) for x in val)


def is_pair(val: object) -> TypeGuard[tuple[int, str]]:
    return (
        isinstance(val, tuple)
        and len(val) == 2
        and isinstance(val[0], int)
        and isinstance(val[1], str)
    )


mixed: list[object] = ["a", "b", "c"]
if is_string_list(mixed):
    joined: str = "".join(mixed)
    print(f"  Joined string list: {joined}")

val: object = (1, "hello")
if is_pair(val):
    num, word = val
    print(f"  Pair unpacked: {num}, {word}")


# ============================================================
# 19. RECURSIVE TYPES
# ============================================================
print("\n" + "=" * 60)
print("19. RECURSIVE TYPES")
print("=" * 60)


class TreeNode(Generic[T]):
    """A binary tree node - requires `from __future__ import annotations`."""

    def __init__(
        self,
        value: T,
        left: TreeNode[T] | None = None,
        right: TreeNode[T] | None = None,
    ) -> None:
        self.value = value
        self.left = left
        self.right = right


# Recursive type using Python 3.10+ union pipe syntax
JSON: TypeAlias = (
    None | bool | int | float | str | list["JSON"] | dict[str, "JSON"]
)


def serialize(data: JSON) -> str:
    import json

    return json.dumps(data)


root: TreeNode[int] = TreeNode(1, TreeNode(2), TreeNode(3))
print(f"  Tree root value: {root.value}")
print(f"  JSON serialize: {serialize({'key': [1, 2, {'nested': True}]})}")


# ============================================================
# 20. OVERLOAD (Function with multiple signatures)
# ============================================================
print("\n" + "=" * 60)
print("20. FUNCTION OVERLOADS")
print("=" * 60)


@overload
def process_value(value: int) -> int: ...


@overload
def process_value(value: str) -> str: ...


@overload
def process_value(value: list[int]) -> list[int]: ...


def process_value(value):
    """Actual implementation - type checker uses @overload decorators above."""
    if isinstance(value, int):
        return value * 2
    elif isinstance(value, str):
        return value.upper()
    elif isinstance(value, list):
        return [x * 2 for x in value]
    raise TypeError(f"Unsupported type: {type(value)}")


print(f"  process_value(5) = {process_value(5)}")
print(f"  process_value('hi') = {process_value('hi')}")
print(f"  process_value([1, 2, 3]) = {process_value([1, 2, 3])}")


print("\n" + "=" * 60)
print("All type hinting demonstrations completed!")
print("=" * 60)
