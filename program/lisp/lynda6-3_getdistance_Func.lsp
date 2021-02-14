(VL-LOAD-COM)
(DEFUN C:GETDATA (/ RETPNT RETDIST) 
  (SETQ RETPNT (GETPOINT "\n point: "))
  (IF (/= RETPNT NIL) 
    (PROGN 
      (SETQ RETDIST (GETDIST RETPNT "\n distance: "))
      (IF (/= RETDIST NIL) 
        (PRINC 
          (STRCAT "distance :" (RTOS RETDIST (GETVAR "LUNITS") (GETVAR "LUPREC")))
        )
      )
    )
  )

  (PRINC)
)