BEGIN

INPUT n

CREATE empty list applicants

FOR i = 1 TO n

    INPUT name
    INPUT maths
    INPUT physics
    INPUT chemistry

    total = maths + physics + chemistry
    average = total / 3

    IF maths >= 50 AND physics >= 50 AND chemistry >= 50 THEN
        eligible = "Yes"
    ELSE
        eligible = "No"
    ENDIF

    STORE applicant details

ENDFOR

CREATE empty list eligible_students

FOR each applicant

    IF eligible = "Yes" THEN
        ADD applicant to eligible_students
    ENDIF

ENDFOR

SORT eligible_students by
    Total Marks (Descending)

IF Total Marks are equal THEN
    Compare Maths Marks
ENDIF

DISPLAY Rank List

DISPLAY Rejected Students

END