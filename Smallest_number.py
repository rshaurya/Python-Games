def Min_Num(list):
    min2 = list [0]
    for i in list:
        if i < min2:
            min2 = i
    return min2

result = Min_Num([-9, 542, -98, 46, -569])
print(result)
