import n19dcat032

while True:
    print('''
        +------------ MENU --------------+
        | 1: convert_m_to_yd()           |
        | 2: fibonacci()                 |
        | 3: is_prime()                  |
        | 4: count_o_e_d()               |
        | 5: is_triangle()	             |
        | 6: area_triangle()             |
        | 7: factorial()                 |
        | 8: area_rectangle()            |
        | 9: gcd()                       |
        | 10: rotate()                   |        
        | 0: QUIT                        |
        +--------------------------------+
        ''')

    choice = int(input('Enter your choose: '))
    if choice == 1:
        minute = int(input('Enter minutes: '))
        print(str(n19dcat032.convert_m_to_yd(minute)[0]) + " year, " + str(
            n19dcat032.convert_m_to_yd(minute)[1]) + "days")
    elif choice == 2:
        number = int(input("Enter length of Fibonacci: "))
        list = n19dcat032.fibonacci(number)
        print("The top ", number, " numbers of the Fibonacci sequence are:", end=" ")
        for i in list:
            print(i, end=" ")
    elif choice == 3:
        number = int(input("Enter number: "))
        if n19dcat032.is_prime(number):
            print(str(number) + "is a prime")
        else:
            print(str(number) + "not is a prime")
    elif choice == 4:
        number = int(input("Enter a number number: "))
        n19dcat032.count_o_e_d(number)
    elif choice == 5:
        number1 = int(input("Enter an integer number: "))
        number2 = int(input("Enter an integer number: "))
        number3 = int(input("Enter an integer number: "))
        if n19dcat032.is_triangle(number1, number2, number3):
            print(str(number1) + str(number2) + str(number3) + " is triangle")
        else:
            print(str(number1) + str(number2) + str(number3) + " is not triangle")

    elif choice == 6:
        number1 = int(input("Enter an integer number: "))
        number2 = int(input("Enter an integer number: "))
        number3 = int(input("Enter an integer number: "))
        if n19dcat032.area_triangle(number1, number2, number3) != 0:
            print("area triangle: " + str(n19dcat032.area_triangle(number1, number2, number3)))
        else:
            print(str(number1) + str(number2) + str(number3) + " is not triangle")

    elif choice == 7:
        number = int(input("Enter a number: "))
        print(" factorial: " + str(n19dcat032.factorial(number)))
    elif choice == 8:
        number1 = int(input("Enter a width number: "))
        number2 = int(input("Enter a height number: "))
        print("Area rectangle: " + str(n19dcat032.area_rectangle(number1, number2)))
    elif choice == 9:
        number1 = int(input("Enter a width number: "))
        number2 = int(input("Enter a height number: "))
        print("gcd: " + str(n19dcat032.gcd(number1, number2)))

    elif choice == 10:
        x = input("Enter a string: ")
        y = int(input("Enter a key (only number): "))
        print(n19dcat032.rotate(x, y))
    elif choice == 0:
        print('GOOD BYE!')
        break
    else:
        print("Your choose is incorrect! Please choice again...")
