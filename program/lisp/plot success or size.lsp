(VL-LOAD-COM)
(defun C:test (/ layout num) 
  (setq ACADOBJ nil) ; èâä˙âª
  (SETQ ACADOBJ (VLAX-GET-ACAD-OBJECT))
  (SETQ ACDOC (VLA-GET-ACTIVEDOCUMENT ACADOBJ))
  (SETQ FILENAME (vla-get-Name ACDOC))
  (SETQ FILENAME (vl-string-right-trim ".dwg" FILENAME))
  ;  (alert (strcat FILENAME ".pdf"))
  (setq layouts (layoutlist)) ; list all paperspace layouts in the drawing
  (command ".-PLOT" "Yes" ;; Detailed plot configuration? [Yes/No] <No>: y
           ;(nth num layouts) ;;Enter a layout name or [?] <Test_001>:
           "Model" ; page setting name
           "Print As PDF.pc3" ;;Enter an output device name or [?] <DWG To PDF.pc3>:
           "ISO A4 (210.00 x 297.00 MM)" ;;Enter paper size or [?] <ISO A3 (297.00 x 420.00 MM)>:
           "Millimeters" ;;Enter paper units [Inches/Millimeters] <Millimeters>:
           "L" ;;Enter drawing orientation [Portrait/Landscape] <Landscape>:
           "N" ;;Plot upside down? [Yes/No] <No>:
           "L" ;;Enter plot area [Display/Extents/Layout/View/Window] <Layout>:
           "Fit" ;1:1;;Enter plot scale (Plotted Millimeters=Drawing Units) or [Fit] <1:1>:
           "0.00, 0.00" ;;Enter plot offset (x,y) <0.00,0.00>:
           "Yes" ;;Plot with plot styles? [Yes/No] <Yes>:
           "BLACK.ctb" ;;Enter plot style table name or [?] (enter . for none) <acad.ctb>:
           "Yes" ;;Plot with lineweights? [Yes/No] <Yes>:
           "A" ;;shade plot
           "" ; file name(Ç†Ç∆Ç≈directoryÇèCê≥)
           "N" ;;Save changes to page setup [Yes/No]? <N>
           "Y" ;;Proceed with plot [Yes/No] <Y>:
  ) ;; end .-plot
) ; end function