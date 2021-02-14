;while
(WHILE (= OBJSEL NIL) 
  (SETQ OBJSEL (ENTSEL "Select : "))
)

; for
(SETQ CNTR 0)
(REPEAT 10 
  (PRINC (STRCAT "\n" (ITOA CNTR)))
  (SETQ CNTR (+ CNTR 1))
)

; loop
(DEFUN C:LOOPIT (/ NUMLIST) 
  (SETQ NUMLIST '(1 2 3 4 5 6))
  (FOREACH XVAR NUMLIST 
    (IF (< XVAR 4) 
      (PRINC "number is less than 4")
      (PRINC (STRCAT "\n" (ITOA XVAR)))
    )
  )
  (PRINC)
)