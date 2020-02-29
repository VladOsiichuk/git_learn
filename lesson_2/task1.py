#solving square equations
def main():
    a = float(input("Введіть а: "))
    b = float(input("Введіть b: "))
    c = float(input("Введіть c: ")) #user variables

    if (b == 0):
        x = (-c / a)**0.5
        print("x1 =", x, "Тип цього числа:", type(x))  # output values
        print("x2 =", -x, "Тип цього цисла:", type(-x))
        return
    D = b ** 2 - 4 * a * c  # looking for a discriminant
    if (D < 0):   #looking for a X if discriminant < 0
        print ("У рівняння немає розв'язків")
        return
    if (D == 0):  #looking for a X if discriminant = 0
        x = -b / (2 * a)
        x = round(x, 2)
        print("x =", x, type(x))
        return

    x2 = (-b - (D ** 0.5)) / (2 * a) #looking for a X1 and X2 if discriminant > 0
    x1 = (-b + (D ** 0.5)) / (2 * a)
    x1 = round(x1, 2)
    x2 = round(x2, 2)
    print("x1 =", x1, "Тип цього числа:", type(x1)) #output values
    print("x2 =", x2, "Тип цього цисла:", type(x2))
    print(D)

if __name__ == "__main__":
    main()

