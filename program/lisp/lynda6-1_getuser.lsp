; option T で、スペースが入力可能
(SETQ NAMESTRING (GETSTRING T "\nEnter name: "))
(PRINC (STRCAT "\nYou are compny" NAMESTRING))
(PRINC)

; get point
(SETQ RETPNT (GETPOINT "\n Specify: "))

; get distance
(SETQ RETDIST (GETDIST "\n distance: "))