# NESTED LOOP EXAMINATION SEATING GENERATOR

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("\nSEATING ARRANGEMENT\n")

for i in range(rows):

    row_letter = chr(65 + i)

    for j in range(1, cols + 1):

        # Reserved / Alternate Seating

        if (i + j) % 2 == 0:

            print("XX", end="\t")

        else:

            seat = row_letter + str(j)
            print(seat, end="\t")

    print()