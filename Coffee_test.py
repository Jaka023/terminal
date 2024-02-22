#/usr/bin/env python

import unittest
from io import StringIO
from unittest.mock import patch
from Coffee_terminal import CoffeeMachine

class TestCoffeeMachine(unittest.TestCase):

    def setUp(self):
        self.machine = CoffeeMachine()

    def test_display_menu(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.machine.display_menu()
            expected_output = "Меню кофе:\nЛатте: $3.50\nКапучино: $3.00\nАмерикано: $2.50\nЭспрессо: $2.00\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_make_coffee_valid_choice(self):
        with patch('builtins.input', return_value='Латте'), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.machine.make_coffee(input())
            expected_output = "Готовим Латте... Ваш кофе готов! Пожалуйста, внесите оплату: $3.50\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_make_coffee_invalid_choice(self):
        with patch('builtins.input', return_value='Чай'), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.machine.make_coffee(input())
            expected_output = "Извините, выбранного кофе нет в нашем ассортименте.\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()

