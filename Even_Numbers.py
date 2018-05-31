def Even_Numbers(list):

    for i in list:
        if i % 2 == 0:
            list.remove(i)
    return list


value = Even_Numbers([56, 23, 3, 10])
print(value)