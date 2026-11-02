# REPEATED TRANSACTION DETECTION

n = int(input("Enter number of transactions: "))

transaction_ids = []
amounts = []

for i in range(n):

    print("\nTransaction", i + 1)

    tid = input("Enter Transaction ID: ")
    amount = float(input("Enter Amount: "))

    transaction_ids.append(tid)
    amounts.append(amount)

print("\nSUSPICIOUS TRANSACTIONS")

for i in range(n):

    suspicious = False

    # Duplicate Detection

    for j in range(i + 1, n):

        if transaction_ids[i] == transaction_idssuspicious = True

    # Threshold Check

    if amounts[i] > 10000:

        suspicious = True

    if suspicious:

        print("ID :", transaction_ids[i],
              " Amount :", amounts[i])