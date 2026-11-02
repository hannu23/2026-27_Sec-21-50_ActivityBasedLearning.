# ADVANCED NUMERIC PATTERN GENERATOR

n = int(input("Enter an odd dimension: "))

if n <= 0 or n % 2 == 0:

    print("Invalid Dimension")

else:

    mid = n // 2

    # Upper Half

    for i in range(mid + 1):

        for s in range(mid - i):
            print(" ", end=" ")

        for j in range(2 * i + 1):

            if j == 0 or j == 2 * i or i == 0:
                print(i + 1, end=" ")
            else:
                print(" ", end=" ")

        print()

    # Lower Half

    for i in range(mid - 1, -1, -1):

        for s in range(mid - i):
            print(" ", end=" ")

        for j in range(2 * i + 1):

            if j == 0 or j == 2 * i or i == 0:
                print(i + 1, end=" ")
            else:
                print(" ", end=" ")

        print()