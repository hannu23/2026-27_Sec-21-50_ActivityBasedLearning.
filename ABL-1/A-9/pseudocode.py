BEGIN

INPUT n

CREATE empty id_list
CREATE empty amount_list

FOR i = 1 TO n

    INPUT transaction_id
    INPUT amount

    STORE transaction_id
    STORE amount

ENDFOR

FOR i = 0 TO n-1

    suspicious = NO

    FOR j = i+1 TO n-1

        IF id_list[i] = id_list[j] THEN

            suspicious = YES

        ENDIF

    ENDFOR

    IF amount_list[i] > 10000 THEN

        suspicious = YES

    ENDIF

    IF suspicious = YES THEN

        DISPLAY transaction_id

    ENDIF

ENDFOR

END