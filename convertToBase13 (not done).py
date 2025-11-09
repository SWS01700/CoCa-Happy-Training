def convertToBase13(num):
    Base13 = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
        10: 'A', 11: 'B', 12: 'C'
    }

    if num <=9:
        return num
    if num > 9:
        remain = num % 13
        numnum = (num - remain) // 13
        if numnum == 0:
            return str(Base13[remain])
        return str(numnum) + str(Base13[remain])
    
#please ask for help