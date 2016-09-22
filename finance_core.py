class FinanceCore(object):
		
	def __init__(self):
		self.data = []

	global INVALID_INPUT
	INVALID_INPUT = "One or more invalid parameters was entered"

	'''
	HELPERS
	'''
	def process_percent_input(self,value):
		if(value != '' and value.isdigit()):
			return float(value)/100
		else:
			return 0

	def process_input(self,value):
		if(value != '' and value.isdigit()):
			return int(value)
		else:
			return 0

	def input_is_valid(self,values):
		for i in values:
			if(i == 0):
				return False
		return True

	'''
	Method of estimating present value for a given future cash flow
	PV = FV/(1+R)^n
		
	PV - present value
	FV - future value
	R - preiodic discount rate
	n - number of periods
	'''
	def pv_f(self,fv,r,n):
		
		if(self.input_is_valid([fv,r,n])):
			print fv/(1+r)**n
		else:
			print INVALID_INPUT 
	
	'''
	Method for calculating present value of perpetuity
	PV(perpetuity) = c/R

	c - the constant periodic cash flow occurring at the end of each period
	R - periodic discount rate	
	'''
	def pv_perpetuity(self,c,r):
		
		if(self.input_is_valid([c,r])):
			print c/r
		else:
			print INVALID_INPUT 

	'''
	Method for calculating growing perpetuity
	PV(growing perpetuity) = c/(R-g)

	c - first cashflow occuring at the end of the first period
	R - is effective periodic rate
	g - constant grow rate
	'''
	def pv_growing_perpetuity(self,c,r,g):
		
		if(r < g):
			print("r<g !!!")
		else:
			if(self.input_is_valid([c,r,g])):
				print (c/(r-g))
			else:
				print INVALID_INPUT

	'''
	Method for calculating present ordinary annuity value(cash flows occur at the end of each period)
	PV(annuity) = PMT/R[1 - 1/(1+R)^n]

	PMT - equal periodic payment
	R - periodic discout rate
	n - number of periods
	'''
	def pv_ordinary_annuity(self,pmt,r,n):

		if(self.input_is_valid([pmt,r,n])):
			print (pmt/r)*(1 - 1/(1+r)**n)
		else:
			print INVALID_INPUT 

	'''
	Method for calculating future ordinary annuity value(cash flows occur at the end of each period)
	FV(annuity) = PMT/R[(1+R)^n - 1]
		
	PMT - equal periodic payment
	R - periodic discout rate
	n - number of periods
	'''
	def fv_ordinary_annuity(self,pmt,r,n):
				
		if(self.input_is_valid([pmt,r,n])):
			print (pmt/r)*((1+r)**n -1)
		else:
			print INVALID_INPUT 

	'''
	Method to calculate effective annual rate
	EAR = (1+APR/m)**m -1

	APR - annual persentage rate
	m - compunding frequency within one year
	'''
	def ear_estimation(self, apr, m):

		if(self.input_is_valid([apr,m])):
			print (1+apr/m)**m - 1
		else:
			print INVALID_INPUT 
		

	'''
	Method to calculate effective rate
	Rm2 = (1+APR/m1)**m1/m2 -1

	APR - annual persentage rate
	m1,m2 - compunding frequencies
	'''
	def reffective_estimation(self,apr1,m1,m2):

		if(self.input_is_valid([apr,m1,m2])):
			print (1+apr/m1)**m1/m2 - 1
		else:
			print INVALID_INPUT

	'''
	Method to calculate continuously compuonded interest rate 
	Rc = m*ln(1+APR/m)

	APR - annual persentage rate
	m - compunding frequency per year
	'''
	def cont_compound_rate(self, arp, m):

		if(self.input_is_valid([apr,m])):
			print m*math.log(1+arp/m)
		else:
			print INVALID_INPUT
		
