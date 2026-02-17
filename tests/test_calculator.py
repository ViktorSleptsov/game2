import unittest
import sys
import os

# Добавляем путь к основному модулю
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Импортируем ваш калькулятор
from calculator import Calculator  # Предполагаем, что класс Calculator в файле calculator.py
import tkinter as tk

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        """Создание экземпляра калькулятора для тестов"""
        self.root = tk.Tk()
        self.calc = Calculator(self.root)
    
    def test_addition(self):
        """Тест сложения"""
        self.calc.button_click('2')
        self.calc.button_click('+')
        self.calc.button_click('3')
        self.calc.button_click('=')
        self.assertEqual(self.calc.result_var.get(), '5')
    
    def test_subtraction(self):
        """Тест вычитания"""
        self.calc.button_click('5')
        self.calc.button_click('-')
        self.calc.button_click('3')
        self.calc.button_click('=')
        self.assertEqual(self.calc.result_var.get(), '2')
    
    def test_multiplication(self):
        """Тест умножения"""
        self.calc.button_click('4')
        self.calc.button_click('*')
        self.calc.button_click('3')
        self.calc.button_click('=')
        self.assertEqual(self.calc.result_var.get(), '12')
    
    def test_division(self):
        """Тест деления"""
        self.calc.button_click('8')
        self.calc.button_click('/')
        self.calc.button_click('2')
        self.calc.button_click('=')
        self.assertEqual(self.calc.result_var.get(), '4.0')
    
    def test_square_root(self):
        """Тест квадратного корня"""
        self.calc.button_click('9')
        self.calc.button_click('√')
        self.assertEqual(self.calc.result_var.get(), '3.0')
    
    def test_clear(self):
        """Тест очистки"""
        self.calc.button_click('1')
        self.calc.button_click('2')
        self.calc.button_click('3')
        self.calc.button_click('C')
        self.assertEqual(self.calc.result_var.get(), '0')
    
    def test_negative_square_root(self):
        """Тест корня из отрицательного числа"""
        self.calc.button_click('-')
        self.calc.button_click('9')
        self.calc.button_click('√')
        self.assertEqual(self.calc.result_var.get(), "Ошибка: √ отр. числа")
    
    def tearDown(self):
        """Очистка после тестов"""
        self.root.destroy()

if __name__ == '__main__':
    unittest.main()