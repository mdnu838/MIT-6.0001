
def saving_in_months(annual_salary,portion_saved,semi_annual_raise = 0.07,in_months=36):
    r = 0.04/12
    month=0
    current_savings = 0
    while month<in_months:
        month += 1
        current_savings = current_savings + current_savings * r + annual_salary * portion_saved / 12
        if month %6==0:
            annual_salary = annual_salary + annual_salary*semi_annual_raise
    return current_savings


def portion_saved_finder(annual_salary,portion_saved_min =0, portion_saved_max=10000, in_months=36,i=0,down_payment=250000):
    i+=1
    if portion_saved_max >= portion_saved_min:

        portion_saved = portion_saved_min + (portion_saved_max - portion_saved_min) // 2
        current_savings = saving_in_months(annual_salary,portion_saved/10000,in_months=in_months)
        if abs(down_payment-current_savings)<100 :
            return portion_saved/10000,i

        elif current_savings > down_payment:
            return portion_saved_finder(annual_salary,portion_saved_min = portion_saved_min, portion_saved_max = portion_saved - 1, in_months=in_months,i=i,down_payment=down_payment)

        else:
            return portion_saved_finder(annual_salary,portion_saved_min = portion_saved + 1, portion_saved_max = portion_saved_max, in_months=in_months,i=i,down_payment=down_payment)

    else:
        return -1,i
#

annual_salary  = int(input('Enter your annual salary: '))

portion_down_payment = 0.25
total_cost = 1000000
down_payment = int(total_cost * portion_down_payment)

portion_saved,i = portion_saved_finder(annual_salary = annual_salary, down_payment=down_payment)

if portion_saved != -1:
    print("Best savings rate:​  {}".format(portion_saved))
    print('Steps in bisection search:​  {}'.format(i))
else:
    print("It is not possible to pay the down payment in three years. ")

