# LABORATORY CHEMICAL INVENTORY VALIDATION

n = int(input("Enter number of chemical records: "))

for i in range(n):

    print("\nChemical Record", i + 1)

    chemical = input("Chemical Name: ")

    category = input("Storage Category (Flammable/Corrosive/General): ")

    quantity = int(input("Quantity in Litres: "))

    compatibility = input("Compatibility Status (Compatible/Incompatible): ")

    valid = "YES"

    if category.lower() == "flammable" and quantity > 50:
        valid = "NO"

    elif category.lower() == "corrosive" and quantity > 30:
        valid = "NO"

    if compatibility.lower() == "incompatible":
        valid = "NO"

    print("\nChemical :", chemical)

    if valid == "YES":
        print("Status   : VALID RECORD")
    else:
        print("Status   : INVALID RECORD")