BEGIN

INPUT n

FOR each household

    INPUT name
    INPUT units

    IF units <= 100 THEN
         bill = units * 2

    ELSE IF units <= 200 THEN
         bill = (100 * 2) +
                ((units - 100) * 3)

    ELSE
         bill = (100 * 2) +
                (100 * 3) +
                ((units - 200) * 5)

    ENDIF

    bill = bill + 50

    IF units > 300 THEN
         bill = bill + 200
         DISPLAY "Excessive Usage"
    ENDIF

    DISPLAY bill

ENDFOR

END