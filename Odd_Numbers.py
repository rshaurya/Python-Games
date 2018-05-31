def Odd_Numbers(strings):
    for i in strings:
        if i % 2 != 0:
            strings.remove(i)
    return strings


num = Odd_Numbers([67, 62, 3, 7])
print(num)