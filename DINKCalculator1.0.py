def DINKcalculator():
    #name_a = input("What is the first spouse's name? ")
    #name_b = input("What is the second spouse's name? ")
    print(name_a + " and " + name_b + " are evaluating job offers. ")
    #rent = input("How much are your monthly housing costs? ")
    #health = input("How much are your monthly healthcare costs? ")
    #transportation = input("How much are your monthly transportation costs? ")
    #food = input("How much are your monthly food costs? ")
    #shopping = input("How much other money do you spend each month? ")
    buffer = input("What is your monthly expense buffer? ")
    #ene_a = input("Is " + name_a + " paid a wage or a salary? ")
    #if ene_a == "wage":
        #ene_a = 1
        #wage(name_a)
        #income_a = wage(name_a)
        #print(income_a)
    #elif ene_a == "salary":
        #ene_a = 2
        #income_a = salary(name_a)
        #print(income_a)
    #else:
        #print("I'm sorry, I did not recognize that input. ")
    income_a = ene(name_a)
    ene_b = input("Is " + name_b + " paid a wage or a salary? ")
    if ene_b == "wage":
        ene_b = 1
        #wage(name_b)
        income_b = wage(name_b)
        print(income_b)
    elif ene_b == "salary":
        ene_b = 2
        income_b = salary(name_b)
        print(income_b)
    else:
        print("I'm sorry, I did not recognize that input. ")
    combined_income = income_a + income_b
    print("Their combined monthly income is " + '${:,.2f}'.format(combined_income) + ".")

def ene(name_var):
    name_var = name_var
    print(type(name_var))
    ene = input("Is " + name_var + " paid a wage or a salary? ")
    if ene == "wage":
        ene = 1
        #wage(name_a)
        income = wage(name_var)
        print(income)
        return income
    elif ene == "salary":
        ene = 2
        income_a = salary(name_var)
        print(income)
        return income
    else:
        print("I'm sorry, I did not recognize that input. Please start over.")
        #return
        DINKcalculator()

def wage(name_var):
    #print("wage")
    hours = float(input("How many hours does " + name_var + " work per week? "))
    #print(hours)
    wage_var = float(input("How much does " + name_var + " make per hour? "))
    #print(wage_var)
    weekly = hours*wage_var
    #print(weekly)
    monthly = weekly*4
    #print(monthly)
    print(name_var + " makes " + '${:,.2f}'.format(weekly) + " per week and approximately " + '${:,.2f}'.format(monthly) + " per month.")
    return monthly

def salary(name_var):
    #print("salary")
    yearly = float(input("What is " + name_var + "'s annual salary? "))
    #print(yearly)
    monthly = yearly / 12
    #print(monthly)
    print(name_var + " makes " + '${:,.2f}'.format(monthly) + " per month.")
    return monthly

#DINKcalculator()
