# PROGRESSIVE WATER TARIFF ANALYSIS

n = int(input("Enter number of households: "))

for i in range(n):

    print("\nHousehold", i + 1)

    name = input("Enter household name: ")
    units = int(input("Enter water consumption: "))

    if units <= 100:

        bill = units * 2

    elif units <= 200:

        bill = (100 * 2) + ((units - 100) * 3)

    else:

        bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)

    fixed_fee = 50
    bill = bill + fixed_fee

    if units > 300:
        bill = bill + 200
        status = "EXCESSIVE USAGE"
    else:
        status = "NORMAL USAGE"

    print("\nHousehold :", name)
    print("Bill      :", bill)
    print("Status    :", status)