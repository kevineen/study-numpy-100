(GETREAL "number: ")
(GETINT "number: ")

; yes no 入力
(INITGET 128 "Yes No")
(SETQ RETKWORD (GETKWORD "do you want continue [Yes/No] <Yes>: "))

; get entity info
;  entsel 関数が返す座標値は、選択されたオブジェクト上の点を常に示すわけではありません。
; entity name, mouse coursor point
(SETQ RETSEL (ENTSEL "select : "))
; 保存したオブジェクトの情報
(SETQ ENTOBJ (ENTGET (CAR RETSEL)))

; file open
(SETQ FPATH (GETFILED "Select lisp file" "C:/" "lsp" 12))