import unittest
from unittest.mock import patch
from io import StringIO
from A import a

class BFunctionTest(unittest.TestCase):
    @patch('builtins.input', side_effect=['a'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_one_word(self, mock_stdout, mock_input):
        a()
        self.assertEqual(mock_stdout.getvalue().strip(), 'a')

    @patch('builtins.input', side_effect=['a  b c'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_many_spaces(self, mock_stdout, mock_input):
        a()
        self.assertEqual(mock_stdout.getvalue().strip(), 'c b a')

    @patch('builtins.input', side_effect=['ana con da  boo  o caaaa'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_just_words(self, mock_stdout, mock_input):
        a()
        self.assertEqual(mock_stdout.getvalue().strip(), 'caaaa o boo da con ana')

    @patch('builtins.input', side_effect=['hello let’s play today'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_example(self, mock_stdout, mock_input):
        a()
        self.assertEqual(mock_stdout.getvalue().strip(), 'today play let’s hello')

    @patch('builtins.input', side_effect=['hello let’s play today hello let’s play today hello let’s play today hello let’s play today hello let’s play today hello let’s play today hello let’s play today hello let’s play today hello let’s play today hello let’s play today '])
    @patch('sys.stdout', new_callable=StringIO)
    def test_big(self, mock_stdout, mock_input):
        a()
        self.assertEqual(mock_stdout.getvalue().strip(), 'today play let’s hello today play let’s hello today play let’s hello today play let’s hello today play let’s hello today play let’s hello today play let’s hello today play let’s hello today play let’s hello today play let’s hello')

    @patch('builtins.input', side_effect=['1 2  3   '])
    @patch('sys.stdout', new_callable=StringIO)
    def test_many_spaces(self, mock_stdout, mock_input):
        a()
        self.assertEqual(mock_stdout.getvalue().strip(), '3 2 1')

    @patch('builtins.input', side_effect=['1 2  3№%32 fd   кап кап'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_symbols(self, mock_stdout, mock_input):
        a()
        self.assertEqual(mock_stdout.getvalue().strip(), 'кап кап fd 3№%32 2 1')

    @patch('builtins.input', side_effect=['1 2  3№%32 有些  东西'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_symbols(self, mock_stdout, mock_input):
        a()
        self.assertEqual(mock_stdout.getvalue().strip(), '东西 有些 3№%32 2 1')