
def house_hunting(annual_salary,portion_saved,total_cost,semi_annual_raise):
    portion_down_payment = 0.25
    r = 0.04/12
    month=0
    down_payment = total_cost* portion_down_payment
    current_savings = 0
    while current_savings < down_payment:
        current_savings = current_savings + current_savings*r + annual_salary*portion_saved/12
        month += 1
        if month %6==0:
            annual_salary = annual_salary + annual_salary*semi_annual_raise
    return month

annual_salary  = int(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = int(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi­annual raise, as a decimal: '))
months = house_hunting(annual_salary,portion_saved,total_cost,semi_annual_raise)
print('Number of months:​  {} '.format(months))

