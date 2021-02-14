; get current dir
(VL-STRING-TRANSLATE "\\" "/" (GETVAR "DWGPREFIX"))
; get current dir kaisou
(VL-STRING-SEARCH (GETVAR "LOGINNAME") (GETVAR "DWGPREFIX"))