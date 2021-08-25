def square(num:int)->int:
    result = 1
    for _ in range(num):
        result *= num

    return result

num = int(2)
print(square(num))