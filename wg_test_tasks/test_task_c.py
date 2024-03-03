import unittest
from unittest.mock import patch
from io import StringIO
from task_c import start
from task_c_upd import start as start_reload

file_path = 'numbers.txt'

try:
    with open(file_path, 'r') as file:
        data = [line.strip() for line in file]
        f, s = data[0], data[1]
        print("Загружено!")
except FileNotFoundError:
    print(f"Файл по пути '{file_path}' не найден.")
except Exception as e:
    print(f"Произошла ошибка при чтении файла: {e}")


class JustTest(unittest.TestCase):
    # @patch('builtins.input', side_effect=[f, s])
    # @patch('sys.stdout', new_callable=StringIO)
    # def test_list(self, mock_stdout, mock_input):
    #     start()
    #     self.assertEqual(mock_stdout.getvalue().strip(), '10 20')

    @patch('builtins.input', side_effect=[f, s])
    @patch('sys.stdout', new_callable=StringIO)
    def test_reload(self, mock_stdout, mock_input):
        start_reload()
        self.assertEqual(mock_stdout.getvalue().strip(), '198 277')


class TaskCTest(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', '42'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_single_element_list(self, mock_stdout, mock_input):
        start()
        self.assertEqual(mock_stdout.getvalue().strip(), '1 1')

    @patch('builtins.input', side_effect=['5', '1 2 3 4 5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_ordered_list(self, mock_stdout, mock_input):
        start()
        self.assertEqual(mock_stdout.getvalue().strip(), '5 5')

    @patch('builtins.input', side_effect=['4', '10 5 20 10'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_random_list(self, mock_stdout, mock_input):
        start()
        self.assertEqual(mock_stdout.getvalue().strip(), '2 3')

    @patch('builtins.input', side_effect=['3', '3 2 1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_reverse_ordered_list(self, mock_stdout, mock_input):
        start()
        self.assertEqual(mock_stdout.getvalue().strip(), '1 2')

    @patch('builtins.input', side_effect=['1', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_one_number(self, mock_stdout, mock_input):
        start()
        self.assertEqual(mock_stdout.getvalue().strip(), '1 1')

    @patch('builtins.input', side_effect=['2', '1 1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_2_equal_nums(self, mock_stdout, mock_input):
        start()
        self.assertEqual(mock_stdout.getvalue().strip(), '1 2')

    @patch('builtins.input', side_effect=['10', '100 200 300 400 500 100 200 300 400 500'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_1(self, mock_stdout, mock_input):
        start()
        self.assertEqual(mock_stdout.getvalue().strip(), '5 10')

    @patch('builtins.input', side_effect=['3', '1 1 1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_3_ones(self, mock_stdout, mock_input):
        start()
        self.assertEqual(mock_stdout.getvalue().strip(), '1 2')

    @patch('builtins.input', side_effect=['4', '1564 12131 13432 4343 2'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_big_numbers(self, mock_stdout, mock_input):
        start()
        self.assertEqual(mock_stdout.getvalue().strip(), '3 4')

    @patch('builtins.input', side_effect=['54', '1564 12131 13432 4343 2 5 1564 12131 13432 4343 2 5 1564 12131 '
                                                '13432 4343 2 5'
                                                ' 1564 12131 13432 4343 2 5 1564 12131 13432 4343 2 5 1564 12131 '
                                                '13432 4343 2 5'
                                                ' 1564 12131 13432 4343 2 5 1564 12131 13432 4343 2 5 1564 12131 13432 4343 2 5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_long_big_numbers(self, mock_stdout, mock_input):
        start()
        self.assertEqual(mock_stdout.getvalue().strip(), '6 12')

    @patch('builtins.input', side_effect=['5', '10 100 1000 10000 100000'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_big_big_numbers(self, mock_stdout, mock_input):
        start()
        self.assertEqual(mock_stdout.getvalue().strip(), '5 5')

    @patch('builtins.input', side_effect=['5', '100000 10000 1000 100 10'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_reverse_big_big_numbers(self, mock_stdout, mock_input):
        start()
        self.assertEqual(mock_stdout.getvalue().strip(), '1 2')


class TaskCReloadTest(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', '42'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_single_element_list(self, mock_stdout, mock_input):
        start_reload()
        self.assertEqual(mock_stdout.getvalue().strip(), '1 1')

    @patch('builtins.input', side_effect=['5', '1 2 3 4 5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_ordered_list(self, mock_stdout, mock_input):
        start_reload()
        self.assertEqual(mock_stdout.getvalue().strip(), '5 5')

    @patch('builtins.input', side_effect=['4', '10 5 20 10'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_random_list(self, mock_stdout, mock_input):
        start_reload()
        self.assertEqual(mock_stdout.getvalue().strip(), '2 3')

    @patch('builtins.input', side_effect=['3', '3 2 1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_reverse_ordered_list(self, mock_stdout, mock_input):
        start_reload()
        self.assertEqual(mock_stdout.getvalue().strip(), '1 2')

    @patch('builtins.input', side_effect=['1', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_one_number(self, mock_stdout, mock_input):
        start_reload()
        self.assertEqual(mock_stdout.getvalue().strip(), '1 1')

    @patch('builtins.input', side_effect=['2', '1 1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_2_equal_nums(self, mock_stdout, mock_input):
        start_reload()
        self.assertEqual(mock_stdout.getvalue().strip(), '1 2')

    @patch('builtins.input', side_effect=['10', '100 200 300 400 500 100 200 300 400 500'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_1(self, mock_stdout, mock_input):
        start_reload()
        self.assertEqual(mock_stdout.getvalue().strip(), '5 10')

    @patch('builtins.input', side_effect=['3', '1 1 1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_3_ones(self, mock_stdout, mock_input):
        start_reload()
        self.assertEqual(mock_stdout.getvalue().strip(), '1 2')

    @patch('builtins.input', side_effect=['4', '1564 12131 13432 4343 2'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_big_numbers(self, mock_stdout, mock_input):
        start_reload()
        self.assertEqual(mock_stdout.getvalue().strip(), '3 4')

    @patch('builtins.input', side_effect=['54', '1564 12131 13432 4343 2 5 1564 12131 13432 4343 2 5 1564 12131 '
                                                '13432 4343 2 5'
                                                ' 1564 12131 13432 4343 2 5 1564 12131 13432 4343 2 5 1564 12131 '
                                                '13432 4343 2 5'
                                                ' 1564 12131 13432 4343 2 5 1564 12131 13432 4343 2 5 1564 12131 13432 4343 2 5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_long_big_numbers(self, mock_stdout, mock_input):
        start_reload()
        self.assertEqual(mock_stdout.getvalue().strip(), '6 12')

    @patch('builtins.input', side_effect=['5', '10 100 1000 10000 100000'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_big_big_numbers(self, mock_stdout, mock_input):
        start_reload()
        self.assertEqual(mock_stdout.getvalue().strip(), '5 5')

    @patch('builtins.input', side_effect=['5', '100000 10000 1000 100 10'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_reverse_big_big_numbers(self, mock_stdout, mock_input):
        start_reload()
        self.assertEqual(mock_stdout.getvalue().strip(), '1 2')


if __name__ == '__main__':
    unittest.main()
