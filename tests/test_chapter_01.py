"""
Tests for chapter_01_basics.

Files in chapter_01_basics are numbered (01_hello_world.py, etc.), so
they can't be imported with a normal `import` statement — Python
identifiers can't start with a digit. We load them directly from their
file path using importlib instead, which lets us test the real code.
"""

import importlib.util
import pathlib
import unittest
from unittest.mock import patch

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent / "chapter_01_basics"


def load_module(filename, module_name):
    """Load a numbered .py file as an importable module object."""
    file_path = BASE_DIR / filename
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestChapter1(unittest.TestCase):

    def test_hello_world(self):
        # Both files are guarded by `if __name__ == "__main__":`, so
        # importing them does NOT auto-run anything — we call main()
        # ourselves and check it prints the real expected output.
        hello_world = load_module("01_hello_world.py", "hello_world")
        with patch("builtins.print") as mock_print:
            hello_world.main()
        mock_print.assert_called_with("Hello, world!")

    @patch("pyjokes.get_joke", return_value="This is a test joke.")
    def test_module_example(self, mock_get_joke):
        module_example = load_module("02_module_example.py", "module_example")
        with patch("builtins.print") as mock_print:
            module_example.print_joke()
        mock_get_joke.assert_called_once()
        mock_print.assert_called_with("This is a test joke.")

    def test_comment_example(self):
        # This file has no functions — it's top-level script code that
        # runs immediately on import, so we patch print BEFORE loading it.
        with patch("builtins.print") as mock_print:
            load_module("02_comment_example.py", "comment_example")
        mock_print.assert_any_call("Hello World!")
        mock_print.assert_any_call("My name is Hamza Shaikh")


if __name__ == "__main__":
    unittest.main()
