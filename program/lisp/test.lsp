(defun test( / ObjNameL i  ObjSet Data Pt10 Pt11 MidPt MidPtL item)

	;ユーザーのCAD設定を記憶するパート（毎回同じ）*********************
	(setq *error* *myerror*)

	;ユーザーが図形を選択するパート**********************
	(while (= ObjSet nil)
		(setq ObjSet (ssget '((0 . "LINE"))))
	)
	;選択した図形セットから図形名のリストを作る
	(setq 	i 0)
	(setq m (sslength ObjSet))
	(repeat m
		(setq ObjNameL (cons  (ssname ObjSet i) ObjNameL))
		(setq i (1+ i))
	)
	(princ "n ObjNameL :  ")(princ ObjNameL)

	;端点の座標を取り出し、中点を計算するパート**********************
	(foreach item ObjNameL
		(setq Data (entget item))

		;一方の点の座標
		(setq Pt10 (cdr (assoc 10 Data)))
		(princ "n Pt10 :  ")(princ Pt10)

		;もう一方の点の座標
		(setq Pt11 (cdr (assoc 11 Data)))
		(princ "n Pt11 :  ")(princ Pt11)

		;中点を求める
		(setq MidPt (list
					(* 0.5 (+ (car Pt10)(car Pt11)))
					(* 0.5 (+ (cadr Pt10)(cadr Pt11)))
				)
		)
		(princ "n MidPt :  ")(princ MidPt)

		;結果の座標をMidPtLというひとつのリストにどんどんつなげていく
		(setq MidPtL (cons  MidPt MidPtL))
		(princ "n MidPtL :  ")(princ MidPtL)
	)

	;結果をもとに作図するパート**********************
	(setvar "OSMODE" 0)		;Oスナップを解除しておく
	(foreach item MidPtL
		(command "._circle" item 10)
	)

	;ユーザーのCAD設定を復元するパート（毎回同じ）*********************
	(A_end)
	(setq *error* nil)
	(princ)
)
;ロードしたら実行されるようにしておく
(test)