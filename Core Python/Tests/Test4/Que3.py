###3. WAP to print following patterns :

def pattern():
    print("*" * 23)

    for i in range(10):
        print(" " * (22 - 2*i) + "*")

    print("*" * 23 + " *")

pattern()


