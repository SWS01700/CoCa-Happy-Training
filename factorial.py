def factorial(num):
    if num < 0:
        return None
    if type(num) != int:
        return None
    if num == 0:
        return 1

    return num * factorial(num - 1)
    #ex: factorial(3) => 3*factorial(2)                   => 3*2*1
    #                      factorial(2) => 2*factorial(1) => 2 * 1 


print(factorial(3))