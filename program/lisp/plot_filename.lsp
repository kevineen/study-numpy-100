(VL-LOAD-COM)
(defun C:test (/ layout num) 
  (setq ACADOBJ nil) ; èâä˙âª
  (SETQ ACADOBJ (VLAX-GET-ACAD-OBJECT))
  (SETQ ACDOC (VLA-GET-ACTIVEDOCUMENT ACADOBJ))
  (SETQ FILENAME (vla-get-Name ACDOC))
  (SETQ FILENAME (vl-string-right-trim ".dwg" FILENAME))
  (alert (strcat FILENAME ".pdf"))
  (setq layouts (layoutlist)) ; list all paperspace layouts in the drawing
  (command ".-PLOT" 
           "N" ;; Detailed plot configuration? [Yes/No] <No>: y
           ;(nth num layouts) ;;Enter a layout name or [?] <Test_001>:
           "Model"
           "" ; page setting name
           "Print As PDF.pc3" ;;Enter an output device name or [?] <DWG To PDF.pc3>:
           (strcat FILENAME ".pdf") ;; the pdf file with the layout name
           ;(strcat (getvar "DWGPREFIX") (getvar "CTAB") ".pdf") ;; the pdf file with the layout name
           "ISO A4 (210.00 x 297.00 MM)" ;;Enter paper size or [?] <ISO A3 (297.00 x 420.00 MM)>:
           "Millimeters" ;;Enter paper units [Inches/Millimeters] <Millimeters>:
           "Landscape" ;;Enter drawing orientation [Portrait/Landscape] <Landscape>:
           "No" ;;Plot upside down? [Yes/No] <No>:
           "Layout" ;;Enter plot area [Display/Extents/Layout/View/Window] <Layout>:
           "1:1" ;;Enter plot scale (Plotted Millimeters=Drawing Units) or [Fit] <1:1>:
           "0.00, 0.00" ;;Enter plot offset (x,y) <0.00,0.00>:
           "Yes" ;;Plot with plot styles? [Yes/No] <Yes>:
           "BLACK.ctb" ;;Enter plot style table name or [?] (enter . for none) <acad.ctb>:
           "Yes" ;;Plot with lineweights? [Yes/No] <Yes>:
           "Yes" ;;Scale lineweights with plot scale? [Yes/No] <No>: y
           "Yes" ;;Plot paper space first? [Yes/No] <No>:
           "No" ;;Hide paperspace objects? [Yes/No] <No>:
           "No" ;;Save changes to page setup [Yes/No]? <N>
           "Yes" ;;Proceed with plot [Yes/No] <Y>:
  ) ;; end .-plot
) ; end function