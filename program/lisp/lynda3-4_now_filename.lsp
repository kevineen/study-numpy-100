(VL-LOAD-COM)
(DEFUN C:VLACADDOBJ (/ ACADOBJ) 
  (SETQ ACADOBJ (VLAX-GET-ACAD-OBJECT))
  (SETQ ACDOC (VLA-GET-ACTIVEDOCUMENT ACADOBJ))
  ; ShiftJIS����Ȃ��Ɠ��{��͕�����������
  (alert (strcat "���݂̃t�@�C��" (vla-get-Name ACDOC)))
  (PRINC)
)