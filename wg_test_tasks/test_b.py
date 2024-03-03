import random
import unittest
from unittest.mock import patch
from io import StringIO
from B import b


class BFunctionTest(unittest.TestCase):
    @patch('builtins.input', side_effect=['2 5', '101,1 102,2 103,3 104,3 105,4', '201,1 202,2 203,2 204,3 205,4'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_common(self, mock_stdout, mock_input):
        b()
        self.assertEqual(mock_stdout.getvalue().strip(), '101 201 102 202 203 103 104 204 105 205')

    @patch('builtins.input', side_effect=['1 1', '1,1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_single_element_list(self, mock_stdout, mock_input):
        b()
        self.assertEqual(mock_stdout.getvalue().strip(), '1')

    @patch('builtins.input', side_effect=['1 11', '1,1 2,1 54,2 12,2 34,1 76,4 23,1 45,5 55,5 101,1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_single_element_list(self, mock_stdout, mock_input):
        b()
        self.assertEqual(mock_stdout.getvalue().strip(), '1 2 23 34 101 12 54 76 45 55')

    @patch('builtins.input',
           side_effect=['11 1', '1,1', '1,1', '1,1', '1,1', '1,1', '1,1', '1,1', '1,1', '1,1', '1,1', '1,1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_max_equal(self, mock_stdout, mock_input):
        b()
        self.assertEqual(mock_stdout.getvalue().strip(), '1 1 1 1 1 1 1 1 1 1 1')


def b_gen(n, m):
    file_name = 'b_numbers.txt'

    with open(file_name, 'a') as file:
        file.write(f"{n} {m}\n")
        for i in range(n):
            random_numbers = " ".join(
                [f"{random.randint(1, 10 ** 10)},{random.randint(1, 10)} " for _ in range(m)])
            if i != n - 1:
                file.write(random_numbers + "\n")
            else:
                file.write(random_numbers)

