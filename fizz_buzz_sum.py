def fizz_buzz_sum(target):
    sum_range_pos = range(0, target)
    sum_list = []
    for num in sum_range_pos:
        if num % 3 == 0 or num % 5 == 0:
            sum_list.append(num)
    return sum(sum_list)
  
print(fizz_buzz_sum(10))