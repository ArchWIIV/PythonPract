def more(a, f):
    if f[1] == "opa":
        print("f = ", a)
    elif f[1] == "c++":
        print("f = ", a + 1)


def more_2(a, f):
    if f[3] == "hyphy":

        print("f = ", a)
    elif f[3] == "metal":
        print("f = ", a + 1)
    elif f[3] == "css":
        print("f = ", a + 2)


def one_two():
    f = []
    # Создание ключа для древа
    while True:
        key = input("")
        if key == "exit":
            break
        else:
            f.append(key)
    # Инициализация древа
    # tree = [[[0, 1], [2, 3], [4, 5]], [[6, 7, 8], [9, 10, 11], 12]]

    if f[2] == "nit":
        if f[3] == "hyphy":
            more(0, f)
        elif f[3] == "metal":
            more(2, f)
        elif f[3] == "css":
            more(4, f)

    elif f[2] == "frege":
        if f[0] == "genie":
            more_2(6, f)
        elif f[0] == "pan":
            more_2(9, f)
        elif f[0] == "hy":
            print("f = 12")


def two_two():
    # 1) d[31-26]; c[25-24]; b[23-12]; a[11-0]
    # 2) a[31-20]; b[19-8]; c[7-6]; d[5-0]
    hex_string = input("Введите строку в формате 16-чной системы: ")
    x_bytes = bin(int(hex_string, base=16))
    x_bytes = list(x_bytes)
    x_bytes.pop(1)
    if len(x_bytes) > 32:
        x_bytes.pop(0)
    print(x_bytes)
    d = []
    c = []
    b = []
    a = []
    for i in range(len(x_bytes)):
        if i <= 5:
            d += x_bytes[i]
        elif 5 < i <= 7:
            c += x_bytes[i]
        elif 7 < i <= 19:
            b += x_bytes[i]
        elif 19 < i <= 31:
            a += x_bytes[i]

    y = a + b + c + d
    out = ''.join(map(str, y))
    out = hex(int(out, 2))
    print(out, len(x_bytes))


def izm_0(x):
    x = x[2] + ", " + x[0][0] + ". " + x[1]
    return x


def izm_1(x):
    x = x[1][0] + x[1][1] + x[1][2] + "-" + x[1][3] + x[1][4] + x[1][5] + x[1][6]
    return x


def izm_2(x):
    x = round(float(x[2]), 1)
    return x


def izm_3(x):
    if x[3] == "Выполнено":
        return "да"
    else:
        return "нет"


# Мирослав Ш. Лишидич 1968921 0.69 Мирослав Ш. Лишидич Выполнено
def two_three():
    x = int(input("Длинна "))
    tabl = [[0 for j in range(0, 4)] for i in range(0, x)]

    for i in range(x):
        print("Введите ", i, "строчку")
        string = input()
        string = string.split(" ")
        try:
            for l in range(3): string.pop(5)
        except IndexError:
            print("Формат таблицы не верен")
        for j in range(len(string)):
            if j == 0:
                tabl[i][j] = izm_0(string)
                string.pop(1)
                string.pop(1)
            elif j == 1:
                tabl[i][j] = izm_1(string)
            elif j == 2:
                tabl[i][j] = izm_2(string)
            elif j == 3:
                tabl[i][j] = izm_3(string)

    for i in range(4):
        for j in range(x):
            print(tabl[j][i], end=" ")


while True:
    choose = int(input("Выбор варианта задания(1,2,3,4 exit - 5) - "))
    if choose == 1:
        one_two()
    elif choose == 2:
        two_two()
    elif choose == 3:
        two_three()
    else:
        print("Завершение работы")
        break
        