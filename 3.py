starting_salary = float(input("Enter the starting salary : "))
house_cost = 1000000
down_payment = house_cost * 0.25
annual_return = 0.04
semi_annual_rate = 0.07
months = 36
monthly_return = annual_return / 12
epsilon = 100
low = 0
high = 10000
steps = 0
current_savings = 0
annual_salary = starting_salary
for i in range(1,months+1):
    monthly_salary = annual_salary / 12
    current_savings += current_savings * monthly_return
    current_savings += monthly_salary * 1
    if i % 6 == 0:
        annual_salary+=annual_salary*semi_annual_rate
if current_savings < down_payment:
    print("It is not possible to pay the down payment in 3 years")
else:
    while True:
        steps+=1
        mid = (low+high) // 2
        rate = mid / 10000
        current_savings = 0
        annual_salary = starting_salary
        for i in range(1,months+1):
            monthly_salary = annual_salary / 12
            current_savings += current_savings * monthly_return
            current_savings += monthly_salary * rate
            if i % 6 == 0:
                annual_salary += annual_salary * semi_annual_rate
        if abs(current_savings - down_payment) <= epsilon:
            print("Best savings rate :",round(rate,4))
            print("Steps in bisection searchh : ",steps)
            break
        elif current_savings < down_payment:  
            low = mid
        else:
            high = mid