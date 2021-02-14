;(NAMEDOBJDICT)

(VLAX-LDATA-PUT "LyndaDictionary" "MySaveValue" 125)
(SETQ RETVAL (VLAX-LDATA-LIST "LyndaDictionary"))
(SETQ RETVAL (VLAX-LDATA-GET "LyndaDictionary" "MySaveValue"))
(VLAX-LDATA-DELETE "LyndaDictionary" "MySavedValue")

(SETQ USERPROD (VLAX-PRODUCT-KEY))
(VLAX-MACHINE-PRODUCT-KEY)

; 作成したlspはアプリケーションファイルをロードに設定すれば自動読込？

(DEFUN *ERROR* (MSG) 
  (PRINC "You had an error")
  (PRINC)
)