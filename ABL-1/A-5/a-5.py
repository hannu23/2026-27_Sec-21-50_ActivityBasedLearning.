# COURIER CHARGE OPTIMIZATION

weight = float(input("Enter parcel weight (kg): "))

zone = input("Enter distance zone (A/B): ")

urgency = input("Enter delivery type (Normal/Express): ")

restriction = input("Restricted Parcel (Yes/No): ")

# Base Charge

if weight <= 5:
    charge = 100
else:
    charge = 200

# Distance Zone

if zone.upper() == "A":
    charge = charge + 50
else:
    charge = charge + 100

# Urgency Charge

if urgency.lower() == "express":
    charge = charge + 150

# Eligibility Check

if restriction.lower() == "yes":

    print("\nParcel Not Eligible For Delivery")

else:

    print("\nCourier Service Options")
    print("1. FastExpress")
    print("2. SpeedCourier")
    print("3. SmartDelivery")

    print("\nSelected Service : FastExpress")
    print("Final Charge     :", charge)