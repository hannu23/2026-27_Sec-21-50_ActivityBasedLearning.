BEGIN

INPUT weight
INPUT zone
INPUT urgency
INPUT restriction

charge = 0

IF weight <= 5 THEN
    charge = 100
ELSE
    charge = 200
ENDIF

IF zone = "A" THEN
    charge = charge + 50
ELSE
    charge = charge + 100
ENDIF

IF urgency = "Express" THEN
    charge = charge + 150
ENDIF

IF restriction = "Yes" THEN
    DISPLAY "Parcel Not Eligible"
ELSE
    DISPLAY "Final Charge =", charge
    DISPLAY "Service Selected"
ENDIF

END