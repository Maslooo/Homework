def find_password(n):
    result = ""
    for i in range(1, n):
        for j in range(i + 1, n):
            pair_sum = i + j
            if n % pair_sum == 0:
                result += str(i) + str(j)
    return result
n = int(input("Введите число от 3 до 20: "))
print("Нужный пароль:", find_password(n))