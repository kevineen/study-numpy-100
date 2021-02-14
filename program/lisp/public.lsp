Public Sub Test()
ThisDrawing.SendCommand ("filedia 0 ")
Dim varFile As String
varFile = "B:\kaggle\beansAf\lisp\" + getfilename + ".pdf"
ThisDrawing.SendCommand ("_-EXPORT" & vbCr & "PDF" & vbCr & "" & vbCr & "" & vbCr & varFile & vbCr)
End Sub