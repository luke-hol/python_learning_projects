birthday = '1879-03-14'

def reduce_digit(digit_string):
    single_digit = 0

    for i in digit_string:
        single_digit += int(i)

    if single_digit >= 10:
        reduce_again = str(single_digit)
        return reduce_digit(reduce_again)
    else:
        return single_digit

year_digit = reduce_digit('1879')
month_digit = reduce_digit('03')
day_digit = reduce_digit('14')

print(year_digit, month_digit, day_digit)