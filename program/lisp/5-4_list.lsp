(SETQ LIST1 (LIST 4 2))
(SETQ LIST2 '(5 41 4))

; get
(NTH 0 LIST2)
; get.length
(LENGTH LIST2)

; .で辞書型
(SETQ DP (CONS 5 6))
(CAR DP); get 0
(CDR DP); get 1

; cadr
(SETQ LIST4 (LIST (CONS 5 0) (CONS 0 5)))
(CADR LIST4)

; append of front
(SETQ LIST8 (LIST 10 11 12 13 14 15))
(APPEND '(8 9) LIST8)

; 置換
(SETQ LIST8 (LIST 10 11 12 13 14 15))
; str, target
(SUBST 20 12 LIST8)

(SETQ LIST9 (LIST 50 51 52 53 54 55))
; get position
(VL-POSITION 52 LIST9)
; 抜いたもので新たなListを作る
(SETQ LIST10 (VL-REMOVE 52 LIST9))