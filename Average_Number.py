def Average_Num(numbers):
    result = 0
    for i in numbers:
        result = result + i
    return result / len(numbers)




value = Average_Num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(value)