# TRAFFIC VIOLATION PENALTY CALCULATOR

n = int(input("Enter number of offenders: "))

for i in range(n):

    print("\nOffender", i + 1)

    vehicle = input("Vehicle Category (Light/Heavy): ")

    print("\nOffence Types")
    print("1. Signal Jumping")
    print("2. Overspeeding")
    print("3. Drunk Driving")

    offence = int(input("Enter offence type: "))

    repeat = input("Repeat Offence (Yes/No): ")

    # Base Fine
    if offence == 1:
        fine = 1000
    elif offence == 2:
        fine = 3000
    else:
        fine = 5000

    # Vehicle Category
    if vehicle.lower() == "heavy":
        fine = fine + 2000

    # Repeat Offence
    if repeat.lower() == "yes":
        fine = fine * 2

    # Disqualification
    if fine >= 10000:
        status = "DISQUALIFIED"
    else:
        status = "VALID"

    print("\nFinal Fine :", fine)
    print("Status     :", status)