# STUDENT TIMETABLE CONFLICT DETECTION

n = int(input("Enter number of courses: "))

timetable = []

for i in range(n):

    print("\nCourse", i + 1)

    course = input("Course Name: ")
    timeslot = input("Time Slot (e.g. Mon-09AM): ")
    room = input("Room Number: ")

    timetable.append((course, timeslot, room))

valid = True

print("\n--- CONFLICT REPORT ---")

for i in range(len(timetable)):

    for j in range(i + 1, len(timetable)):

        c1, t1, r1 = timetable[i]
        c2, t2, r2 = timetable[j]

        if t1 == t2:

            print("\nTime Conflict:")
            print(c1, "and", c2)

            valid = False

            if r1 == r2:
                print("Room Conflict in Room", r1)

if valid:
    print("\nTIMETABLE VALID")
else:
    print("\nTIMETABLE INVALID")