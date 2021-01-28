import re


def display():
    print("Modern Cipher Solver\n")
    print("\nEnter 'C' for Caesar Cipher \nEnter 'M' for Multiplicative Cipher\n ")
    while True:
        cc = (input("Please enter your choice: "))
        if cc not in ('C', 'M'):
            print("Not an appropriate choice!")
        else:
            break

    if cc == 'M':
        print("\nMultiplicative Cipher\n")
        print("MENU:\nEnter 'E' for ENCRYPTION \nEnter 'D' for DECRYPTION \nEnter 'B' for BRUTE_FORCE \nEnter 'X' for "
              "Exit \n ")
        choice()
    else:
        print("\nCaesar Cipher\n")
        print("MENU:\nEnter 'E' for ENCRYPTION \nEnter 'D' for DECRYPTION \nEnter 'B' for BRUTE_FORCE \nEnter 'X' for "
              "Exit \n ")
        choice2()


def choice():
    while True:
        ch = (input("Please enter your choice: "))
        if ch not in ('E', 'D', 'B', 'X'):
            print("Not an appropriate choice!")
        else:
            break

    if ch == 'E':
        print("\nWelcome to Encryption\n")
        encryption()
    elif ch == 'D':
        print("\nWelcome to Decryption\n")
        decryption()
    elif ch == 'B':
        print("\nWelcome to Brute_Force\n")
        brute_force()
    elif ch == 'X':
        exit("\nHmm, The program is now terminated! \n")

    else:
        choice()


print()


def choice2():
    while True:
        ch = (input("Please enter your choice: "))
        if ch not in ('E', 'D', 'B', 'X'):
            print("Not an appropriate choice.")
        else:
            break

    if ch == 'E':
        print("\nWelcome to Encryption\n")
        encryption2()
    elif ch == 'D':
        print("\nWelcome to Decryption\n")
        decryption2()
    elif ch == 'B':
        print("\nWelcome to Brute_Force\n")
        brute_force2()
    elif ch == 'X':
        exit("\nHmm, The program is now terminated! \n")
    else:
        choice2()


print()


def plain_text():
    while True:
        plt = input("Enter plain text: ").strip()
        if plt.isalpha() or bool(re.search(r"\s", plt)):
            return plt.upper()

        else:
            print("Sorry, I didn't understand that.")


def cipher_text():
    while True:
        clt = input("Enter cipher text: ").strip()
        if clt.isalpha() or bool(re.search(r"\s", clt)):
            return clt.upper()

        else:
            print("Sorry, I didn't understand that.")


def key():
    while True:
        in_key = input("Enter the key: ")
        if in_key.isdecimal():
            return in_key

        else:
            print("Invalid key entered!")


def encryption():
    ct = ""
    pt = plain_text()
    k = int(key())
    try:
        for i in pt.split():
            for j in i:
                total = (((ord(j) - 65) * k) % 26)
                ct = ct + (chr(total + 65))
            ct = ct + " "
        print("Cipher Text is: ", ct.lower())
    except:
        print("Something went wrong")
        encryption()
    display()


def inverse():
    # a = int(key())
    xs = []
    for a in range(0,27):
        for x in range(1, 27):
            if (a * x) % 26 == 1:
                xs.append(x)
    return xs


def decryption():
    plt = ""
    ct = cipher_text()
    ks = inverse()
    words = []
    for k in ks:
        print(k)
        plt = ""
        for b in range(0,10):
            print(b)
            for i in ct.split():
                plt = ""
                for j in i:
                    total = ((ord(j) - 65 - b) * k) % 26
                    plt = plt + (chr(total + 65))
                words.append(plt)
            print(words)
            words = []
    display()


def brute_force():
    ct = cipher_text()
    pt = plain_text()

    try:
        if True:
            for a in range(1, 26):
                k = for_brute(a)
                plt = ""
                for i in ct.split():
                    for j in i:
                        total = (((ord(j) - 65) * k) % 26)
                        plt = plt + (chr(total + 65))
                    plt = plt + " "
                if plt.lower() == (pt.lower() + " "):
                    print("Key is: ", a)
    except:
        print("Something went wrong")
        brute_force()
    display()


def for_brute(a):
    a = a % 26
    for x in range(1, 26):
        if (a * x) % 26 == 1:
            return x
    return 1


display()
