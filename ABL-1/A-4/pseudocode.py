BEGIN

INPUT n

CREATE empty list timetable

FOR i = 1 TO n

    INPUT course
    INPUT time_slot
    INPUT room

    STORE values in timetable

ENDFOR

valid = YES

FOR i = 0 TO n-1

    FOR j = i+1 TO n-1

        IF timetable[i].time_slot =
           timetable[j].time_slot THEN

            DISPLAY "Time Conflict Found"

            valid = NO

            IF timetable[i].room =
               timetable[j].room THEN

               DISPLAY "Room Conflict Found"

            ENDIF

        ENDIF

    ENDFOR

ENDFOR

IF valid = YES THEN
     DISPLAY "TIMETABLE VALID"
ELSE
     DISPLAY "TIMETABLE INVALID"
ENDIF

END