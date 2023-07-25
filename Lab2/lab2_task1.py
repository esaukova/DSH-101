money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count_months = 0  # счётчик месяцев

while money_capital > 0:
    budget = money_capital + salary  # бюджет включая подушку и зарплату
    if spend > budget:  # заканчивать цикл когда расходы привысят бюджет
        break
    money_capital += salary - spend
    spend += spend * increase  # Увеличиваем расходы на increase
    count_months += 1  # засчитываем месяц без долгов


# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", count_months)
