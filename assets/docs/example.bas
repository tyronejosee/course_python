Sub SumarColumna()
    ' Declarar variables
    Dim ws As Worksheet
    Dim rango As Range
    Dim total As Double
    
    ' Seleccionar la hoja activa
    Set ws = ActiveSheet
    
    ' Seleccionar el rango (columna A desde la fila 1 hasta la última fila con datos)
    Set rango = ws.Range("A1:A" & ws.Cells(ws.Rows.Count, "A").End(xlUp).Row)
    
    ' Calcular la suma de la columna
    total = Application.WorksheetFunction.Sum(rango)
    
    ' Mostrar el resultado en un cuadro de mensaje
    MsgBox "La suma de la columna A es: " & total
End Sub
