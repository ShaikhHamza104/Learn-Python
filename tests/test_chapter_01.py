import unittest
from unittest.mock import patch
from chapter_01 import hello_world, module_example, comment_example

class TestChapter1(unittest.TestCase):

    @patch('builtins.print')
    def test_hello_world(self, mock_print):
        hello_world.main()
        mock_print.assert_called_with("Hello, world!")

    @patch('pyjokes.get_joke', return_value="This is a test joke.")
    @patch('builtins.print')
    def test_module(self, mock_print, mock_get_joke):
        module_example.print_joke()
        mock_print.assert_called_with("This is a test joke.")

    @patch('builtins.print')
    def test_comment(self, mock_print):
        comment_example.main()
        mock_print.assert_any_call("This line is not a comment.")
        mock_print.assert_any_call("This line is also not a comment.")

if __name__ == '__main__':
    unittest.main()
