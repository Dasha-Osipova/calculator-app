class Calc:

	def __init__(self):
		self.total = 0
		self.memory = []
		

	def add(self, a, b = None):	
		if b is None: 
			self.total += a
			self.memory.append(' + {0}'.format(a))
		
		else:
			self.total = a + b 
			self.memory = [] 
		
		
	def subtract(self, a, b = None):
		if b is None:
			self.total -= a 
			self.memory.append(' - {0}'.format(a))
		else:
			self.total = a - b
			self.memory = []
			
	def multiply(self, a, b = None):
		if b is None:
			self.total *= a
			self.memory.append(' * {0}'.format(a))
		else:
			self.total = a * b
			self.memory = []
			
	def divide(self, a, b = None):
		if b is None:
			self.total /= a
			self.memory.append(' / {0}'.format(a))
		else:
			self.total = a / b 
			self.memory = []
			
	def show_memory(self): 
		for index in range(len(self.memory)):
			print(index,': ',self.memory[index])