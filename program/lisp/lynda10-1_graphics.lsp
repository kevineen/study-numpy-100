"""
; get entity layer
(SETQ ENTOBJ (ENTSEL "Selct entity:"))
(SETQ ENTDATA (ENTGET (CAR ENTOBJ)))
(SETQ LAYNAME (ASSOC 8 ENTDATA))
(STRCAT "Select object: " (CDR LAYNAME))


(SETQ ENTOBJ (ENTSEL "Selct entity:"))
(SETQ ENTDATA (ENTGET (CAR ENTOBJ)))
(SETQ LAYNAME (ASSOC 8 ENTDATA))
; entdata2 のレイヤー名データを指定の文字列にセット
(SETQ UPDATA (SUBST (CONS 8 "NEWLAYER") LAYNAME ENTDATA))
; model layer data update
(SETQ UPDOBJ (ENTMOD UPDATA))
"""
"""
; new Line
(SETQ STPT (GETPOINT "start point: "))
(SETQ ENDPT (GETPOINT STPT "end point: "))
(SETQ NEWENT (ENTMAKE 
               (LIST (CONS 0 "LINE") 
                     (CONS 10 STPT)
                     (CONS 11 ENDPT)
                     (CONS 0 "NEWLINE")
               )
             )
)

; delete ent
(SETQ ENTOBJ (ENTSEL "select :"))
(ENTDEL (CAR ENTOBJ))
"""
; 
(SETQ ENTOBJ (ENTSEL "sel obj: "))
(SETQ VL-OBJ (VLAX-ENAME->VLA-OBJECT (CAR ENTOBJ)))
; get length
(VLA-GET-LENGTH VL-OBJ)
; set obj
(VLA-PUT-LAYER VL-OBJ "CENTER")