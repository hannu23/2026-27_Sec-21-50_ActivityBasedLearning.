BEGIN

INPUT rows
INPUT columns

FOR i = 0 TO rows-1

    FOR j = 1 TO columns

        IF (i+j) MOD 2 = 0 THEN

            DISPLAY XX

        ELSE

            row_letter = CHR(65 + i)

            DISPLAY row_letter + j

        ENDIF

    ENDFOR

    PRINT NEW LINE

ENDFOR

ENDs