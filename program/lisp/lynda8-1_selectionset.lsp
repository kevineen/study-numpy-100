; Enter するまでに選択したオブジェクトの一覧
(SETQ SSVAL (SSGET))
(IF (/= SSVAL NIL) 
  (PROGN 
    (SETQ CNTR 0)
    (WHILE (< CNTR (SSLENGTH SSVAL)) 
      (SETQ ENTOBJ (ENTGET (SSNAME SSVAL CNTR)))
      (PRINC (STRCAT "\Selcted object type is: " (CDR (CADR ENTOBJ))))
      (SETQ CNTR (+ 1 CNTR))
    )
  )
)

; filter select 画層を制限した選択
(SETQ SSVAL (SSGET '((8 . "0"))))