def square(num:int)->int:
    result = 0
    for _ in range(num):
        result += num

    return result

def digit(num:int)->list:
    result = []
    while num != 0:
        result.append(int(num%10))
        if num < 10:
            break
        num = num/10
    return result
num = int(500)
print(square(num))
print(digit(num))