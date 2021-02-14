(defun C:laytopdf (/ cmd) 
  (setq cmd (getvar 'cmdecho))
  (setvar 'cmdecho 0)
  (foreach Layout (layoutlist) 

    (command "_.-PLOT" 
             "No" ; Detailed plot configuration? [Yes/No] <No>: No
             Layout ; Enter a layout name or [?] <Layout1>:
             "" ; Enter a page setup name
             "DWG To PDF.pc3" ; Enter an output device name or [?] <DWG To PDF.pc3>:
             (strcat (getvar "DWGPREFIX") Layout ".pdf") ; Directory to save
             "No" ; save changes to page setup?
             "YES" ; proceed with plot?
    ) ; command
  ) ; foreach
  (vla-put-StyleSheet (vla-get-ActiveLayout (vla-get-ActiveDocument (vlax-get-acad-object ) ) ) 
                      "monochrome.stb"
  )
  (setvar 'cmdecho cmd)
  (princ)
); defun B:\kaggle\beansAf\lisp