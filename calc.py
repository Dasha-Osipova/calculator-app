class Calc:

 def __init__(self):
  self.total = 0
  self.memory = [] 
  self.init_expression = []

 def add(self, a, b = None): 
  if b is None: 
   self.total += a
   self.memory.append(' + {0}'.format(a))
  else:
   self.total = a + b 
   self.memory = []
   self.init_expression.append('{0} + {1}'.format(a, b)) 
  
 def subtract(self, a, b = None):
  if b is None:
   self.total -= a 
   self.memory.append(' - {0}'.format(a))
  else:
   self.total = a - b
   self.memory = []
   self.init_expression.append('{0} - {1}'.format(a, b))
   
 def multiply(self, a, b = None):
  if b is None:
   self.total *= a
   self.memory.append(' * {0}'.format(a))
  else:
   self.total = a * b
   self.memory = []
   self.init_expression.append('{0} * {1}'.format(a, b))
   
 def divide(self, a, b = None):
  if b is None:
   self.total /= a
   self.memory.append(' / {0}'.format(a))
  else:
   self.total = a / b 
   self.memory = []
   self.init_expression.append('{0} / {1}'.format(a, b))   
   
 def show_memory(self): 
  operation_list = self.init_expression + self.memory
  for index in range(len(operation_list)):
   print(index,': ',operation_list[index])