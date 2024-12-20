def month_to_season(month):
    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    elif month in [9, 10, 11]:
        return "Осень"
    else:
        return "Такого месяца не существует"


month_number = 4
season = month_to_season(month_number)

print(f"Месяц {month_number}: {season}")
