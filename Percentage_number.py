def Percentage_Num(value):
    for i in value:
        if i % 2 == 0:
            print( i, 'is even')
        else:
            print( i, 'is odd')


num = Percentage_Num([ 87, 10, 52, 47 ])
print(num)



def getEvenNumbers(list):
    result = []
    for i in list:
        if i % 2 == 0:
            result.append(i)

    return result


num2 = getEvenNumbers([58, 3652, 9, 0, 3569])
print(num2)




def getOddNumbers(list):
    value = []
    for h in list:
        if h % 2 != 0:
            value.append(h)

    return value


result = getOddNumbers([ 5, 589, 52, 6, 98, 2, 10, 1 ])
print(result)