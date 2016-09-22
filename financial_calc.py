import math
from finance_core import FinanceCore

finCore = FinanceCore()


# user selects operation 
operation_number = raw_input('''Choose operation you would like to execute: \n
To estimating present value for a given future cash flow ... press 1
To calculate present value of perpetuity                 ... press 2
To calculate growing perpetuity                          ... press 3
To calculate present ordinary annuity value              ... press 4
To calculate future ordinary annuity value               ... press 5
To calculate effective annual rate                       ... press 6
To calculate effective rate                              ... press 7
To calculate continuously compuonded interest rate       ... press 8\n''');


def getPV_F():
	fv = finCore.process_input(raw_input("Enter future value (FV): "))
	r = finCore.process_percent_input(raw_input("Enter periodic discount rate (R)%: "))
	n = finCore.process_input(raw_input("Enter number of periods (n): "))
	finCore.pv_f(fv,r,n)

def getPV_Perpetuity():
	c = finCore.process_input(raw_input("Enter constant periodic cash flow (c):"))
	r = finCore.process_percent_input(raw_input("Enter periodic discount rate (r):"))
	finCore.pv_perpetuity(c,r)

def getPV_Growing_Perpetuity():
	c = finCore.process_input(raw_input("Enter first cash flow (c):"))
	r = finCore.process_percent_input(raw_input("Enter effective periodic rate (R):"))
	g = finCore.process_percent_input(raw_input("Enter constant grow rate (g):"))
	finCore.pv_growing_perpetuity(c,r,g)

def getPV_Ordinary_Annuity():
	pmt =  finCore.process_input(int(raw_input("Enter equal periodic payment (PMT):")))
	r = finCore.process_percent_input(int(raw_input("Enter periodic discout rate (R)%:")))
	n = finCore.process_input(int(raw_input("Enter number of periods (n):")))
	finCore.pv_ordinary_annuity(pmt,r,n)

def getFV_Ordinary_Annuity():
	pmt = finCore.process_input(raw_input("Enter equal periodic payment (PMT):"))
	r = finCore.process_percent_input(raw_input("Enter periodic discout rate (R)%:"))
	n = finCore.process_input(raw_input("Enter number of periods (n):"))
	finCore.fv_ordinary_annuity()

def getEAR_Estimation():
	apr = finCore.process_percent_input(raw_input("Enter annual persentage rate (APM):%"))
	m = finCore.process_input(raw_input("Enter compunding frequency within one year (m):"))
	finCore.ear_estimation(apr,m)

def getREffective_Estimation():
	apr1 = finCore.process_percent_input(raw_input("Enter annual persentage rate (APM1)%:"))
	m1 = finCore.process_input(raw_input("Enter compunding frequency (m1):"))
	m2 = finCore.process_input(raw_input("Enter compunding frequency (m2):"))
	finCore.reffective_estimation(apr1,m1,m2)

def getCont_Compound_Rate():
	apr = finCore.process_percent_input(raw_input("Enter annual persentage rate (APM1)%:"))
	m = finCore.process_input(raw_input("Enter compunding frequency (m):"))
	finCore.cont_compound_rate(apr,m)


if operation_number == "1":
	getPV_F()
elif operation_number == "2":
	getPV_Perpetuity()
elif operation_number == "3":
	getPV_Growing_Perpetuity()
elif operation_number == "4":
	getPV_Ordinary_Annuity()
elif operation_number == "5":
	getFV_Ordinary_Annuity()
elif operation_number == "6":
	getEAR_Estimation()
elif operation_number == "7":
	getREffective_Estimation()
elif operation_number == "8":
	getCont_Compound_Rate()
else:
	"Option you've choosen doesn't exist"



























