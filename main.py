import re
#changes

def is_valid_snils(snils):
    snils_pattern = r'^\d{3}-\d{3}-\d{3} \d{2}$|^\d{11}$'
    if re.match(snils_pattern, snils):
        snils = snils.replace("-", "").replace(" ", "")  # Удаление разделителей

        check_sum = int(snils[-2:])  # Контрольная сумма из двух последних цифр

        # Расчет контрольной суммы
        calculated_check_sum = sum(int(snils[i]) * (9 - i) for i in range(9))
        calculated_check_sum = (calculated_check_sum % 101) % 100

        return check_sum == calculated_check_sum
    else:
        return False


snils1 = "116-973-385 89" #с разделителями
snils2 = "11697338589" #без разделителей
snils3 = "116-973-385 8" #неправильное кол-во цифр
snils4 = "116-973-385 80" #неправильная контрольная сумма
#using....
print(is_valid_snils(snils1))
print(is_valid_snils(snils2))
print(is_valid_snils(snils3))
print(is_valid_snils(snils4))


