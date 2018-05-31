def Max_Num(list):
    max2 = list [0]
    for i in list:
        if i > max2:
            max2 = i
    return max2

value = Max_Num([2, 7, -9, -1])
print(value)


