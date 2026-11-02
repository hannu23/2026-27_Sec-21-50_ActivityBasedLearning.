BEGIN

INPUT n

IF n <= 0 OR n MOD 2 = 0 THEN

    DISPLAY "Invalid Dimension"

ELSE

    mid = n // 2

    FOR i = 0 TO mid

        PRINT spaces

        FOR j = 0 TO i

            PRINT number pattern

        ENDFOR

    ENDFOR

    FOR i = mid-1 TO 0

        PRINT spaces

        FOR j = 0 TO i

            PRINT number pattern

        ENDFOR

    ENDFOR

ENDIF

END