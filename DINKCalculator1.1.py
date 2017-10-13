def DINKcalculator():
    name_a = input("What is the first spouse's name? ")
    name_b = input("What is the second spouse's name? ")
    print(name_a + " and " + name_b + " are evaluating job offers. ")
    income_a = ene(name_a)
    income_b = ene(name_b)
    combined_income = income_a + income_b
    print("Their gross monthly income is " + '${:,.2f}'.format(combined_income) + ".")
    tax = taxes(combined_income)
    monthly_taxes = tax / 12
    print(name_a + " and " + name_b + " will pay approximately " + '${:,.2f}'.format(monthly_taxes) + " per month in taxes.")
    total_expenses = expenses()
    savings = combined_income - total_expenses - monthly_taxes
    print(name_a + " and " + name_b + " will save about " + '${:,.2f}'.format(savings) + " per month in this scenario.")
    #comp_savings = retirement(savings)

def ene(name_var):
    ene = input("Is " + name_var + " paid a wage or a salary? ")
    if ene == "wage":
        ene = 1
        income = wage(name_var)
        return income
    elif ene == "salary":
        ene = 2
        income = salary(name_var)
        return income
    else:
        print("I'm sorry, I did not recognize that input. Please start over.")
        DINKcalculator()

def wage(name_var):
    hours = float(input("How many hours does " + name_var + " work per week? "))
    wage_var = float(input("How much does " + name_var + " make per hour? "))
    weekly = hours*wage_var
    monthly = weekly*4
    print(name_var + " makes " + '${:,.2f}'.format(weekly) + " per week and approximately " + '${:,.2f}'.format(monthly) + " per month.")
    return monthly

def salary(name_var):
    yearly = float(input("What is " + name_var + "'s annual salary? "))
    monthly = yearly / 12
    print(name_var + " makes " + '${:,.2f}'.format(monthly) + " per month.")
    return monthly

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
    exp_option = input("Would you like to itemize expenses? ")
    if exp_option == "yes":
        rent = float(input("How much are your monthly housing costs? "))
        health = float(input("How much are your monthly healthcare costs? "))
        transportation = float(input("How much are your monthly transportation costs? "))
        food = float(input("How much are your monthly food costs? "))
        debt = float(input("How much are your monthly debt payments? "))
        shopping = float(input("How much other money do you spend each month? "))
        total_expenses = rent + health + transportation + food + shopping + debt
        print("Their monthly expenses are " + '${:,.2f}'.format(total_expenses) + ".")
        return total_expenses
    elif exp_option == "no":
        total_expenses = float(input("What are your total monthly expenses? "))
        print("Their monthly expenses are " + '${:,.2f}'.format(total_expenses) + ".")
        return total_expenses
    else:
        print("I'm sorry, I did not recognize that input. Please start over.")
        DINKcalculator()

#def retirement(mon_save):
    #years_till = int(input("How many years until retirement? "))
    #year_save = mon_save*12

DINKcalculator()
