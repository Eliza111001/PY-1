money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
total_money = money_capital
while total_money >= spend:
    total_money -= spend
    month += 1
    total_money += salary
    spend *= (1 + increase)

print(month)
