BEGIN

INPUT n

FOR i = 1 TO n

    INPUT vehicle_category
    INPUT offence_type
    INPUT repeat_offence_status

    IF offence_type = 1 THEN
        fine = 1000
    ELSE IF offence_type = 2 THEN
        fine = 3000
    ELSE
        fine = 5000
    ENDIF

    IF vehicle_category = "Heavy" THEN
        fine = fine + 2000
    ENDIF

    IF repeat_offence_status = "Yes" THEN
        fine = fine * 2
    ENDIF

    IF fine >= 10000 THEN
         status = "Disqualified"
    ELSE
         status = "Eligible to Drive"
    ENDIF

    DISPLAY penalty and status

ENDFOR

END