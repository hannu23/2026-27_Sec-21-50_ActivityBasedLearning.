# UNIVERSITY ADMISSION DECISION ENGINE

n = int(input("Enter number of applicants: "))

applicants = []

for i in range(n):
    print("\nApplicant", i + 1)

    name = input("Enter name: ")

    maths = int(input("Maths marks: "))
    physics = int(input("Physics marks: "))
    chemistry = int(input("Chemistry marks: "))

    total = maths + physics + chemistry
    average = total / 3

    # Eligibility Check
    if maths >= 50 and physics >= 50 and chemistry >= 50:
        eligible = "Yes"
    else:
        eligible = "No"

    applicants.append([name, maths, physics, chemistry, total, average, eligible])

# Ranking Eligible Students
eligible_students = []

for student in applicants:
    if student[6] == "Yes":
        eligible_students.append(student)

# Bubble Sort by Total Marks (Descending)
for i in range(len(eligible_students)):
    for j in range(len(eligible_students) - i - 1):

        if eligible_students[j][4] < eligible_students[j + 1][4]:
            temp = eligible_students[j]
            eligible_students[j] = eligible_students[j + 1]
            eligible_students[j + 1] = temp

        # Tie Breaking using Maths Marks
        elif eligible_students[j][4] == eligible_students[j + 1][4]:

            if eligible_students[j][1] < eligible_students[j + 1][1]:
                temp = eligible_students[j]
                eligible_students[j] = eligible_students[j + 1]
                eligible_students[j + 1] = temp

print("\nELIGIBLE APPLICANTS RANK LIST")
print("Rank\tName\tTotal\tAverage")

rank = 1

for student in eligible_students:
    print(rank, "\t", student[0], "\t", student[4], "\t", round(student[5], 2))
    rank += 1

print("\nREJECTED APPLICANTS")

for student in applicants:
    if student[6] == "No":
        print(student[0])
