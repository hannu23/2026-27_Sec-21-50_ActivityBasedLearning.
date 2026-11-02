BEGIN

INPUT n

FOR i = 1 TO n

    INPUT chemical_name
    INPUT storage_category
    INPUT quantity
    INPUT compatibility

    valid = "YES"

    IF storage_category = "Flammable" AND quantity > 50 THEN
         valid = "NO"
    ENDIF

    IF storage_category = "Corrosive" AND quantity > 30 THEN
         valid = "NO"
    ENDIF

    IF compatibility = "Incompatible" THEN
         valid = "NO"
    ENDIF

    IF valid = "YES" THEN
         DISPLAY "VALID RECORD"
    ELSE
         DISPLAY "INVALID RECORD"
    ENDIF

ENDFOR

END