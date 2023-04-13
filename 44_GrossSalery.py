def calculate_gross_salary(hra, da, bonus, base):
    hra_amount = (hra/100) * base
    da_amount = (da/100) * base
    bonus_amount = (bonus/100) * base
    gross_salary = base + hra_amount + da_amount + bonus_amount
    return format(gross_salary, ".2f")

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        hra, da, bonus = map(int, input().split())
        base = int(input())
        result = calculate_gross_salary(hra, da, bonus, base)
        print(result)
