def has_no_e():
    string = input("Enter a string: ")
    string = string.split()
    count = 0
    for i in string:
        for j in range(0, len(i)):
            if i[j] == "e":
                check = False
                break
            else:
                check = True
        if check:
            print(i, end=' ')
            count += 1
    print("Percent('e'): ", (count / len(string)) * 100, "%")


if __name__ == '__main__':
    # input: em eu a
    # output: 33,33(3)%
    has_no_e()