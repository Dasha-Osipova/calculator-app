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


if operation_number == "1":
	getPV_F()
elif operation_number == "2":
	getPV_Perpetuity()
elif operation_number == "3":
	getPV_Growing_Perpetuity()
elif operation_number == "4":
	finCore.pv_ordinary_annuity()
elif operation_number == "5":
	finCore.fv_ordinary_annuity()
elif operation_number == "6":
	finCore.ear_estimation()
elif operation_number == "7":
	finCore.reffective_estimation()
elif operation_number == "8":
	finCore.cont_compound_rate()
else:
	"Option you've choosen doesn't exist"



























