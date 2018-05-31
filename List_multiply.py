def ListMul(numbers):
    result = 1
    for i in numbers:
        result = result * i
    return result


product = ListMul([5, 3])
print(product)
