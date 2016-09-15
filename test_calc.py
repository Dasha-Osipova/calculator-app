import unittest
from calc import Calc

class CalcTest(unittest.TestCase):
	
	def test_add(self):
		calc = Calc()
		calc.add(2,2)
		result = calc.total
		self.assertEqual(result,4)

	def test_negative_add(self):
		calc = Calc()
		calc.add(4,-2)
		result = calc.total
		self.assertEqual(result,2)

	def test_both_negative_add(self):
		calc = Calc()
		calc.add(-4,-2)
		result = calc.total
		self.assertEqual(result,-6)

	def test_subtract(self):
		calc = Calc()
		calc.subtract(10,2)
		result = calc.total
		self.assertEqual(result,8)

	def test_negative_subtract(self):
		calc = Calc()
		calc.subtract(10,-2)
		result = calc.total
		self.assertEqual(result,12)

	def test_both_negative_subtract(self):
		calc = Calc()
		calc.subtract(-5,-5)
		result = calc.total
		self.assertEqual(result,0)

	def test_multiply(self):
		calc = Calc()
		calc.multiply(3,3)
		result = calc.total
		self.assertEqual(result,9)

	def test_negative_multiply(self):
		calc = Calc()
		calc.multiply(3,-3)
		result = calc.total
		self.assertEqual(result,-9)

	def test_both_negative_multiply(self):
		calc = Calc()
		calc.multiply(-3,-3)
		result = calc.total
		self.assertEqual(result,9)

	def test_divide(self):
		calc = Calc()
		calc.divide(9,3)
		result = calc.total
		self.assertEqual(result,3)

	def test_negative_divide(self):
		calc = Calc()
		calc.divide(9,-3)
		result = calc.total
		self.assertEqual(result,-3)

	def test_both_negative_divide(self):
		calc = Calc()
		calc.divide(-9,-3)
		result = calc.total
		self.assertEqual(result,3)


if __name__ == '__main__':
	unittest.main()