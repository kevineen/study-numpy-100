;(TBLSEARCH "Style" "Standard")

;(TBLOBJNAME "Style" "Standard")

; フォントの設定
(SETQ ENTOBJ (TBLOBJNAME "Style" "Standard"))
(SETQ VL-OBJ (VLAX-ENAME->VLA-OBJECT ENTOBJ))
(VLA-PUT-HEIGHT VL-OBJ 0.10)