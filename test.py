def square(num:int)->int:
    result = 0
    for _ in range(num):
        result += num

    return result

def cube(num:int)->int:
    result = square(num)
    result = result*num
    return result

num = int(5)
print(square(num))
print(cube(num))