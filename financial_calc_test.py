import unittest
from finance_core import FinanceCore

class FinancialCalcTest(unittest.TestCase):
	
	#Process percent input tests
	def test_char_percent_input_ignored(self):
		finCore = FinanceCore()
		value = finCore.process_percent_input("ee")
		self.assertEqual(value,0)

	def test_empty_percent_input_ignored(self):
		finCore = FinanceCore()
		value = finCore.process_percent_input('')
		self.assertEqual(value,0)

	def test_correct_percent_input(self):
		finCore = FinanceCore()
		value = finCore.process_percent_input('5')
		self.assertEqual(value,0.05)

	#Process input tests
	def test_process_input_char_ignored(self):
		finCore = FinanceCore()
		value = finCore.process_input("ee")
		self.assertEqual(value,0)

	def test_empty_input_ignored(self):
		finCore = FinanceCore()
		value = finCore.process_input('')
		self.assertEqual(value,0)

	def test_correct_percent_input(self):
		finCore = FinanceCore()
		value = finCore.process_input('99')
		self.assertEqual(value,99)

	#Valid input test
	def test_input_is_valid_contains_zero(self):
		finCore = FinanceCore()
		value = finCore.input_is_valid([1,45,0])
		self.assertEqual(value,False)

	def test_input_is_valid_correct_input(self):
		finCore = FinanceCore()
		value = finCore.input_is_valid([33,4,5])
		self.assertEqual(value,True)

	

	





if __name__ == '__main__':
	unittest.main()