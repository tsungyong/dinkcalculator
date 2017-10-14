#personal finance calculator developed by managerclaire
def DINKcalculator():
    name_a = input("First spouse's name: ")
    name_b = input("Second spouse's name: ")
    #print(name_a + " and " + name_b + " are evaluating job offers. ")
    income_a = ene(name_a)
    income_b = ene(name_b)
    combined_income = income_a + income_b
    print("Gross monthly income: " + '${:,.2f}'.format(combined_income))
    tax = taxes(combined_income)
    monthly_taxes = tax / 12
    print("Approximate monthly taxes: " + '${:,.2f}'.format(monthly_taxes))
    total_expenses = expenses()
    savings = combined_income - total_expenses - monthly_taxes
    print("Approximate monthly savings: " + '${:,.2f}'.format(savings))
    final_savings = retirement(savings)
    print("Retirement balance: " + '${:,.2f}'.format(final_savings))

#pulls name_a or name_b from DINKcalculator()
def ene(name_var):
    valid = False
    while valid == False:
        ene = int(input("Enter 1 if " + name_var + " is paid an hourly wage or 2 if " + name_var + " is paid a salary: "))
        if ene == 1:
            income = wage(name_var)
            valid = True
        elif ene == 2:
            income = salary(name_var)
            valid = True
    return income

#pulls name_a or name_b from DINKcalculator()
def wage(name_var):
    hours = float(input("How many hours does " + name_var + " work per week? "))
    wage_var = float(input("How much does " + name_var + " make per hour? "))
    weekly = hours*wage_var
    monthly = weekly*4
    print(name_var + " makes " + '${:,.2f}'.format(weekly) + " per week and approximately " + '${:,.2f}'.format(monthly) + " per month.")
    return monthly

#pulls name_a or name_b from DINKcalculator()
def salary(name_var):
    yearly = float(input("What is " + name_var + "'s annual salary? "))
    monthly = yearly / 12
    print(name_var + " makes " + '${:,.2f}'.format(monthly) + " per month.")
    return monthly

#pulls combined_income from DINKcalculator()
def taxes(income):
    annual_income = income*12
    tax_income = annual_income - 12700 - 4050*2
    if tax_income <= 18650:
        pct = .10
    elif tax_income <= 75900:
        pct = .15
    elif tax_income <= 153100:
        pct = .25
    elif tax_income <= 233350:
        pct = .28
    elif tax_income <= 416700:
        pct = .33
    elif tax_income <= 470700:
        pct = .35
    else:
        pct = .396
    taxes = tax_income*pct
    return taxes

def expenses():
    valid = False
    while valid == False:
        exp_option = int(input("Enter 1 if you would like to itemize expenses or 2 to not: "))
        #int input for each expense category
        if exp_option == 1:
            valid = True
            rent = float(input("Monthly housing costs: "))
            health = float(input("Monthly healthcare costs: "))
            transportation = float(input("Monthly transportation costs: "))
            food = float(input("Monthly food costs: "))
            debt = float(input("Monthly debt payments: "))
            shopping = float(input("Other monthly expenses: "))
            total_expenses = rent + health + transportation + food + shopping + debt
            #int input for total expenses
        elif exp_option == 2:
            valid = True
            total_expenses = float(input("Total monthly expenses: "))
    print("Total monthly expenses: " + '${:,.2f}'.format(total_expenses))
    return total_expenses

def retirement(mon_save):
    valid = False
    balance = float(input("How much do you currently have saved for retirement? "))
    years_till = int(input("How many years until retirement? "))
    while valid == False:
        rate_choice = int(input("Enter 1 to use default growth rate. Enter 2 to use a custom rate. "))
        if rate_choice == 1:
            valid = True
            if years_till <= 10:
                rate = .04
            elif years_till <= 25:
                rate = .05
            else:
                rate = .06
        elif rate_choice == 2:
            valid = True
            rate = float(input("Enter an interest rate in decimals: "))
    monthly_rate = rate/12
    n_months = years_till*12
    final_savings = balance*(1+monthly_rate)**n_months + ((1+monthly_rate)**n_months-1)/monthly_rate*mon_save
    return final_savings

DINKcalculator()
