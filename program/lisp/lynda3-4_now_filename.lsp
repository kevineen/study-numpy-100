(VL-LOAD-COM)
(DEFUN C:VLACADDOBJ (/ ACADOBJ) 
  (SETQ ACADOBJ (VLAX-GET-ACAD-OBJECT))
  (SETQ ACDOC (VLA-GET-ACTIVEDOCUMENT ACADOBJ))
  ; ShiftJISじゃないと日本語は文字化けする
  (alert (strcat "現在のファイル" (vla-get-Name ACDOC)))
  (PRINC)
)