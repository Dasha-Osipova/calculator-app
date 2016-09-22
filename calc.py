class Calc:

# returns a calculator object? the constructor is created constructor creates new calculator object
 def __init__(self):
  # maintains the running total
  self.total = 0
  # the list that maintains the memory except the initial operation
  self.memory = [] 
  # the list that saves the initial operation in particular
  self.init_expression = []

 def add(self, a, b = None): 
  if b is None: 
   self.total += a
   self.memory.append(' + {0}'.format(a))
  else:
   # resets the total when given two values, will start over with the new running total
   self.total = a + b
   # resets self.memory so that it equals to an empty list
   self.memory = []
   # saves the initial operation when two values are provided 
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
 
# loops through all the contents of the list operation_list and outputs the value for all indexes found within the range created by len() function
 def show_memory(self): 
  operation_list = self.init_expression + self.memory
  for index in range(len(operation_list)):
   print(index,': ',operation_list[index])