(defun c:toggle (/ dcl_id Act Path_toggle A B)
	(read_registry_toggle)

	(setq dcl_id (load_dialog "toggle.dcl"))
	(new_dialog "toggles" dcl_id)
	(set_tile "A" A)
	(set_tile "B" B)
	(mode_tile "ButtonA" (- 1 (atoi A)))
	(mode_tile "ButtonB" (- 1 (atoi B)))
	(action_tile "accept" "(get_value_toggle)(done_dialog 1)")
	(action_tile "cancel" "(done_dialog 0)")
	(setq Act (start_dialog))
	(unload_dialog dcl_id)
	(if (= Act 1)
		(princ (strcat "\n A is " A "\n B is " B))
		(princ "\n Dialog Cancelled")
	)
(princ)
)
;;*************************************************************************
(defun display_value_toggle ()
	(mode_tile "ButtonA" (- 1 (atoi (get_tile "A"))))
	(mode_tile "ButtonB" (- 1 (atoi (get_tile "B"))))
)
;;*************************************************************************
(defun get_value_toggle ()
	(setq A (get_tile "A"))
	(setq B (get_tile "B"))
	(write_registry_toggle)
)
;;*************************************************************************
(defun read_registry_toggle ()
	(setq Path_toggle "HKEY_CURRENT_USER\\Software\\SampleDCL")
	(setq A (vl-registry-read Path_toggle "A"))
	(if (null A)(setq A "0"))
	(setq B (vl-registry-read Path_toggle "B"))
	(if (null B)(setq B "0"))
)

;;*************************************************************************
(defun write_registry_toggle ()
	(setq Path_toggle "HKEY_CURRENT_USER\\Software\\SampleDCL")
	(vl-registry-write Path_toggle "A" A)
	(vl-registry-write Path_toggle "B" B)
)
(princ)
(c:toggle)

こっちがDCLファイル。toggle.dclで保存してください。

toggles :dialog{label= "Toggle DCL";
	:toggle {label="A"; key="A";action= "(display_value_toggle)";}
	:toggle {label="B"; key="B";action= "(display_value_toggle)";}
	:button {label="Button A"; key="ButtonA";}
	:button {label="Button B"; key="ButtonB";}
	ok_cancel;
}
