(defun c:A3_dwg_pdf ()  
(if (findfile "T:/Drawing Tools/Templates/CCC2009.dwt")
   (progn
     (command "_.psetupin" (findfile "T:/Drawing Tools/Templates/CCC2009.dwt") "A3-dwg-pdf")
     (while (wcmatch (getvar "cmdnames") "*PSETUPIN*")
       (command "_yes")
     ) ;_ while
     T
   ) ;_ progn
 ) ;_ if
(PROMPT ".....PRINTING DRAWING TO pdf's....")
(setvar "cmddia" 0)
(setvar "filedia" 0)
(setq doc (vla-get-activedocument (vlax-get-acad-object)))
(vlax-for lay (vla-get-Layouts doc)
 (setq plotabs (cons (vla-get-name lay) plotabs))
)
(setq dwgname (GETVAR "dwgname"))
(setq len (strlen dwgname))
(setq dwgname (substr dwgname 1 (- len 4)))
(setq plottablist (acad_strlsort plotabs))
(setq len (length plottablist))
(setq x 0)
(repeat len
 (setq name (nth x plottablist))
 (princ name)
(setq pdfname (strcat (getvar "dwgprefix") dwgname "-" name))
 (if (/= name "Model")
   (progn
     (setvar "ctab" name)
     
(command "-plot" "n" "" "A3-dwg-pdf" "" "n" "y" "y")
   )
 )
 (setq x (+ x 1))
)
(setvar "cmddia" 1)
(setvar "filedia" 1)
(setq DWGNAME nil
     LEN nil
     NAME nil
     PLOTTABLIST nil) 
(princ)
)