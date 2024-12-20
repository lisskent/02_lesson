def is_year_leap(year):
    return year % 4 == 0


yeartocheck = int(input("Введите год: "))

result = is_year_leap(yeartocheck)

print(f"Год {yeartocheck}: {result}")
