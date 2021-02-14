;MergePdfs
;Merges multiple pdf (or eps) files into one
;

; make a batch file ?
;gs -sDEVICE=pdfwrite \
;    -dNOPAUSE -dBATCH -dSAFER \
;    -sOutputFile=combined.pdf \
;    first.pdf \
;    second.pdf \
;    third.pdf [...]

;Ghostscript (http://www.ghostscript.com/) can be used to combine PDFs.

; Something like this should work: by Roy_043

(defun KGA_String_Join (strLst delim)
(if strLst
(apply
'strcat
(cons
(car strLst)
(mapcar '(lambda (a) (strcat delim a)) (cdr strLst))
)
)
""
)
)

; (CombinePdf 
  (setq gsexe "C:\\Program Files\\gs\\gs9.19\\bin\\gswin64c.exe")
; (setq srcFilelst  '("D:\\Tmp\\A.pdf" "D:\\Tmp\\B.pdf"))
; (setq trgfile "C:\\Acadtemp\\Total.pdf")
; )
; Note: Existing trgFile will be overwritten.
(defun CombinePdf (gsExe srcFileLst trgFile)
(startapp 
(strcat
gsExe " "
"-sDEVICE=pdfwrite -dBATCH -dNOPAUSE -dQUIET  "
"-sOutputFile=\"" trgFile "\" "
"\"" (KGA_String_Join srcFileLst "\" \"") "\""
)
)
)


