money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count = 0
while money_capital > 0:
        money_capital = money_capital + salary - spend*(1+increase)**count
        if money_capital > 0:
                count += 1
print("Количество месяцев, которое можно протянуть без долгов:", count)
