def is_abecedarian():
    w = input("Input word: ").lower()
    is_abe_list = []
    if w.isalpha():
        for i in w:

            is_abe_list.append(i)

        is_abe_list.sort()

        is_abe_list = "".join(is_abe_list)

        if is_abe_list == w:
            return True
        else:
            return False
    else:
        print("Value Error!")
        return False


if is_abecedarian():
    print("This is abecedarian")
else:
    print("This is not abecedarian")

